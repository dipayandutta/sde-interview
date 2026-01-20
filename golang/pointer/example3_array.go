package main

import "fmt"

func main() {
	arr := [3] int {1,2,3}
	ptr := &arr[0]
	fmt.Println(*ptr)
	*ptr++
	fmt.Println(*ptr)
}
