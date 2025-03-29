def water_column_height(tower_height, tank_height):
    """Compute the height of the water column."""
    return tower_height + (3 * tank_height) / 4

def pressure_gain_from_water_height(height):
    """Compute the pressure gain from a given water column height."""
    density_water = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    return (density_water * gravity * height) / 1000  # Convert to kPa

def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Compute the pressure loss from a pipe due to friction."""
    density_water = 998.2  # kg/m^3
    return (-friction_factor * pipe_length * density_water * (fluid_velocity ** 2)) / (2000 * pipe_diameter)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """Compute the pressure loss from pipe fittings due to bends in the pipeline."""
    density_water = 998.2  # kg/m^3
    return (-0.04 * density_water * (fluid_velocity ** 2) * quantity_fittings) / 2000  # Convert to kPa

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """Compute the Reynolds number for a pipe with water flowing through it."""
    # Define the density of water in kg/m^3
    density_water = 998.2  # kg/m^3
    # Define the dynamic viscosity of water in Pascal-seconds (Pa·s)
    dynamic_viscosity_water = 0.0010016  # Pascal-seconds (Pa·s)

    # Compute the Reynolds number using the formula: Re = (density * hydraulic_diameter * fluid_velocity) / dynamic_viscosity
    return (density_water * hydraulic_diameter * fluid_velocity) / dynamic_viscosity_water


def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculate the water pressure loss due to pipe diameter reduction.
    
    Parameters:
        larger_diameter (float): Diameter of the larger pipe in meters.
        fluid_velocity (float): Velocity of water in the larger pipe (m/s).
        reynolds_number (float): Reynolds number corresponding to the larger pipe.
        smaller_diameter (float): Diameter of the smaller pipe in meters.
    
    Returns:
        float: Pressure loss in kilopascals (kPa).
    """
    water_density = 998.2  # kg/m³
    
    # Calculate k using the given formula
    k = (.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    
    # Calculate pressure loss P in kPa
    pressure_loss = (-k * water_density * (fluid_velocity ** 2)) / 2000
    
    return pressure_loss


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

def kpa_to_psi(kpa):
    """Convert kilopascals (kPa) to pounds per square inch (psi)."""
    # Multiply the input value by the conversion factor to get the result
    return kpa * 14.5038


def main():
    # Get user input for the height of the water tower, tank walls, length of supply pipe, number of 90° angles in supply pipe, and length of pipe from supply to house
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    # Calculate the water column height
    water_height = water_column_height(tower_height, tank_height)
    # Calculate the pressure gain from the water height
    pressure = pressure_gain_from_water_height(water_height)
    # Set the diameter, friction factor, and velocity for the PVC pipe
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    # Calculate the Reynolds number
    reynolds = reynolds_number(diameter, velocity)
    # Calculate the pressure loss from the pipe
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    # Calculate the pressure loss from the fittings
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    # Calculate the pressure loss from the pipe reduction
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    # Set the diameter, friction factor, and velocity for the HDPE pipe
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    # Calculate the pressure loss from the pipe
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss


    # Print the pressure at the house
    print(f"Pressure at house: {pressure:.1f} kilopascals ({kpa_to_psi(pressure):.2f} psi)")

    #print(f"Pressure at house: {pressure} kilopascals")
if __name__ == "__main__":
    main()
