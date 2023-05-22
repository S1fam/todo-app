from converters import convert
import parser

feet_inches = input("Enter feet and inches: ")

parsed = parser.parse(feet_inches)

result = convert(parsed["feet"], parsed["inches"])
print(f"We have: {parsed['feet']} feet {parsed['inches']} inches. That is: {result} meters")

if result < 1:
    print("Result is under meter")
else:
    print("Result is above meter")

# select multiple lines of code -> right click -> refactor -> Move... -> From: To: -> choose name at the end of path
