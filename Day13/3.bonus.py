# we expect two numbers divided by space
# we parse arguments in this bonus

feet_inches = input("Enter feet and inches: ")


def parse(feet_inches_local):
    parts = feet_inches_local.split(" ")
    feet_local = float(parts[0])
    inches_local = float(parts[1])
    return {"feet": feet_local, "inches": inches_local}


def convert(feet_local, inches_local):
    meters = feet_local * 0.3048 + inches_local * 0.0254
    return meters


parsed = parse(feet_inches)
feet = parsed["feet"]
inches = parsed["inches"]
print(f"we have {feet} feet {inches} inches")


result = convert(feet, inches)
print(f"that is: {result} meters")

if result < 1:
    print("Result is under meter")
else:
    print("Result is above meter")
