import os
import time
import random
import cv2
import dropbox

def snapshot():
    imageName = ""
    cap = cv2.VideoCapture(0)
    result = True
    while result:
        ret, frame = cap.read()
        randomID = random.randint(0, 1000)
        imageName = f"security{randomID}.jpg"
        cv2.imwrite(imageName, frame)   
        result = False
    cap.release()
    cv2.destroyAllWindows()
    print("Snapshot Taken")
    return imageName

def uploadFile(fromFile, toDir):
    accessToken = "RgK7dekoPiUAAAAAAAAAAaAXcXUnSB45lCxGe2bo65cz-m5bWzgci2sn2FHW4IX1"
    dbx = dropbox.Dropbox(accessToken)
    with open(fromFile, 'rb') as f:
        dbx.files_upload(f.read(), toDir, mode=dropbox.files.WriteMode.overwrite)
    print("Files Has Been Uploaded")

def main():
    start_time = time.time()
    while True:
        current_time = time.time()
        time_change = current_time - start_time
        print(time_change)
        if time_change >=  10:
            snappedImage = snapshot()

            print(snappedImage)
            uploadFile(snappedImage, "/C102SecurityImages/" + snappedImage)
            start_time = time.time()
        
if __name__ == '__main__':
    main()

