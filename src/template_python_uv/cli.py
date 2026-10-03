import sys

from . import greet


def main() -> int:
    try:
        print(greet(sys.argv[1] if len(sys.argv) > 1 else "world"))
    except ValueError as error:
        print(error, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
