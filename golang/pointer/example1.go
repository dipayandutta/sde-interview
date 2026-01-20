package main

import "fmt"

func main(){
var x int = 10
var ptr *int = &x

fmt.Println(x)
fmt.Println(ptr)
fmt.Println(*ptr)
}
