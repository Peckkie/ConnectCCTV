
import numpy as np
import pandas as pd
import cv2
import os
import datetime
import sys


def connectCCTV():

    save_interval = 2 # The default value for setting the number of seconds of the desired image

    name = 'CCTV_IP_111' # [1] Setting name folder for save save frame in subfolder
    name = os.path.join(os.getcwd(), name) # Create head path name for save image
    print("ALl logs saved in dir:", name)
    os.makedirs(name, exist_ok=True) # Create head path

    # cap = cv2.VideoCapture("rtsp://admin:HD123456@192.168.1.111:554/Streaming/Channels/1/") # [2] Setting username, password and IP of CCTV
    cap = cv2.VideoCapture(0)
    fps = int(cap.get(cv2.CAP_PROP_FPS)) # Keep fps of CCTV

    while True: # Endless loop repeat
        date = datetime.datetime.now() # First timer

        dir = str(date.strftime("%Y"))+str(date.strftime("%m"))+str(date.strftime("%d"))+'_'+str(date.strftime("%H-%M-%S")) # Folder name keep image
        path = name + '/' + str(dir) # Create name path for keep image
        os.makedirs(path, exist_ok=True) # Create sub path

        print((int(cap.get(3)), int(cap.get(4)))) # Show resolution of image
        print(fps) # Show fps
        print(path) # Show sub path

        count = 1 # The default value for count frame

        while cap.isOpened(): # Started capturing the frames

            for i in range(1, 61): # [3] Setting count frame by computing fps*sec
            
                ret, frame = cap.read() # Read the frames from our video. It return ret and actual frame
                
                if ret == True: # The ret is true if the frame is read successfully

                        cv2.imwrite(path + '/' + str(i) + '.jpg', frame) # Save image
                        
                        if count % (fps * save_interval) == 0: # Condition keep image every 2 sec.
                            date = datetime.datetime.now() # Next timer
                            dir = str(date.strftime("%Y"))+str(date.strftime("%m"))+str(date.strftime("%d"))+'_'+str(date.strftime("%H-%M-%S")) # Folder name keep image
                            path = name + '/' + str(dir) # Create name path for keep image
                            os.makedirs(path, exist_ok=True) # Create sub path
                            print(path) # Show sub path
                        
                        count += 1

        cap.release() # Release the camera when it's done.
        cv2.destroyAllWindows() #  Simply destroys all the windows we created

    return path