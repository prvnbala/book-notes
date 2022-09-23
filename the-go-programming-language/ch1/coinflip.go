package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	heads := 0
	tails := 0
	for i := 0; i < 20; i++ {
		switch coinflip() {
		case "heads":
			heads++
		case "tails":
			tails++
		default:
			fmt.Println("Coin landed on edge!")
		}
	}

	fmt.Println("Heads count:", heads)
}

func coinflip() string {
	rand.Seed(time.Now().UnixNano())
	n := rand.Intn(2)
	switch n {
	case 0:
		return "heads"
	case 1:
		return "tails"
	}
	return ""
}
