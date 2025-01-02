##############################################################################
App Control Graphics
##############################################################################

In this chapter, we will use a potentiometer to make the graphics change in Processing.

App 2.1 Ellipse
****************************************************************

This project uses two potentiometers to control the size and shape of an ellipse respectively.

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

.. |Chapter01_04| image:: ../_static/imgs/1_LED/Chapter01_04.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter01_06| image:: ../_static/imgs/1_LED/Chapter01_06.png

Circuit
================================================================

.. list-table:: 
    :width: 100%
    :align: center
    :class: product-table

    *   -   Schematic diagram
    *   -   |APP2_00|
    *   -   Hardware connection:
    *   -   |APP2_01|

.. |APP2_00| image:: ../_static/imgs/App_2_Control_Graphics/APP2_00.png
.. |APP2_01| image:: ../_static/imgs/App_2_Control_Graphics/APP2_01.png

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com

Sketch
================================================================

Sketch 2.1.1 Ellipse

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com

First, enter where the project is located:

.. code-block:: console

    /home/pi/Freenove_Kit/Processing/Apps/App_02_1_1_Ellipse

And then right-click to select Processing IDE

.. image:: ../_static/imgs/App_2_Control_Graphics/APP2_02.png
    :align: center

Or you can enter a command in the terminal to open the file App_02_1_1_Ellipse. (The following is only one line of command. There is a Space after Processing.)

.. code-block:: console

    processing ~/Freenove_Kit/Processing/Apps/App_02_1_1_Ellipse/App_02_1_1_Ellipse.pde

Open Processing and click Run

.. image:: ../_static/imgs/App_2_Control_Graphics/APP2_03.png
    :align: center

The result is as shown below. Rotating RP1 and RP2 potentimeters will change the length of the circle.

.. image:: ../_static/imgs/App_2_Control_Graphics/APP2_04.png
    :align: center

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com