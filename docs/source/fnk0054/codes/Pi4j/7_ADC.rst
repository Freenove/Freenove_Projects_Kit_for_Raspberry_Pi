.. _ADC:

##############################################################################
Chapter (Important) Chapter ADC
##############################################################################

We have learned how to control the brightness of an LED through PWM and that PWM is not a real analog signal. In this chapter, we will learn how to read analog values via an ADC Module and convert these analog values into digital.

Project 7.1 Read the Voltage of Potentiometer 
****************************************************************

In this project, we will use the ADC function of an ADC Module to read the voltage value of a potentiometer. 

Circuit knowledge
================================================================

ADC
----------------------------------------------------------------

**An ADC is an electronic integrated circuit used to convert analog signals such as voltages to digital or binary form consisting of 1s and 0s.** The range of our ADC module is 8 bits, that means the resolution is 2^8=256, so that its range (at 3.3V) will be divided equally to 256 parts. 

Any analog value can be mapped to one digital value using the resolution of the converter. So the more bits the ADC has, the denser the partition of analog will be and the greater the precision of the resulting conversion.

.. image:: ../_static/imgs/7_ADC/Chapter07_00.png
    :align: center

Subsection 1: the analog in range of 0V-3.3/256 V corresponds to digital 0;

Subsection 2: the analog in range of 3.3 /256 V-2*3.3 /256V corresponds to digital 1;

The resultant analog signal will be divided accordingly.

DAC
----------------------------------------------------------------

The reversing this process requires a DAC, Digital-to-Analog Converter. The digital I/O port can output high level and low level (0 or 1), but cannot output an intermediate voltage value. This is where a DAC is useful. The DAC module PCF8591 has a DAC output pin with 8-bit accuracy, which can divide VDD (here is 3.3V) into 28=256 parts. For example, when the digital quantity is 1, the output voltage value is 3.3/256 *1 V, and when the digital quantity is 128, the output voltage value is 3.3/256 *128=1.65V, the higher the accuracy of DAC, the higher the accuracy of output voltage value will be.

Component knowledge
================================================================

Potentiometer
----------------------------------------------------------------

Potentiometer is a resistive element with three Terminal parts. Unlike the resistors that we have used thus far in our project which have a fixed resistance value, the resistance value of a potentiometer can be adjusted. A potentiometer is often made up by a resistive substance (a wire or carbon element) and movable contact brush. When the brush moves along the resistor element, there will be a change in the resistance of the potentiometer’s output side (3) (or change in the voltage of the circuit that is a part). The illustration below represents a linear sliding potentiometer and its electronic symbol on the right.

.. image:: ../_static/imgs/7_ADC/Chapter07_01.png
    :align: center

Between potentiometer pin 1 and pin 2 is the resistive element (a resistance wire or carbon) and pin 3 is connected to the brush that makes contact with the resistive element. In our illustration, when the brush moves from pin 1 to pin 2, the resistance value between pin 1 and pin 3 will increase linearly (until it reaches the highest value of the resistive element) and at the same time the resistance between pin 2 and pin 3 will decrease linearly and conversely down to zero. At the midpoint of the slider the measured resistance values between pin 1 and 3 and between pin 2 and 3 will be the same.

In a circuit, both sides of resistive element are often connected to the positive and negative electrodes of power. When you slide the brush “pin 3”, you can get variable voltage within the range of the power supply.

.. image:: ../_static/imgs/7_ADC/Chapter07_02.png
    :align: center

Rotary potentiometer
----------------------------------------------------------------

Rotary potentiometers and linear potentiometers have the same function; the only difference being the physical action being a rotational rather than a sliding movement.

ADS7830
----------------------------------------------------------------

The ADS7830 is a single-supply, low-power, 8-bit data acquisition device that features a serial I2C interface and an 8-channel multiplexer. The following table is the pin definition diagram of ADS7830.

