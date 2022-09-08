// echo2 prints its command line arguments
package main

import (
	"fmt"
	"os"
)

func main() {
	s, sep := "", ""
	for _, word := range os.Args[1:] {
		s += sep + word
		sep = " "
	}
	fmt.Println(s)
}
