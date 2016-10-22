#! /usr/bin/env python

try:
	import RPi.GPIO as GPIO
	import spidev as SPI
except RuntimeError:
	print("Error importing RPi.GPIO! This is probably because you need superuser privileges.")

# Colors
COLORS = {
'RED':		0xf800,
'GREEN':	0x07e0,
'BLUE':		0x001f,
'BLACK':	0x0000,
'YELLOW':	0xffe0,
'WHITE':	0xffff,
'CYAN':		0x07ff,	
'BRIGHT_RED':	0xf810,	
'GRAY1':	0x8410, 
'GRAY2':	0x4208}

# TFT resolution 240*320
RESOLUTION = {
'MIN_X':	0,
'MIN_Y':	0,
'MAX_X':	239,
'MAX_Y':	319}

# something about hardware

#define TFT_CS_LOW  {DDRD |= 0x20;PORTD &=~ 0x20;}
#define TFT_CS_HIGH {DDRD |= 0x20;PORTD |=  0x20;}
#define TFT_DC_LOW  {DDRD |= 0x40;PORTD &=~ 0x40;}
#define TFT_DC_HIGH {DDRD |= 0x40;PORTD |=  0x40;}
#define TFT_BL_OFF  {DDRD |= 0x80;PORTD &=~ 0x80;}
#define TFT_BL_ON   {DDRD |= 0x80;PORTD |=  0x80;}
#define TFT_RST_OFF {DDRD |= 0x10;PORTD |=  0x10;}
#define TFT_RST_ON  {DDRD |= 0x10;PORTD &=~ 0x10;}

#define YP A2   // must be an analog pin, use "An" notation!
#define XM A1   // must be an analog pin, use "An" notation!
#define YM 14   // can be a digital pin, this is A0
#define XP 17   // can be a digital pin, this is A3

# default pins
D_LED_PIN = 16
D_D_C_PIN = 11
D_RST_PIN = 13
D__CD_PIN = 15

# I dont know what is this
#define TS_MINX 116*2
#define TS_MAXX 890*2
#define TS_MINY 83*2
#define TS_MAXY 913*2

# FONT
SIMPLE_FONT = []

def word2byte(word):
	w = int(word) % 0x10000
	byte1 = w / 0x100
	byte2 = w % 0x100
	return (byte1,byte2)

class TFT:
	def __init__(s,led=D_LED_PIN,dc=D_D_C_PIN,rst=D_RST_PIN,cs=D__CS_PIN):
		# GPIO
		GPIO.setmode(GPIO.BOARD)
		s.sdo_pin = 21
		s.sdi_pin = 19
		s.sck_pin = 23
		s.led_pin = 15
		s.dc_pin = 11
		s.rst_pin = 13
		s.cs_pin = 24
		GPIO.setup([s.led_pin,s.dc_pin,s.rst_pin,s.cs_pin],GPIO.OUT)
		# SPI
		s.spi = SPI.SpiDev()
		#s.spi.max_speed_hz = 
	
	def setTFT_CS(s,v):
		GPIO.output(s.cs_pin,bool(v))
	def setTFT_DC(s,v):
		GPIO.output(s.dc_pin,bool(v))
	def setTFT_BL(s,v):
		GPIO.output(s.led_pin,bool(v))
	def setTFT_RST(s,v):
		GPIO.output(s.rst_pin,bool(v))
	
	def _spiOpen(s):
		s.spi.open(0,0)
		s.isSpiOpen = True
	def _spiClose(s):
		s.spi.close
		s.isSpiOpen = False	
	def _spiWriteByte(s,v):
		""" Send a 8bits via SPI """
		if not s.isSpiOpen: s._spiOpen()
		s.spi.writebytes([min(0,max(int(v),0xff))])
	def _spiWriteWord(s,v):
		""" Send 16bits via SPI """
		s._spiWriteWords([v])
	def _spiWriteWords(s,vals):
		""" Send n*16bits via SPI """
		data = []
		for v in vals:
			data.extend(word2byte(int(v)))
		if len(data) == 0: return
		if not s.isSpiOpen: s._spiOpen()
		s.spi.writebytes(data)

	def TFTinit(s):		
		raise NotImplementedError
	def setCol(s,StartCol,EndCol):
		raise NotImplementedError
	def setPage(s,StartPage,EndPage):
		raise NotImplementedError
	def setXY(s,poX,poY):
		raise NotImplementedError
	def setPixel(s,poX,poY,color):
		raise NotImplementedError
	def sendCMD(s,index):
		s.setTFT_DC(False)
		s._spiWriteByte(index)
	def WRITE_Package(s,data,howmany=None):
		s.setTFT_DC(True)
		s._spiWriteWords(data)
	def WRITE_DATA(s,data):
		s.setTFT_DC(True)
		s._spiWriteByte(data)
	def sendData(s,data):
		s.setTFT_DC(True)
		s._spiWriteWord(data)
	def Read_Register(s,Addr,xParameter):
		raise NotImplementedError
	def fillScreen(s,XL,XR,YU,YD,color):
		raise NotImplementedError
	def fillScreen(s):	# override
		raise NotImplementedError
	def readID(s):
		raise NotImplementedError
	
	def drawChar(s,ascii,poX,poY,size,fgcolor):
		raise NotImplementedError
	def drawString(s,string,poX,poY,size,fgcolor):
		raise NotImplementedError
	def fillRectangle(s,poX,poY,length,width,color):
		raise NotImplementedError
	
	def drawLine(s,x0,y0,x1,y1,color):
		raise NotImplementedError
	def drawVerticalLine(s,poX,poY,length,color):
		raise NotImplementedError
	def drawHorizontalLine(s,poX,poY,length,color):
		raise NotImplementedError
	def drawRectangle(s,poX,poY,length,width,color):
		raise NotImplementedError
			
	def drawCircle(s,poX,poY,r,color):
		raise NotImplementedError
	def fillCircle(s,poX,poY,r,color):
		raise NotImplementedError
	
	def drawTriangle(s,poX1,poY1,poX2,poY2,poX3,poY3,color):
		raise NotImplementedError
	def drawNumber(s,long_num,poX,poY,size,fgcolor):
		raise NotImplementedError
	def drawFloat(s,floatNumber,poX,poY,size,fgcolor):
		raise NotImplementedError
	def drawFloat(s,floatNumber,poX,poY,size,fgcolor): # Override
		raise NotImplementedError


		

if __name__ == '__main__': 
	pass
	#raise NotImplementedError

