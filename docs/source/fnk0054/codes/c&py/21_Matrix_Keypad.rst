##############################################################################
Chapter Matrix Keypad
##############################################################################

Earlier we learned about a single Push Button Switch. In this chapter, we will learn about Matrix Keyboards, which integrates a number of Push Button Switches as Keys for the purposes of Input.

Project 21 Matrix Keypad
****************************************************************

In this project, we will attempt to get every key code on the Matrix Keypad to work.

Component knowledge
================================================================

4x4 Matrix Keypad
----------------------------------------------------------------

A Keypad Matrix is a device that integrates a number of keys in one package. As is shown below, a 4x4 Keypad Matrix integrates 16 keys (think of this as 16 Push Button Switches in one module):

.. image:: ../_static/imgs/21_Matrix_Keypad/Chapter21_00.png
    :align: center

Similar to the integration of an LED Matrix, the 4x4 Keypad Matrix has each row of keys connected with one pin and this is the same for the columns. Such efficient connections reduce the number of processor ports required. The internal circuit of the Keypad Matrix is shown below.

.. image:: ../_static/imgs/21_Matrix_Keypad/Chapter21_01.png
    :align: center

The method of usage is similar to the Matrix LED, by using a row or column scanning method to detect the state of each key’s position by column and row. Take column scanning method as an example, send low level to the first 1 column (Pin1), detect level state of rows 5, 6, 7, 8 to judge whether the keys A, B, C, D are pressed. Then send low level to columns 2, 3, 4 in turn to detect whether other keys are pressed. Therefore, you can get the state of all of the keys.

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
| 4x4 Matrix Keypad                           |
|                                             |
|  |Chapter21_02|                             |                              
+---------------------------------------------+

.. |Chapter01_04| image:: ../_static/imgs/1_LED/Chapter01_04.png
.. |Chapter01_05| image:: ../_static/imgs/1_LED/Chapter01_05.png
.. |Chapter01_06| image:: ../_static/imgs/1_LED/Chapter01_06.png
.. |Chapter21_02| image:: ../_static/imgs/21_Matrix_Keypad/Chapter21_02.png

Circuit
================================================================

.. list-table:: 
    :width: 100%
    :align: center
    :class: product-table

    *   -   Schematic diagram
    *   -   |Chapter21_03|
    *   -   Hardware connection:
    *   -   |Chapter21_04|

.. |Chapter21_03| image:: ../_static/imgs/20_Hygrothermograph_DHT11/Chapter21_03.png
.. |Chapter21_04| image:: ../_static/imgs/20_Hygrothermograph_DHT11/Chapter21_04.png

.. note::
    
    :red:`If you have any concerns, please send an email to:` support@freenove.com

Code
================================================================

This code is used to obtain all key codes of the 4x4 Matrix Keypad, when one of the keys is pressed, the key code will be displayed in the terminal window.

C Code 21.1 MatrixKeypad
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

If you have any concerns, please send an email to: support@freenove.com

1.	Use cd command to enter 21_MatrixKeypad directory of C code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/C_Code/21_MatrixKeypad

2.	Code of this project contains a custom header file. Use the following command to compile the code MatrixKeypad.cpp, Keypad.cpp and Key.cpp generate executable file MatrixKeypad. The custom header file will be compiled at the same time.

.. code-block:: console

    $ gcc MatrixKeypad.cpp Keypad.cpp Key.cpp -o MatrixKeypad -lwiringPi

3.	Run the generated file "MatrixKeypad".

.. code-block:: console

    $ ./MatrixKeypad

After the program runs, pressing any key on the MatrixKeypad, will display the corresponding key code on the Terminal. As is shown below:

.. image:: ../_static/imgs/21_Matrix_Keypad/Chapter21_05.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/21_MatrixKeypad/MatrixKeypad.cpp
    :linenos: 
    :language: c

In this project code, we use two custom library file "Keypad.hpp" and "Key.hpp". They are located in the same directory with program files "MatrixKeypad.cpp", "Keypad.cpp" and "Key.cpp". The Library Keypad is “transplanted” from the Arduino Library Keypad. This library file provides a method to read the Matrix Keyboard's input. By using this library, we can easily read the pressed keys of the Matrix Keyboard.

First, we define the information of the Matrix Keyboard used in this project: the number of rows and columns, code designation of each key and GPIO pin connected to each column and row. It is necessary to include the header file "Keypad.hpp".

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/21_MatrixKeypad/MatrixKeypad.cpp
    :linenos: 
    :language: c
    :lines: 7-18

