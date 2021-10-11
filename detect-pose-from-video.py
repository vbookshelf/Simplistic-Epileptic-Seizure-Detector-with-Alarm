
import cv2
import mediapipe as mp
import numpy as np
import time
import serial

# Notes:
# 1- mediapipe uses RGB images

# .......................................
# Set up serial comms between this 
# python script and the Arduino.


# To get the port name to enter below:
# Make sure that the Arduino is connected to the laptop.
# In the Arduino IDE select Tools and look at the port name.
# You will see: /dev/cu.usbmodem14201 (Arduino Uno)
# The port name is: dev/cu.usbmodem14201
# Note that when you use a different USB connection on your computer,
# the port name may also change and your code won't work.

# timeout=1 means that if there's an issue with the serial connection,
# after 1 second it will timeout and it won't freeze up the entire script.

##################################

# Change this to your port

my_port = "/dev/cu.usbmodem14201"

##################################


ser = serial.Serial(my_port, 9600, timeout=1)

# Flush the buffer of any additional information.
ser.flush()


# ser.name returns the name of the port that's
# actually being used.
# See: https://pythonhosted.org/pyserial/shortintro.html#opening-serial-ports
# Here I'm using it as a way to check that serial communication
# has been established.

# if serial communication has been established
if ser.name:
	
	# get the name of the port being used
	port = ser.name
	
	# print a status message
	print(f'Serial comms established on port: {port}')


	
# .......................................	





# Define the colours
WHITE_COLOR = (224, 224, 224)
BLACK_COLOR = (0, 0, 0)
RED_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 128, 0)
BLUE_COLOR = (255, 0, 0)


mp_pose = mp.solutions.pose
pose = mp_pose.Pose() # there are parameters that can be entered here

# to draw the landmarks
mp_draw = mp.solutions.drawing_utils



# Create a video capture object
# ..............................

# For Video file:
# create a video capture object
#cap = cv2.VideoCapture('videos/couple.mp4')

# For Webcam:
# Using webcam number 0.
cap = cv2.VideoCapture(0)
video_width = 640
video_height = 480
cap.set(3, video_width)
cap.set(4, video_height)



# A video is just a sequence of images.
# Create a loop to loop through each image.
	
start_time = 0
seizure_status = 0

while True:

	
	# 'success' is a boolean that indicates if the image was read.
	# 'image' is the image frame that was read.
	success, image = cap.read()
	
	# convert the image from BGR to RGB
	image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	
	# process the image and store the results in an object
	results = pose.process(image_rgb)
	
	#print(results.pose_landmarks)
	
	
	# Draw a rectangle on the screen
	# This where we will be writing the seizure status.
	cv2.rectangle(image, (25, 130), (100, 200), BLUE_COLOR, cv2.FILLED)
	
	
	# This is how to create a black background image
	h, w, c = image.shape
	black_image = np.zeros((h, w, c)) + 255
	
	# Choose to display the original image or
	# a black background.
	display_image = image
	#display_image = black_image
	
	
	if results.pose_landmarks:
		
		x_list = []
		y_list = []
		
		
		# draw the lanmarks on the image (as dots)
		mp_draw.draw_landmarks(image, results.pose_landmarks)
		
		
		# draw connections between the dots
		mp_draw.draw_landmarks(display_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
		
		
		
		# Extract each coord
		
		# By following this link you will find a diagram that shows which index values
		# correspond to which points on a hand:
		# https://google.github.io/mediapipe/solutions/pose
		# The origin point (0,0) on images is in the top left corner.
		
		for id, lm in enumerate(results.pose_landmarks.landmark):
			
			h, w, c = image.shape
			#print(id, lm)
			
			
			# Get the x and y coords of the dot
			# The coords of each point (dot) are specified as a ratio of the image size.
			# We need to convert that ration into a length.
			cx = int(lm.x * w)
			cy = int(lm.y * h)
			
			# Add the x and y coords to a list.
			# The position in the list corresponds to the landmark number e.g.
			# landmark 12 is at x_list[12].
			x_list.append(cx)
			y_list.append(cy)
			
			# draw a circle overlaid over the dots
			#cv2.circle(display_image, (cx, cy), 5, (255,0,0), cv2.FILLED)
			
			
			# These are the landmarks that we will be using:
			# shoulders and hips
			
			# 11 - left_shoulder
			# 12 - right_shoulder
			# 23 - left_hip
			# 24 - right_hip
			
			id_list = [11, 12, 23, 24]
			
			# Draw a circle at each landmark in id_list so we
			# can easily see them in the output.
			if id in id_list:

				# draw a circle overlaid over the dots
				cv2.circle(display_image, (cx, cy), 10, (255,255,255), cv2.FILLED)
				
				
		# If some parts of the body are not visible
		# then their landmarks may not be detected.
		# This if statement checks that the keypoints we need
		# have been detected.	
		if len(y_list) >= 23:
			
			# if the left hip is above the left shoulder
			# We use less than (<) because the origin is in the top left corner.
			if y_list[23] < (y_list[11] - 10):
				
				seizure_status = 1
				
			else:
				seizure_status = 0
				
			
		# If some parts of the body are not visible
		# then their landmarks won't be detected.
		# This if statement checks that the keypoints we need
		# have been detected.	
		if len(y_list) >= 24:
			
			# if the left hip is above the left shoulder
			# We use less than (<) because the origin is in the top left corner.
			if y_list[24] < (y_list[12] - 10):
				
				seizure_status = 1
				
			else:
				seizure_status = 0
				
				
				
		
		# ser.name returns the name of the port that's
		# actually being used.
		# Here I'm using it as a way to check that serial communication
		# has been established.
		if ser.name:
		
			if seizure_status == 1:
			
				# --> Send a communication to the Arduino.
				# Note that we add a newline character because
				# the Arduino code reads up to a newline character.
				ser.write(b"one\n")
				
			
			if seizure_status == 0:
			
				# --> Send a communication to the Arduino.
				ser.write(b"zero\n")
			
			
			
			
		# write the seizure status onto the webccam image
		cv2.putText(image, str(seizure_status), (50, 180), cv2.FONT_HERSHEY_PLAIN, 3,
		WHITE_COLOR, 3)
		
		
	# If there's no person in the image		
	else:
		
		print("No person detected")
		
			
	
	# Get the frame rate
	current_time = time.time()
	fps = 1/(current_time - start_time)
	start_time = current_time
	
	# Display the frame rate on the image (top left corner)
	cv2.putText(display_image, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
				(255,255,255), 3)
				
				
	
	# Display the video frame
	cv2.imshow('Video', display_image)

	
	
	# This adds a delay and stops the video when q is pressed
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
		
		
		