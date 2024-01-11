from setuptools import setup

APP = ['your_script.py']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['rarfile'],
    'excludes': ['tkinter'],
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)