
import numpy as np
import pandas as pd
import cv2
import os
import datetime

save_interval = 2 
video_codec = cv2.VideoWriter_fourcc("D", "I", "V", "X")

name = 'CCTV_IP_111' # [1] Setting name folder for save save frame in subfolder
name = os.path.join(os.getcwd(), name)
print("ALl logs saved in dir:", name)
os.makedirs(name, exist_ok=True)


cap = cv2.VideoCapture("rtsp://admin:HD123456@192.168.1.111:554/Streaming/Channels/1/") # [2] Setting username, password and IP of CCTV
fps = int(cap.get(cv2.CAP_PROP_FPS))

date = datetime.datetime.now()

dir = str(date.strftime("%Y"))+str(date.strftime("%m"))+str(date.strftime("%d"))+'_'+str(date.strftime("%H-%M-%S"))
path = name + '/' + str(dir)
os.makedirs(path, exist_ok=True)
print(path)

print((int(cap.get(3)), int(cap.get(4))))

count = 1

while cap.isOpened():
    
    ret, frame = cap.read()
    if ret == True:
        for i in range(1, 41): # [3] Setting count frame by computing fps*sec
            cv2.imshow("frame", frame)
            cv2.imwrite(path + '/' + str(i) + '.jpg', frame)
            
            if count % (fps * save_interval) == 0:
                date = datetime.datetime.now()
                dir = str(date.strftime("%Y"))+str(date.strftime("%m"))+str(date.strftime("%d"))+'_'+str(date.strftime("%H-%M-%S"))
                path = name + '/' + str(dir)
                os.makedirs(path, exist_ok=True)
                print(path)
            
            count += 1

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    else:
        break


cap.release()
cv2.destroyAllWindows()