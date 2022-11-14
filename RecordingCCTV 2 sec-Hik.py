
import numpy as np
import pandas as pd
import cv2
import os
import datetime
from hikvisionapi import Client

save_interval = 2 
video_codec = cv2.VideoWriter_fourcc("D", "I", "V", "X")

name = 'CCTV_IP_111' # [1] Setting name folder for save save frame in subfolder
name = os.path.join(os.getcwd(), name)
print("ALl logs saved in dir:", name)
os.makedirs(name, exist_ok=True)


# cap = cv2.VideoCapture("rtsp://admin:HD123456@192.168.1.111:554/Streaming/Channels/1/") # [2] Setting username, password and IP of CCTV
# fps = int(cap.get(cv2.CAP_PROP_FPS))
cam = Client('http://192.168.1.111', 'admin', 'HD123456')

dates = datetime.datetime.now()

dir = str(dates.strftime("%Y"))+str(dates.strftime("%m"))+str(dates.strftime("%d"))+'_'+str(dates.strftime("%H-%M-%S"))
path = name + '/' + str(dir)
os.makedirs(path, exist_ok=True)
print(path)

# print((int(cap.get(3)), int(cap.get(4))))

# count = 1
while True:
    # count = 1
    vid = cam.Streaming.channels[102].picture(method ='get', type = 'opaque_data')
            
    bytes = b''
    # with open('screen.jpg', 'wb') as f:
    for chunk in vid.iter_content(chunk_size=1024):
        count = 1

        bytes += chunk
        a = bytes.find(b'\xff\xd8')
        b = bytes.find(b'\xff\xd9')
        if a != -1 and b != -1:
            jpg = bytes[a:b+2]
            bytes = bytes[b+2:]
            frame = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
            # fps = int(cap.get(cv2.CAP_PROP_FPS))
            for i in range(1, 41): # [3] Setting count frame by computing fps*sec
                # cv2.imshow("frame", frame)
                cv2.imwrite(path + '/' + str(i) + '.jpg', frame)
                
                if count % (20 * save_interval) == 0:
                    print(count % (20 * save_interval))
                    date = datetime.datetime.now()
                    dir = str(date.strftime("%Y"))+str(date.strftime("%m"))+str(date.strftime("%d"))+'_'+str(date.strftime("%H-%M-%S"))
                    path = name + '/' + str(dir)
                    os.makedirs(path, exist_ok=True)
                    print(path)
                
                count += 1



# cap.release()
# cv2.destroyAllWindows()