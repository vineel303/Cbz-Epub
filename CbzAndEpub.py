import AppData.Epubs2Pics as Epubs2Pics
import AppData.Cbzs2Pics as Cbzs2Pics
import AppData.Pics2Cbzs as Pics2Cbzs
import TerminalFormatting as f
import os

defaultPath = r"D:\Code\ProgramFiles\Cbz&Epub\#Here"

while True:

    print("0: Epubs to Pictures")
    print("1: Manga to Pictures")
    print("2: Pictures to Manga")
    userInput = int(f.specialInput("Operation: ", f.Dim, f.Red + f.Bold))
    if userInput not in [0, 1, 2]:
        print("Invalid input. Retry.")

    print("Empty string is default path.")
    path = f.specialInput("Folder path: ", f.Dim, f.Red + f.Bold)
    if path:
        if not os.path.isdir(path):
            print("Invalid folder path. Retry.")
            continue
        
    if userInput == 0:
        if path:
            Epubs2Pics.Main(path)
        else:
            Epubs2Pics.Main(defaultPath)
    elif userInput == 1:
        if path:
            Cbzs2Pics.Main(path)
        else:
            Cbzs2Pics.Main(defaultPath)
    else:
        if path:
            Pics2Cbzs.Main(path)
        else:
            Pics2Cbzs.Main(defaultPath)

    print("")
