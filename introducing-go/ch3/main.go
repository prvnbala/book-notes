package main

import "fmt"

var name = "John Doe"

func main() {

	// concatString()
	// accessGlobalVariable()
	// doubleInput()
	// convertFahrenheitToCelsius()
	convertFeetToMeter()
}

func accessGlobalVariable() {
	fmt.Println("accessGlobalVariable func's name:", name)
	someFunc()
}

func concatString() {
	var x string
	x = "Hello"
	fmt.Println(x)
	x = x + " " + "World!"
	fmt.Println(x)
}

func someFunc() {
	fmt.Println("SomeFunc's name:", name)
}

func doubleInput() {
	fmt.Println("Enter a number:")
	var input float64
	fmt.Scanf("%f", &input)
	output := input * 2
	fmt.Println(output)
}

func convertFahrenheitToCelsius() {
	fmt.Println("Enter a temperature in Fahrenheit:")
	var input float64
	fmt.Scanf("%f", &input)
	output := ((input - 32) * (5.0 / 9.0))
	fmt.Println("Temperature in Celsius: ", output)
}

func convertFeetToMeter() {
	const feetToMeterRatio float64 = 0.3048
	var input float64
	fmt.Println("Enter the distance in feet:")
	fmt.Scanf("%f", &input)
	output := input * feetToMeterRatio
	fmt.Println("Distance in meter: ", output)
}
