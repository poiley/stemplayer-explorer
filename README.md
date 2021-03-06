# ![Stem Player Icon](/docs/img/stemplayer_25px.png) stemplayer-explorer

## :newspaper: Stem Player & Stem Player Explorer

### **Per the Stem Player website:**

|                **FEATURES**                   | **SPECS**                       |
|-----------------------------------------------|---------------------------------|
| CUSTOMIZE ANY SONG, SPLIT ANY SONG INTO STEMS | BLUETOOTH                       |
| CONTROL VOCALS, DRUMS, BASS & SAMPLES         | HAPTICS                         |
| ISOLATE PARTS                                 | 4 TOUCH SENSITIVE LIGHT SLIDERS |
| REAL TIME LOOP & SPEED CONTROL                | 97DB SPEAKER                    |
| TACTILE EFFECTS                               | 3.5 MM JACK, USB-C POWER & DATA |
| SAVE, PLAYBACK, & DOWNLOAD  MIXES             | 8GB STORAGE                     |


### **About this App**

The Stem Player Explorer is a multi-platform desktop application written in Python particularly utilizing the PyQT5 library for its user interface that I'm working on for fun :smiley: The goal is to be an organized and informative desktop version of the Stem Player [website](https://stemplayer.com). 

## :black_nib: Usage

With the Stem Player disconnected, power it off. Plug the Stem Player in and while holding the central play/pause button, then power it on. This will allow the Stem Player to be mounted as a readable and writable file system.

From there, the app will detect the Stem Player automatically and load the device contents. If there is more than one Stem Player connected upon application start, select the desired device from the list by serial number (Windows) or mount directory (Linux/MacOS).

## :inbox_tray: Installation

This app was developed using Python v3.10.2. Create a virtual environment by using that version of Python, installing the `virtualenv` pip, and install required packages by running:

```bash
# Create a Virtual Environment
python -m venv env

# Start the Virtual Environment
## Windows
.\env\Scripts\activate

## MacOS and Linux
source env/bin/activate

## Linux Only
sudo apt-get install python3 python3-dev xcb python3-pyqt5 pyqt5-dev pyqt5-dev-tools
export DISPLAY=:0

# Install Python packages
pip install -r requirements.txt
```

The app can then be run with `python main.py`

## :camera: Screenshots

*Screenshots come from early development*

Upon starting the app, if no Stem Player is found:

![No Device Found - Image](/docs/img/nodevicefound.JPG)

If a single device is found, the app will read all albums from the Stem Player:

![Device Init - Image](/docs/img/devicestart.JPG)

Upon selecting an album, the contents of the config file will be displayed next to all downloaded songs from said album.

![Album View - Image](/docs/img/withsongs.JPG)

## :briefcase: License

This project was created under the [GNU General Public License v3](https://choosealicense.com/licenses/gpl-3.0/). Why?

> **"Fuck all this dick swinging contest. We all gon be dead in 100 Years. Let the kids have the music."** 
> - _Kanye West, Stem Player creator_