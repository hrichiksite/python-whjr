import cv2
import time
import random
import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

token = "00000000000"
dropbox_utility = TransferData(token)

def take_snapshot(imgName):
    videoCapture = cv2.VideoCapture(0) # initialize video capture object
    result = True
    while (result):
        ret, frame = videoCapture.read() # read the video frame when camera is active
        cv2.imwrite(imgName , frame) # save the image
        result = False
    
    videoCapture.release() # release the camera
    cv2.destroyAllWindows() # close all the opened windows


while True:
    imgName = "image_" + str(time.time()) + ".jpg"
    take_snapshot(imgName)
    dropbox_utility.upload_file(imgName, "/" + imgName)
    print('got picture')
    time.sleep(5)
