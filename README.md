# stemplayer-explorer

## Stem Player & Stem Player Explorer

**Per the Stem Player website:**

**FEATURES**

 - CUSTOMIZE ANY SONG, SPLIT ANY SONG INTO STEMS
 - CONTROL VOCALS, DRUMS, BASS, AND SAMPLES
 - ISOLATE PARTS
 - ADD EFFECTS
 - 4 CHANNEL LOSSLESS AUDIO MIXING
 - REAL TIME LOOP AND SPEED CONTROL
 - TACTILE EFFECTS
 - SAVE, PLAYBACK, AND DOWNLOAD MIXES

**SPECS**

 - BLUETOOTH
 - HAPTICS
 - 4 TOUCH SENSITIVE LIGHT SLIDERS
 - 97DB SPEAKER
 - 3.5MM JACK, USB-C POWER AND DATA
 - 8GB STORAGE

The Stem Player Explorer is a multi-platform desktop application written in Python particularly utilizing the PyQT5 library for its user interface that I'm working on for fun :smiley:The goal is to be an organized and informative desktop version of the Stem Player [website](https://stemplayer.com). 

## Usage

With the Stem Player disconnected, power it off. Plug the Stem Player in and while holding the central play/pause button, power it on. This will allow the Stem Player to be mounted as a file system.

From there, the app will detect the Stem Player automatically and load its filesystem. If there is more than one Stem Player connected upon application start, select the desired device from the list by serial number.

## Installation

This app was developed using Python v3.10.2. Create a virtual environment and install required packages by running:

```bash
# Create a Virtual Environment
python -m venv env

# Start the Virtual Environment
## Windows
.\env\Scripts\activate

## MacOS and Linux
source env/bin/activate

# Install Python packages
pip install -r requirements.txt
```

The app can then be run with `python main.py`

## Screenshots

*Screenshots come from early development*

Upon starting the app, if no Stem Player is found:

![No Device Found - Image](/docs/img/nodevicefound.JPG)

If a single device is found, the app will read all albums from the Stem Player:

![Device Init - Image](/docs/img/devicestart.JPG)

Upon selecting an album, the contents of the config file will be displayed next to all downloaded songs from said album.

![Album View - Image](/docs/img/withsongs.JPG)