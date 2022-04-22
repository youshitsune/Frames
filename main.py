from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
from tkinter import StringVar
import cv2
import os

root = Tk()

root.title("Frames")

root.geometry("400x400")

text = StringVar()

def open_file():
    file = askopenfile(mode='r',filetypes=[("All Files", '*.*')])
    if file:
        file_path = os.path.abspath(file.name)
        start(file_path)

caution = Label(root, text = "Caution: When you select file you can't stop making images from GUI. If you want to stop making images you have to do it from terminal").pack()
file_button = Button(root, text="Select a video file", command=open_file).pack(pady=20)
label = Label(root, textvariable=text).pack()
exit_button = Button(root, text="Exit", width=20, command=root.destroy).pack(pady=20)
def start(path):
    global label
    video = cv2.VideoCapture(path)

    try:
        if not os.path.exists('data'):
            os.makedirs('data')

    except OSError:
        print('Error: Creating a directory')

    currentframe = 0

    while True:
        ret, frame = video.read()

        if ret:
            name = './data/frame' + str(currentframe) + '.jpg'
            text.set(f"Creating... {name}")
            root.update_idletasks()
            cv2.imwrite(name, frame)

            currentframe +=1
        else:
            break

    cam.release()
    sys.exit()

root.mainloop()
