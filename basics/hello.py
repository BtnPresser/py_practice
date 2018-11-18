# This is a introdutory program that doesn't really do anything in particular...
# It also does the basic saying hello to a person thing

def print_hello():
    print("Hello World\n")


def ask_name():
    inputName = input("What is your name? ")
    print("Hello {0}!".format(inputName))


if __name__ == "__main__":
    print_hello()
    # ask_name()
