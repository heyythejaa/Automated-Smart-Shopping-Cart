import random
import sqlite3

product_id = [
    '8901030723829','8901719124022','8901207038986','8901030729784',
    '4902430713781','8901491102016','8901030752454','7506206822187',
    '8906002012011','8901526101509'
]

# Connect to database ONCE
conn = sqlite3.connect("products.db")
cursor = conn.cursor()

total_amount = 0

while True:
    # 1️⃣ Randomly select barcode
    selected_barcode = random.choice(product_id)
    print("\nRandomly selected barcode:", selected_barcode)

    # 2️⃣ Fetch product details
    cursor.execute(
        "SELECT name, price, weight_grams FROM products WHERE barcode = ?",
        (selected_barcode,)
    )

    product = cursor.fetchone()

    # 3️⃣ Display result
    if product:
        name, price, weight = product
        print("Product Name :", name)
        print("Price        : ₹", price)
        print("Weight       :", weight, "grams")

        total_amount += price
    else:
        print("Product not found in database")

    # 4️⃣ Ask user to continue or stop
    choice = input("\nDo you want more product? (yes/no): ").lower()

    if choice == "yes":
        continue
    elif choice == "no":
        break
    else:
        print("Invalid input. Type only yes or no.")

# Close DB connection
conn.close()

print("\n------ FINAL BILL ------")
print("Total Amount to Pay: ₹", total_amount)
print("Thank you for shopping 😊")


#low=1
#high=100
#options=("rock","paper","scissor")
#cards=["2","3","4","5","6","7","o","p","k"]
#number=random.randint(low,high)
#number=random.random()
#option=random.choice(options)
#card=random.shuffle(cards)
#print(cards)
#product=random.choice(product_id)
#print(product)