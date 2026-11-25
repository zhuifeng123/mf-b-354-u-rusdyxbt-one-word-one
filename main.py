#!/usr/bin/env python3
import os


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    entry = "punbelievable"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
