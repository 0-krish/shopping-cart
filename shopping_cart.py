#
# shopping_cart.py
#
# Shopping Cart Exercise
#
# Author: Krish Sarawgi
#   Github: "0-krish"
#   NetID: ks1730

import pandas
from datetime import datetime
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

csv_filepath = "data/products.csv"
products_csv = pandas.read_csv(csv_filepath)
products_dict = pandas.DataFrame.to_dict(products_csv)

# products = [
#     {
#         "id": 1,
#         "name": "Chocolate Sandwich Cookies",
#         "department": "snacks",
#         "aisle": "cookies cakes",
#         "price": 3.50
#     },
#     {"id": 2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#     {"id": 3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#     {"id": 4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#     {"id": 5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#     {"id": 6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#     {"id": 7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#     {"id": 8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#     {"id": 9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#     {"id": 10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#     {"id": 11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#     {"id": 12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#     {"id": 13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#     {"id": 14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#     {"id": 15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#     {"id": 16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#     {"id": 17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#     {"id": 18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#     {"id": 19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#     {"id": 20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
# ]  # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017




def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}"  # > $12,000.71


# Code below adapted from in-class exercise for the shopping cart deliverable

print("---------------------------------")
print("Welcome to the Green Foods Grocery Checkout System!")

subtotal_price = 0
selected_ids = []
stored_ids = []
matching_products = []

print("Type 'DONE' once all desired items have been scanned.")
print("---------------------------------")

for product in products_dict:
    #stored_ids.append(product["id"])
    print(product)

while True:
    selected_id = input("Please input a product identifier: ")
    if selected_id == "DONE" or selected_id == "done" or selected_id == "Done":
        break
    elif selected_id in stored_ids:
        selected_ids.append(selected_id)
    else:
        print("Are you sure that this product identifier is correct? Please try again!")

# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
today = datetime.now()
today_string = today.strftime("%Y-%m-%d %I:%M %p")

print("#> ---------------------------------")
print("#> GREEN FOODS GROCERY")
print("#> WWW.GREEN-FOODS-GROCERY.COM")
print("#> ---------------------------------")
print("#> CHECKOUT AT:", today_string)
print("#> ---------------------------------")
print("#> SELECTED PRODUCTS:")

for selected_id in selected_ids:
    matching_products = [p for p in products_dict if str(p["id"]) == str(selected_id)]
    matching_product = matching_products[0]
    subtotal_price = subtotal_price + matching_product["price"]
    print("#>  ... " + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")

tax_rate = float(os.getenv("TAX_RATE", default="0.0875"))
tax_amount = tax_rate * subtotal_price
total_price = subtotal_price + tax_amount

print("#> ---------------------------------")
print("#> SUBTOTAL:", to_usd(subtotal_price))
print(f"#> TAX ({tax_rate*100:,.2f}%): " + to_usd(tax_amount))
print("#> TOTAL: " + to_usd(total_price))
print("#> ---------------------------------")

# Receipt by email

receipt_preference = input("Would the customer like a copy of the receipt to be sent to them via email? [y/n]: ")
receipt_preference.lower()

if receipt_preference == "y" or receipt_preference == "yes":

    # code adapted from https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md

    customer_email = input("Please enter the customer's email ID: ")

    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

    client = SendGridAPIClient(SENDGRID_API_KEY)  # > <class 'sendgrid.sendgrid.SendGridAPIClient>

    subject = "Your Receipt from the Green Grocery Store"

    html_content = ""

    html_content += "---------------------------------<br>\n"
    html_content += "GREEN FOODS GROCERY<br>\n"
    html_content += "WWW.GREEN-FOODS-GROCERY.COM<br>\n"
    html_content += "---------------------------------<br>\n"
    html_content += "CHECKOUT AT: "
    html_content += str(today_string)
    html_content += "\n<br>---------------------------------<br>\n"
    html_content += "PRODUCTS PURCHASED:<br>\n"

    for selected_id in selected_ids:
        matching_products = [p for p in products_dict if str(p["id"]) == str(selected_id)]
        matching_product = matching_products[0]
        html_content += "  ... " + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")<br>\n"

    html_content += "---------------------------------<br>"
    html_content += "SUBTOTAL: "
    html_content += str(to_usd(subtotal_price))
    html_content += f"\n<br>TAX ({tax_rate*100:,.2f}%): "
    html_content += str(to_usd(tax_amount))
    html_content += "\n<br>TOTAL: "
    html_content += str(to_usd(total_price))
    html_content += "\n<br>---------------------------------"
    html_content += "\n<br>THANK YOU FOR SHOPPING WITH US. SEE YOU AGAIN SOON!"
    html_content += "\n<br>---------------------------------"

    message = Mail(
        from_email=SENDER_ADDRESS,
        to_emails=customer_email,
        subject=subject,
        html_content=html_content)

    try:
        response = client.send(message)
        if str(response.status_code) == "202":
            print("Email to", customer_email, "sent!")

    except Exception as err:
        print(type(err))
        print(err)

print("#> ---------------------------------")
print("#> THANKS, SEE YOU AGAIN SOON!")
print("#> ---------------------------------")
