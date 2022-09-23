package main

import "fmt"

func main() {
	x := 5
	xAddr := &x

	fmt.Println(x, xAddr, *xAddr)

	*xAddr = 10
	fmt.Println(x, xAddr, *xAddr)
}
