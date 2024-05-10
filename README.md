# Clicky :keyboard: :sound:

Welcome to Clicky, a fun tool that adds satisfying click sounds to your keyboard. It's like typing on a typewriter, but without the heavy machinery!

## :book: Description

Clicky is designed to make your typing experience more enjoyable. Whether you're coding, writing an essay, or just browsing the web, Clicky adds a satisfying auditory feedback to your keystrokes. It's a simple way to make your workspace more dynamic and engaging.

## :wrench: Installation

Getting Clicky up and running is a breeze. Follow the steps below to install the necessary dependencies and distribute the application.

### :package: Dependencies

First, you'll need to install some packages. Open your terminal and run the following commands:

```
sudo dnf install gtk3-devel gobject-introspection-devel libappindicator-gtk3-devel SDL2 SDL2_mixer
```

Next, install the Python dependencies listed in the requirements.txt file:

```
pip install -r requirements.txt
```

## :rocket: Distribution

To distribute Clicky, you'll need to install `pyinstaller` and run it with the provided spec file. Here's how:

```
pip install pyinstaller
pyinstaller Clicky.spec
```

And that's it! You're now ready to enjoy a more satisfying typing experience with Clicky. Happy typing! :tada:

