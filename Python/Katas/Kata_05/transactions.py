
def add_transaction(transactions: dict, customer: str, transaction_id: str, amount: int) -> str:
    """Adds a transaction"""

    if transaction_id in transactions.keys():
        raise ValueError()
    
    if amount < 0:
        raise ValueError()
    
    transactions[transaction_id] = {"customer": customer, "amount": amount}
    
    return transactions


def get_total_spent(transactions: dict, customer: str) -> int:
    """Returns total amount spent by a customer"""
    
    total = 0
    for transaction in transactions.values():
        if transaction["customer"] == customer:
            total += transaction["amount"]
    return total

def remove_transaction(transactions: dict, customer: str, transaction_id: str) -> bool:
    """Removes a transaction for a specific customer"""

    if transaction_id not in transactions.keys():
        return transaction_id in transactions
    
    if transaction_id in transactions.keys():
        del transactions[transaction_id]
    
    return transaction_id not in transactions
    
 

def update_transaction_amount(transactions: dict, customer: str, transaction_id: str, new_amount: int) -> bool:
    """Updates the amount of a specific transaction for a customer"""

    if transaction_id not in transactions.keys():
        return False
    
    for transaction in transactions.values():
        if transaction["customer"] == customer:
            transaction["amount"] = new_amount
    return transactions[transaction_id]["amount"] == new_amount





def get_customer_transactions(transactions: dict, customer: str) -> list:
    """Returns a list of all transactions for a specific customer"""


def get_all_customers(transactions: dict) -> list:
    """Returns a list of all unique customers in the transactions"""


def get_highest_spending_customer(transactions: dict) -> str:
    """Returns the customer who has spent the most in total"""


def get_lowest_spending_customer(transactions: dict) -> str:
    """Returns the customer who has spent the least in total"""


def get_average_spending(transactions: dict, customer: str) -> float:
    """Returns the average amount spent per transaction for a specific customer"""


def get_transaction_count(transactions: dict, customer: str) -> int:
    """Returns the total number of transactions for a specific customer"""


def get_transactions_in_range(transactions: dict, customer: str, min_amount: int, max_amount: int) -> list:
    """Returns a list of transactions for a customer within a specified amount range"""


def clear_all_transactions(transactions: dict) -> None:
    """Clears all transactions from the dictionary"""
            
