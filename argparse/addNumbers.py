import argparse

def main():
    parser = argparse.ArgumentParser(
            description = "Add two numbers"
            )

    parser.add_argument(
        "num1",
        type=float,
        help="First Number"
            )
    parser.add_argument(
            "num2",
            type=float,
            help="Second Number"
            )

    args = parser.parse_args()
    result = args.num1+args.num2
    print(result)

if __name__ == '__main__':
    main()
