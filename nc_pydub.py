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
ratio = float(input("Enter the desired speed ratio: [1.3]") or 1.3)
output_folder = "./output"
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
filename = filepath.split("/")[-1].split(".")[0]
newsong = song._spawn(song.raw_data, overrides={"frame_rate": int(song.frame_rate * ratio)})
newsong = newsong.set_frame_rate(song.frame_rate)
newsong.export(output_folder + "/nc_" + filename + "_x" + str(ratio) +  "." + format, format = format)