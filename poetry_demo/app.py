import matplotlib.pyplot as plt


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return 'Person(name = {}, age = {})'.format(self.name, self.age)


def from_user():
    message = input("Insert something: ")
    print(message)


def display():
    squares = [1, 4, 9, 16, 25]
    fig, ax = plt.subplots()
    ax.plot(squares)
    plt.show()


def main():
    print("Hello World!")
    # from_user()
    person = Person("marco", 5)
    print(person.show())
    with open("../text.txt") as file:
        content = file.read()
    print(content)
    with open("app.py") as python_file:
        for line in python_file:
            print(line)

    display()


if __name__ == "__main__":
    main()
