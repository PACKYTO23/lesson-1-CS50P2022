# # # Ask user for their name.
# name = input("What's your name? ").strip().title()

# # # Split user's name into first name and last name.
# first, last = name.split(" ")

# # # Say hello to user.
# print(f"Hello, {first}")


def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="World"):
    print("Hello,", to)


main()
