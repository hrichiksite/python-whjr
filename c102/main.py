import cv2

def take_snapshot():
    videoCapture = cv2.VideoCapture(0) # initialize video capture object
    result = True
    while (result):
        ret, frame = videoCapture.read() # read the video frame when camera is active
        cv2.imwrite("image.jpg", frame) # save the image
        result = False
    
    videoCapture.release() # release the camera
    cv2.destroyAllWindows() # close all the opened windows

