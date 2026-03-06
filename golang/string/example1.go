package main

import (
	"fmt"
	"strings"
)

func main(){
	text := "golang is powerfull"

	fmt.Println(strings.Contains(text,"golang"))
	fmt.Println(strings.Contains(text,"java"))
}
