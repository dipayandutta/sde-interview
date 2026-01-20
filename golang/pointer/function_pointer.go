package main

import "fmt"

func swap(x *int , y *int){
	z := *x
	*x = *y 
	*y = z
}

func main(){
	a := 10
	b := 20
	fmt.Println(a,b)
	swap(&a,&b)
	fmt.Println(a,b)
}
