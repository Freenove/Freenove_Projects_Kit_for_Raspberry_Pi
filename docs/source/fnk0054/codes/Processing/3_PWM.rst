##############################################################################
Chapter 3 PWM
##############################################################################

In this chapter, we will learn how to use PWM.

Project 3.1 BreathingLED
****************************************************************

In this project, we will make a breathing LED, which means that an LED that is OFF will then turn ON gradually and then gradually turn OFF like "breathing" and the Display Window will show a breathing LED pattern and a progress bar at the same time.

Component List
================================================================

.. table:: 
    :align: center
    :width: 80%
    :class: table-line
    
    +------------------------------------------+
    | Freenove Projects Board for Raspberry Pi |
    |                                          |
    |  |Chapter01_04|                          |
    +---------------------+--------------------+
    | Raspberry Pi        | GPIO Ribbon Cable  |
    |                     |                    |
    |  |Chapter01_05|     |  |Chapter01_06|    |
    +---------------------+--------------------+

.. |Chapter01_04| image:: ../_static/imgs/1_LED/Chapter01_04.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter01_06| image:: ../_static/imgs/1_LED/Chapter01_06.png

Circuit
================================================================

.. list-table:: 
    :width: 80%
    :align: center
    :class: table-line

    * - Schematic diagram
    * - |Chapter04_02|
    * - Hardware connection:
        
        Switch ON NO.5 switch and the four switches of NO.2.
    * - |Chapter04_03|

.. |Chapter04_02| image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_02.png
.. |Chapter04_03| image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_03.png

.. note::
    
    :combo:`red font-bolder:If you have any concerns, please send an email to:` support@freenove.com

Sketch
================================================================

Sketch 3.1.1 BreathingLED
----------------------------------------------------------------

.. note::
    
    :combo:`red font-bolder:If you have any concerns, please send an email to:` support@freenove.com

First, enter where the project is located:

.. code-block:: console
    
    /home/pi/Freenove_Kit/Processing/Sketches/Sketch_03_1_1_BreadthingLED

And then right-click to select Processing IDE

.. image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_09.png
    :align: center

Or you can enter a command in the terminal to open the file Sketch_03_1_1_BreadthingLED. (The following is only one line of command. There is a Space after Processing.)

.. code-block:: console
    
    processing ~/Freenove_Kit/Processing/Sketches/Sketch_03_1_1_BreadthingLED/Sketch_03_1_1_BreadthingLED.pde

Open Processing and click Run.

.. image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_10.png
    :align: center

The result is as shown below. The LED will light up gradually, and then extinguish and light up again. You can control the brightness with the mouse.

.. image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_11.png
    :align: center

The following is program code:

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_03_1_1_BreadthingLED/Sketch_03_1_1_BreadthingLED.pde
    :linenos: 
    :language: c
    :dedent:

First, use SOFTPWM class to create a PWM pin, which is used to control the brightness of LED. Then define a variable “t” and a variable “tStep” to control the PWM duty cycle and the rate at which “t” increases.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_03_1_1_BreadthingLED/Sketch_03_1_1_BreadthingLED.pde
    :linenos: 
    :language: c
    :lines: 11-13
    :dedent:

In the function draw, if there is a click detected, the coordinate in X direction of the mouse will be mapped into the duty cycle “t”; Otherwise, duty cycle “t” will be increased gradually and PWM with the duty cycle will be output.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_03_1_1_BreadthingLED/Sketch_03_1_1_BreadthingLED.pde
    :linenos: 
    :language: c
    :lines: 21-28
    :dedent:

The next code is designed to draw a circle filled with colors in different depth according to the “t” value, which is used to simulate LEDs with different brightness.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_03_1_1_BreadthingLED/Sketch_03_1_1_BreadthingLED.pde
    :linenos: 
    :language: c
    :lines: 32-33
    :dedent:

The last code is designed to draw the progress bar and the percentage of the progress.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_03_1_1_BreadthingLED/Sketch_03_1_1_BreadthingLED.pde
    :linenos: 
    :language: c
    :lines: 39-48
    :dedent:

In processing software, you will see a tag page "SOFTPWM" in addition to the above code.

.. image:: ../_static/imgs/4_Analog_&_PWM/Chapter04_12.png
    :align: center

Reference
----------------------------------------------------------------

.. py:function:: class SOFTPWM

    public **SOFTPWM** (int iPin, int dc, int pwmRange):
    
    Constructor, used to create a PWM pin, set the pwmRange and initial duty cycle. The minimum of pwmRange is 0.1ms. So pwmRange=100 means that the PWM duty cycle is 0.1ms*100=10ms.
    
    public void softPwmWrite(int value)
    
    Set PMW duty cycle.
    
    public void **softPwmStop** ()
    
    Stop outputting PWM.

.. note::
    
    :combo:`red font-bolder:If you have any concerns, please send an email to:` support@freenove.com