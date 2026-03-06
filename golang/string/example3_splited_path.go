package main

import ( 
	"fmt"
	"strings"
)

func main(){
	
	path := "/usr/bin:/bin:/usr/local/bin"
	dirs := strings.Split(path,":")

	for _,dir := range dirs {
		fmt.Println(dir)
	}
}
