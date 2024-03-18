import cv2
url='http://192.168.29.124:8080/video'


cap=cv2.VideoCapture(url)
cap_webcam=cv2.VideoCapture(0)
framesize=(720,520)

while True:
    ret,frame=cap.read()
    ret_webcam,frame_webcam=cap_webcam.read()
    frame_webcam=cv2.resize(frame_webcam,framesize)
    frame=cv2.resize(frame,framesize)
    
    combined=cv2.hconcat([frame,frame_webcam])
    
    
    
    cv2.imshow("mobilecam",combined)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):#changing into ascii value of q
        break
    
cap.release()
cap_webcam.release()

cv2.destroyAllWindows()