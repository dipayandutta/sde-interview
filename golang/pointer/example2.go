package main

import "fmt"

func addOne(x *int){
	*x++
}

func main(){
	x := 10
	fmt.Println(x)
	addOne(&x)
	fmt.Println(x)
}
