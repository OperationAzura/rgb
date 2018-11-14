package main

import (
	"fmt"
	"strconv"
	"sync"
	"time"

	rpio "github.com/go-rpio"
)

//
//dutyCycle = tOn / hz
//

var wg = new(sync.WaitGroup)

func main() {
	var pwmHz = 0.60
	var dutyCycle = 100.99
	rpio.Open()
	defer rpio.Close()

	bluePin := rpio.Pin(2)
	bluePin.Output()
	redPin := rpio.Pin(3)
	redPin.Output()
	greenPin := rpio.Pin(4)
	greenPin.Output()

	for {
		wg.Add(1)
		go pinOn(pwmHz, dutyCycle, &redPin)
		wg.Add(1)
		go pinOn(pwmHz, dutyCycle, &bluePin)
		wg.Add(1)
		go pinOn(pwmHz, dutyCycle, &greenPin)
		wg.Wait()
		//dutyCycle--
		if dutyCycle < 0 {
			dutyCycle = 100
		}
	}

}

func pinOn(pwmHz, dutyCycle float64, pin *rpio.Pin) {
	//wg.Add(1)
	var tOn = (dutyCycle / 100) * pwmHz
	var tOnString = strconv.FormatFloat(tOn, 'f', 6, 64//strconv.Itoa(tOn)
	timeOn, err := time.ParseDuration((tOnString + "ms"))
	if err != nil {
		fmt.Println(err)
	}
	var tOffString = strconv.FormatFloat((pwmHz - tOn), 'f', 6, 64//strconv.Itoa(pwmHz - tOn)
	timeOff, err := time.ParseDuration((tOffString + "ms"))
	if err != nil {
		fmt.Println(err)
	}
	pin.High()
	time.Sleep(timeOn)
	pin.Low()
	time.Sleep(timeOff)
	wg.Done()
}
