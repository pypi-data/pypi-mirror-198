import argparse

from flitton_fib_py.fib_calcs.fib_number import recurring_fibonacci_number


def fib_numb() -> None:
    parser = argparse.ArgumentParser(description="Calculate Fibonacci numbers")

    parser.add_argument(
        "--number",
        action="store",
        type=int,
        required=True,
        help="Fib number to calc",
    )

    args = parser.parse_args()

    print(f"Your Fib number is: {recurring_fibonacci_number(number=args.number)}")
