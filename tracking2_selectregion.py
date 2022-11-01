import cv2

video = cv2.VideoCapture("bb3.mp4")

# Load tracker 
tracker = cv2.TrackerCSRT_create()


# Read the first frame of the video
returned, img = video.read()

 # Select the bounding box on the image
bbox = cv2.selectROI("Tracking", img, False)

# Initialise the tracker on the img and the bounding box
tracker.init(img, bbox)
print(bbox)

cv2.imshow("result", img)