+-----------+-----+---------------------------------------------------+-----------------------------------------------+
| SYMBOL    | PIN |                    DESCRIPTION                    |                    TOP VIEW                   |
+===========+=====+===================================================+===============================================+
|  CH0      |  1  |                                                   |                                               |
+-----------+-----+                                                   |                                               |
|  CH1      |  2  |                                                   |                                               |
+-----------+-----+                                                   |                                               |
|  CH2      |  3  |                                                   |                                               |
+-----------+-----+                                                   |                                               |
|  CH3      |  4  |                                                   |                                               |                                               
+-----------+-----+       Analog input channels  (A/D converter)      |                                               |
|  CH4      |  5  |                                                   |                                               |
+-----------+-----+                                                   |                                               |
|  CH5      |  6  |                                                   |                                               |
+-----------+-----+                                                   |                                               |
|  CH6      |  7  |                                                   |                                               |
+-----------+-----+                                                   |                                               |
|  CH7      |  8  |                                                   ||Chapter07_03|                                  |
+-----------+-----+---------------------------------------------------+                                               |
|  GND      |  9  |   Ground                                          |                                               |
+-----------+-----+---------------------------------------------------+                                               |
|           |     | Internal +2.5V Reference,External                 |                                               |
|REF in/out |  10 |                                                   |                                               |
|           |     | Reference Input                                   |                                               |
+-----------+-----+---------------------------------------------------+                                               |
|  COM      |  11 |   Common to Analog Input Channel                  |                                               |
+-----------+-----+---------------------------------------------------+                                               |
|  A0       |  12 |                                                   |                                               |
+-----------+-----+   Hardware address                                |                                               |
|  A1       |  13 |                                                   |                                               |
+-----------+-----+---------------------------------------------------+                                               |
|  SCL      |  14 |   Serial Clock                                    |                                               |
+-----------+-----+---------------------------------------------------+                                               |
|  SDA      |  15 |   Serial Sata                                     |                                               |
+-----------+-----+---------------------------------------------------+                                               |
|  +VDD     |  16 |   Power Supply, 3.3V Nominal                      |                                               |
+-----------+-----+---------------------------------------------------+-----------------------------------------------+

.. |Chapter07_03| image:: ../_static/imgs/7_ADC/Chapter07_03.png

I2C communication
----------------------------------------------------------------

I2C (Inter-Integrated Circuit) has a two-wire serial communication mode, which can be used to connect a micro-controller and its peripheral equipment. Devices using I2C communications must be connected to the serial data line (SDA), and serial clock line (SCL) (called I2C bus). Each device has a unique address which can be used as a transmitter or receiver to communicate with devices connected via the bus.

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
    *   -   |Chapter07_04|
    *   -   Hardware connection:
    *   -   |Chapter07_05|

.. |Chapter07_04| image:: ../_static/imgs/7_ADC/Chapter07_04.png
.. |Chapter07_05| image:: ../_static/imgs/7_ADC/Chapter07_05.png

Configure I2C and Install Smbus 
================================================================

Enable I2C
----------------------------------------------------------------

The I2C interface in Raspberry Pi is disabled by default. You will need to open it manually and enable the I2C interface as follows:

Type command in the Terminal:

.. code-block:: console

    $ sudo raspi-config

Then open the following dialog box:

.. image:: ../_static/imgs/7_ADC/Chapter07_06.png
    :align: center

Choose “Interfacing Options” then “I5 I2C” then “Yes” and then “Finish” in this order and restart your RPi. The I2C module will then be started.

Type a command to check whether the I2C module is started:

.. code-block:: console

    $ lsmod | grep i2c

If the I2C module has been started, the following content will be shown. 

Different models of Raspberry Pi display different contents depending on the CPU installed:

.. image:: ../_static/imgs/7_ADC/Chapter07_07.png
    :align: center

Install I2C-Tools
----------------------------------------------------------------

Next, type the command to install I2C-Tools. It is available with the Raspberry Pi OS by default.

.. code-block:: console

    $ sudo apt-get install i2c-tools
    $ sudo apt-get install python3-smbus

I2C device address detection:

.. code-block:: console

    $ i2cdetect -y 1

When you are using the ADS7830 Module, the result should look like this:

.. image:: ../_static/imgs/7_ADC/Chapter07_08.png
    :align: center

Here, 48 (HEX) is the I2C address of ADC Module (ADS7830).

