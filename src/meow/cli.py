import argparse


def meow(times: int = 1, emoji: bool = True) -> None:
    # TODO: Add docstring
    for _ in range(times):
        msg = "Meow!"
        if emoji:
            msg = "🐱 " + msg
        print(msg)


def woof(times: int = 1, emoji: bool = True) -> None:
    # TODO: Add docstring
    for _ in range(times):
        msg = "Woof!"
        if emoji:
            msg = "🐶 " + msg
        print(msg)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="A cuet CLI that meows 🐱 and woofs 🐶")
    parser.add_argument("--command", choices=[
                        "meow", "woof"], help="Dog team or Cat team?", default="woof")
    parser.add_argument("--times", type=int, default=1,
                        help="Number of times to meow or woof")
    parser.add_argument(
        "--no-emoji", action="store_true", help="Hide the cat emoji in the output"
    )
    args = parser.parse_args()

    # BUG: --no-emoji option is ignored (for workshop exercise)
    if (args.command == "woof"):
        woof(times=args.times, emoji=True)
    else:
        meow(times=args.times, emoji=True)
