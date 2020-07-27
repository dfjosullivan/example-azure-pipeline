from example_package.simple_functions import find_number

if __name__ == '__main__':
    try:
        print(find_number())
    except KeyboardInterrupt:
        print("Interruption")