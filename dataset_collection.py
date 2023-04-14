import cv2
import os


cam = cv2.VideoCapture(1)
path = "dataset"
numberOfPics = 0
numberOfAlreadyExistingPics = len(os.listdir(path))

while(True):
    _, frame = cam.read()

    cv2.imshow('Camera', frame)

    if(cv2.waitKey(1) & 0xFF == ord('p')):
        numOfPics = numberOfPics+numberOfAlreadyExistingPics
        cv2.imwrite(path+"/"+str(numOfPics)+".jpg", frame)
        print("Took", numOfPics, "th pic.")
        numberOfPics += 1

        
    elif cv2.waitKey(1) & 0xFF == ord('e'):
        break

cam.release()
cv2.destroyAllWindows()