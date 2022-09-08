// echo1 prints its command line arguments
package main

import (
	"fmt"
	"os"
)

func main() {
	var result, separator string

	for i := 1; i < len(os.Args); i++ {
		result += separator + os.Args[i]
		separator = " "
	}

	fmt.Println(result)
}
