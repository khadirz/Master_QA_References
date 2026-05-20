/*
25 - Interfaces
Interface defines the shape of an object.
*/
interface Product {
  name: string;
  price: number;
  inStock: boolean;
}
const laptop: Product = {
  name: "Laptop",
  price: 1200,
  inStock: true,
};
console.log(laptop);
console.log(laptop.name);
