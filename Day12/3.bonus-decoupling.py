# we expect two numbers divided by space
feet_inches = input("Enter feet and inches: ")


def convert(feet_inches_local):
    parts = feet_inches_local.split(" ")  # we want to split at space character
    feet_local = float(parts[0])
    inches_local = float(parts[1])
    meters = feet_local * 0.3048 + inches_local * 0.0254
    return meters


input_decoupled = feet_inches.split(" ")
feet = float(input_decoupled[0])
inches = float(input_decoupled[1])
print(f"we have {feet} feet {inches} inches")

result = convert(feet_inches)
print(f"that is: {result} meters")

if result < 1:
    print("Result is under meter")
else:
    print("Result is above meter")
