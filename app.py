import tkinter as tk
from tkinter import messagebox
from getpass import getpass  
from abc import ABC, abstractmethod

class PIN(ABC):
    @abstractmethod
    def validate(self, pin: str) -> bool:
        pass

class ATM(PIN):
    def __init__(self, pin: str):
        self._pin = pin

    def validate(self, pin: str) -> bool:
        return self._pin == pin

class User:
    def __init__(self, name: str, pin: str):
        self.name = name
        self.pin = ATM(pin)

    def login(self, pin: str) -> bool:
        return self.pin.validate(pin)

class BankAccount:
    def __init__(self, balance: float = 0.0):
        self._balance = balance

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self._balance += amount
            return True
        return False

    def withdraw(self, amount: float) -> bool:
        if 0 < amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def get_balance(self) -> float:
        return self._balance

class ATMGUI:
    def __init__(self, root, user, account):
        self.root = root
        self.user = user
        self.account = account

        self.root.title("ATM System")
        self.root.geometry("300x300")

        self.login_screen()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Enter PIN").pack(pady=10)

        self.pin_entry = tk.Entry(self.root, show="*")
        self.pin_entry.pack(pady=5)

        tk.Button(self.root, text="Login", command=self.check_login).pack(pady=10)

    def check_login(self):
        pin = self.pin_entry.get()
        if self.user.login(pin):
            self.menu_screen()
        else:
            messagebox.showerror("Error", "Invalid PIN")

    def menu_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="ATM Menu").pack(pady=10)

        tk.Button(self.root, text="Check Balance", command=self.show_balance).pack(pady=5)
        tk.Button(self.root, text="Deposit", command=self.deposit_screen).pack(pady=5)
        tk.Button(self.root, text="Withdraw", command=self.withdraw_screen).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)

    def show_balance(self):
        balance = self.account.get_balance()
        messagebox.showinfo("Balance", f"Balance: ${balance}")

    def deposit_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Deposit Amount").pack(pady=10)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)

        tk.Button(self.root, text="Submit", command=self.deposit).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.menu_screen).pack(pady=5)

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if self.account.deposit(amount):
                messagebox.showinfo("Success", "Deposit successful")
                self.menu_screen()
            else:
                messagebox.showerror("Error", "Invalid amount")
        except:
            messagebox.showerror("Error", "Enter a valid number")

    def withdraw_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Withdraw Amount").pack(pady=10)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=5)

        tk.Button(self.root, text="Submit", command=self.withdraw).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.menu_screen).pack(pady=5)

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if self.account.withdraw(amount):
                messagebox.showinfo("Success", "Withdrawal successful")
                self.menu_screen()
            else:
                messagebox.showerror("Error", "Insufficient funds or invalid amount")
        except:
            messagebox.showerror("Error", "Enter a valid number")


if __name__ == "__main__":
    root = tk.Tk()

    user = User("Drake", "1234")
    account = BankAccount(1000.0)

    app = ATMGUI(root, user, account)

    root.mainloop()