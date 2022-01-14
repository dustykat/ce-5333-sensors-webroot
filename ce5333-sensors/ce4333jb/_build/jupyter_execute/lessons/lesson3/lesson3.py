#!/usr/bin/env python
# coding: utf-8

# # Non-Contact Temperature Sensor

# A simple sensor system to measure temperature without direct contact. 
# 
# ## Objective
# 
# Our objective is to use an IR sensor to measure temperature of objects without contact.  The sensor and code can be adapted to practical uses, so although simplistic here - a little refinement can produce a useful tool for some engineering measurements. The motivating problem is measurement of thermal behavior of concrete mixtures as they cure - imbedding a thermal probe would be a legitimate approach, but here we want to explore remote measurement.  Unlike our PIR project, we now care about accuracy.
# 
# ## Operation Principle
# 
# The MLX90614 sensor is manufactured by Melexis Microelectronics Integrated systems, it works on the principle of InfraRed thermopile sensor for temperature measurement. 
# These sensors consist of two units embedded internally to give the temperature output. 
# The first unit is the sensing unit which has an infrared detector which is followed by the second unit which performs the computation of the data with Digital signal processing (DSP). 
# 
# This sensor works based on the [Stefan-Boltzmann law](https://en.wikipedia.org/wiki/Stefan%E2%80%93Boltzmann_law) that states the power radiated by a black body is proportional to its temperature. In simple terms, any object emits IR energy and the intensity of that will be directly proportional to the temperature of that object. MLX90614 sensor converts the detected value into 17-bit value using an on-board ADC that can be accessed using the I2C communication protocol. These sensors measure the ambient temperature as well as object temperature with the resolution calibration of 0.02°C. To learn more about the MLX90614 sensor, refer to the [MLX90614 Datasheet](https://www.sparkfun.com/datasheets/Sensors/Temperature/MLX90614_rev001.pdf).
# 
# ## Hardware
# 
# For this lesson we will use the MLX90614 IR Temperature Sensor. This sensor different from the PIR sensor in that it can give us object temperature and ambient temperature. You can buy it at Amazon and a few other sources for about \$13 [https://www.amazon.com/HiLetgo-MLX90614ESF-Non-contact-Infrared-Temperature](https://www.amazon.com/HiLetgo-MLX90614ESF-Non-contact-Infrared-Temperature/dp/B071VF2RWM/ref=sr_1_1_sspa?crid=3K12PBA02OOKG&keywords=MLX90614&qid=1642181841&sprefix=mlx90614%2Caps%2C483&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFFSVNCVDlCOFQ0MkQmZW5jcnlwdGVkSWQ9QTA2MDUzMzMzMEEyWlVOU1hYODdRJmVuY3J5cHRlZEFkSWQ9QTAzMzE4NzYzTFVMWkdOOEYzQU5SJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==)  
# 
# ## I2C interface and libraries
# 
# This sensor uses the I2C interface and will use a different set of libraries than the GPIO libraries used in the PIR sensor.  The I2C acronym stands for inter-integrated circuit and is a method designed to allow one chip to talk to another synchronously. 
# 
# > (from Wikipedia ...) I2C (Inter-Integrated Circuit, eye-squared-C), alternatively known as I2C or IIC, is a synchronous, multi-controller/multi-target (master/slave), packet switched, single-ended, serial communication bus invented in 1982 by Philips Semiconductors. It is widely used for attaching lower-speed peripheral ICs to processors and microcontrollers in short-distance, intra-board communication. 
# 
# For our use it is just another way to access the sensor, because the module has an A/D built into it, I2C is a preferred approach.  We will still use the GPIO pins, but using the I2C interface reassigns them to specific parts of the SBC processor and interface hardware.
# 
# ### Interfacing MLX90614 with Raspberry Pi
# 
# #### Step1: Enabling the I2C from Raspberry Pi setting.
# 
# Type sudo raspi-config and then go to interfacing options.
# 
# ```{figure} select-interface.png
# ---
# width: 500px
# name: select-interface
# ---
# `sudo raspi-config` ncurses terminal. Select Interfaces.
# ```
# 
# ```{figure} select-i2c.png
# ---
# width: 500px
# name: select-i2c
# ---
# `sudo raspi-config` ncurses terminal. Select I2C.
# ```
# 
# ```{figure} select-enable.png
# ---
# width: 500px
# name: select-enable
# ---
# `sudo raspi-config` ncurses terminal. Select Yes.
# ```
# 
# ```{figure} i2c-enabled.png
# ---
# width: 500px
# name: i2c-enabled
# ---
# `sudo raspi-config` ncurses terminal interface. Confirm I2C is active.
# ```
# 
# #### Step2.0: Download the package/library of MLX90614 
# 
# Navigate to https://pypi.org/project/PyMLX90614/#files, then **right click and copy** the link address. 
# 
# Go to RPI terminal and type `wget` and paste the link copied like below.
# 
# ```{figure} get-libraries.png
# ---
# width: 500px
# name: get-libraries
# ---
# Command line `wget https://files.pythonhosted.org/packages/67/8a/443af31ff99cca1e30304dba28a60d3f07d247c8d410822411054e170c9c/PyMLX90614-0.0.3.tar.gz` ready to run
# ```
# It will download the library in the zip file name ‘PyMLX90614-0.0.3.tar.gz’. 
# 
# ```{figure} lib-dl-complete.png
# ---
# width: 500px
# name: lib-dl-complete
# ---
# Library download complete; no errors reported
# ```
# #### Step2.1: Extract the library
# 
# Then extract the folder with the extension of `tar -xvf file name`
# 
# ```{figure} extract-lib.png
# ---
# width: 600px
# name: extract-lib
# ---
# Extracting the `.tar.gz` file
# ```
# 
# #### Step 3.0 Updating the OS to interact with the library
# 
# Next we will get some tools and install them in the OS distribution (most Blog posts will tell you to update the OS which is the first line below
# 
# ```
# sudo apt-get update && sudo apt-get upgrade
# ```
# 
# Then execute
# ```
# sudo apt-get install python-setuptools 
# ```
# ```{figure} python-tools.png
# ---
# width: 400px
# name: python-tools
# ---
# Installing Python-SetUp Tools.  
# ```
# 
# Then execute
# ```
# sudo apt-get install -y i2c-tools
# ```
# 
# ```{figure} i2c-tools.png
# ---
# width: 400px
# name: i2c-tools
# ---
# Installing I2C Tools; here it was already done elsewhere, so we get a warning and no more.
# ```
# 
# Then we run
# 
# ```
# sudo python setup.py install
# sudo python3 setup.py install
# ``` 
# in the extracted library directory.
# 
# :::{note}
# I choose to run both default python and python3 so that either interpreter has access to the library.  Most of the scripts in this book assume python3 is what is used.
# :::
# 
# 
# 
# 
# Now we interface the MLX90614 sensor with Raspberry Pi using the circuit below.
# 
# ```{figure} CircuitCity.png
# ---
# width: 400px
# name: CircuitCity
# ---
# Circuit diagram from Ujjainwala (2020).
# ```
# 
# ```{figure} prototype.png
# ---
# width: 400px
# name: prototype
# ---
# Circuit diagram from Ujjainwala (2020).
# ```
# 
# ```{figure} sensor-module.png
# ---
# width: 400px
# name: sensor-module
# ---
# Circuit diagram from Ujjainwala (2020).
# ```
# 
# ```{figure} pin-out.png
# ---
# width: 400px
# name: pin-out
# ---
# Circuit diagram from Ujjainwala (2020).
# ```
# 
# #### Check I2C addressing
# 
# ### Now Try out the sensor
# 
# 
# Now, we make a new file name mlxread.py and write a sample program to check the data from the sensor.
# 
# ```
# # python2.7 code
# from smbus2 import SMBus
# from mlx90614 import MLX90614
# bus = SMBus(1)
# sensor = MLX90614(bus, address=0x5A)
# print "Ambient Temperature :", sensor.get_ambient()
# print "Object Temperature :", sensor.get_object_1()
# bus.close()
# ```
# 
# ```
# # python3.X code
# from smbus2 import SMBus
# from mlx90614 import MLX90614
# bus = SMBus(1)
# sensor = MLX90614(bus, address=0x5A)
# print("Ambient Temperature :", sensor.get_ambient())
# print("Object Temperature :", sensor.get_object_1())
# bus.close()
# ```
# 
# Once the file is created, we will run it with python extension python mlxread.py. 
# The output is shown below. I used a torch (flashlight) as the heat source.
# 
# ```{figure} example-run.png
# ---
# width: 400px
# name: example-run
# ---
# Circuit diagram from Ujjainwala (2020).
# ```
# 
# 
# 

# ## Exercises
# 
# 1. Using the `time` module, capture the time when the reading is taken.
# 2. Put the script into a function, then embed the function into another script to take readings every 15 seconds for 10 minutes.
# 3. (Advanced) Write a BASH script to run the sensor for 24 hours using the `cron` table and your modified script.  Have the script append to a file, so that if the system fails (power interrupt) you don't lose all the data.

# ## 

# ## 

# ## References
# 
# 1. [MLX90614 Datasheet (Melexis LLC)](https://www.sparkfun.com/datasheets/Sensors/Temperature/MLX90614_rev001.pdf)
# 
# 2. [I2C interface (Wikipedia)](https://en.wikipedia.org/wiki/I%C2%B2C)
# 
# 1. Taher Ujjainwala (2020).  *IoT Based Contactless Body Temperature Monitoring using Raspberry Pi with Camera and Email Alert* [https://circuitdigest.com/microcontroller-projects/iot-based-contactless-body-temperature-monitoring-using-raspberry-pi-with-camera-and-email-alert](https://circuitdigest.com/microcontroller-projects/iot-based-contactless-body-temperature-monitoring-using-raspberry-pi-with-camera-and-email-alert)
# 
# 

# 

# 

# 
