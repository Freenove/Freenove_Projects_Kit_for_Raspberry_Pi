##############################################################################
Chapter 11 Motor & Driver
##############################################################################

In this chapter, we will learn about DC Motors and DC Motor Drivers and how to control the speed and direction of a DC Motor.

Project 11.1 Control a DC Motor with a Potentiometer
****************************************************************

In this project, a potentiometer will be used to control a DC Motor. When the Potentiometer is at the midpoint position, the DC Motor will STOP, and when the Potentiometer is turned in either direction of this midpoint, the DC Motor speed increases until it reached the endpoint where the DC Motor achieves its maximum speed. When the Potentiometer is turned “Left” of the midpoint, the DC Motor will ROTATE in one direction and when turned “Right” the DC Motor will ROTATE in the opposite direction. 

Component knowledge
================================================================

DC Motor
----------------------------------------------------------------

DC Motor is a device that converts electrical energy into mechanical energy. DC Motors consist of two major parts, a Stator and the Rotor. The stationary part of a DC Motor is the Stator and the part that Rotates is the Rotor. The Stator is usually part of the outer case of motor (if it is simply a pair of permanent magnets), and it has terminals to connect to the power if it is made up of electromagnet coils. Most Hobby DC Motors only use Permanent Magnets for the Stator Field. The Rotor is usually the shaft of motor with 3 or more electromagnets connected to a commutator where the brushes (via the terminals 1 & 2 below) supply electrical power, which can drive other mechanical devices. The diagram below shows a small DC Motor with two terminal pins.

.. image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_00.png
    :align: center

When a DC Motor is connected to a power supply, it will rotate in one direction. If you reverse the polarity of the power supply, the DC Motor will rotate in opposite direction. This is important to note.

.. image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_01.png
    :align: center

L293D
-----------------------------------------

L293D is an IC Chip (Integrated Circuit Chip) with a 4-channel motor drive. You can drive a Unidirectional DC Motor with 4 ports or a Bi-Directional DC Motor with 2 ports or a Stepper Motor (Stepper Motors are covered later in this Tutorial).

.. image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_13.png
    :align: center

Port description of L293D module is as follows:

.. table::
    :align: center
    :class: zebra
    
    +----------+--------------+---------------------------------------------------------------------------------------------------------------+
    | Pin name |  Pin number  |                                                  Description                                                  |
    +==========+==============+===============================================================================================================+
    | In x     | 2, 7, 10, 15 | Channel x digital signal input pin                                                                            |
    +----------+--------------+---------------------------------------------------------------------------------------------------------------+
    | Out x    | 3, 6, 11, 14 | Channel x output pin, input high or low level according to In x pin, gets connected to +Vmotor or 0V          |
    +----------+--------------+---------------------------------------------------------------------------------------------------------------+
    | Enable1  | 1            | Channel 1 and Channel 2 enable pin, high level enable                                                         |
    +----------+--------------+---------------------------------------------------------------------------------------------------------------+
    | Enable2  | 9            | Channel 3 and Channel 4 enable pin, high level enable                                                         |
    +----------+--------------+---------------------------------------------------------------------------------------------------------------+
    | 0V       | 4, 5, 12, 13 | Power Cathode (GND)                                                                                           |
    +----------+--------------+---------------------------------------------------------------------------------------------------------------+
    | +V       | 16           | Positive Electrode (VCC) of power supply, supply voltage 4.5~36V                                              |
    +----------+--------------+---------------------------------------------------------------------------------------------------------------+
    | +Vmotor  | 8            | Positive Electrode of load power supply, provide power supply for the Out pin x, the supply voltage is +V~36V |
    +----------+--------------+---------------------------------------------------------------------------------------------------------------+

For more details, please see the datasheet for this IC Chip.

When using the L293D to drive a DC Motor, there are usually two connection options.

The following connection option uses one channel of the L239D, which can control motor speed through the PWM, However the motor then can only rotate in one direction.

.. image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_14.png
    :align: center

