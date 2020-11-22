# ce5333sensors-webroot
CE 5333 Civil Engineering Sensor Systems Integration - install in webroot

This repository contains course materials for CE 5333 sensors course.  
The repository is designed to be installed on a web server just off the FQDN webroot (or wherever you want to make the symlink).  

I use Apache but it will probably work as well or better on NGINX

## Description

A hands-on "maker" course to develop homebrew sensor and data aquisition tools. Useful for beginning researchers to collect data at low cost for screening level data. The sensors and programs are adaptable to professional use. Entire systems will be built and demonstrated -- the projects are mostly water related, but concepts are transferable to other Civil sub-disciplines. Intended for graduate students with minimal electronics skills, and minimal computer administration skills. Students should know how to solder and have had a circuits class somewhere.

## Objectives
Upon successful completion of this course, the participant will:
1. Provision a single-board computer(Raspberry PI; Hardkernel XU4; Arduino, etc) to run a Linux instance and host a wireless network.
2. Construct Analog-to-Digital Converter using MP3008 microprocessor.
3. Select and attach sensors to the computer system using the GPIO pins. Sensor type based on environmental variable of interest and data type (counting, voltage level, current level)
4. Write custom Python scripts to control senors, collect, and process data.
5. Use custom built system to control a device based on sensor input (by activating a relay on demand).
6. Deploy onto a second SBC and control by wireless remote procedure calls.

## Notes:

1. `3-Readings` may contain copyright materials, so this directory should be protected (.htaccess should be secure enough to fit in fair use)
2.  Many of the notes do not have complete citations; very little of my work is original, so as the content matures the notes will eventually have complete, proper, citations.

