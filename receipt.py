import csv
import random
from datetime import datetime

def main():
    try:
        # Read products and build product dictionary
        products = read_products("products.csv")
        
        # Process request and build receipt
        process_request("request.csv", products)
        
    except FileNotFoundError as e:
        print(f"Error: Missing file - {e.filename}")
    except PermissionError:
        print("Error: Permission denied when accessing a file.")
    except KeyError as e:
        print(f"Error: Unknown product ID in request - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def read_products(filename):
    products = {}
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row
        
        for row in reader:
            product_id = row[0]
            product_name = row[1]
            product_price = float(row[2])
            
            products[product_id] = {
                "name": product_name,
                "price": product_price
            }
    
    return products


def process_request(filename, products):
    ordered_items = []
    
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row
        
        for row in reader:
            product_id = row[0]
            quantity = int(row[1])
            
            product = products[product_id]
            ordered_items.append({
                "id": product_id,
                "name": product["name"],
                "price": product["price"],
                "quantity": quantity
            })
    
    # Print receipt
    print_receipt(ordered_items)

def print_receipt(items):
    # Store name and header
    print("\nTeory Ventures Limited")
    print("----------------------------")
    
    # Ordered items
    total_quantity = 0
    subtotal = 0.0
    
    for item in items:
        print(f"{item['name']}: {item['quantity']} @ {item['price']:.2f}")
        total_quantity += item['quantity']
        subtotal += item['quantity'] * item['price']


    # Apply 10% discount for orders over $50
    discount = 0.0
    if subtotal > 50:
        discount = subtotal * 0.10
        print(f"\nDiscount (10% for orders over $50): -{discount:.2f}")
        subtotal -= discount
    
    # Calculate taxes and total
    tax_rate = 0.06
    sales_tax = subtotal * tax_rate
    total = subtotal + sales_tax
    
    # Print totals
    print("\n----------------------------")
    print(f"Number of Items: {total_quantity}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}\n")
    
    # Thank you message
    print("Thank you for shopping at the Teory Ventures Limited")
    
    # Current date and time
    current_datetime = datetime.now()
    print(current_datetime.strftime("%a %b %d %H:%M:%S %Y"))


    if items:
        coupon_item = random.choice(items)
        coupon_discount = round(coupon_item['price'] * 0.20, 2)
        print("\n----------------------------")
        print("YOUR EXCLUSIVE COUPON:")
        print(f"20% OFF your next purchase of {coupon_item['name']}!")
        print(f"Save ${coupon_discount:.2f} on your next order!")
        print(f"Regular price: ${coupon_item['price']:.2f}")
        print("Coupon valid for 30 days")
        print("Code: TEORY" + str(random.randint(1000, 9999)))
        print("----------------------------")


if __name__ == "__main__":
    main()


#def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    #dictionary = {}
    
    #with open(filename, 'rt') as csv_file:
       # reader = csv.reader(csv_file)
        #next(reader)  # Skip the header row
        
        #for row in reader:
            #if len(row) != 0:  # Skip empty rows if any
               ## key = row[key_column_index]
                # Convert price to float
                #row[2] = float(row[2])
                #dictionary[key] = row
                
    #return dictionary

#def main():
    # Read the products into a dictionary
    #products_dict = read_dictionary('products.csv', 0)
    
    # Print the products dictionary
    #print("All Products")
    #print(products_dict)
    print()
    
    # Process the request.csv file
    #print("Requested Items")
    #with open('request.csv', 'rt') as csv_file:
        #reader = csv.reader(csv_file)
        #next(reader)  # Skip the header row
        
        #for row in reader:
           # if len(row) != 0:  # Skip empty rows if any
                #product_number = row[0]
                #quantity = int(row[1])
                
                # Get the product details from the dictionary
                #product = products_dict[product_number]
                #product_name = product[1]
                #price = product[2]
                
                # Print the product details
               # print(f"{product_name}: {quantity} @ {price}")

# Call the main function if this file is run as a script
#if __name__ == "__main__":
    #main()