The following connection uses two channels of the L239D: one channel outputs the PWM wave, and the other channel connects to GND. Therefore, you can control the speed of the motor. When these two channel signals are exchanged, it not only controls the speed of motor, but also can control the direction of the motor.

.. image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_15.png
    :align: center

In practical use, the motor is usually connected to channel 1 and by outputting different levels to in1 and in2 to control the rotational direction of the motor, and output to the PWM wave to Enable1 port to control the motor's rotational speed. If the motor is connected to channel 3 and 4 by outputting different levels to in3 and in4 to control the motor's rotation direction, and output to the PWM wave to Enable2 pin to control the motor’s rotational speed.

Component List
================================================================

.. table::
    :class: table-line
    :align: center
    :width: 80%

    +---------------------------------------------+
    | Freenove Projects Board for Raspberry Pi    |
    |                                             |
    |  |Chapter01_04|                             |
    +---------------------+-----------------------+
    | Raspberry Pi        | GPIO Ribbon Cable     |
    |                     |                       |
    |  |Chapter01_05|     |  |Chapter01_06|       |
    +---------------------+-----------------------+
    | Jumper Wire         | Motor                 |
    |                     |                       |
    |  |Chapter05_02|     |  |Chapter11_02|       |
    +---------------------+-----------------------+
    | 9V Battery (you provide) & 9V Battery Cable |
    |                                             |
    |  |Chapter11_03|                             |
    +---------------------------------------------+

.. |Chapter01_04| image:: ../_static/imgs/1_LED/Chapter01_04.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter01_06| image:: ../_static/imgs/1_LED/Chapter01_06.png
.. |Chapter05_02| image:: ../_static/imgs/5_RGB_LED/Chapter05_02.png
.. |Chapter11_02| image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_02.png
.. |Chapter11_03| image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_03.png

Circuit
================================================================

.. list-table:: 
    :width: 80%
    :align: center
    :class: table-line

    *   -   Schematic diagram
    *   -   |Chapter11_04|
    *   -   Hardware connection:
    *   -   |Chapter11_05|

.. |Chapter11_04| image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_04.png
.. |Chapter11_05| image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_05.png

.. note::
    
    :combo:`red font-bolder:If you have any concerns, please send an email to:` support@freenove.com

Sketch
================================================================

In this chapter, we will learn how to use the potentiometer to control the rotation speed and direction of the DC motor.

Sketch_11_Motor
----------------------------------------------------------------

First, enter where the project is located:

.. code-block:: console

    $ cd ~/Freenove_Kit/Pi4j/Sketches/Sketch_11_Motor

.. image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_08.png
    :align: center

Enter the command to run the code.

.. code-block:: console

    $ jbang Motor.java

.. image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_09.png
    :align: center

When the code is running, Raspberry Pi will obtain the value of the potentiometer and control the direct of the motor accordingly.

.. image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_10.png
    :align: center

Press Ctrl+C to exit the code.

.. image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_11.png
    :align: center

You can run the following command to open the code with Geany to view and edit it.

.. code-block:: console

    $ geany Motor.java

Click the icon to run the code.

.. image:: ../_static/imgs/11_Motor_&_Driver/Chapter11_12.png
    :align: center

If the code fails to run, please check :ref:`Geany Configuration<geany>`.

The following is program code:

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_11_Motor/Motor.java
    :linenos: 
    :language: java

The range of ADC value is 0-255, with 128 as the middle value. If the ADC value is greater than 128, the Raspberry Pi controls the motor to rotate forward. The larger the ADC value, the faster the motor speed. Conversely, if the ADC value is less than 128, the Raspberry Pi controls the motor to rotate backward. The smaller the ADC value, the faster the motor speed.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_11_Motor/Motor.java
    :linenos: 
    :language: java
    :lines: 150-171
    :dedent:

The ADC value at the potentiometer is obtained every 100 milliseconds, and the ADC value is sent as a parameter to the motor function to control the direction and speed of the motor, and the ADC value is printed out in the terminal.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_11_Motor/Motor.java
    :linenos: 
    :language: java
    :lines: 182-187
    :dedent:

