
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


