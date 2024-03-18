import uuid

class CustomerModule:
    customers = []

    @staticmethod
    def add_customer(name, postcode='', phone=''):
        customer_id = str(uuid.uuid4())[:8]  # Generate a unique customer_id
        customer = {'customer_id': customer_id, 'name': name, 'postcode': postcode, 'phone': phone}
        CustomerModule.customers.append(customer)
        print(f"Customer added successfully. Customer ID: {customer_id}")

    @staticmethod
    def search_customers(search_string):
        search_string = search_string.lower()
        matching_customers = [customer for customer in CustomerModule.customers
                              if search_string in customer['customer_id'].lower()
                              or search_string in customer['name'].lower()
                              or search_string in customer['postcode'].lower()
                              or search_string in customer['phone'].lower()]

        if matching_customers:
            print("Matching Customers:")
            for customer in matching_customers:
                print(customer)
        else:
            print("No matching customers found.")

    @staticmethod
    def delete_customer(customer_id):
        for customer in CustomerModule.customers:
            if customer['customer_id'] == customer_id:
                CustomerModule.customers.remove(customer)
                print(f"Customer {customer_id} and associated transactions deleted.")
                break
        else:
            print("Customer not found.")

class TransactionModule:
    transactions = []

    @staticmethod
    def add_transaction(customer_id, date, category):
        transaction_id = str(uuid.uuid4())[:8]  # Generate a unique transaction_id
        transaction = {'transaction_id': transaction_id, 'customer_id': customer_id, 'date': date, 'category': category}
        TransactionModule.transactions.append(transaction)
        print(f"Transaction added successfully. Transaction ID: {transaction_id}")

    @staticmethod
    def search_transactions(search_string):
        search_string = search_string.lower()
        matching_transactions = [transaction for transaction in TransactionModule.transactions
                                 if search_string in transaction['customer_id'].lower()
                                 or search_string in transaction['date'].lower()
                                 or search_string in transaction['category'].lower()]

        if matching_transactions:
            print("Matching Transactions:")
            for transaction in matching_transactions:
                print(transaction)
        else:
            print("No matching transactions found.")

    @staticmethod
    def delete_transaction(transaction_id):
        for transaction in TransactionModule.transactions:
            if transaction['transaction_id'] == transaction_id:
                TransactionModule.transactions.remove(transaction)
                print(f"Transaction {transaction_id} deleted.")
                break
        else:
            print("Transaction not found.")

    @staticmethod
    def display_transactions_for_customer(customer_id):
        customer_transactions = [transaction for transaction in TransactionModule.transactions
                                 if transaction['customer_id'] == customer_id]

        if customer_transactions:
            print(f"Transactions for Customer {customer_id}:")
            for transaction in customer_transactions:
                formatted_transaction = (
                    f"Transaction ID: {transaction['transaction_id']}\n"
                    f"Date: {transaction['date']}\n"
                    f"Category: {transaction['category']}"
                )
                print(formatted_transaction)
        else:
            print("No transactions found for this customer.")

def display_menu():
    print("\nMenu:")
    print("1. Add a new customer")
    print("2. Add a new transaction for a customer")
    print("3. Search customers")
    print("4. Search transactions")
    print("5. Display transactions for a customer")
    print("6. Delete a transaction")
    print("7. Delete a customer and associated transactions")
    print("8. Quit")

def get_valid_input(prompt, input_type=str):
    while True:
        try:
            user_input = input_type(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def main():
    while True:
        display_menu()
        choice = get_valid_input("Enter your choice (1-8): ", int)

        if choice == 1:
            name = input("Enter customer's name: ")
            postcode = input("Enter customer's postcode (optional): ")
            phone = input("Enter customer's phone number (optional): ")
            CustomerModule.add_customer(name, postcode, phone)

        elif choice == 2:
            customer_id = input("Enter customer ID: ")
            date = input("Enter transaction date: ")
            category = input("Enter transaction category: ")
            TransactionModule.add_transaction(customer_id, date, category)

        elif choice == 3:
            search_string = input("Enter search string: ")
            CustomerModule.search_customers(search_string)

        elif choice == 4:
            search_string = input("Enter search string: ")
            TransactionModule.search_transactions(search_string)

        elif choice == 5:
            customer_id = input("Enter customer ID: ")
            TransactionModule.display_transactions_for_customer(customer_id)

        elif choice == 6:
            transaction_id = input("Enter transaction ID: ")
            TransactionModule.delete_transaction(transaction_id)

        elif choice == 7:
            customer_id = input("Enter customer ID: ")
            CustomerModule.delete_customer(customer_id)

        elif choice == 8:
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
