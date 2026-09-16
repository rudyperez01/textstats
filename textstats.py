"""Small CLI utility for computing basic statistics about a text file."""
import sys


def count_lines(text):
    if text == "":
        return 0
    return len(text.splitlines())


def count_words(text):
    return len(text.split())


def count_chars(text):
    return len(text)


def stats(text):
    return {
        "lines": count_lines(text),
        "words": count_words(text),
        "chars": count_chars(text),
    }


def main(argv):
    if len(argv) != 2:
        print("Usage: python textstats.py <file>", file=sys.stderr)
        return 1

    with open(argv[1], "r") as f:
        text = f.read()

    result = stats(text)
    print(f"lines: {result['lines']}")
    print(f"words: {result['words']}")
    print(f"chars: {result['chars']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
