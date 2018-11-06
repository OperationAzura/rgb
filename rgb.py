import RPi.GPIO as GPIO
import time

def LightOn( pin ):
	GPIO.output(pin, GPIO.LOW)

def LightOff( pin ):
	GPIO.output(pin, GPIO.HIGH)

def RedOn():
	GPIO.output(red, GPIO.LOW)

def RedOff():
	GPIO.output(red, GPIO.HIGH)

def BlueOn():
	GPIO.output(blue, GPIO.LOW)

def BlueOff():
	GPIO.output(blue, GPIO.HIGH)

def GreenOn():
	GPIO.output(green, GPIO.LOW)

def GreenOff():
	GPIO.output(green, GPIO.HIGH)

def PurpleOn():
	RedOn()
	BlueOn()

def PurpleOff():
	RedOff()
	BlueOff()

def YellowOn():
	RedOn()
	GreenOn()

def YellowOff():
	RedOff()
	GreenOff()

def WhiteOn():
	RedOn()
	BlueOn()
	GreenOn()

def WhiteOff():
	RedOff()
	BlueOff()
	GreenOff()

def CyanOn():
	BlueOn()
	GreenOn()

def CyanOff():
	BlueOff()
	GreenOff()

class Light:
	"Light object to controll a pwm powered led"
	
	dutyCycleUp = True
	dutyCycle = 0
	pin = 0
		
t = 1
flashTime = 300
blue = 2
red = 3
green = 4
pwmHz = 255

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(blue, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

bluePWM = GPIO.PWM(blue, pwmHz)
redPWM = GPIO.PWM(red, pwmHz)
greenPWM = GPIO.PWM(green, pwmHz)

#pins act as ground, so 100 = off
bluePWM.start(100)
redPWM.start(100)
greenPWM.start(100)
while True:
	WhiteOff()
	while True:
		bx = 100
		rx = 50
		gx = 0
		while bx > 0:
			#greenPWM.ChangeDutyCycle(gx)
			#redPWM.ChangeDutyCycle(rx)
			bluePWM.ChangeDutyCycle(bx)
			bx = bx - 1
			rx = rx - 1
			gx = gx + 1
			time.sleep(.05)
		while bx < 100:
			#greenPWM.ChangeDutyCycle(gx)
			#redPWM.ChangeDutyCycle(rx)
			bluePWM.ChangeDutyCycle(bx)
			bx = bx + 1
			rx = rx + 1 
			gx = gx - 11
			time.sleep(.05)

	YellowOn()
	time.sleep(t)
	YellowOff()
	CyanOn()
	time.sleep(t)
	CyanOff()
	WhiteOn()
	time.sleep(t)
	WhiteOff()
	
	PurpleOn()
	time.sleep(t)
	PurpleOff()
	RedOn()
	time.sleep(t)
	RedOff()
	BlueOn()
	time.sleep(t)
	BlueOff()
	GreenOn()
	time.sleep(t)
	GreenOff()

	print"flashing light"
	#for x in range (flashTime):
		#GPIO.output(pin, GPIO.HIGH)
		#GPIO.output(pin2, GPIO.HIGH)
		#GPIO.output(pin3, GPIO.HIGH)
		#time.sleep(0.1)
		#GPIO.output(pin, GPIO.LOW)
		#GPIO.output(pin2, GPIO.LOW)
		#GPIO.output(pin3, GPIO.LOW)
		#time.sleep(0.1)

