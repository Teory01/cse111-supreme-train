import math

def compute_volume(radius, height):
    """Computes the volume of a cylinder."""
    # Compute the volume of a cylinder using the formula: pi * (radius ** 2) * height
    return math.pi * (radius ** 2) * height
def compute_surface_area(radius, height):
    """Computes the surface area of a cylinder."""
    # Calculate the surface area of a cylinder using the formula 2 * pi * radius * (radius + height)
    return 2 * math.pi * radius * (radius + height)

def compute_storage_efficiency(volume , surface_area,):
    """Computes the storage efficiency as volume divided by surface area."""
    return volume / surface_area



def main():
    cans = [
        ("#1 Picnic", 6.83, 10.16, 0.28),
        ("#1 Tall", 7.78, 11.91, 0.43),
        ("#2", 8.73, 11.59, 0.45),
        ("#2.5", 10.32, 11.91, 0.61),
        ("#3 Cylinder", 10.79, 17.78, 0.86),
        ("#5", 13.02, 14.29, 0.83),
        ("#6Z", 5.40, 8.89, 0.22),
        ("#8Z short", 6.83, 7.62, 0.26),
        ("#10", 15.72, 17.78, 1.53),
        ("#211", 6.83, 12.38, 0.34),
        ("#300", 7.62, 11.27, 0.38),
        ("#303", 8.10, 11.11, 0.42)
    ]
    
    best_can = ""
    highest_efficiency = 0
    
    print(f"{'Can Name':<15}{'Volume (cm³)':<20}{ 'surface area (cm²)':<25}{'Storage Efficiency (cm³)':<30}")
    print("-" * 90)
    
    for name, radius, height, cost in cans:
        volume = compute_volume(radius, height)
        surface_area = compute_surface_area(radius, height)
        efficiency = compute_storage_efficiency(volume, surface_area)
        
        # Print the can size and its efficiency in cubic centimeters per dollar.
        print(f"{name:<15}{volume:<20.2f}{surface_area:<25.2f}{efficiency:<20.4f}")
        
        
        if efficiency > highest_efficiency:
            highest_efficiency = efficiency
            best_can = name
    
    print("\nThe can size with the highest storage efficiency is:", best_can)

if __name__ == "__main__":
    main()
