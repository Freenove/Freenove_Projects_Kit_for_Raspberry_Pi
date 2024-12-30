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

In this project, we will drive the LED matrix to display different contents.

Sketch_17_LEDMatrix
----------------------------------------------------------------

First, enter where the project is located:

.. code-block:: console

    $ cd ~/Freenove_Kit/Pi4j/Sketches/Sketch_17_LEDMatrix

.. image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_05.png
    :align: center

Enter the command to run the code.

.. code-block:: console

    $ jbang LEDMatrix.java

.. image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_06.png
    :align: center

When the code is running, you can see that the LED matrix first displays a smiley face, then scrolls through the characters 0-F, and repeats this process in a continuous loop.

.. image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_07.png
    :align: center

Press Ctrl+C to exit the program.

.. image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_08.png
    :align: center

You can run the following command to open the code with Geany to view and edit it.

.. code-block:: console

    $ geany LEDMatrix.java

Click the icon to run the code.

.. image:: ../_static/imgs/18_74HC595_&_LED_Matrix/Chapter18_09.png
    :align: center

If the code fails to run, please check :ref:`Geany Configuration<geany>`.

The following is program code:

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_17_LEDMatrix/LEDMatrix.java
    :linenos: 
    :language: java
    :dedent:

Define the contents displayed on the LED matrix.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_17_LEDMatrix/LEDMatrix.java
    :linenos: 
    :language: java
    :lines: 105-125
    :dedent:

Use 2 nested for functions to make the LED dot matrix display a smiley face and loop it 500 times.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_17_LEDMatrix/LEDMatrix.java
    :linenos: 
    :language: java
    :lines: 133-142
    :dedent:

Display the array from character 0 and loop 10 times to ensure that it is visible to human eyes then move the array elements one by one to make the characters scroll.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_17_LEDMatrix/LEDMatrix.java
    :linenos: 
    :language: java
    :lines: 143-154
    :dedent: