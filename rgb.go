package main

import (
	"fmt"
	"os"
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
	var pwmHz = 60.00
	var dutyCycle = 70.00
	rpio.Open()
	defer rpio.Close()

	_ = wg
	bluePin := rpio.Pin(2)
	bluePin.High()
	bluePin.Output()
	redPin := rpio.Pin(3)
	redPin.High()
	redPin.Output()
	tOn, tOff := CalcPWM(dutyCycle, pwmHz)
	greenPin := rpio.Pin(4)
	greenPin.High()
	greenPin.Output()

	fmt.Println("tOn: ",tOn)
	fmt.Println("tOff: ",tOff)


	for {
		/*
		redPin.High()
		time.Sleep(tOff)
		redPin.Low()
		time.Sleep(tOn)
		*/
		wg.Add(1)
		pinOn(tOn, tOff, , &redPin)
		wg.Add(1)
		go pinOn(tOn, tOff, , &bluePin)
		wg.Add(1)
		go pinOn(tOn, tOff, , &greenPin)
		wg.Wait()
	}

}

func pinOn(timeOn, timeOff time.Duration pin *rpio.Pin) {
	pin.High()
	time.Sleep(timeOff)
	pin.Low()
	time.Sleep(timeOn)
	wg.Done()
}

//CalcPWM calculates the on off times for a softPWM
func CalcPWM(dutyCycle, pwmHz float64) (time.Duration, time.Duration) {
	var tOn = (dutyCycle / 100) * (1 / pwmHz)
	var tOnString = strconv.FormatFloat(tOn, 'f', 6, 64) //strconv.Itoa(tOn)
	timeOn, err := time.ParseDuration((tOnString + "ms"))
	if err != nil {
		fmt.Println(err)
	}
	var tOffString = strconv.FormatFloat(((1 / pwmHz) - tOn), 'f', 6, 64) //strconv.Itoa(pwmHz - tOn)
	timeOff, err := time.ParseDuration((tOffString + "ms"))
	if err != nil {
		fmt.Println(err)
	}
	return timeOn, timeOff
}