Then, based on the above information, initiates a Keypad class object to operate the Matrix Keyboard.
.. code-block:: c

    Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

Set the debounce time to 50ms, and this value can be set based on the actual characteristics of the keyboard’s flexibly, with a default time of 10ms.

.. code-block:: c

    keypad.setDebounceTime(50);

In the "while" loop, use the function key= keypad.getKey () to read the keyboard constantly. If there is a key pressed, its key code will be stored in the variable "key", then be displayed.

.. literalinclude:: ../../../freenove_Kit/Code/C_Code/21_MatrixKeypad/MatrixKeypad.cpp
    :linenos: 
    :language: c
    :lines: 29-34

The Keypad Library used for the RPi is transplanted from the Arduino Keypad Library. And the source files can be obtained by visiting http://playground.arduino.cc/Code/Keypad. As for transplanted function library, the function and method of all classes, functions, variables, etc. are the same as the original library. Partial contents of the Keypad library are described below:

.. c:function:: class Keypad

    **Keypad**(char *userKeymap, byte *row, byte *col, byte numRows, byte numCols);
    
    Constructor, the parameters are: key code of keyboard, row pin, column pin, the number of rows, the number of columns.
    
    char **getKey**();
    
    Get the key code of the pressed key. If no key is pressed, the return value is NULL.
    
    void **setDebounceTime**(uint);
    
    Set the debounce time. And the default time is 10ms.
    
    void **setHoldTime**(uint);
    
    Set the time when the key holds stable state after pressed.
    
    bool **isPressed**(char keyChar);
    
    Judge whether the key with code "keyChar" is pressed.
    
    char **waitForKey**();
    
    Wait for a key to be pressed, and return key code of the pressed key.
    
    KeyState **getState**();
    
    Get state of the keys.
    
    bool **keyStateChanged**();
    
    Judge whether there is a change of key state, then return True or False.

For More information about Keypad, please visit: http://playground.arduino.cc/Code/Keypad or through the opening file "Keypad.hpp".

Python Code 21.1 MatrixKeypad
----------------------------------------------------------------

First, observe the project result, and then learn about the code in detail.

If you have any concerns, please send an email to: support@freenove.com

1.	Use cd command to enter 21_MatrixKeypad directory of Python code.

.. code-block:: console

    $ cd ~/Freenove_Kit/Code/Python_GPIOZero_Code/21_MatrixKeypad

2.	Use Python command to execute code "MatrixKeypad.py".

.. code-block:: console

    $ python MatrixKeypad.py

After the program runs, pressing any key on the MatrixKeypad, will display the corresponding key code on the Terminal. As is shown below:

.. image:: ../_static/imgs/21_Matrix_Keypad/Chapter21_06.png
    :align: center

The following is the program code:

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/21_MatrixKeypad/MatrixKeypad.py
    :linenos: 
    :language: python

Import Keypad. Define row and column. Define key value variable. Define row pins and column pins.

.. literalinclude:: ../../../freenove_Kit/Code/Python_GPIOZero_Code/21_MatrixKeypad/MatrixKeypad.py
    :linenos: 
    :language: python
    :lines: 8-16

Then, based on the above information, initiates a Keypad class object to operate the Matrix Keyboard.

.. code-block:: c

    keypad.setDebounceTime(100)      #set the debounce time

In the "while" loop, use the function key= keypad.getKey () to read the keyboard constantly. If there is a key pressed, its key code will be stored in the variable "key", and then be displayed.

.. code-block:: c

    while(True):
        key = keypad.getKey()       #obtain the state of keys
        if(key != keypad.NULL):     #if there is key pressed, print its key code.
            print ("You Pressed Key : %c "%(key))

.. c:function:: class Keypad
    def **__init__**(self,usrKeyMap,row_Pins,col_Pins,num_Rows,num_Cols):
    
    Constructed function, the parameters are: key code of keyboard, row pin, column pin, the number of rows, the number of columns.
    
    def **getKey**(self):
    
    Get a pressed key. If no key is pressed, the return value is keypad NULL.
    
    def **setDebounceTime**(self,ms):
    
    Set the debounce time. And the default time is 10ms.
    
    def **setHoldTime**(self,ms):
    
    Set the time when the key holds stable state after pressed.
    
    def **isPressed**(keyChar):
    
    Judge whether the key with code "keyChar" is pressed.
    
    def **waitForKey**():
    
    Wait for a key to be pressed, and return key code of the pressed key.
    
    def **getState**():
    
    Get state of the keys.
    
    def **keyStateChanged**():
    
    Judge whether there is a change of key state, then return True or False.