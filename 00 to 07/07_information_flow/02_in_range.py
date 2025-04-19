def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    """
    return low <= n <= high

# Get input from the user
n = int(input("Enter the number to check: "))
low = int(input("Enter the lower bound: "))
high = int(input("Enter the upper bound: "))

# Check and display the result
if in_range(n, low, high):
    print(f"{n} is in the range [{low}, {high}].")
else:
    print(f"{n} is NOT in the range [{low}, {high}].")