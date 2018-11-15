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
	var pwmHz = 160.00
	var dutyCycle = 30.00
	rpio.Open()
	defer rpio.Close()

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

	for {
		redPin.High()
		time.Sleep(tOff)
		redPin.Low()
		time.Sleep(tOn)
		//wg.Add(1)
		//pinOn(pwmHz, dutyCycle, &redPin)
		//wg.Add(1)
		//go pinOn(pwmHz, dutyCycle, &bluePin)
		//wg.Add(1)
		//go pinOn(pwmHz, dutyCycle, &greenPin)
		wg.Wait()
		//dutyCycle--
	}

}

func pinOn(pwmHz, dutyCycle float64, pin *rpio.Pin) {
	start := time.Now()
	//wg.Add(1)
	var tOn = (dutyCycle / 100) * (1 / pwmHz)
	var tOnString = strconv.FormatFloat(tOn, 'f', 6, 64) //strconv.Itoa(tOn)
	timeOn, _ := time.ParseDuration((tOnString + "ms"))
	//if err != nil {
	//	fmt.Println(err)
	//}
	var tOffString = strconv.FormatFloat(((1 / pwmHz) - tOn), 'f', 6, 64) //strconv.Itoa(pwmHz - tOn)
	timeOff, _ := time.ParseDuration((tOffString + "ms"))
	//if err != nil {
	//	fmt.Println(err)
	//}
	fmt.Println("tOff: ", timeOn)
	fmt.Println("tOn", timeOff)
	//os.Exit(1)
	pin.High()
	time.Sleep(timeOff)
	pin.Low()
	time.Sleep(timeOn)
	wg.Done()
	fmt.Println("it took: ", time.Since(start))
	os.Exit(1)
}

//CalcPWM calculates the on off times for a softPWM
func CalcPWM(dutyCycle, pwmHz float64) (string, string) {
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
