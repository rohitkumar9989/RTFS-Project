import cv2 
from ultralytics import YOLO

model=YOLO("best.pt")
vid= cv2.VideoCapture(0)
while (True):
    _, frame= vid.read()
    results=model.predict(source=frame, show=True, conf=0.85)
    print (results)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
