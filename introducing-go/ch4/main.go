package main

import (
	"fmt"
)

func main() {
	// print10Numbers()
	// printEnglishName()
	// printMultipleOfThree()
	fizzBuzz()
}

func print10Numbers() {
	for i := 1; i <= 10; i++ {
		var oddEven string
		if i%2 == 0 {
			oddEven = "even"
		} else {
			oddEven = "odd"
		}
		fmt.Println(i, oddEven)
	}
}

func printEnglishName() {
	fmt.Println("Enter a number from 1 to 9")
	var input int
	fmt.Scanf("%d", &input)
	fmt.Println(getEnglishName(input))
}

func getEnglishName(input int) string {
	switch input {
	case 0:
		return "Zero"
	case 1:
		return "One"
	case 2:
		return "Two"
	case 3:
		return "Three"
	case 4:
		return "Four"
	case 5:
		return "Five"
	case 6:
		return "Six"
	case 7:
		return "Seven"
	case 8:
		return "Eight"
	case 9:
		return "Nine"
	}
	return "Unknown Value"
}

func printMultipleOfThree() {
	for i := 1; 3*i <= 100; i++ {
		fmt.Println(3 * i)
	}
}

func fizzBuzz() {
	for i := 1; i <= 100; i++ {
		if i%15 == 0 {
			fmt.Println(i, "FizzBuzz")
		} else if i%3 == 0 {
			fmt.Println(i, "Fizz")
		} else if i%5 == 0 {
			fmt.Println(i, "Buzz")
		} else {
			fmt.Println(i)
		}
	}
}
