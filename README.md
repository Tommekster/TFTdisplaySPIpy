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
	----+                   04 --|oo|-- 14
	 SDO|---------------,  GND --|oo|-- 15
	 LED|->LED ,--------+---17 --|oo|---18
	 SCK|-----/-, ,-----+---27 --|oo|-- GND
	 SDI|----/-, X   ,--+---22 --|oo|-- 23--->LED
	 D/C|---'   X \ / ,-+--3v3 --|oo|-- 24
	 RST|------' '-X-/--+---10 --|oo|-- GND
	  CS|---------' X   '---09 --|oo|-- 25
	 GND|----------/,'------11 --|oo|-- 08
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
| LED           | 16                  | GPIO23           |
| SCK           | 23                  | CLK              |
| SDI (MOSI)    | 19                  | MOSI             |
| D/C           | 11                  | GPIO17           |
| RST           | 13                  | GPIO27           |
| CS            | 15                  | GPIO22           |
| GND           | 25                  | GND              |
| VCC           | 17                  | 3v3              |
