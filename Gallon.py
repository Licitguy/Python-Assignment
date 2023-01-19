int_str = input("Enter the inch of rainfall; ")

acre_str = input("Enter the number of the acre; ")

acre_int = int(acre_str)

gallon = 6272640 * acre_int / 231

print("Three are ", gallon , "gallon in" , acre_int, "acre of land")