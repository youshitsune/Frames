import cv2
import os
import click

@click.command()
@click.argument('path', type=str)
def start(path):
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
            print('Creating...' + name)

            cv2.imwrite(name, frame)

            currentframe +=1

        else:
            break

    cam.release()
    sys.exit()

if __name__ == '__main__':
    start()
