package main

import "fmt"

func main() {

	fmt.Println("\nCreate array of size 5 and setting 5th element to be 100---------------")
	var x [5]int
	x[4] = 100
	fmt.Println("Array 1: ", x)

	fmt.Println("\nCreating a 5 element array and finding average of it-------------------")
	y := [5]float64{
		93,
		93,
		77,
		82,
		83,
	}
	fmt.Println("Created array: ", y)

	var sum float64

	//for looping
	sum = 0
	for i := 0; i < len(y); i++ {
		sum += y[i]
	}
	fmt.Println("Sum with for-loop is: ", sum)

	//for each looping
	sum = 0
	for _, value := range y {
		sum += value
	}
	fmt.Println("Sum with for-each-loop is: ", sum)
	fmt.Println("Average of the array: ", sum/float64(len(y)))

	//slice
	var z []int
	fmt.Println("Empty slice before append:", z)
	fmt.Println("Appending 1 to the slice")
	z = append(z, 1)
	fmt.Println("Slice after append:", z)

	//creating a slice of size 10
	slice1 := make([]int, 5)
	fmt.Println("Slice of size 5:", slice1)
	slice1 = append(slice1, 6)
	fmt.Println("Slice1 after append:", slice1)

	//appending slice and assigning to a new slice
	slice2 := make([]int, 5)
	slice2[0] = 1
	slice2[1] = 2
	slice2[2] = 3
	slice3 := append(slice2, 4, 5)
	fmt.Println(slice2, slice3)
}
