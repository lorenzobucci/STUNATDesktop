# STUNAT Desktop

**Project for Human Computer Interaction course 2021/2022**

The project consists in the development of a desktop application that determines the type of NAT present in the network of the device carrying out the test.
The GUI of the application is really simple, so it can be used by an average user but also by a network engineer who may need to customize some settings.

The whole project was written in Python 3.9 using the PyQt5 framework and the _pystun_ library.
This library makes use of the protocol and techniques called **STUN** (Session Traversal Utilities for NAT) which, thanks to the use of an external server, allow to establish the type of NAT that is in the middle of the network path.

## Program execution

### Step 0: Launch

To launch the application simply run from the command line the *main.py* script in the *src* folder, as specified below:

```console
python3 src/main.py
```

Otherwise, it is possible to download the binaries for Windows and Linux (tested on Ubuntu) from the Release section of GitHub, both in the 64-bit version.

### Step 1: Start test

The program is ready to use and clicking on _Start test_ it will establish a communication with the STUN server _stun.sipgate.net_ on UDP port 3478.
After running the test, the result and some additional details will be shown, including the ability to view a more advanced log relating to the operations of the _pystun_ library.

For more details on the possible results obtained, you can go to the Wikipedia NAT page: https://en.wikipedia.org/wiki/Network_address_translation#Methods_of_translation.
If there is no NAT present, i.e. the system has a public IP address, the application will return "Open Internet" or "Symmetric UDP Firewall" if it detects the presence of a firewall that blocks UDP ports.

### Step 2: Advanced options

It's possible to customize some advanced parameters that will modify the execution of the test:
* _STUN Server_: allows you to change the STUN server with which the test will be performed.
* _Source IP address_: if your system has multiple network cards, you can choose which local IP address to use for testing. The _Default_ option uses the default network card given by the operating system.
* _Local port_: allows you to select the UDP port from which to start communication with the STUN server. This field, when compared with the resulting external port, allows you to understand if port numbers are changed by the NAT or not.

#### Language

The language is automatically chosen at startup based on the operating system's language. However, there's an option that allows you to manually change the program language.
Currently, it's possible to choose between English or Italian.

