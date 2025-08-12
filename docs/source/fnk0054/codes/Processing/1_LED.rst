##############################################################################
Chapter 1 LED
##############################################################################

We will still start from Blink LED in this chapter, and also learn the usage of some commonly used functions of Processing Software.

Project 1.1 Blink
****************************************************************

In this project, we will make a LED blink and have the Display window of Processing Blink at the same time.

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
    * - |Chapter01_07|
    * - Hardware connection:

        Turn ON the power switch and NO.5 toggle switch. 

        Power switch should be turned ON in all the projects.
    * - |Chapter01_08|

.. |Chapter01_07| image:: ../_static/imgs/1_LED/Chapter01_07.png
.. |Chapter01_08| image:: ../_static/imgs/1_LED/Chapter01_08.png

.. note::
    
    :combo:`red font-bolder:If you have any concerns, please send an email to:` support@freenove.com

Sketch
================================================================

Sketch 1.1.1 Blink
----------------------------------------------------------------

.. note::
    
    :combo:`red font-bolder:If you have any concerns, please send an email to:` support@freenove.com

First, enter where the project is located:

.. code-block:: console
    
    /home/pi/Freenove_Kit/Processing/Sketches/Sketch_01_1_1_Blink

And then right-click to select Processing IDE

.. image:: ../_static/imgs/1_LED/Chapter01_23.png
    :align: center

Or you can enter a command in the terminal to open the file Sketch_01_1_1_Blink. :combo:`red font-bolder:(The following is only one line of command. There is a Space after Processing.)`

.. code-block:: console
    
    $ processing ~/Freenove_Kit/Processing/Sketches/Sketch_01_1_1_Blink/Sketch_01_1_1_Blink.pde

Open Processing and click Run.

.. image:: ../_static/imgs/1_LED/Chapter01_24.png
    :align: center

After the program runs, LED will start Blinking and the background of Display window will change with the change of LED state.

.. image:: ../_static/imgs/1_LED/Chapter01_25.png
    :align: center

The following is program code:

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_01_1_1_Blink/Sketch_01_1_1_Blink.pde
    :linenos: 
    :language: c
    :dedent:

Processing code usually have two functions: setup() and draw(), where the function setup() is only executed once while the function draw() will be executed repeatedly. In the function setup(), size(100, 100) specifies the size of the Display Window to 100x100pixl. FrameRate(1) specifies the refresh rate of Display Window to once per second, which means the draw() function will be executed once per second. GPIO.pinMode (ledPin, GPIO.OUTPUT) is used to set ledPin to output mode.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_01_1_1_Blink/Sketch_01_1_1_Blink.pde
    :linenos: 
    :language: c
    :lines: 12-16
    :dedent:

In draw() function, each execution will invert the variable "ledState". When “ledState” is true, LED is turned ON, and the background color of display window is set to red. And when the “ledState” is false, the LED is turned OFF and the background color of display window is set to gray. Since the function draw() is executed once per second, the background color of Display Window and the state of LED will also change once per second. This process will repeat in an endless loop to achieve the effect of blinking.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_01_1_1_Blink/Sketch_01_1_1_Blink.pde
    :linenos: 
    :language: c
    :lines: 18-27
    :dedent:

The following is a brief description of some functions:

.. py:function:: setup()

    The setup() function is run once when the program starts.

.. py:function:: draw()

    It is called directly after the setup() function. The draw() function continuously executes the lines of code within its block until the program stops or noLoop() is called. draw() is called automatically and should never be called explicitly.

.. py:function:: size()

    Defines width and height of the display window in pixels.

.. py:function:: framerate()

    Specifies the number of frames to be displayed every second.

.. py:function:: background()

    Set the color of the background of the display window.

.. py:function:: GPIO.pinMode()

    Configures a pin to act either as input or output.

.. py:function:: GPIO.digitalWrite()

    Sets an output pin to be either high or low.

All functions used in this code can be found in the Reference of Processing Software, in which built-in functions are described in details, and there are some sample programs. It is recommended that beginners learn more about usage and function of those functions. The localization of Reference can be opened with the following steps: click the menu bar "Help" -> "Reference".

.. image:: ../_static/imgs/1_LED/Chapter01_26.png
    :align: center

Then the following page will be displayed in the web browser:

.. image:: ../_static/imgs/1_LED/Chapter01_27.png
    :align: center

Or you can directly access to the official website for reference:http://processing.org/reference/

Project 1.2 MouseLED
****************************************************************

In this project, we will use the mouse to control the state of LED.

The components and circuits of this project are the same as the previous section.

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

Circuit
================================================================

.. list-table:: 
    :width: 80%
    :align: center
    :class: table-line

    *   -   Schematic diagram
    *   -   |Chapter01_07|
    *   -   Hardware connection:

            Turn ON the power switch and NO.5 toggle switch. 

            Power switch should be turned ON in all the projects.
    *   -   |Chapter01_08|

.. note::
    
    :combo:`red font-bolder:If you have any concerns, please send an email to:` support@freenove.com

Sketch
================================================================

Sketch 1.2.1 MouseLED
----------------------------------------------------------------

If you have any concerns, please send an email to: support@freenove.com

First, enter where the project is located:

.. code-block:: console
    
    /home/pi/Freenove_Kit/Processing/Sketches/Sketch_01_2_1_MouseLED

And then right-click to select Processing IDE.

.. image:: ../_static/imgs/1_LED/Chapter01_28.png
    :align: center

Or you can enter a command in the terminal to open the file Sketch_01_2_1_MouseLED. (The following is only one line of command. There is a Space after Processing.)

.. code-block:: console
    
    processing ~/Freenove_Kit/Processing/Sketches/Sketch_01_2_1_MouseLED/Sketch_01_2_1_MouseLED.pde

Open Processing and click Run. 

.. image:: ../_static/imgs/1_LED/Chapter01_29.png
    :align: center

After the program runs, the LED is in OFF-state, and background color of Display window is gray. Click the grey area of the Display Window with the mouse, LED is turned ON and Display window background color becomes blue. Click on the Display Window again, the LED is turned OFF and the background color becomes gray, as shown below.

.. image:: ../_static/imgs/1_LED/Chapter01_30.png
    :align: center

The following is program code:

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_01_2_1_MouseLED/Sketch_01_2_1_MouseLED.pde
    :linenos: 
    :language: c
    :dedent:

The function mouseClicked() in this code is used to capture the mouse click events. Once the mouse is clicked, the function will be executed. We can change the state of the variable “ledState” in this function to realize controlling LED by clicking on the mouse.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_01_2_1_MouseLED/Sketch_01_2_1_MouseLED.pde
    :linenos: 
    :language: c
    :lines: 27-29
    :dedent:

.. note::
    
    :combo:`red font-bolder:If you have any concerns, please send an email to:` support@freenove.com