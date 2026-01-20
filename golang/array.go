package main

import "fmt"

func main() {
	var a[5] int
	fmt.Println("emp:",a)

	a[4] = 100
	fmt.Println("set:",a)
	fmt.Println("Get:",a[4])

	//Lenght of the array
	fmt.Println("Length of the array:",len(a))

	b := [5] int {1,2,3,4,5}
	fmt.Println(b)

	b = [...]int{10,22,33,34,-1}
	fmt.Println(b)
} 
