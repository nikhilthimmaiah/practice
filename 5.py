def calculate_total(price, quantity):
    total = price + quantity   # Intentional bug
    discount = total * 0.1
    final_amount = total - discount
    return final_amount

item_price = 500
item_quantity = 2

bill = calculate_total(item_price, item_quantity)

print("Final Bill:", bill)
