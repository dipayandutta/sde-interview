package main

import "fmt"

type Employee struct{
	name string 
	age int
	isRemote bool
}

func(e *Employee) updateName(newName string){
	e.name = newName
}

func main(){
	employee1 := Employee{
		name: "Alice",
		age:	30,
		isRemote:	true,
	}

	employee1.updateName("Bob")
	fmt.Println("Employee Name: ",employee1.name)
	fmt.Println("Employee Age: ",employee1.age)
	fmt.Println("Employee Location: ",employee1.isRemote)
	//Anonynomus Struct
	job := struct {
		title string
		salary int
	}{
		title: "SE",
		salary: 1000000,
	}

	fmt.Println("Job",job.title)


	employeePtr := &employee1
	employeePtr.age = 31
}
