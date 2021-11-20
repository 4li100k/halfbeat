# pyinstaller --onefile hb_pydub.py

from pydub import AudioSegment
import os #for creating the output folder
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

print("Launching file picker")
Tk().withdraw()
filepath = askopenfilename(initialdir = ".",title = "Select file",filetypes = (("supported sound files","*.wav *.mp3 *.ogg *.flv *.wma *.mp4"),("all files","*.*")))
format = filepath.split(".")[-1]
if format == "mp3":
    song = AudioSegment.from_mp3(filepath)
elif format == "wav":
    song = AudioSegment.from_wav(filepath)
elif format == "ogg":
    song = AudioSegment.from_ogg(filepath)
elif format == "flv":
    song = AudioSegment.from_flv(filepath)
elif format in ["mp4", "wma"]:
    song = AudioSegment.from_file(filepath, format)
else:
    print("not a supported file")
    raise SystemExit(0)
sr = 1000
bpm = int(input("Enter the BPM of the audio file: "))
usek = (60/bpm)*sr
pocet_usekov = round(song.duration_seconds*sr/usek)
print("Processing...")
newsong = AudioSegment.empty()
for i in range(pocet_usekov):
    if (i % 2) == 0 and i != 0:
        newsong = newsong + song[round((i-1)*usek):round(i*usek)]
output_folder = "./output"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
filename = filepath.split("/")[-1].split(".")[0]
newsong.export(output_folder + "/hb_" + filename + "." + format, format = format)