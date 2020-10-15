from src.biograder.Homework18 import Homework18


def main():
    hw18 = Homework18()
    # print(hw18.submit("TEST2", 2, 12))
    testString = "TEST2"

    print(hw18.submit(testString, 2, "netid"))


if __name__ == "__main__":
    main()
