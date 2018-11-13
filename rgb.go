package main

import (
	"sync"
	"time"

	rpio "github.com/go-rpio"
)

var wg = new(sync.WaitGroup)

func main() {
	var flashTime = 300
	var pwmHz = 55 * time.Nanosecond
	var dutyCycle = 100

	rpio.Open()
	defer rpio.Close()

	bluePin := rpio.Pin(2)
	bluePin.Output()
	redPin := rpio.Pin(3)
	redPin.Output()
	greenPin := rpio.Pin(4)
	greenPin.Output()

	for {
		go pinOn(pwmHz, dutyCycle, &redPin)
		go pinOn(pwmHz, dutyCycle, &bluePin)
		go pinOn(pwmHz, dutyCycle, &greenPin)
		wg.Wait()
	}
}

func pinOn(pwmHz, dutyCycle int, pin rpio.Pin) bool {
	wg.Add()
	var hz = pwmHz * time.Millisecond
	var pulse = ((dutyCycle / 10) * pwmHz) * time.Millisecond
	pin.High()
	time.Sleep(pulse)
	pin.Low()
	time.Sleep(pulse)
	wg.Done()
}
