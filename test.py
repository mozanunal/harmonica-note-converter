from musthe import *
from harmonica import swan1040, diatonic_C
from song import Song

"""Shifting
    intervals = {
        'd1': -1,           'P1': 0,            'A1': 1,
        'd2': 0,  'm2': 1,            'M2': 2,  'A2': 3,
        'd3': 2,  'm3': 3,            'M3': 4,  'A3': 5,
        'd4': 4,            'P4': 5,            'A4': 6,
        'd5': 6,            'P5': 7,            'A5': 8,
        'd6': 7,  'm6': 8,            'M6': 9,  'A6': 10,
        'd7': 9,  'm7': 10,           'M7': 11, 'A7': 12,
        'd8': 11,           'P8': 12,           'A8': 13,
    }
"""


danceOfDeath = Song("Dance Of Death")
danceOfDeath.getFromTabs(
    diatonic_C,
"""
-6 -7 7 -8 7 -6
8 8 -8 7 -7 -6
8 8 9 8 -8 7 -8 7 -6
8 8 -8 7 -7 -6 
"""
)
danceOfDeath.shift(-12)
danceOfDeath.exportTabs( swan1040 )

hobbit = Song("Hobbit")
hobbit.getFromTabs(
    diatonic_C,
"""
4 -4 5 6 5 -4 4
5 6 -6 7 -7 6 5 -5 5 -4
4 -4 5 6 5 -4 4
5 6 -6 -6 6 5 -4
4 -4 5 5 -6 7 -8 7 -7 6 5 -5 5 -4 4 -4 5 
5 -6 7 -8 7 -8 8 8 7 -6 6  6 5 4 -4
"""
)
hobbit.shift(-5)
#hobbit.printNotes()
hobbit.exportTabs( swan1040 )

istanbuldaSonbahar = Song("Istanbulda Sonbahar")
istanbuldaSonbahar.getFromTabs(
    diatonic_C,
"""
4 4 4 4 -4 5
5 -6 6 -5 6 -5
-4 -5 7 -7 -6 6 5
5 5 -5 5 -4 4 -4
4 4 4 4 4 -5 5
4 4 4 4 -4 5
-6 6 -5 6 -5
5 7 -7 -6 6 5
5 -5 5 -4 4 -4 
4 4 -4 4 4 -5 5
-5 -5 5 -5 -6
5 5 5 -4 5 4
-5 -5 5 -5 -6 6 -5 5
-5 -5 5 -5 -6
5 5 -4 5 4
4 4 4 -5 5 -5 5 	
-6 -7 -6 -5
-6 6 -4 5
-6 -7 -6 -5 5 -4     
-4 4 -4 5 -4 5
""".replace("\t","")
)
istanbuldaSonbahar.shift(-12)
istanbuldaSonbahar.exportTabs(swan1040)

hallelujah = Song("Hallelujah")
hallelujah.getFromTabs(
    diatonic_C,
"""
5 6 6 6 6 -6 -6 -6 
5 6 6 6 6 6 -6 -6 -6 
6 -6 -6 -6 -6 -6 6 6 -5 6 6 
5 6 6 6 6 -6 -6 -7 
6 7 7 -6 7 7 -8 
7 -8 -8 -8 -8 8 8 8 -8 -8 7 7 
5 6 -6 -6 -6 6 5 5 
5 6 -6 -6 -6 6 5 -5 5 -4 4 -3 4  
"""
)
hallelujah.shift(-7)
hallelujah.exportTabs(swan1040)

gotTheme = Song("Got Theme")
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

windOfChange = Song("Wind of Change")
windOfChange.getFromTabs(
    diatonic_C,
"""
-6 -7 7 -6 -7 7 -8 7 
-6 -7 7 -6 -7 7 -8 7 
7 -8 8 7 -8 6 7 -7
4 -4 5 4 -4  
-4 5 -5 6 5  
4 -5 5 -4 5 -4 3 4 -3  
4 -4 5 4 -4  
-4 5 -5 6 5  
4 -5 5 -4 5 -4 3 4 -3
5 -4 -4 5 -5 -5 -5 -5 6 -5   
5 -4 5 -4 -4 
-4 5 -5 -5 -5 -5 6 -5 5 -4 5  
4 4 -5 5 -4 
"""
)
windOfChange.shift(-7)
windOfChange.exportTabs(swan1040)


lavienrose = Song("la vien rose")
lavienrose.getFromTabs(
    diatonic_C,
"""
7 -7 -6 6 5 7 -7 
-6 6 5 4 -7 -6 
6 5 4 4 -7 -6 6 
7 -7 -6 6 5 7 -7 
-6 6 5 4 -7 -6
6  5  4   4  -7 -6 6 
7 -7 -6 6 5 7 -7  
-6 6 5 4 -7 -6 
6 5 4 4 -7 -6 6
-8 -8 7 -8 -8 7 -8 -8 7 6 
-8 -8 7 -8 -8 7 -8 -8 7 8 -8 
7 -7 -6 6 5 7 -7  
-6 6 5 4 -7 -6 
6 -6 -6 7 
"""
)
lavienrose.shift(-12)
lavienrose.exportTabs(swan1040)

engman = Song("english man in new york")
engman.getFromTabs(
    diatonic_C,
"""
8 7
7 7 7 -7 -6 
-7 -7 -8 -8  7 -7 -6
-6 -7   7  7  7  -7   6  -6

5 -6  7 -8 -7  6 -5 5 -7 -7 
5 -6  7 -8 -7  6 -5 5 
5 -6 7 -8 -7  6 -5  5 -7 -7 -6 -7
-6 -7 7   7 -7 -6  6 -6 -6

8  8  8  8  9  8    8 -8 -8 -8 -8 -9 -8
7  7  7  7  8  8  7  7  -7
-6 -6 -6 -6  7 -6   -6 -7  -7  -7  -7  -8  -7
-7 -8 -8 -8 -8 -9  8 -8 -8  8
"""
)
engman.shift(-12)
engman.exportTabs(swan1040)



