package main

import (
	"fmt"
	"strings"
)

func main(){
	text := "go is simple go is powerful"

	words := strings.Fields(text)
	fmt.Println(words)

	frequency := make(map[string]int)
	fmt.Println(frequency)

	for _,word := range words{
		frequency[word]++
	}

	fmt.Println(frequency)

	for word,count := range frequency {
		fmt.Println(word,":",count)
	}
}
