import cv2
url='http://192.168.29.124:8080/video'
url="http://192.168.29.207.8080/video"

cap=cv2.VideoCapture(url)
cap=cv2.VideoCapture(url2)

cap_webcam=cv2.VideoCapture(0)

framesize=(720,520)

while True:
    ret,frame=cap.read()
    ret_webcam,frame_webcam=cap_webcam.read()
    frame_webcam=cv2.resize(frame_webcam,frame_size)
    
    
    
    frame=cv2.resize(frame_webcam,frame_size)
    frame2=cv2.resize(frame2,frame_size)
    
    
    combined=cv2.hconcat([frame,frame_webcam,frame2])
    
    
    
    cv2.imshow("tricam",combined)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):#changing into ascii value of q
        break
    
cap.release()
cap_webcam.release()

cv2.destroyAllWindows()