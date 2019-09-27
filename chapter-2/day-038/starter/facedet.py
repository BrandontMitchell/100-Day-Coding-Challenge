# pip install opencv-python
import cv2
import sys

# Get user supplied values
imagePath = sys.argv[1]
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image

# Detect faces in the image
faces = faceCascade.detectMultiScale(

)

print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    

cv2.imshow("Faces found", image)
cv2.waitKey(0)