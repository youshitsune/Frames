import cv2
import os

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

