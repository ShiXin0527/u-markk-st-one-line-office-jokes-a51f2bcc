#!/usr/bin/env python3
"""make.fun bounty entry: One-Line Office Jokes.

One line, one office, one joke that everyone in the meeting
pretends not to understand — while understanding it perfectly.
"""

JOKE = "Our office has an open-door policy: the door is open, the manager is out, the Wi-Fi is still down — and the meeting is already running late."


def joke():
    """Return the one-line office joke."""
    return JOKE


def main():
    print(joke())


if __name__ == "__main__":
    main()
