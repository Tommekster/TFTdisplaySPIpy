# TFT display SPI driver in Python

## Aim

I am going to rewrite Arduino library from https://github.com/gmtii/ili9341-arduino
in order to control this kind of TFT display using Raspberry Pi SPI (interface).

## Hardware

### Chart
	
	                             +--+      
	                        3v3--|oo|-- 5v 
	                        02 --|oo|-- 5v 
	                        03 --|oo|---GND
	----+     ,-------,     04 --|oo|-- 14
	 SDO|----/--------+-,  GND --|oo|-- 15
	 LED|---'  ,------+-+---17 --|oo|---18
	 SCK|-----/-, ,---+-+---27 --|oo|-- GND
	 SDI|----/-, X    '-+---22 --|oo|-- 23
	 D/C|---'   X \   ,-+--3v3 --|oo|-- 24
	 RST|------' '-\-/--+---10 --|oo|-- GND
	  CS|->CS       X   '---09 --|oo|-- 25
	 GND|----------/,'------11 --|oo|-- 08--->CS
	 VCC|---------'  '-----GND --|oo|-- 07
	----+                  IDSD--|oo|-- ID_SC
	                        05 --|oo|-- GND
	                        06 --|oo|-- 12
	                        13 --|oo|-- GND
	                        19 --|oo|-- 16
	                        26 --|oo|-- 20
	                       GND --|oo|-- 21
	                             +--+
### Pinout

| Display pin   | Rpi GPIO Header pin | Rpi pin function |
|:-------------:|:-------------------:|:----------------:|
| SDO (MISO)    | 21                  | MISO             |
| LED           | 15                  | GPIO22           |
| SCK           | 23                  | CLK              |
| SDI (MOSI)    | 19                  | MOSI             |
| D/C           | 11                  | GPIO17           |
| RST           | 13                  | GPIO27           |
| CS            | 24                  | SPI_CE0_N        |
| GND           | 25                  | GND              |
| VCC           | 17                  | 3v3              |


## SPI interface
I am using *spidev* python module. 
It is available on [Github][spidev github].
Before install ensure that you have *python-dev* package, 
otherwise `sudo apt-get install python-dev`.

## Reference
* [Arduino library](https://github.com/gmtii/ili9341-arduino)
* [Python Spidev][spidev github]
* [Usind Spidev](http://www.100randomtasks.com/simple-spi-on-raspberry-pi)

[spidev github]: https://github.com/doceme/py-spidev
