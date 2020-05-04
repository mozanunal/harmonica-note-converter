# Harmonica Note Converter

**Harmonica Note Converter** aims to create a python library to convert notes or tabs for different kind of harmonicas. 
It is based on [musthe](https://github.com/gciruelos/musthe).


## Story

Some of you know that I am an ameteur harmonica player and I love harmonicas. I usually play diatonic harmonicas but last time I have bought a chromatic harmonica, which has quite different tone and it is hard to find music notes for it.

I am not the best at playing instruments. However, I am good at coding and music theory. That's why I decide to develop a tool to convert music notes for any instrument to notes for my harmonicas. I also create an modular structure to define new instruments.

## Getting Started

### Installing 

First, The source code of the project should be cloned to your PC.

```ss
git clone https://github.com/mozanunal/harmonica-note-converter
```

### Demo

To test this project in your computer, you should run following commands.

```sh
cd harmonica-note-converter
python3 test.py
#python test.py
```

It is a video to demonstrate the tone shift feature of my code. It is quite easy to use. I suggest you to have a look in this link and test the script with following code. See you!

## Use It For Your Instruments and Notes 

### Defining Instruments

Example code of C tone diatonic harmonica. You should add your instrument to harmonica folder and add to init file.

```python
diatonic_C = {
    "1": "C2",
    "1*": "C#2",
    "-1": "D2",
    "-1*": "D#2",
    "2": "E3",
    "2*": "E#3",
    "-2": "G2",
    "-2*": "G#2",
    "3": "G2",
    "3*": "G#2",
    "-3": "B2",
    "-3*": "B#2",
    "4": "C3",
    "4*": "C#3",
    "-4": "D3",
    "-4*": "D#3",
    "5": "E3",
    "5*": "E#3",
    "-5": "F3",
    "-5*": "F#3",
    "6": "G3",
    "6*": "G#3",
    "-6": "A3",
    "-6*": "A#3",
    "7": "C4",
    "7*": "C#4",
    "-7": "B3",
    "-7*": "B#3",
    "8": "E4",
    "8*": "E#4",
    "-8": "D4",
    "-8*": "D#4",
    "9": "G4",
    "9*": "G#4",
    "-9": "F4",
    "-9*": "F#4",
    "10": "A4",
    "10*": "A#4",
    "-10": "C5",
    "-10*": "C#5"
}
```

### Converting Tab Between Instruments


Following script is written to convert Game of Thrones theme song tabs
for diatonic C harmonica to chromatic harmonica tabs. In the first part, the tab string is converted to a song object. Then song exported for `swan1040` harmonica. Above this part, you have already learned to implement your instrument. Now, you can export these notes as tab for your instrument.

```python
from harmonica import swan1040, diatonic_C
from song import Song

gotTheme = Song("GoT Theme")
gotTheme.getFromTabs(
    diatonic_C,
"""
-6  -4  -5  +6  -6  -4  -5  +6  +5
+6  +4  +5  -5  +6  +4  -5  +5  -4
-6  -4  -5  +6  -6  -4  -5  +6  +5
+6  +4  +5  -5  +5  +4  -4
-8  +7  -4  -6  -3* -5  +6  -6
-8 +7 +6 -6 -3* -5 +5 -4
""".replace("\t"," ").replace("+","")
)

gotTheme.exportTabs(swan1040)
```

Script output:

```python
GoT Theme
--------------
-7 -5 -6 7 -7 -5 -6 7 6
7 5 6 -6 7 5 -6 6 -5
-7 -5 -6 7 -7 -5 -6 7 6
7 5 6 -6 6 5 -5
-9 -8* -5 -7 5 -6 7 -7
-9 -8* 7 -7 5 -6 6 -5
--------------
```

## Shifting the Tone

The other feature which I implemented is tone shifting. It is possible to shift the tone of the song which you give to the system. Probably, it is quite easy task for real musicians, but it is always a challenge for me. It is quite easy to implememted it with code. In that why, I can easily change the tone of the songs which I want to play with my harmonica.

Test script:

```python
from harmonica import swan1040, diatonic_C
from song import Song

gotTheme = Song("GoT Theme")
gotTheme.getFromTabs(
    diatonic_C,
"""
-6  -4  -5  +6  -6  -4  -5  +6  +5
+6  +4  +5  -5  +6  +4  -5  +5  -4
-6  -4  -5  +6  -6  -4  -5  +6  +5
+6  +4  +5  -5  +5  +4  -4
-8  +7  -4  -6  -3* -5  +6  -6
-8 +7 +6 -6 -3* -5 +5 -4
""".replace("\t"," ").replace("+","")
)

gotTheme.exportTabs(swan1040)


gotTheme.shift(-12)
gotTheme.exportTabs(swan1040)

gotTheme.shift(+14)
```

Output is like:

```python
GoT Theme
--------------
-7 -5 -6 7 -7 -5 -6 7 6
7 5 6 -6 7 5 -6 6 -5
-7 -5 -6 7 -7 -5 -6 7 6
7 5 6 -6 6 5 -5
-9 -8* -5 -7 5 -6 7 -7
-9 -8* 7 -7 5 -6 6 -5
--------------
--------------
GoT Theme

-3 -1 -2 3 -3 -1 -2 3 2
3 1 2 -2 3 1 -2 2 -1
-3 -1 -2 3 -3 -1 -2 3 2
3 1 2 -2 2 1 -1
-5 5 -1 -3 1 -2 3 -3
-5 5 3 -3 1 -2 2 -1
--------------
--------------
GoT Theme

-8 6 7 -7 -8 6 7 -7 -6* 
-7 -5 -6* 7 -7 -5 7 -6* 6 
-8 6 7 -7 -8 6 7 -7 -6*
-7 -5 -6* 7 -6* -5 6
9 -9 6 -8 -5 7 -7 -8
9 -9 -7 -8 -5 7 -6* 6 
--------------
```


## Built With

* [Python](https://python.org/) Python <3
* [musthe](https://github.com/gciruelos/musthe) Music Theory Implementation

## Contributing

Please feel yourself free to add new instruments or new tricks to this mini script.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
