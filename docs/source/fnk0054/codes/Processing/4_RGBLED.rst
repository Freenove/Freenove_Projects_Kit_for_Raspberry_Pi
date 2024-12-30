##############################################################################
Chapter RGB LED
##############################################################################

In this chapter, we will learn how to control an RGB LED.

An RGB LED has 3 LEDs integrated into one LED component. It can respectively emit Red, Green and Blue light. In order to do this, it requires 4 pins (this is also how you identify it). The long pin (1) is the common which is the Anode (+) or positive lead, the other 3 are the Cathodes (-) or negative leads. A rendering of an RGB LED and its electronic symbol are shown below. We can make RGB LED emit various colors of light and brightness by controlling the 3 Cathodes (2, 3 & 4) of the RGB LED

.. image:: ../_static/imgs/5_RGB_LED/Chapter05_00.png
    :align: center
    
Red, Green, and Blue light are called 3 Primary Colors when discussing light (Note: for pigments such as paints, the 3 Primary Colors are Red, Blue and Yellow). When you combine these three Primary Colors of light with varied brightness, they can produce almost any color of visible light. Computer screens, single pixels of cell phone screens, neon lamps, etc. can all produce millions of colors due to phenomenon.

.. image:: ../_static/imgs/5_RGB_LED/Chapter05_01.png
    :align: center
    
If we use a three 8 bit PWM to control the RGB LED, in theory, we can create 28*28*28=16777216 (16 million) colors through different combinations of RGB light brightness.

Next, we will use RGB LED to make a multicolored LED. 

Project 4.1 Multicolored LED
****************************************************************

In this project, we will make a multicolored LED, which we can program the RGB LED to automatically change colors.

Component List
================================================================

+------------------------------------------+
| Freenove Projects Board for Raspberry Pi |
|                                          |
|  |Chapter01_04|                          |
+---------------------+--------------------+
| Raspberry Pi        | GPIO Ribbon Cable  |
|                     |                    |
|  |Chapter01_05|     |  |Chapter01_06|    |
+---------------------+--------------------+
| Jumper Wire         | RGBLED Module      |
|                     |                    |
|  |Chapter05_02|     |  |Chapter05_03|    |
+---------------------+--------------------+

.. |Chapter01_04| image:: ../_static/imgs/1_LED/Chapter01_04.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter01_06| image:: ../_static/imgs/1_LED/Chapter01_06.png
.. |Chapter05_02| image:: ../_static/imgs/5_RGB_LED/Chapter05_02.png
.. |Chapter05_03| image:: ../_static/imgs/5_RGB_LED/Chapter05_03.png

Circuit
================================================================

.. list-table:: 
    :width: 100%
    :align: center
    :class: product-table

    *   -   Schematic diagram
    *   -   |Chapter05_04|
    *   -   Hardware connection:
    *   -   |Chapter05_05|

.. |Chapter05_04| image:: ../_static/imgs/5_RGB_LED/Chapter05_04.png
.. |Chapter05_05| image:: ../_static/imgs/5_RGB_LED/Chapter05_05.png

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com

Sketch
================================================================

Sketch 4.1.1 ColorfulLED
----------------------------------------------------------------

If you have any concerns, please send an email to: support@freenove.com

First, enter where the project is located:

.. code-block:: console
    
    /home/pi/Freenove_Kit/Processing/Sketches/Sketch_04_1_1_ColorfulLED

And then right-click to select Processing IDE

.. image:: ../_static/imgs/5_RGB_LED/Chapter05_11.png
    :align: center

Or you can enter a command in the terminal to open the file Sketch_04_1_1_ColorfulLED. (The following is only one line of command. There is a Space after Processing.)

.. code-block:: console
    
    processing ~/Freenove_Kit/Processing/Sketches/Sketch_04_1_1_ColorfulLED/Sketch_04_1_1_ColorfulLED.pde

Open Processing and click Run.

.. image:: ../_static/imgs/5_RGB_LED/Chapter05_12.png
    :align: center

The result is as shown below. You can change the color of the LED by dragging the slider.

.. image:: ../_static/imgs/5_RGB_LED/Chapter05_13.png
    :align: center

This project contains a lot of code files, and the core code is contained in the file Sketch_04_1_1_ColorfulLED. The other files only contain some custom classes.

.. image:: ../_static/imgs/5_RGB_LED/Chapter05_14.png
    :align: center

The following is program code:

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_04_1_1_ColorfulLED/Sketch_04_1_1_ColorfulLED.pde
    :linenos: 
    :language: c
    :dedent:

In the code, first create three PWM pins and three progress bars to control RGBLED.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_04_1_1_ColorfulLED/Sketch_04_1_1_ColorfulLED.pde
    :linenos: 
    :language: c
    :lines: 13-18
    :dedent:

And then in function setup(), define position and length of progress bar according to the size of Display Window, and set the name of each progress bar.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_04_1_1_ColorfulLED/Sketch_04_1_1_ColorfulLED.pde
    :linenos: 
    :language: c
    :lines: 20-31
    :dedent:

In function draw(), first set background, header and other basic information. Then draw a circle and set its color according to the duty cycle of three channels of RGB. Finally draw three progress bars.

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_04_1_1_ColorfulLED/Sketch_04_1_1_ColorfulLED.pde
    :linenos: 
    :language: c
    :lines: 33-43
    :dedent:

System functions mousePressed(), mouseReleased() and mouseDragged() are used to determine whether the mouse drags the progress bar and set the schedule. If the mouse button is pressed in a progress bar, then the mousePressed () sets the progress flag rgbMouse to true, mouseDragged (mouseX) maps progress value to set corresponding PWM. When the mouse is released, mouseReleased() sets the progress flag rgbMouse to false.. 

.. literalinclude:: ../../../freenove_Kit/Processing/Sketches/Sketch_04_1_1_ColorfulLED/Sketch_04_1_1_ColorfulLED.pde
    :linenos: 
    :language: c
    :lines: 45-72
    :dedent:

Reference
----------------------------------------------------------------

.. c:function:: class ProgressBar

    This is a custom class that is used to create a progress bar.
    
    public **ProgressBar** (int ix, int iy, int barlen)
    
    Constructor, used to create ProgressBar, the parameters for coordinates X, Y and length of ProgressBar.
    
    public void **setTitle** (String str)
    
    Used to set the name of progress bar, which will be displayed in the middle of the progress bar.
    
    public void **setProgress** (float pgress)
    
    Used to set the progress of progress bar. The parameter: 0<pgress<1.0.
    
    public void **create()** & public void **create** (float pgress)
    
    Used to draw progress bar.

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com