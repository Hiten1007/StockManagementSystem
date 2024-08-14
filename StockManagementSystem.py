class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def __str__(self):
        return f"Name: {self.name}, Position: {self.position}"

class Company:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        if self.employees:
            print("Employees:")
            for employee in self.employees:
                print(employee)
        else:
            print("No employees.")

class Stock:
    def __init__(self, symbol, name, price, quantity, company_name):
        self.symbol = symbol
        self.name = name
        self.price = price
        self.quantity = quantity
        self.company_name = company_name

    def __str__(self):
        return f"Symbol: {self.symbol}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

class Transaction:
    def __init__(self, transaction_id, date, company_name, symbol, quantity, transaction_type):
        self.transaction_id = transaction_id
        self.date = date
        self.company_name = company_name
        self.symbol = symbol
        self.quantity = quantity
        self.transaction_type = transaction_type

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Date: {self.date}, Company: {self.company_name}, Symbol: {self.symbol}, Quantity: {self.quantity}, Type: {self.transaction_type}"

class StockManagementSystem:
    def __init__(self):
        self.companies = []
        self.stocks = []
        self.transactions = []

    def add_company(self, name):
        company = Company(name)
        self.companies.append(company)
        print(f"Company '{name}' added successfully.")

    def add_employee(self, company_name, name, position):
        for company in self.companies:
            if company.name == company_name:
                employee = Employee(name, position)
                company.add_employee(employee)
                print(f"Employee '{name}' added to company '{company_name}' as '{position}'.")
                return
        print(f"Company '{company_name}' not found.")

    def add_stock(self, symbol, name, price, quantity, company_name):
        stock = Stock(symbol, name, price, quantity, company_name)
        self.stocks.append(stock)
        print(f"Stock '{symbol}' added successfully.")

    def display_company_info(self, company_name):
        for company in self.companies:
            if company.name == company_name:
                print(f"Company: {company_name}")
                company.display_employees()
                print("Stocks:")
                company_stocks = [stock for stock in self.stocks if stock.company_name == company_name]
                if company_stocks:
                    for stock in company_stocks:
                        print(stock)
                else:
                    print("No stocks associated with this company.")
                return
        print(f"Company '{company_name}' not found.")

    def add_transaction(self, transaction_id, date, company_name, symbol, quantity, transaction_type):
        transaction = Transaction(transaction_id, date, company_name, symbol, quantity, transaction_type)
        self.transactions.append(transaction)
        print("Transaction added successfully.")

    def display_transactions(self):
        if self.transactions:
            for transaction in self.transactions:
                print(transaction)
        else:
            print("No transactions available.")

    def remove_stock(self, symbol):
        for stock in self.stocks:
            if stock.symbol == symbol:
                self.stocks.remove(stock)
                print(f"Stock '{symbol}' removed successfully.")
                return
        print(f"Stock '{symbol}' not found.")

    def update_stock_price(self, symbol, new_price):
        for stock in self.stocks:
            if stock.symbol == symbol:
                stock.price = new_price
                print(f"Price for stock '{symbol}' updated to {new_price}.")
                return
        print(f"Stock '{symbol}' not found.")

    def display_stock_details(self, symbol):
        found_stock = None
        for stock in self.stocks:
            if stock.symbol == symbol:
                found_stock = stock
                break

        if found_stock:
            print(found_stock)
        else:
            print(f"Stock with symbol '{symbol}' not found.")

    def display_employee_details(self):
        if self.companies:
            for company in self.companies:
                company.display_employees()
        else:
            print("No employee details available.")

def main():
    stock_system = StockManagementSystem()
    
    print("Welcome to Stock Management System")

    while True:
        print("\nOptions:")
        print("1. Add Company")
        print("2. Add Employee")
        print("3. Add Stock")
        print("4. Update Stock Price")
        print("5. Display Company Information")
        print("6. Display Employee Details")
        print("7. Add Transaction")
        print("8. Display Transactions")
        print("9. Remove Stock")
        print("10. Display Stock Details")
        print("11. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name of the company: ")
            stock_system.add_company(name)
        elif choice == "2":
            company_name = input("Enter the name of the company: ")
            name = input("Enter the name of the employee: ")
            position = input("Enter the position of the employee: ")
            stock_system.add_employee(company_name, name, position)
        elif choice == "3":
            symbol = input("Enter the symbol of the stock: ")
            name = input("Enter the name of the stock: ")
            price = float(input("Enter the price of the stock: "))
            quantity = int(input("Enter the quantity of the stock: "))
            company_name = input("Enter the name of the company: ")
            stock_system.add_stock(symbol, name, price, quantity, company_name)
        elif choice == "4":
            symbol = input("Enter the symbol of the stock: ")
            new_price = float(input("Enter the new price: "))
            stock_system.update_stock_price(symbol, new_price)
        elif choice == "5":
            company_name = input("Enter the name of the company: ")
            stock_system.display_company_info(company_name)
        elif choice == "6":
            stock_system.display_employee_details()
        elif choice == "7":
            transaction_id = input("Enter transaction ID: ")
            date = input("Enter transaction date: ")
            company_name = input("Enter company name: ")
            symbol = input("Enter stock symbol: ")
            quantity = int(input("Enter quantity: "))
            transaction_type = input("Enter transaction type (buy/sell): ")
            stock_system.add_transaction(transaction_id, date, company_name, symbol, quantity, transaction_type)
        elif choice == "8":
            stock_system.display_transactions()
        elif choice == "9":
            symbol = input("Enter stock symbol to remove: ")
            stock_system.remove_stock(symbol)
        elif choice == "10":
            symbol = input("Enter stock symbol: ")
            stock_system.display_stock_details(symbol)
        elif choice == "11":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

main()
