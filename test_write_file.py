from functions.write_file import write_file


def test() -> None:
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print("Result 1:")
    print(result)
    print("")

    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print("Result 2:")
    print(result)
    print("")

    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print("Result 3:")
    print(result)


if __name__ == "__main__":
    test()
