##############################################################################
Chapter 74HC595 & LED Matrix
##############################################################################

Thus far we have learned how to use the 74HC595 IC Chip to control the Bar Graph LED and the 7-Segment Display. We will now use 74HC595 IC Chips to control an LED Matrix.

Project 18.1 LED Matrix
****************************************************************

In this project, we will use two 74HC595 IC chips to control a monochrome (one color) (8X8) LED Matrix to make it display both simple graphics and characters.

Component knowledge
================================================================

LED matrix
----------------------------------------------------------------

An LED Matrix is a rectangular display module that consists of a uniform grid of LEDs. The following is an 8X8 monochrome (one color) LED Matrix containing 64 LEDs (8 rows by 8 columns).

.. image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_00.png
    :align: center

In order to facilitate the operation and reduce the number of ports required to drive this component, the Positive Poles of the LEDs in each row and Negative Poles of the LEDs in each column are respectively connected together inside the LED Matrix module, which is called a Common Anode. There is another arrangement type. Negative Poles of the LEDs in each row and the Positive Poles of the LEDs in each column are respectively connected together, which is called a Common Cathode.

The LED Matrix that we use in this project is a Common Anode LED Matrix.

.. image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_01.png
    :align: center

Here is how a Common Anode LED Matrix works. First, choose 16 ports on RPI board to connect to the 16 ports of LED Matrix. Configure one port in columns for low level, which makes that column the selected port. Then configure the eight port in the row to display content in the selected column. Add a delay value and then select the next column that outputs the corresponding content. This kind of operation by column is called Scan. If you want to display the following image of a smiling face, you can display it in 8 columns, and each column is represented by one byte.

.. image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_02.png
    :align: center

.. list-table:: 
    :width: 100%
    :align: center
    :class: product-table

    *   -  Column 
        -  Binary
        -  Hexadecimal

    *   -  1
        -  0001 1100
        -  0x1c

    *   -  2
        -  0010 0010
        -  0x22

    *   -  3
        -  0101 0001
        -  0x51

    *   -  4
        -  0100 0101
        -  0x45

    *   -  5
        -  0100 0101
        -  0x45

    *   -  6
        -  0101 0001
        -  0x51

    *   -  7
        -  0010 0010
        -  0x22

    *   -  8
        -  0001 1100
        -  0x1c

To begin, display the first column, then turn off the first column and display the second column. (and so on) .... turn off the seventh column and display the 8th column, and then start the process over from the first column again like the control of LED Bar Graph project. The whole process will be repeated rapidly in a loop. Due to the principle of optical afterglow effect and the vision persistence effect in human sight, we will see a picture of a smiling face directly rather than individual columns of LEDs turned ON one column at a time (although in fact this is the reality we cannot perceive). 

Scanning rows is another option to display on an LED Matrix (dot matrix grid). Whether scanning by row or column, 16 GPIO is required. In order to save GPIO ports of control board, two 74HC595 IC Chips are used in the circuit. Every 74HC595 IC Chip has eight parallel output ports, so two of these have a combined total of 16 ports, which is just enough for our project. The control lines and data lines of the two 74HC595 IC Chips are not all connected to the RPi, but connect to the Q7 pin of first stage 74HC595 IC Chip and to the data pin of second IC Chip. The two 74HC595 IC Chips are connected in series, which is the same as using one "74HC595 IC Chip" with 16 parallel output ports.

Component List
================================================================

+---------------------------------------------+
| Freenove Projects Board for Raspberry Pi    |
|                                             |
|  |Chapter01_04|                             |
+---------------------+-----------------------+
| Raspberry Pi        | GPIO Ribbon Cable     |
|                     |                       |
|  |Chapter01_05|     |  |Chapter01_06|       |
+---------------------+-----------------------+
| LED matrix                                  |
|                                             |
|  |Chapter18_00|                             |                              
+---------------------------------------------+

.. |Chapter01_04| image:: ../_static/imgs/1_LED/Chapter01_04.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter01_06| image:: ../_static/imgs/1_LED/Chapter01_06.png
.. |Chapter17_00| image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_00.png

Circuit
================================================================

.. list-table:: 
    :width: 100%
    :align: center
    :class: product-table

    *   -   Schematic diagram
    *   -   |Chapter18_03|
    *   -   Hardware connection:
    *   -   |Chapter18_04|

.. |Chapter18_03| image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_03.png
.. |Chapter18_04| image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_04.png

.. hint::

    :red:`If it dosen't work, rotate the LED matrix for 180°.`

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com

Sketch
================================================================

Sketch 12.1.1 LEDMatrix
----------------------------------------------------------------

First, enter where the project is located:

.. code-block:: console

    /home/pi/Freenove_Kit/Processing/Sketches/Sketch_12_1_1_LEDMatrix

And then right-click to select Processing IDE

.. image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_10.png
    :align: center

Or you can enter a command in the terminal to open the file Sketch_12_1_1_LEDMatrix. (The following is only one line of command. There is a Space after Processing.)

.. code-block:: console

    processing ~/Freenove_Kit/Processing/Sketches/Sketch_12_1_1_LEDMatrix/Sketch_12_1_1_LEDMatrix.pde

Open Processing and click Run

.. image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_11.png
    :align: center

The result is as shown below. LED matrix will display a smiling face first and then character 0-F.

The speed can be changed by dragging the slider.

.. image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_12.png
    :align: center

This project contains a lot of code files, and the core code is contained in the file Sketch_12_1_1_LEDMatrix. The other files only contain some custom classes.

.. image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_13.png
    :align: center

The following is program code:

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_12_1_1_LEDMatrix/Sketch_12_1_1_LEDMatrix.pde
    :linenos: 
    :language: c
    :lines: 28-58
    :dedent:

In the code, first define the data of the smiling face and characters "0-F".

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_12_1_1_LEDMatrix/Sketch_12_1_1_LEDMatrix.pde
    :linenos: 
    :language: c
    :lines: 17-39
    :dedent:

Then create a new thread t. LEDMatrix scan display code will be executed in run() of this thread.

.. code-block:: c

    myThread t = new myThread();    //create a new thread for ledmatrix
    ......
    class myThread extends Thread {
        public void run() {
            while (true) {
            showMatrix();    //show smile picture 
            showNum();      //show the character "0-F"
            }
        }
    }

The function setup(), defines size of Display Window, ProgressBar class objects and IC75HC595 class object, and starts the thread t.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_12_1_1_LEDMatrix/Sketch_12_1_1_LEDMatrix.pde
    :linenos: 
    :language: c
    :lines: 41-47
    :dedent:

In draw(), draw the relevant information and the current number to display.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_12_1_1_LEDMatrix/Sketch_12_1_1_LEDMatrix.pde
    :linenos: 
    :language: c
    :lines: 41-47
    :dedent:

Subfunction showMatrix () makes LEDMatrix display a smiling face pattern, which lasts for a period of time.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_12_1_1_LEDMatrix/Sketch_12_1_1_LEDMatrix.pde
    :linenos: 
    :language: c
    :lines: 64-75
    :dedent:

Subfunction showNum() makes LEDMatrix scroll displaying character "0-F", in which the variable k is used to adjust the scrolling speed.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_12_1_1_LEDMatrix/Sketch_12_1_1_LEDMatrix.pde
    :linenos: 
    :language: c
    :lines: 76-90
    :dedent:

If you have more interests in LED matrix, you can download an interesting app to explore.

https://play.google.com/store/apps/details?id=com.vitogusmano.arduinoledmatrixanimator

If you have any concerns about the app, please contact with Vito Gusmano (vigus9000@gmail.com).

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com