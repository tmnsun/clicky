import gi
import sys
import os
import pygame
from pynput import keyboard

gi.require_version("Gtk", "3.0")
gi.require_version("AppIndicator3", "0.1")
from gi.repository import Gtk, AppIndicator3


class TrayIcon:
    def __init__(self):
        # Initialize pygame mixer
        pygame.mixer.init()

        self.volume = 0.4

        if getattr(sys, "frozen", False):
            # If the application is run as a bundle, the pyInstaller bootloader
            # extends the sys module by a flag frozen=True and sets the app
            # path into variable _MEIPASS'.
            base_path = sys._MEIPASS
        else:
            # Normal development path
            base_path = os.path.dirname(__file__)

        keydown_sound_path = os.path.join(base_path, "sounds/sunshine/down.mp3")
        keyup_sound_path = os.path.join(base_path, "sounds/sunshine/up.mp3")

        # Load sound files
        self.keydown_sound = pygame.mixer.Sound(keydown_sound_path)
        self.keyup_sound = pygame.mixer.Sound(keyup_sound_path)

        self.keydown_sound.set_volume(self.volume)
        self.keyup_sound.set_volume(self.volume)

        self.indicator = AppIndicator3.Indicator.new(
            "custom_tray",
            "system-run",
            # os.path.abspath(
            #     "icon.png"
            # ),  # Ensure you have an icon.png or change this to a system icon name
            AppIndicator3.IndicatorCategory.APPLICATION_STATUS,
        )
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
        self.indicator.set_menu(self.create_menu())
        self.indicator.set_label("Clicky", "app")

        self.listener = keyboard.Listener(
            on_press=self.on_press, on_release=self.on_release
        )
        self.listener.start()

    def create_menu(self):
        menu = Gtk.Menu()

        # Current volume display
        self.item_current_volume = Gtk.MenuItem(
            label=f"Volume: {int(self.volume * 100)}%"
        )
        menu.append(self.item_current_volume)

        # Add volume up option
        item_volume_up = Gtk.MenuItem(label="Volume Up")
        item_volume_up.connect("activate", self.increase_volume)
        menu.append(item_volume_up)

        # Add volume down option
        item_volume_down = Gtk.MenuItem(label="Volume Down")
        item_volume_down.connect("activate", self.decrease_volume)
        menu.append(item_volume_down)

        item_quit = Gtk.MenuItem(label="Quit")
        item_quit.connect("activate", self.quit)
        menu.append(item_quit)

        menu.show_all()
        return menu

    def on_press(self, key):
        self.keydown_sound.play()

    def on_release(self, key):
        self.keyup_sound.play()

    def increase_volume(self, widget):
        if self.volume < 1.0:
            self.volume += 0.1  # Increase volume by 10%
            self.volume = min(self.volume, 1.0)  # Ensure volume does not exceed 100%
            self.update_volume()

    def decrease_volume(self, widget):
        if self.volume > 0.0:
            self.volume -= 0.1  # Decrease volume by 10%
            self.volume = max(self.volume, 0.0)  # Ensure volume does not go below 0%
            self.update_volume()

    def update_volume(self):
        # Set the new volume for sound effects
        self.keydown_sound.set_volume(self.volume)
        self.keyup_sound.set_volume(self.volume)

        self.item_current_volume.set_label(f"Volume: {int(self.volume * 100)}%")

    def quit(self, widget):
        self.listener.stop()  # Stop the keyboard listener
        pygame.mixer.quit()  # Quit the mixer module to clean up resources
        Gtk.main_quit()


def main():
    app = TrayIcon()
    Gtk.main()


if __name__ == "__main__":
    main()
