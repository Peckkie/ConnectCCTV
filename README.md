# ConnectCCTV

## การเชื่อมต่อกล้อง
1. ต้องทราบ IP กล้อง และ admin and password ของกล้อง
2. ตั้งค่า fps ของกล้อง
	- เข้าไปที่เว็บไซต์ของกล้องผ่าน IPCamera: 'http://{IP CAMERA}'
	- login ด้วย admin and password ของกล้อง
	- เลือก Configuration ที่แถบด้านบน
	- เลือก Video/Audio
	- เลือก Frame rate แล้วปรับค่าเป็น fps ที่ต้องการ จากนั้นกด Save
3. ตั้งชื่อ Folder สำหรับ เก็บข้อมูลภาพ โดยเปลี่ยนตัวแปรนี้  name = 'CCTV_IP_111' --> name = ชื่อ Folder
4. นำข้อมูลข้างต้นมาเปลี่ยนค่าในบรรทัดที่มีข้อความนี้

cap = cv2.VideoCapture("rtsp://admin:HD123456@192.168.1.111:554/Streaming/Channels/1/")

ให้เปลี่ยนตรงจุดที่ใส่ * ไว้ 3 ที่
					    *       *           *
cap = cv2.VideoCapture("rtsp://{ADMIN}:{PASSWORD}@{IP CAMERA}:554/Streaming/Channels/1/")

4. แทนค่าจำนวนเฟรมต่อวินาทีทั้งหมดที่ต้องการในบรรทัดนี้
	for i in range(1, 41):
	โดยลงแทนค่าที่ 41 โดยคำนวณจาก (fps*จำนวนวินาทีที่ต้องการ) + 1

----

git clone https://github.com/ChainSirirat/ConnectCCTV.git

conda create -n guts python=3.7 -y
conda activate guts

conda install numpy 
conda install pandas
pip install opencv-python

pip install flask
pip install requests
