#tire_volume activity


#import math  # Import math module for π

# Display message to the user
#print("This program calculates the volume of a tire based on its dimensions.")

# Get input from the user
#width = float(input("Enter the width of the tire in mm ; "))
#aspect_ratio = float(input("Enter the aspect ratio of the tire ; "))
#diameter = float(input("Enter the diameter of the wheel in inches ; "))

# Compute the volume using the formula
#volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display the calculated volume , leaving final values in litres
#print(f"\nThe volume of the tire is approximately {volume:.2f} liters.")

# Display a message thanking the user for using the program
#print("\nThank you for using this program!")

import math
from datetime import datetime

def calculate_tire_volume(width, aspect_ratio, diameter):
    """Computes the approximate volume of a tire."""
    return (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

def get_tire_price(width, aspect_ratio, diameter):
    """Returns the price of a tire based on its dimensions."""
    if width == 200 and aspect_ratio == 45 and diameter == 10:
        return 120.99
    elif width == 215 and aspect_ratio == 60 and diameter == 17:
        return 135.50
    elif width == 225 and aspect_ratio == 65 and diameter == 17:
        return 149.75
    elif width == 245 and aspect_ratio == 45 and diameter == 18:
        return 165.99
    else:
        return None  # No price available for this tire

# Display program title
print("\nTIRE VOLUME CALCULATION")
print("=" * 30)

try:
    # Get user input
    width = float(input("Enter the width of the tire in mm : "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire : "))
    diameter = float(input("Enter the diameter of the wheel in inches : "))

    # Compute volume
    volume = calculate_tire_volume(width, aspect_ratio, diameter)

    # Display results
    print("\nRESULTS")
    print("-" * 30)
    print(f"Tire Width       : {width:.1f} mm")
    print(f"Aspect Ratio     : {aspect_ratio:.1f}")
    print(f"Wheel Diameter   : {diameter:.1f} inches")
    print(f"Tire Volume      : {volume:.2f} liters")
    print("=" * 30)
    
    # Get tire price
    # Ask user if they want to buy more tires than they have
    buy_tires = input("Would you like to purchase tires? (yes/no): ").strip().lower()

    # Default if user doesn't want to buy   
    phone_number = "N/A"  
    if buy_tires == "yes":
        phone_number = input("Enter your phone number: ").strip()


    
    if buy_tires == "yes":
        price_per_tire = float(input("Enter the price per tire: $"))
        quantity = int(input("How many tires would you like to buy? "))
        total_cost = price_per_tire * quantity
        print(f"Total cost: ${total_cost:.2f}")
    else:
        print("Thank you for using the calculator!")

    # Get the current date (without time)
    current_date = datetime.now().strftime("%Y-%m-%d")

    # Append data to the volumes.txt file
    with open("volumes.txt", "a") as file:
        file.write(f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone_number}\n")

    print("\nData has been saved to 'volumes.txt'. Thank you!\n")

except ValueError:
    print("\nError: Please enter valid numeric values.\n")
