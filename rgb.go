package main

import (
	"time"

	rpio "github.com/go-rpio"
)

func main() {
	var t = 1
	var flashTime = 300
	var pwmHz = 55 * time.Nanosecond

	rpio.Open()
	defer rpio.Close()

	bluePin := rpio.Pin(2)
	bluePin.Output()
	redPin := rpio.Pin(3)
	redPin.Output()
	greenPin := rpio.Pin(4)
	greenPin.Output()

	for {
		redPin.Low()
		bluePin.Low()
		greenPin.Low()
		time.Sleep(pwmHz)
		redPin.High()
		bluePin.High()
		greenPin.High()
		time.Sleep(pwmHz)
	}

}
