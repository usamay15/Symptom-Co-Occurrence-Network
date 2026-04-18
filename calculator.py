#!/usr/bin/env python3
"""A simple command-line calculator."""

from __future__ import annotations

import argparse
import sys


def calculate(operation: str, left: float, right: float) -> float:
    if operation == "add":
        return left + right
    elif operation == "sub":
        return left - right
    elif operation == "mul":
        return left * right
    elif operation == "div":
        if right == 0:
            raise ValueError("Division by zero is not allowed.")
        return left / right
    raise ValueError(f"Unsupported operation: {operation}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple calculator")
    parser.add_argument(
        "operation",
        choices=["add", "sub", "mul", "div"],
        help="Operation to perform",
    )
    parser.add_argument("left", type=float, help="First number")
    parser.add_argument("right", type=float, help="Second number")
    args = parser.parse_args()

    try:
        result = calculate(args.operation, args.left, args.right)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(result)


if __name__ == "__main__":
    main()
