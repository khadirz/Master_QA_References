/*
31 - OOP: Class and Object
Class is a blueprint.
Object is a real thing created from the class.
*/
class ShoppingCart {
  owner: string;
  items: string[];

  constructor(owner: string) {
    this.owner = owner;
    this.items = [];
  }

  addItem(item: string): void {
    this.items.push(item);
    console.log(`${item} added to ${this.owner}'s cart`);
  }

  showItems(): void {
    console.log(`${this.owner}'s cart contains:`, this.items);
  }
}

const userACart = new ShoppingCart("User A");
const userBCart = new ShoppingCart("User B");
userACart.addItem("Laptop");
userBCart.addItem("Phone");
userACart.showItems();
userBCart.showItems();
