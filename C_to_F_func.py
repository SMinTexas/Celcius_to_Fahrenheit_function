# Write a function that takes a temperature in Celsius, converts it to Fahrenheit,
# and returns the value.
#
# The formula to convert a temperature from Celsius to Fahrenheit is:
# F = (C * 9/5) + 32

def c_to_f(C):
    return (C * 9/5) + 32

# Main program flow
Celsius = float(input("Please enter today's temperature in Celsius "))
print(f"Today's temperature in Fahrenheit will be {c_to_f(Celsius)} degrees.")
