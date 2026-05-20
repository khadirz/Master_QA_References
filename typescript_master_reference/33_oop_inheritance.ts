/*
33 - OOP: Inheritance
A child class can inherit from a parent class.
*/
class Animal {
  name: string;

  constructor(name: string) {
    this.name = name;
  }

  speak(): void {
    console.log("Animal makes a sound");
  }
}

class Dog extends Animal {
  speak(): void {
    console.log(`${this.name} says woof!`);
  }
}

const dog = new Dog("Buddy");
dog.speak();
