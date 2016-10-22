#! /usr/bin/env python

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


# I dont know what is this
#define TS_MINX 116*2
#define TS_MAXX 890*2
#define TS_MINY 83*2
#define TS_MAXY 913*2

# FONT
SIMPLE_FONT = []

class TFT:
	def __init__(s):
		raise NotImplementedError
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
		raise NotImplementedError
	def WRITE_Package(s,data,howmany):
		raise NotImplementedError
	def WRITE_DATA(s,data):
		raise NotImplementedError
	def sendData(s,data):
		raise NotImplementedError
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