Sketch
================================================================

In this chapter, we will learn the combined usage of ADC and potentiometer.

Sketch_07_1_ADC
----------------------------------------------------------------

First, enter where the project is located:

.. code-block:: console

    $ cd ~/Freenove_Kit/Pi4j/Sketches/Sketch_07_1_ADC

.. image:: ../_static/imgs/7_ADC/Chapter07_18.png
    :align: center

Enter the command to run the code.

.. code-block:: console

    $ jbang ADC.java

.. image:: ../_static/imgs/7_ADC/Chapter07_19.png
    :align: center

When the code is running, rotate the potentiometer marked below.

.. image:: ../_static/imgs/7_ADC/Chapter07_20.png
    :align: center

You can see that the ADC values change with the rotation of the potentiometer. The value 0 means that the potentiometer’s voltage read by ADC is 0V, 255 indicates that the voltage is 5V.

.. image:: ../_static/imgs/7_ADC/Chapter07_21.png
    :align: center

Press Ctrl+C to exit the code.

.. image:: ../_static/imgs/7_ADC/Chapter07_22.png
    :align: center

You can open the code with Geany with the following command to view and edit it.

.. code-block:: console

    $ geany ADC.java

Click the icon to run the code.

.. image:: ../_static/imgs/7_ADC/Chapter07_23.png
    :align: center

If the code fails to run, please check :ref:`Geany Configuration<geany>`.

The following is program code:

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_1_ADC/ADC.java
    :linenos: 
    :language: java

Dependency declaration, these libraries will be automatically downloaded by jbang at runtime and added to the classpath.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_1_ADC/ADC.java
    :linenos: 
    :language: java
    :lines: 3-8

Import I2C library. In this project, we use I2C to read the channel value of ADS7830.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_1_ADC/ADC.java
    :linenos: 
    :language: java
    :lines: 10-15

Constructor of ADCDevice class, which is used to initialize I2C bus to facilitate later reading and writing ADS7830 chip.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_1_ADC/ADC.java
    :linenos: 
    :language: java
    :lines: 21-25

Write a byte to the target chip, and then read the data. If the data can be read, it means the target chip exists and communication is successful. If an I2C exception is detected, it means the target chip does not exist.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_1_ADC/ADC.java
    :linenos: 
    :language: java
    :lines: 27-36

Write the read command to the ADS7830 and read the corresponding ADC value. It is returned by the return value.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_1_ADC/ADC.java
    :linenos: 
    :language: java
    :lines: 38-49

Create a pi4j context to get the Raspberry PI i2c interface.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_1_ADC/ADC.java
    :linenos: 
    :language: java
    :lines: 60-61

The I2C address of the ADS7830 is 0x48.

Create an ADCDevice class, associate it with the Raspberry PI I2C interface, and assign a value to the adcDevice.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_1_ADC/ADC.java
    :linenos: 
    :language: java
    :lines: 63-64

Check whether the chip can communicate normally. If the communication is successful, read channel 2 of the ADS7830 chip and print it out in the terminal.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_1_ADC/ADC.java
    :linenos: 
    :language: java
    :lines: 65-77

If communication with the chip fails, a prompt message is printed on the terminal.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_1_ADC/ADC.java
    :linenos: 
    :language: java
    :lines: 78-80

When the code finishes running, close the Pi4J context.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_1_ADC/ADC.java
    :linenos: 
    :language: java
    :lines: 82-84

Project 7.2 Soft Light
****************************************************************

In this project, we will make a soft light. We will use an ADC Module to read ADC values of a potentiometer and map it to duty cycle ratio of the PWM used to control the brightness of an LED. Then you can change the brightness of an LED by adjusting the potentiometer.

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
    *   -   |Chapter07_13|
    *   -   Hardware connection:
    *   -   |Chapter07_14|

.. |Chapter07_13| image:: ../_static/imgs/7_ADC/Chapter07_13.png
.. |Chapter07_14| image:: ../_static/imgs/7_ADC/Chapter07_14.png

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com

Sketch
================================================================

In this project, we learn how to control the brightness of LED with the potentiometer.

Sketch_07_2_Softlight
----------------------------------------------------------------

