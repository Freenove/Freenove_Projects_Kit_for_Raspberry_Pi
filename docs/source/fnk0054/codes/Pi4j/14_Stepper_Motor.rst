##############################################################################
Chapter Stepper Motor
##############################################################################

Thus far, we have learned about DC Motors and Servos. A DC motor can rotate constantly in on direction but we cannot control the rotation to a specific angle. On the contrary, a Servo can rotate to a specific angle but cannot rotate constantly in one direction. In this chapter, we will learn about a Stepper Motor which is also a type of motor. A Stepper Motor can rotate constantly and also to a specific angle. Using a Stepper Motor can easily achieve higher accuracies in mechanical motion.

Project 14.1 Stepper Motor
****************************************************************

In this project, we will learn how to drive a Stepper Motor, and understand its working principle.

Component knowledge
================================================================

Stepper Motor
----------------------------------------------------------------

Stepper Motors are an open-loop control device, which converts an electronic pulse signal into angular displacement or linear displacement. In a non-overload condition, the speed of the motor and the location of the stops depends only on the pulse signal frequency and number of pulses and is not affected by changes in load as with a DC Motor. A small Four-Phase Deceleration Stepper Motor is shown here:

.. image:: ../_static/imgs/14_Stepper_Motor/Chapter14_00.png
    :align: center

The electronic schematic diagram of a Four-Phase Stepper Motor is shown below:

.. image:: ../_static/imgs/14_Stepper_Motor/Chapter14_01.png
    :align: center

The outside case or housing of the Stepper Motor is the Stator and inside the Stator is the Rotor. There is a specific number of individual coils, usually an integer multiple of the number of phases the motor has, when the Stator is powered ON, an electromagnetic field will be formed to attract a corresponding convex diagonal groove or indentation in the Rotor’s surface. The Rotor is usually made of iron or a permanent magnet. Therefore, the Stepper Motor can be driven by powering the coils on the Stator in an ordered sequence (producing a series of “steps” or stepped movements).

A common driving sequence is shown here:

.. image:: ../_static/imgs/14_Stepper_Motor/Chapter14_02.png
    :align: center

In the sequence above, the Stepper Motor rotates by a certain angle at once, which is called a “step”. By controlling the number of rotational steps, you can then control the Stepper Motor's rotation angle. By defining the time between two steps, you can control the Stepper Motor's rotation speed. When rotating clockwise, the order of coil powered on is: A -> B -> C -> D -> A ->……. And the rotor will rotate in accordance with this order, step by step, called four-steps, four-part. If the coils is powered ON in the reverse order, D -> C -> B -> A -> D ->…… , the rotor will rotate in counter-clockwise direction.

There are other methods to control Stepper Motors, such as: connect A phase, then connect A B phase, the stator will be located in the center of A B, which is called a half-step. This method can improve the stability of the Stepper Motor and reduces noise. Tise sequence of powering the coils looks like this: A -> AB -> B -> BC -> C -> CD -> D -> DA -> A ->……, the rotor will rotate in accordance to this sequence ar, a half-step at a time, called four-steps, eight-part. Conversely, if the coils are powered ON in the reverse order the Stepper Motor will rotate in the opposite direction.

The stator in the Stepper Motor we have supplied has 32 magnetic poles. Therefore, to complete one full revolution requires 32 full steps. The rotor (or output shaft) of the Stepper Motor is connected to a speed reduction set of gears and the reduction ratio is 1:64. Therefore, the final output shaft (exiting the Stepper Motor’s housing) requires 32 X 64 = 2048 steps to make one full revolution.

ULN2003 Stepper Motor driver
----------------------------------------------------------------

A ULN2003 Stepper Motor Driver is used to convert weak signals into more powerful control signals in order to drive the Stepper Motor. In the illustration below, the input signal IN1-IN4 corresponds to the output signal A-D, and 4 LEDs are integrated into the board to indicate the state of these signals. The PWR interface can be used as a power supply for the Stepper Motor. By default, PWR and VCC are connected.

.. image:: ../_static/imgs/14_Stepper_Motor/Chapter14_03.png
    :align: center

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
| Stepper Motor                               |
|                                             |
|  |Chapter14_04|                             |                              
|                                             |
+---------------------------------------------+

