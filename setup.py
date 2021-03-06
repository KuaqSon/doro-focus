from setuptools import setup
import pkg_resources.py2_warn

APP = ["pomodoro.py"]
DATA_FILES = []
OPTIONS = {
    "argv_emulation": True,
    "iconfile": "icon.icns",
    "plist": {
        "CFBundleShortVersionString": "0.2.0",
        "LSUIElement": True,
    },
    "packages": ["rumps"],
    "excludes": ["pillow", "Image"],  # exclude unwanted dependencies
}

setup(
    app=APP,
    name="DoroFocus",
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
    install_requires=["rumps"],
)