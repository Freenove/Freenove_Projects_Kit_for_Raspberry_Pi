##############################################################################
Chapter Infrared Motion Sensor
##############################################################################

In this chapter, we will learn a widely used sensor, Infrared Motion Sensor. 

Project 22.1 PIR Infrared Motion Detector with LED Indicator
****************************************************************

In this project, we will make a Motion Detector, with the human body infrared pyroelectric sensors.

When someone is in close proximity to the Motion Detector, it will automatically light up and when there is no one close by, it will be out.

This Infrared Motion Sensor can detect the infrared spectrum (heat signatures) emitted by living humans and animals.

Component Knowledge
================================================================

The following is the diagram of the Infrared Motion Sensor(HC SR-501)a PIR Sensor:

.. list-table:: 
    :width: 100%
    :align: center
    :class: product-table

    *   -   Top
        -   Bottom 
        -   Schematic
    
    *   -   |Chapter22_00|
        -   |Chapter22_01|
        -   |Chapter22_02|

.. |Chapter22_00| image:: ../_static/imgs/22_Infrared_Motion_Sensor/Chapter22_00.png
.. |Chapter22_01| image:: ../_static/imgs/22_Infrared_Motion_Sensor/Chapter22_01.png
.. |Chapter22_02| image:: ../_static/imgs/22_Infrared_Motion_Sensor/Chapter22_02.png

Description: 

1.	Working voltage: 5v-20v(DC) Static current: 65uA.

2.	Automatic Trigger. When a living body enters into the active area of sensor, the module will output high level (3.3V). When the body leaves the sensor's active detection area, it will output high level lasting for time period T, then output low level(0V). Delay time T can be adjusted by the potentiometer R1.

3.	According to the position of Fresnel lenses dome, you can choose non-repeatable trigger modes or repeatable modes.

L: non-repeatable trigger mode. The module outputs high level after sensing a body, then when the delay time is over, the module will output low level. During high level time, the sensor no longer actively senses bodies.  

H: repeatable trigger mode. The distinction from the L mode is that it can sense a body until that body leaves during the period of high level output. After this, it starts to time and output low level after delaying T time.

4.	Induction block time: the induction will stay in block condition and does not induce external signal at lesser time intervals (less than delay time) after outputting high level or low level 

5.	Initialization time: the module needs about 1 minute to initialize after being powered ON. During this period, it will alternately output high or low level. 

6.	One characteristic of this sensor is when a body moves close to or moves away from the sensor's dome edge, the sensor will work at high sensitively. When a body moves close to or moves away from the sensor's dome in a vertical direction (perpendicular to the dome), the sensor cannot detect well (please take note of this deficiency). Actually this makes sense when you consider that this sensor is usually placed on a celling as part of a security product. Note: The Sensing Range (distance before a body is detected) is adjusted by the potentiometer.

We can regard this sensor as a simple inductive switch when in use.

Component List
================================================================

+------------------------------------------------+
| Freenove Projects Board for Raspberry Pi       |
|                                                |
|  |Chapter01_04|                                |
+---------------------+--------------------------+
| Raspberry Pi        | GPIO Ribbon Cable        |
|                     |                          |
|  |Chapter01_05|     |  |Chapter01_06|          |
+---------------------+--------------------------+
| Jumper Wire         | HC SR501                 |
|                     |                          |
|  |Chapter05_02|     |  |Chapter22_00|          |
+---------------------+--------------------------+

.. |Chapter01_04| image:: ../_static/imgs/1_LED/Chapter01_04.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter01_06| image:: ../_static/imgs/1_LED/Chapter01_06.png
.. |Chapter05_02| image:: ../_static/imgs/5_RGB_LED/Chapter05_02.png
.. |Chapter22_00| image:: ../_static/imgs/22_Infrared_Motion_Sensor/Chapter22_00.png

Circuit
================================================================

.. list-table:: 
    :width: 100%
    :align: center
    :class: product-table

    *   -   Schematic diagram
    *   -   |Chapter22_03|
    *   -   Hardware connection:
    *   -   |Chapter22_04|

.. |Chapter22_03| image:: ../_static/imgs/22_Infrared_Motion_Sensor/Chapter22_03.png
.. |Chapter22_04| image:: ../_static/imgs/22_Infrared_Motion_Sensor/Chapter22_04.png

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com

**How to use this sensor?**

.. list-table:: 
    :width: 100%
    :align: center
    :class: product-table

    *   -   Top
        -   Bottom 
    
    *   -   |Chapter22_00|
        -   |Chapter22_01|

Description: 

1.	You can choose non-repeatable trigger modes or repeatable modes.

L: non-repeatable trigger mode. The module outputs high level after sensing a body, then when the delay time is over, the module will output low level. During high level time, the sensor no longer actively senses bodies.  

H: repeatable trigger mode. The distinction from the L mode is that it can sense a body until that body leaves. After this, it starts to time and output low level after delaying T time.

2.	R1 is used to adjust HIGH level lasting time when sensor detects human motion, 1.2s-320s.

3.	R2 is used to adjust the maxmum distance the sensor can detect, 3~5m.

:red:`Here we connect L and adjust R1 and R2 like below to do this project.`

:red:`Put you hand close and away from the sensor slowly. Obsever the LED in previous circuit.`

:red:`It need some time between two detections.`

.. image:: ../_static/imgs/22_Infrared_Motion_Sensor/Chapter22_05.png
    :align: center

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com

Sketch
================================================================

Sketch 18.1.1 SenseLED
----------------------------------------------------------------

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com

First, enter where the project is located:

.. code-block:: console

    /home/pi/Freenove_Kit/Processing/Sketches/Sketch_18_1_1_SenseLED

And then right-click to select Processing IDE

.. image:: ../_static/imgs/22_Infrared_Motion_Sensor/Chapter22_13.png
    :align: center

Or you can enter a command in the terminal to open the file Sketch_18_1_1_SenseLED. (The following is only one line of command. There is a Space after Processing.)

.. code-block:: console

    processing ~/Freenove_Kit/Processing/Sketches/Sketch_18_1_1_SenseLED/Sketch_18_1_1_SenseLED.pde

Open Processing and click Run

.. image:: ../_static/imgs/22_Infrared_Motion_Sensor/Chapter22_14.png
    :align: center

The result is as shown below. When the sensor detects a person's movement, it will light up LED. 

.. image:: ../_static/imgs/22_Infrared_Motion_Sensor/Chapter22_15.png
    :align: center

The following is program code:

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_18_1_1_SenseLED/Sketch_18_1_1_SenseLED.pde
    :linenos: 
    :language: c
    :dedent:

In this project, the code is relatively simple. In the function draw(), read level of sensor pin. When it is a high level, LED is turned on. At the same time the filled color will be changed to green. When the level is low, LED turns off and the filled color turns white. Finally, it draws a circle.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_18_1_1_SenseLED/Sketch_18_1_1_SenseLED.pde
    :linenos: 
    :language: c
    :lines: 17-29
    :dedent:

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com