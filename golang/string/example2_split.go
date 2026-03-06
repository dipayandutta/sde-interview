package main

import (
	"fmt"
	"strings"
)
func main(){
	data := "read,write,append"
	splitedData := strings.Split(data,",")

	fmt.Println(splitedData)

	for i:=0;i<len(splitedData);i++{
		fmt.Println(splitedData[i])
	}
}
