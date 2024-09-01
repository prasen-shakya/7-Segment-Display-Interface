<h1>Seven Segment Display Interface</h1>

<h2>Overview</h2>
<p>A user-friendly GUI built with pygame and pyserial that allows the user to control a 7-segment display connected to an Arduino via serial communication. The interface sends commands to the Arduino
to turn off or on certain segments on the display.</p>

GUI            |  Hardware
:-------------------------:|:-------------------------:
![image of the GUI](https://github.com/user-attachments/assets/9a909354-3cb0-42ed-af4d-aefa7452212d) | ![image of the hardware](https://github.com/user-attachments/assets/c0629243-1fea-4d5b-a1ea-dcf9d9f8f2d9)







<h2>Requirements</h2>
<ul>
  <li>Arduino</li>
  <li>Resistor</li>
  <li>7 Segment Display</li>
  <li>9 Jumper Wires</li>
  <li>USB Cable For Serial Communication</li>
</ul>

<h2>Set Up</h2>
<h3>Arduino</h3>
<p>Set up the Arduino according to the Tinkercad diagram as shown:</p>

![Diagram of Arduino](https://github.com/user-attachments/assets/fb5c6e58-aa22-4fd6-8c14-af01e63b0013)


Follow this, upload [sketch.ino](sketch.ino) into the Arduino using the Arduino IDE


<h2>Installation</h2>
<ol>
  <li><b>Install Pygame:</b></li>

  ```
  pip install pygame
  ```

  <li><b>Install PySerial:</b></li>

  ```
  pip install pyserial
  ```

 <li><b>Clone or download this repository </b> to your local machine.</li>
</ol>
