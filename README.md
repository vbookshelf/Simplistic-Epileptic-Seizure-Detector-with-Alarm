## Simplistic-Epileptic-Seizure-Detector-with-Alarm

(UNDER CONSTRUCTION)

This project demonstrates a simplistic way to use MediaPipe pose detection, a laptop, a laptop webcam, an Arduino and a piezoelectric buzzer to automatically detect when a person is experiencing an epileptic seizure. When the seizure is detected, the system triggers an audible alarm to call for help.

Someone with greater knowledge of epileptic seizures could use this basic approach as a starting point to create a more sophisticated seizure detector.

### How this works

1- Google MediaPipe has a Pose detector that outputs 32 keypoints for different locations on the body. The model runs on a CPU. This is an example:

<br>
<img src="https://github.com/vbookshelf/Simplistic-Epileptic-Seizure-Detector-with-Alarm/blob/main/images/key-points.png" width="300"></img>
<i>Image by Ben Weber on Unsplash</i><br>
<br>

2- There are different types of seizures. But during some seizures the person's body goes into the position shown in the figure below. You will note that the shoulders are below the hips.

<br>
<img src="https://github.com/vbookshelf/Simplistic-Epileptic-Seizure-Detector-with-Alarm/blob/main/images/seizure-pose.png" width="400"></img>
<i>Source:</i> https://miamineurosciencecenter.com/en/conditions/epilepsy/<br>

<br>

3- We apply the MediaPipe pose detection model to the real-time video feed of the person being monitored. When the hip keypoints are found to be above the shoulder keypoints the system infers that the person is having and seizure. A signal is sent from the python code running on the laptop to the Arduino using serial communication. This triggers an alarm.

### Alternative Approaches

1- Create a trigger word detection system that will detect the Epileptic Cry. This is the same approach as the well knpw trigger words "Hey Google" and "Hey Siri".<br>
2- Train a model to detect seizure poses in the same way that models are trained to detect sign language hand signs. If this system was being created to be used to monitor just one person then the training image data could be created from seizure videos of that person.

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


