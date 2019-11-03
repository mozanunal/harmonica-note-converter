from __future__ import print_function
from musthe import *

def convertNoteMap(noteMap):
    newNoteMap = {}
    for key, value in noteMap.items():
        newNoteMap[key] = Note(value).number
    return newNoteMap

class Song(object):
    def __init__(self, name):
        self.name = name
        self.noteList = []
        self.lineBreakList = []


    def shift(self, ratio):
        newNoteList = []
        for note in self.noteList:
            newNoteList.append(note+ratio)
        self.noteList = newNoteList

    def getFromTabs(self, noteMap, tabs):
        tabList = []
        # read file
        counter = 0
        for line in tabs.splitlines():
            for tab in line.split(" "):
                if tab is not "":
                    tabList.append(tab)
                    counter += 1
            self.lineBreakList.append(counter)
        # convert generic notes
        for tab in tabList:
            self.noteList.append(
                Note( noteMap[tab] ).number
            )

    def exportTabs(self, noteMap):
        convertedNoteMap = convertNoteMap(noteMap)
        invNoteMap = {v: k for k, v in convertedNoteMap.items()}
        tabs = []
        for note in self.noteList:
            try:
                tabs.append( invNoteMap[ note ] )
            except:
                tabs.append( "XX" )
        self.printTabs(tabs)
        return tabs

    def printNotes(self):
        print ("--------------")
        print (self.name)
        for id, note in enumerate(self.noteList):
            if id in self.lineBreakList:
                print("")
            print(str(note.letter)+str(note.accidental)+str(note.octave),)
        print ("\n--------------")

    def printTabs(self, tabs):
        print ("--------------")
        print (self.name)
        for idx, tab in enumerate(tabs):
            if idx in self.lineBreakList:
                print("")
            print(tab, end=" ")
        print ("\n--------------")

        
