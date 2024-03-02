# Twelve-tone series generator

This program generates and displays a random twelve-tone series.  
  
Twelve-tone series are a type of musical material that can be used to compose music. The method of composing with twelve-tone series, namely the twelve-tone technique, was developped in the 1920s and is still used by some composers nowadays.  
  
## Installation

Install [`python3`](https://www.python.org/).  
  
Install [`music21`](https://web.mit.edu/music21/doc/usersGuide/usersGuide_01_installing.html). On Debian/Ubuntu systems :

```sh
pip install music21
```

Install a XML reader, for example the free software [`Musescore`](https://musescore.org/en).  
  
Configure `music21` so that it recognizes your XML reader. There are two ways to do that :

#### 1st method

Run :  

```sh
python3 -m music21.configure
```

This command will ask you the path to your XML reader.  
However, if it doesn't, use the 2nd method.

#### 2nd method

Run the following Python script by replacing `'ABSOLUTE_PATH_TO_YOUR_XML_READER'` by the aboslute path to your XML reader (e.g. `'/home/julia/.local/bin/MuseScore-4.2.1.240230938-x86_64.AppImage'`).  

```py
from music21 import *
environment.set('musicxmlPath', 'ABSOLUTE_PATH_TO_YOUR_XML_READER')
```

## Usage

Run :

```sh
python3 main.py
```
Your XML reader should open and display a random twelve-tone series.  
