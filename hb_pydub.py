from pydub import AudioSegment
import os #for creating the output folder
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

print("Launching file picker")
Tk().withdraw()
filepath = askopenfilename(initialdir = ".",title = "Select file",filetypes = (("supported sound files","*.wav *.mp3 *.ogg *.flv *.wma *.mp4"),("all files","*.*")))
format = filepath.split(".")[-1]
if format in ["mp4", "wma", "mp3", "wav", "ogg", "flv"]:
    song = AudioSegment.from_file(filepath, format)
else:
    print("not a supported file")
    raise SystemExit(0)
sr = 1000
bpm = int(input("Enter the BPM of the audio file: "))
usek = (60/bpm)*sr
print("usek length: " + str(usek))
pocet_usekov = round(song.duration_seconds*sr/usek)
print("Processing...")
newsong1 = AudioSegment.empty()
newsong2 = AudioSegment.empty()
for i in range(pocet_usekov):
    if (i % 2) == 0 and i != 0:
        newsong1 = newsong1 + song[round((i-1)*usek):round(i*usek)]
    else:
        newsong2 = newsong2 + song[round((i-1)*usek):round(i*usek)]
output_folder = "./half_beat_output"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
filename = filepath.split("/")[-1].split(".")[0]
newsong1.export(output_folder + "/hb_" + filename + "a." + format, format = format)
newsong2.export(output_folder + "/hb_" + filename + "b." + format, format = format)