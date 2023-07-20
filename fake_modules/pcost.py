import csv
from io import StringIO

portfolio_dat = '''AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
'''

def portfolio_cost(portfolio_data: str) -> float:
    reader = csv.DictReader(
        f=StringIO(portfolio_data),
        delimiter=" ",
        fieldnames=["ticker", "quantity", "purchase_price"]
    )
    total_basis_costs = 0
    for record in reader:
        # print(record)
        ticker = record["ticker"]
        try:
            quantity = int(record["quantity"])
        except ValueError:
            quantity = None
            print(
                f"Couldn't parse quantity value '{quantity}' from record" +
                f"  '{record}'  to type int."
            )
        try:
            purchase_price = float(record["purchase_price"])
        except ValueError:
            purchase_price = None
            print(
                f"Couldn't parse purchase_price value '{purchase_price}' from" +
                f"  '{record}'  to type float"
            )
        try:
            cost_basis = round(quantity * purchase_price, 2)
            total_basis_costs = total_basis_costs + cost_basis
        except TypeError:
            print(
                f"Couldn't produce cost_basis." +
                f"  quantity: {quantity}," +
                f"  purchase_price: {purchase_price}"
            )
    return round(total_basis_costs, 2)

if __name__ == "__main__":
    print(portfolio_cost(portfolio_dat))

