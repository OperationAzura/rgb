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
	Pin = 0
	pwmHz = 255
	pwm = GPIO.PWM

	def SetPWM(self):
		self.pwm = GPIO.PWM(self.pin, self.pwmHz)
	def StartPWM(self,dc):
		self.pwm.start(dc)
	def LightPWM(self):
		self.pwm.ChangeDutyCycle(self.dutyCycle)
		self.IncrementDutyCycle()
		print"incrementing"
	#IncrementDutyCycle will either increment or decrement as dutycycle cannot go above 100 or below 0
	def IncrementDutyCycle(self):
		#set dutyCycleUp
		if (self.dutyCycle == 0):
			self.dutyCycleUp = True
		elif (self.dutyCycle == 100):
			self.dutyCycleUp = False
		if (self.dutyCycleUp == True): #increment
			print"increment"
			self.dutyCycle = self.dutyCycle + 1
		else: #decrement
			print"decrement"
			self.dutyCycle = self.dutyCycle - 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


t = 1
flashTime = 300
blue = 2
red = 3
green = 4
pwmHz = 255

GPIO.setup(blue, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)


g = Light()
b = Light()
r = Light()
g.pin = green
b.pin = blue
r.pin = red
g.SetPWM()
b.SetPWM()
r.SetPWM()
g.StartPWM(0)
b.StartPWM(50)
r.StartPWM(100)

bluePWM = GPIO.PWM(blue, pwmHz)
redPWM = GPIO.PWM(red, pwmHz)
greenPWM = GPIO.PWM(green, pwmHz)
b.dutyCycle = 100
r.dutyCycle = 50
g.dutyCycle = 0

#pins act as ground, so 100 = off
#bluePWM.start(100)
#redPWM.start(100)
#greenPWM.start(100)
while True:
	WhiteOff()
	while True:
		g.LightPWM()
		time.sleep(.01)
		b.LightPWM()
		r.LightPWM()
		
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
