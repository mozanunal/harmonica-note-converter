
from harmonica import swan1040, diatonic_C
from song import Song

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


gotTheme.shift(-12)
gotTheme.exportTabs(swan1040)



gotTheme.shift(+14)
gotTheme.exportTabs(swan1040)