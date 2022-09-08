// echo3 prints its command line arguments
package main

import (
	"fmt"
	"os"
	"strings"
	"time"
)

func main() {
	fmt.Println(strings.Join(os.Args[1:], " "))
	fmt.Println(os.Args[1:])

	//printing the first element as well
	fmt.Println(os.Args)

	//printing each arg in new line
	for index, arg := range os.Args {
		fmt.Println(index, arg)
	}

	//time measurement between two approaches
	start := time.Now()
	sentence, separator := "", ""
	for _, arg := range os.Args[1:] {
		sentence += separator + arg
		separator = " "
	}
	// fmt.Println(sentence)
	fmt.Println("Time elapsed: ", time.Since(start).Microseconds())

	start = time.Now()
	sentence, separator = "", ""
	sentence = strings.Join(os.Args[1:], " ")
	// fmt.Println(sentence)
	fmt.Println("Time elapsed: ", time.Since(start).Microseconds())

}
