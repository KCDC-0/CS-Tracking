#### Designing Functions

## Key ideas:
# - documentation (readability)
# - default values


def pressure(v, t, n=6.022e23):
        """Compute the pressure in pascals of an ideal gas.

        v -- volume of gas, in cubic meters
        t -- absolute temperature in degrees kelvin
        n -- particles of gas (default: one mole)
        """
        k = 1.38e-23  # Boltzmann's constant
        return n * k * t / v

# Here, we  include documentation describing the function, called a docstring
# help(pressure) will show the docstring
# Also, the '=' in the def statement header 
# indicates a default value to use when the pressure function is called
# Thus, pressure(1, 273.15) and pressure(1, 273.15, 3 * 6.022e23) will result in different values
