# import the necessary packages
from imutils.video import VideoStream
import imutils
import time
import cv2

# initialize the video stream and allow the cammera sensor to warmup
print("[INFO] starting video stream...")
vs = VideoStream(src=0).start()
#vs = VideoStream(usePiCamera=True, resolution=(640, 480)).start()
time.sleep(2.0)

# loop over the frames from the video stream
while True:
	# grab the frame from the video stream and resize it to have a
	# maximum width of 400 pixels
	frame = vs.read()
	frame = imutils.resize(frame, width=400)

	# show the output frame
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key was pressed, break from the loop
	if key == ord("q"):
		break

# do a bit of cleanup
cv2.destroyAllWindows()
vs.stop()
