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

	def __init__(self, pin, dutyCycle, pwmHz):
		GPIO.setup(pin, GPIO.OUT)
		self.pin = pin
		self.pwmHz = pwmHz
		self.SetPWM()
		self.dutyCycle = dutyCycle
		self.StartPWM(dutyCycle)

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

g = Light(green, 33, 50)
b = Light(blue, 66, 50)
r = Light(red, 99, 50)
while True:
	WhiteOff()
	while True:
		g.LightPWM()
		time.sleep(.06)
		b.LightPWM()
		r.LightPWM()
		
