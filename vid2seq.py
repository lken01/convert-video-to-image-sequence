import cv2
import numpy as np
import os


def createFolder(directory, dir_path):
    try:
        if not os.path.exists(directory):
            os.makedirs(dir_path + directory)
            return True
    except OSError:
        print('Error creating directory ' + directory)
        return False

if __name__ == '__main__':
    video_no = 16
    left_cam = cv2.VideoCapture("../videos/output_left"+str(video_no)+".avi")
    right_cam = cv2.VideoCapture("../videos/output_right"+str(video_no)+".avi")

    #create folders
    path = '../sequences/'+str(video_no)+'/'
    dir_statL = createFolder('image_0', path)
    dir_statR = createFolder('image_1', path)

    frame_no = 0
    while True:
        if not(left_cam.grab() and right_cam.grab()):
            print("End of frame")
            break

        frame_no += 1

        left_res, left_frame = left_cam.read()
        right_res, right_frame = right_cam.read()

        if left_res is True and right_res is True and \
            dir_statL is True and dir_statR is True:
            print("Writting frame_no", frame_no)
            cv2.imwrite(path+'image_0/'+str(frame_no).rjust(5,'0')+'.png',left_frame)
            cv2.imwrite(path+'image_1/'+str(frame_no).rjust(5,'0')+'.png',right_frame)

        else:
            print('Frame no. {} not written'.format(frame_no))
            continue
