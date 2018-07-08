# Raspberry Pi RFID Door Lock
---
### A simple, yet powerful RFID verified Door Strike controller for Raspberry Pi based on MySQL and PHP.

*Originally created for Davenport Central High School Robotics Teams.*

__*NOTE: This product is still in development. Features that are described in the README might not be in effect in the latest iteration of the repo. Check commits to see latest revisions.*__

## How it Works
---
1. Each user is given a unique RFID tag that is then input into a MySQL database.
2. When a tag is scanned, the `Unique ID` of the card is then cross-refrenced with the MySQL Database and then either verified or denied. There is also an option to enable time verification features in the [DB-Update](../master/DB-Update.py) file.
    1. If verified:
        * User is Granted Access by changing the state of a GPIO Pin connected to the strike plate control circuit.
        * [MySQL-Update](../master/MySQL-Update) runs to update the database and toggle the current state of the user.
             (If the user is currently OUT, status will change to IN, and vice versa.)
        * Changes to the Database will be reflected in the Webpage.
    2. If denied:
        * User will not be granted access, status light will blink red, and failed attempt will be logged in the database/webpage

## Installation Instructions
---
1. Package Requirements
    1. LAMP
        * Linux
        * Apache HTTP Server
        * MySQL Database Management System
        * PHP Language
    2. PyMySQL
        * This will allow us to interface with the MySQL database by using a Python script
    3. RPi.GPIO
        * This will control the Strike Plate circuit
    4. ondryaso's [pi-rc522](https://github.com/ondryaso/pi-rc522) repo
        * Allows the program to read the RFID cards scanned
    5. Packages needed for pi-rc522
        1. [spidev](https://pypi.org/project/spidev/)
        1. [RPi.GPIO](https://pypi.org/project/RPi.GPIO/)
    
    
        
## Circuit Diagram
---
