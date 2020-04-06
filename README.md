# Weatherbox 

Weatherbox is a simple weather display built with a Raspberry Pi and a [Waveshare ePaper display](https://www.waveshare.com/wiki/4.2inch_e-Paper_Module). 

## Installation and setup

### Software Setup

First, install Node.js. Make sure to download the version of Node.js that corresponds to your Raspberry Pi's architecture.

For Raspberry Pi 4/3 B+ (armv7l):

```bash
$ wget https://nodejs.org/dist/latest-v12.x/node-v12.6.0-linux-armv7l.tar.gz
$ tar -xzf node-v12.6.0-linux-armv7l.tar.gz
$ sudo cp -R node-v12.6.0-linux-armv7l/* /usr/local/
```

For Raspberry Pi Zero (armv61):

```bash
$ wget https://nodejs.org/dist/v11.15.0/node-v11.15.0-linux-armv6l.tar.gz
$ tar -xzf node-v11.15.0-linux-armv6l.tar.gz
$ sudo cp -R node-v11.15.0-linux-armv6l/* /usr/local/
```

Next, install the libraries required for the display:

```bash
$ sudo apt install python3-pip
$ sudo apt install python-imaging
$ sudo pip3 install spidev
$ sudo pip3 install RPi.GPIO
$ sudo pip3 install python-pil
$ sudo apt install fonts-roboto
$ pip install pyyaml
```

Since, the Waveshare display uses the SPI interface, we have to enable it on the Raspberry Pi. You can find a guide [here](https://www.raspberrypi-spy.co.uk/2014/08/enabling-the-spi-interface-on-the-raspberry-pi/).

### ePaper to Raspberry Pi Hardware connection

| ePaper | Raspberry Pi (GPIO) |
|--------|---------------------|
| 3.3V   | 3.3V                |
| GND    | GND                 |
| DIN    | 19                  |
| CLK    | 23                  |
| CS     | 24                  |
| DC     | 22                  |
| RST    | 11                  |
| BUSY   | 18                  |

### Cronjob Setup

Finally, schedule a cronjob:

```bash
$ cd cronjob
$ ./add_cronjob.sh
```
![Weatherbox display](resources/weatherbox.jpg)