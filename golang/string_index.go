package main

import "fmt"

func main(){

	for index, s:= range "Dipayan" {
		fmt.Println("%c is %d \n",s,index)
	}
}
