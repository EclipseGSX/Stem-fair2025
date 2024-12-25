
# "Yellow" there!

You probably found this domain from scaning the QRL at my stemfair board. $${\color{green}Great!!!}$$
In this domain/repository, it will contain the two main code required for the hand detection model.

&nbsp;

If you see anything that could be improve upon feel free to write a comment!

&nbsp;

$${\color{red}REQUIREMENTS:}$$
&nbsp;

For the code to function you have to import and download somethings and follow the steps below.
- install visual studio code and set the code language to python
- install arduino ide
- import standered firmata onto both of your board's

  &nbsp;
- $${\color{red}How?:}$$ Upload the code for each arduino, one by one/when you have finished uploading for one arduino, unplug it, plug in the other board, select the board port and then upload it
  - step by stpe guide: https://www.instructables.com/Arduino-Installing-Standard-Firmata/
- Copy and past the code from the assistance module.
  - Can be found here
    
  ![Instruction quatre](https://github.com/user-attachments/assets/c864475e-16e4-4e22-89c6-75258a2c8e16)

  &nbsp;

- Aquire both of your arduino ports id and then import it into the blank space for
  
&nbsp;
<pre> Arduino_port = Arduino('YOUR VALUE HERE') </pre>
<pre> Arduino_port2 = Arduino('YOUR VALUE HERE') </pre>

&nbsp;

- Arduino 1 = fingers being raised up and down
- Arduino 2 = fingers being lowred
  &nbsp;
  
  - This is very $${\color{red}IMPORTANT}$$ since it would show which ardunio shows what reaction.
  &nbsp;

 - These ports values can be found when you select your communication ports in arduino.
    - (the identity of the port are different for differnt devices and arduinos SO DO NOT COPY THE PORTS VALUE UNDERNEATH AND FIND YOUR OWN)
 
  &nbsp;

-  $${\color{red}For}$$  $${\color{red}Example:}$$

  &nbsp;
- For windows: We would type "Com3" since that is the port for the arduino on windows
  
  ![Instruction duo](https://github.com/user-attachments/assets/969650dd-9c4a-4c83-82d6-d2019e57a3d8)

  &nbsp;

- For Mac: We would type "/dev/cu.usbmodem11201" since that is the port for the arduino on mac
  
![instruction trois](https://github.com/user-attachments/assets/6b327f6e-ec8b-4391-86d0-3bacfd373b3f)


- Run the code
  
- Name the code:

<pre> Assistance_module </pre>  

The name have to be very specific so that the code which operates the whole things can refer to it 

- Do $${\color{red}NOT}$$ worry if there is a error, the purpose was to just open the terminal.
  
- Go into your terminal.
  
  ![Instruction uno](https://github.com/user-attachments/assets/adc15f03-8bc7-4d4d-b5f9-c04bd100fd86)
  
  - (The terminal is the giant rectangle at the bottom of your screen)
  
&nbsp;


- In terminal type:
  <pre>pip install mediapipe</pre>
  
   - this installs mediapipe
&nbsp;
- In terminal type:
  <pre> pip install opencv-python</pre>
  - this installs opencv
&nbsp;

- In terminal type:
  <pre>pip install pyfirmata2</pre>
  - this installs pyfirmata2

And $${\color{green}Voila!}$$ you are done with the python part for assistance module great job, Now the main system...... (Pt1 out of 2)

&nbsp; 

Pt2 = https://github.com/EclipseGSX/Stemfair2025_Main_module 






