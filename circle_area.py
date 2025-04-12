import tkinter as tk
from tkinter import ttk
from number_entry import IntEntry

import tkinter as tk
from tkinter import ttk

def calculate_area():
    """Compute and display the area of a circle."""
    try:
        # Get the radius from the radius entry widget
        radius = float(radius_entry.get())
        
        # Calculate the area
        area = 3.141592653589793 * radius ** 2
        
        # Display the area in the results label
        result_label.config(text=f"Area: {area:,.2f}")
        
    except ValueError:
        # The user entered an invalid radius
        result_label.config(text="Please enter a valid number")

def clear_inputs():
    """Clear all inputs and results."""
    radius_entry.delete(0, tk.END)
    result_label.config(text="")

def main():
    """Create and run the area calculator application."""
    global radius_entry, result_label  # Make these accessible to other functions
    
    # Create the main window
    root = tk.Tk()
    root.title("Area of a Circle Calculator")

    # Create a frame to hold all the widgets
    frame = ttk.Frame(root, padding="20")
    frame.grid()

    # Radius label and entry
    radius_label = ttk.Label(frame, text="Radius:")
    radius_label.grid(column=0, row=0, sticky=tk.W)
    radius_entry = ttk.Entry(frame, width=20)
    radius_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

    # Calculate button
    calculate_button = ttk.Button(frame, text="Calculate", command=calculate_area)
    calculate_button.grid(column=0, row=1, columnspan=2, pady=10)

    # Clear button (stretch challenge)
    clear_button = ttk.Button(frame, text="Clear", command=clear_inputs)
    clear_button.grid(column=0, row=2, columnspan=2, pady=5)

    # Result label
    result_label = ttk.Label(frame, text="")
    result_label.grid(column=0, row=3, columnspan=2)

    # Configure column weights to make entry expand with window
    frame.columnconfigure(1, weight=1)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()