/*
34 - OOP: Encapsulation
private means the property can only be used inside the class.
*/
class BankAccount {
  owner: string;
  private balance: number;

  constructor(owner: string, balance: number) {
    this.owner = owner;
    this.balance = balance;
  }

  deposit(amount: number): void {
    if (amount > 0) {
      this.balance += amount;
      console.log(`Deposited ${amount}`);
    }
  }

  getBalance(): number {
    return this.balance;
  }
}

const account = new BankAccount("Khadir", 100);
account.deposit(50);
console.log(account.getBalance());
// console.log(account.balance); // Error because balance is private
