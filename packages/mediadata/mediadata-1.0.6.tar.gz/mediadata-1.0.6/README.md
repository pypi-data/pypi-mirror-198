## A simple wrapper for mediainfo tool available as Global PYPI Python Package

### For Python

Pip Install :

```
pip install mediadata
```
```
Package Link: https://pypi.org/project/mediadata/1.0.4/
```
### Prerequisites :

This tool needs&nbsp;<mark>mediainfo</mark>&nbsp;to be installed inorder to work properly.

Soon available on Ubuntu/Debian:

```
sudo apt install mediainfo
sudo apt install mediadata
```

#### Usage

To get all available info about a video file. It works with all media types.

```
mediadata --file="some video.mp4" track --type={General/Audio/Video} --list-keys

```

To get info about one particular key:

```
mediadata --file="some video.mp4" track --type={General/Audio/Video} --key=Duration

```

#### Build Deb

```
python setup.py --command-packages=stdeb.command bdist_deb
```

<!-- #### Install Deb

```
sudo apt install python3-pymongo python3-gridfs python3-pymongo-ext python3-bson
sudo dpkg -i python3-mediadata_0.1.5-1_all.deb
``` -->

