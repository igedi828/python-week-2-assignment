# Simple Bill Calculator

price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

total = price * quantity

print("\n----- BILL SUMMARY -----")
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
print("Thank you for shopping!")
