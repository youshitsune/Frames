import typer
import cv2
import os

def main(path: str):
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
            print(name)
            cv2.imwrite(name, frame)

            currentframe +=1
        else:
            break

    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    typer.run(main)