First, enter where the project is located:

.. code-block:: console

    $ cd ~/Freenove_Kit/Pi4j/Sketches/Sketch_07_2_Softlight

.. image:: ../_static/imgs/7_ADC/Chapter07_24.png
    :align: center

Enter the command to run code.

.. code-block:: console

    $ jbang Softlight.java

.. image:: ../_static/imgs/7_ADC/Chapter07_25.png
    :align: center

When the code is running, turn the potentiometer marked below and you can see the brightness of the LED change.

.. image:: ../_static/imgs/7_ADC/Chapter07_26.png
    :align: center

On the Terminal, you can see the printed ADC values and the calculated voltage values.

.. image:: ../_static/imgs/7_ADC/Chapter07_27.png
    :align: center
 
Press Ctrl+C to exit the program.

You can open the code with Geany with the following command to view and edit it.

.. code-block:: console

    $ geany Softlight.java

Click the icon to run the code.

.. image:: ../_static/imgs/7_ADC/Chapter07_28.png
    :align: center

If the code fails to run, please check :ref:`Geany Configuration<geany>`.

The following is program code:

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_2_Softlight/Softlight.java
    :linenos: 
    :language: java

The ADC value of the potentiometer is obtained every 100 milliseconds and printed on the terminal. Meanwhile, the ADC value is converted into the duty cycle value of the LED to control the brightness of the LED.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_2_Softlight/Softlight.java
    :linenos: 
    :language: java
    :lines: 158-168


Project 7.3 Colorful Light 
****************************************************************

In this project, 3 potentiometers are used to control the RGB LED and in principle it is the same as with the Soft Light. project. Namely, read the voltage value of the potentiometer and then convert it to PWM used to control LED brightness. Difference is that the previous soft light project needed only one LED while this one required (3) RGB LEDs.

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
    *   -   |Chapter07_15|
    *   -   Hardware connection:
    *   -   |Chapter07_16|

.. |Chapter07_15| image:: ../_static/imgs/7_ADC/Chapter07_15.png
.. |Chapter07_16| image:: ../_static/imgs/7_ADC/Chapter07_16.png

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com

Sketch
================================================================

In this project, we learn to use the potentiometer to control the color and brightness of the RGB LED.

Sketch_07_3_ColorfulSoftlight
----------------------------------------------------------------

First, enter where the project is located:

.. code-block:: console

    $ cd ~/Freenove_Kit/Pi4j/Sketches/Sketch_07_3_ColorfulSoftlight
 
.. image:: ../_static/imgs/7_ADC/Chapter07_29.png
    :align: center

Enter the command to run the code.

.. code-block:: console

    $ jbang ColorfulSoftlight.java

.. image:: ../_static/imgs/7_ADC/Chapter07_30.png
    :align: center

When the code is running, rotate the three potentiometers marked below, you will see the RGB LED’s color and brightness change. 

.. image:: ../_static/imgs/7_ADC/Chapter07_31.png
    :align: center

The ADC value is printed on the terminal.

.. image:: ../_static/imgs/7_ADC/Chapter07_32.png
    :align: center

Press Ctrl+C to exit the program.

You can open the code with Geany with the following command to view and edit it.

.. code-block:: console

    $ geany ColorfulSoftlight.java

Click the icon to run the code.

.. image:: ../_static/imgs/7_ADC/Chapter07_33.png
    :align: center

If the code fails to run, please check :ref:`Geany Configuration<geany>`.

The following is program code:

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_3_ColorfulSoftlight/ColorfulSoftlight.java
    :linenos: 
    :language: java

Initialize the pins that control the RGB LED.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_3_ColorfulSoftlight/ColorfulSoftlight.java
    :linenos: 
    :language: java
    :lines: 152-158

Get the ADC values corresponding to the 3 rotentiometers every 100 milliseconds; convert the values into duty cycle values corresponding to PWM, and print prompt information on the terminal.

.. literalinclude:: ../../../freenove_Kit/Pi4j/Sketches/Sketch_07_3_ColorfulSoftlight/ColorfulSoftlight.java
    :linenos: 
    :language: java
    :lines: 163-174