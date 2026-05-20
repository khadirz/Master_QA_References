/*
32 - OOP: Attributes and Methods
Attributes are data inside an object.
Methods are actions inside a class.
*/
class Person {
  name: string;
  age: number;

  constructor(name: string, age: number) {
    this.name = name;
    this.age = age;
  }

  introduce(): void {
    console.log(`My name is ${this.name} and I am ${this.age} years old.`);
  }
}

const person1 = new Person("Khadir", 40);
person1.introduce();
