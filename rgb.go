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
	var pwmHz = 60
	var dutyCycle = 100
	rpio.Open()
	defer rpio.Close()

	bluePin := rpio.Pin(2)
	bluePin.Output()
	redPin := rpio.Pin(3)
	redPin.Output()
	greenPin := rpio.Pin(4)
	greenPin.Output()

	
/*
	for {
		wg.Add(1)
		go pinOn(pwmHz, dutyCycle, &redPin)
		wg.Add(1)
		go pinOn(pwmHz, dutyCycle, &bluePin)
		wg.Add(1)
		go pinOn(pwmHz, dutyCycle, &greenPin)
		wg.Wait()
		//dutyCycle--
		if dutyCycle < 0{
			dutyCycle = 100
		}
	}
	*/
}

func pinOn(pwmHz, dutyCycle int, pin *rpio.Pin) {
	//wg.Add(1)
	var pString = strconv.Itoa((dutyCycle  / 100 ) * pwmHz)
	pulse, err := time.ParseDuration((pString+"ms"))
	if err != nil{
		fmt.Println(err)
	}
	pin.High()
	time.Sleep(pulse)
	pin.Low()
	time.Sleep(pulse )
	wg.Done()
}
