import cv2

video = cv2.VideoCapture("bb3.mp4")

while True:
    returned, img = video.read()

    cv2.imshow("result", img)

    key = cv2.waitKey(25)
    if key == 32:
        print("Stopped")
        break
