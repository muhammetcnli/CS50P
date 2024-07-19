amount_due = 50

while True:
    print(f"Amount_due: {amount_due}")
    inserted = int(input("Insert coin: "))
    if inserted > 25:
        pass
    else:
        amount_due -= inserted

    if amount_due < 0:
        print(f"Change Owed: {str(amount_due).split("-")[1]}")
        break