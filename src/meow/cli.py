import argparse


def meow(times: int = 1, emoji: bool = True) -> None:
    # TODO: Add docstring
    for _ in range(times):
        msg = "Meow!"
        if emoji:
            msg = "🐱 " + msg
        print(msg)


def main() -> None:
    parser = argparse.ArgumentParser(description="A cute CLI that meows 🐱")
    parser.add_argument("--times", type=int, default=1, help="Number of times to meow")
    parser.add_argument(
        "--no-emoji", action="store_true", help="Hide the cat emoji in the output"
    )
    args = parser.parse_args()

    # BUG: --no-emoji option is ignored (for workshop exercise)
    meow(times=args.times, emoji=not args.no_emoji)
