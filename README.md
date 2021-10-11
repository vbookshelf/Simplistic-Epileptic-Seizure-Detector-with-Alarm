## Simplistic Epileptic Seizure Detector with Alarm

(UNDER CONSTRUCTION)

This project demonstrates a simplistic way to use MediaPipe Pose detection with a laptop, a laptop webcam, an Arduino and a piezoelectric buzzer to automatically detect when a person is having an epileptic seizure. When the seizure is detected, the system triggers an audible alarm to call for help.

Someone with greater knowledge of epileptic seizures could use this basic workflow as a starting point to create a more sophisticated seizure detector.

### How this works

1- Google MediaPipe has a Pose model that outputs 32 landmarks for different locations on the body. Each keypoint has an x,y coordinate with the origin (0,0) in the top left corner of the image. The model runs on a CPU. This is an example of the output:

<br>
<img src="https://github.com/vbookshelf/Simplistic-Epileptic-Seizure-Detector-with-Alarm/blob/main/images/key-points.png" width="300"></img>
<i>Image by Ben Weber on Unsplash</i><br>
<br>



<br>
<img src="https://github.com/vbookshelf/Simplistic-Epileptic-Seizure-Detector-with-Alarm/blob/main/images/pose-landmarks.png" width="600"></img>
<i>Source:</i> https://google.github.io/mediapipe/solutions/pose<br>
<br>

2- By doing a quick Google search I learned that there are different types of seizures. During some seizures the person's body goes into the position shown in the figure below. You will note that the shoulders are below the hips.

<br>
<img src="https://github.com/vbookshelf/Simplistic-Epileptic-Seizure-Detector-with-Alarm/blob/main/images/seizure-pose.png" width="400"></img>
<i>Source:</i> https://miamineurosciencecenter.com/en/conditions/epilepsy/<br>

<br>

3- This approach applies the MediaPipe Pose model to the real-time video feed of the person being monitored. When the y coordinate of the hip landmarks are found to be above the shoulder landmarks the system infers that the person is having a seizure. A signal is then sent from the python code, running on the laptop, to the Arduino. This triggers an alarm.

### Alternative Approaches

This solution, using body keypoint locations, is not robust. Here are a few alternative ways to approach this problem:

1- Train a trigger word detection model to detect the Epileptic Cry. "Hey Google" and "Hey Siri" are examples of well known trigger words.<br>
2- Train a model to detect seizure poses in the same way that models are trained to detect deaf sign language signs or to differentiate between cats and dogs.<br>
3- Train a model to detect a seizure facial expression - in the same way that models are trained to detect emotional facial expressions like "happy" and "sad".

<br>

## Reference Resources

These resources will help you understand what 
the Python and Arduino code is doing.

Latest Pose Estimation Realtime (24 FPS) using CPU | Computer Vision | OpenCV Python 2021<br>
https://www.youtube.com/watch?v=brwgBf6VB0I

Arduino - Send Commands with Serial Communication<br>
https://www.youtube.com/watch?v=utnPvE8hN3o

Arduino - Bidirectional Serial Communication with Raspberry Pi<br>
(It doesn't have to be a Raspberry Pi. It could also be a pc or laptop.)<br>
https://www.youtube.com/watch?v=OJtpA_qTNL0

Google Mediapipe Pose detection <br>
https://google.github.io/mediapipe/solutions/pose

Interfacing Piezoelectric buzzer with Arduino<br>
https://create.arduino.cc/projecthub/akshayjoseph666/interface-buzzer-with-arduino-uno-694059?ref=user&ref_id=600499&offset=3

How to use Buzzer / Piezo - speaker with Arduino + Star Wars theme<br>
https://www.youtube.com/watch?v=zl1o-t_17oQ


Also, if you have never used OpenCV with a webcam then I suggest watching
this tutorial:<br>
https://www.youtube.com/watch?v=WQeoO7MI0Bs&t=305s


Epilepsy and Seizures<br>
Increasing Epilepsy Awareness<br>
https://miamineurosciencecenter.com/en/conditions/epilepsy/

<br>

## How to run this project 

These instructions are for Mac OSX but the process to run a python file in Windows should be similar.

1- Connect your Arduino to a USB port on your laptop.<br>
2- Connect the Piezo Buzzer as shown on the wiring diagram.<br>
3- Upload the arduino-sketch folder to your Arduino.<br>
4- Change the port variable in the arduino-finger-counter.py file to match the port you are using. The steps to do this are described in the detect-pose-from-video.py file.<br>

5- On the command line: Navigate to the folder containing the detect-pose-from-video.py file.<br>
6- On the command line type: python detect-pose-from-video.py<br>
7- A window will open showing what your webcam is seeing.<br>

8- Point the webcam to a place where you can lie down e.g. a couch or bed.<br>
9- Lie down on your back.<br>
10- When you look at the screen you will see that 0 is shown indicating that no seizure has been detected.<br>

11- As you lie on your back, raise your hips.<br>
12- The status shown on the screen will change to 1 and the alarm will be triggered.<br>
13- Press the reset button on the Arduino to silence the alarm.<br>
14- Press q on the keyboard to close the webcam window.<br>

## Packages

These are the packages that I used:

- Python 3.7.0
- OpenCV
- numpy==1.21.2
- mediapipe==0.8.7.3
- pyserial==3.5


