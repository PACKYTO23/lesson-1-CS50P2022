# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x / y, 2)

# # # f-String way to return two digits.
# print(f"{z:.2f}")

# # # It formats the result with commas every three digits (American style).
# print(f"{z:,}")

def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n
    # return n ** 2
    # return pow(n, 2)


main()