.. |Chapter01_04| image:: ../_static/imgs/1_LED/Chapter01_04.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter01_06| image:: ../_static/imgs/1_LED/Chapter01_06.png
.. |Chapter14_04| image:: ../_static/imgs/14_Stepper_Motor/Chapter14_04.png

Circuit
================================================================

.. list-table:: 
    :width: 100%
    :align: center
    :class: product-table

    *   -   Schematic diagram
    *   -   |Chapter14_05|
    *   -   Hardware connection:
    *   -   |Chapter14_06|

.. |Chapter14_05| image:: ../_static/imgs/14_Stepper_Motor/Chapter14_05.png
.. |Chapter14_06| image:: ../_static/imgs/14_Stepper_Motor/Chapter14_06.png

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com

Sketch
================================================================

In this project, we will use a stepper motor.

Sketch_14_SteppingMotor
----------------------------------------------------------------

First, enter where the project is located:

.. code-block:: console

    $ cd ~/Freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor

.. image:: ../_static/imgs/14_Stepper_Motor/Chapter14_07.png
    :align: center

Enter the command to run the code.

.. code-block:: console

    $ jbang SteppingMotor.java

.. image:: ../_static/imgs/14_Stepper_Motor/Chapter14_08.png
    :align: center

When the code is running, you can observe that the stepper motor first rotates one circle forward, then one circle reversely, and repeats this process back and forth.

.. image:: ../_static/imgs/14_Stepper_Motor/Chapter14_09.png
    :align: center

On the terminal, you can see the messages printed.

.. image:: ../_static/imgs/14_Stepper_Motor/Chapter14_10.png
    :align: center

Press Ctrl+C to exit the program.

.. image:: ../_static/imgs/14_Stepper_Motor/Chapter14_11.png
    :align: center

You can run the following command to open the code with Geany to view and edit it.

.. code-block:: console

    $ geany SteppingMotor.java

Click the icon to run the code.

.. image:: ../_static/imgs/14_Stepper_Motor/Chapter14_12.png
    :align: center

If the code fails to run, please check :ref:`Geany Configuration<geany>`.

The following is program code:

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor/SteppingMotor.java
    :linenos: 
    :language: java

Define the GPIO pins for motor control and the GPIO outputs used to control the motors.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor/SteppingMotor.java
    :linenos: 
    :language: java
    :lines: 17-18

Define the motor's rotation direction and the array of step sequences for clockwise and counter-clockwise directions.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor/SteppingMotor.java
    :linenos: 
    :language: java
    :lines: 20-22

Constructor, initialize GPIO pins.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor/SteppingMotor.java
    :linenos: 
    :language: java
    :lines: 24-29

Control the stepper motor to execute a one-step sequence cycle.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor/SteppingMotor.java
    :linenos: 
    :language: java
    :lines: 31-44

The stepper motor driving function controls the direction of motor rotation, the execution time of each stepping action, and the number of stepping sequences to execute.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor/SteppingMotor.java
    :linenos: 
    :language: java
    :lines: 46-50

Stepper motor stop function that stops the motor.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor/SteppingMotor.java
    :linenos: 
    :language: java
    :lines: 52-56

Implement the AutoCloseable interface to ensure that resources are released when they are no longer needed.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor/SteppingMotor.java
    :linenos: 
    :language: java
    :lines: 58-66

Initialize stepper motor controller.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor/SteppingMotor.java
    :linenos: 
    :language: java
    :lines: 79-79

Add JVM shutdown hook to ensure motors are stopped on program exit.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor/SteppingMotor.java
    :linenos: 
    :language: java
    :lines: 80-80

First, control the stepper motor to rotate forward one circle, then pause for 500 milliseconds, then control the stepper motor to rotate reversely one circle, then pause for 500 milliseconds, and repeat this process.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor/SteppingMotor.java
    :linenos: 
    :language: java
    :lines: 82-87

If a thread termination exception or other exception occurs, it will be printed out on the terminal interface.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor/SteppingMotor.java
    :linenos: 
    :language: java
    :lines: 89-94

Make sure the resources are released when the program ends.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_14_SteppingMotor/SteppingMotor.java
    :linenos: 
    :language: java
    :lines: 94-102
