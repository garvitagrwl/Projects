str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
combined = str1 + str2

print("\n--- String Method Outputs ---")
print("Lower:", combined.lower())
print("Upper:", combined.upper())
print("Title:", combined.title())
print("Swapcase:", combined.swapcase())
print("Capitalize:", combined.capitalize())
print("Casefold:", combined.casefold())
print("Center (width=20):", combined.center(20))
print("Count of 'a':", combined.count('a'))
print("Endswith 'ing':", combined.endswith('ing'))
print("Find 'a':", combined.find('a'))
print("Is Alphanumeric:", combined.isalnum())
print("Is Digit:", combined.isdigit())
print("Is Numeric:", combined.isnumeric())
print("Is Space:", combined.isspace())
print("Replace 'a' with '@':", combined.replace('a', '@'))
