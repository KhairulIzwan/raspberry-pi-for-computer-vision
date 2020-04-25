# import the necessary packages
from imutils.video import VideoStream
from datetime import datetime
import argparse
import signal
import time
import cv2
import sys
import os

# function to handle keyboard interrupt
def signal_handler(sig, frame):
	print("[INFO] You pressed `ctrl + c`! Your pictures are saved" \
	" in the output directory you specified...")
	sys.exit(0)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", required=True,
help="Path to the output directory")
ap.add_argument("-d", "--delay", type=float, default=5.0,
help="Delay in seconds between frames captured")
ap.add_argument("-dp", "--display", type=int, default=0,
help="boolean used to indicate if frames should be displayed")
args = vars(ap.parse_args())

# initialize the output directory path and create the output
# directory
outputDir = os.path.join(args["output"],
datetime.now().strftime("%Y-%m-%d-%H%M"))
os.makedirs(outputDir)

# initialize the video stream and allow the camera sensor to warmup
print("[INFO] warming up camera...")
vs = VideoStream(src=0).start()
#vs = VideoStream(usePiCamera=True, resolution=(1920, 1280), 
#framerate=30).start()
time.sleep(2.0)

# set the frame count to zero
count = 0

# signal trap to handle keyboard interrupt
signal.signal(signal.SIGINT, signal_handler)
print("[INFO] Press `ctrl + c` to exit, or 'q' to quit if you have" \
" the display option on...")

# loop over frames from the video stream
while True:
	# grab the next frame from the stream
	frame = vs.read()

	# draw the timestamp on the frame
	ts = datetime.now().strftime("%A %d %B %Y %I:%M:%S%p")
	cv2.putText(frame, ts, (10, frame.shape[0] - 10),
	cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

	# write the current frame to output directory
	filename = "{}.jpg".format(str(count).zfill(16))
	cv2.imwrite(os.path.join(outputDir, filename), frame)

	# display the frame and detect keypresses if the flag is set
	if args["display"]:
		cv2.imshow("frame", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the `q` key is pressed, break from the loop
		if key == ord("q"):
			break

	# increment the count
	count += 1

	# sleep for specified number of seconds
	time.sleep(args["delay"])

# close any open windows and release the video stream pointer
print("[INFO] cleaning up...")
if args["display"]:
	cv2.destroyAllWindows()
vs.stop()
