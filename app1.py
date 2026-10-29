def calculate_total(price, quantity, discount_percent=0.0):
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must be non-negative.")
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount must be between 0 and 100.")
    subtotal = price * quantity
    discount_amount = subtotal * (discount_percent / 100.0)
    return subtotal - discount_amount

def main():
    print("=== Shopping Bill Calculator (v2 with Discount) ===")
    try:
        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))
        discount = float(input("Enter discount % (0 if none): "))
        total = calculate_total(price, quantity, discount)
        print(f"Final Discounted Bill: ${total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
