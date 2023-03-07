from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2


print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()   #uncomment this line incase of using webcam
# vs = VideoStream(usePiCamera=True).start()   #uncomment this line incase of using usbcam
time.sleep(2.0)

# loop over the frames from the video stream
while True:
	# grab the frame from the threaded video stream and resize it to
	# have a maximum width of 400 pixels
	img = vs.read()
	img = imutils.resize(img, width=400)
	barcodes = pyzbar.decode(img)

	for barcode in barcodes:
		x,y,w,h = barcode.rect
		cv2.rectangle(img,(x,y),(x+w,y+h),0,0,255,4)
		bdata = barcode.data.decode("utf-8")
		btype = barcode.type
		text = f"{bdata},{btype}"
		cv2.putText(img,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)
		

	cv2.imshow("img",img)
	key = cv2.waitKey(0)
	if key == ord("q"):
		break
cv2.destroyAllWindows()