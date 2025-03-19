class BankAccount:
    def __init__(self, account_number: str, owner_name: str, balance: float, transactions: list[dict] | None = None) -> None:
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.transactions = transactions if transactions is not None else []

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
            self.transactions.append({"type": "deposit",
                                      "amount": amount,
                                      "balance_after": self.balance})

            print(f"You have deposited ${amount}. Your account balance is: ${self.balance:.2f}")
        else:
            print("Deposit amount must be a positive number.")

    def withdraw(self, amount: float) -> None:
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.transactions.append({"type": "withdraw",
                                          "amount": amount,
                                          "balance_after": self.balance})

                print(f"You have withdrawn ${amount}. Your account balance is: ${self.balance:.2f}")
            else:
                print(f"Not enough balance to withdraw ${amount}. Current balance: ${self.balance:.2f}")
        else:
            print("Withdraw amount must be a positive number.")

    def transaction_history(self) -> None:
        print("\nTransaction history:")
        for transaction in self.transactions:
            print(
                f"{transaction['type'].title()}",
                f"Amount: ${transaction['amount']:.2f}",
                f"Balance: ${transaction['balance_after']:.2f}"
            )

class SavingsAccount(BankAccount):
    def __init__(self, account_number: str, owner_name: str, balance: float, interest_rate: float = 0.03) -> None:
        super().__init__(account_number, owner_name, balance)
        self.interest_rate = interest_rate

    def apply_interest(self) -> None:
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append({"type": "interest",
                                  "amount": interest,
                                  "balance_after": self.balance})

        print(f"Interest applied: ${interest:.2f}. New balance: ${self.balance:.2f}")

def main() -> None:
    account:SavingsAccount = SavingsAccount("123", "Nola", 0)

    account.deposit(50)
    account.withdraw(30)
    account.apply_interest()
    account.transaction_history()

if __name__ == "__main__":
    main()