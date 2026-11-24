"""Dad Joke Showdown entry: one original dad joke, written to /output/entry.txt."""

# Revision note: verified locally that main() writes TEXT byte-identical to /output/entry.txt.
import os

TEXT = "I told my wife I wanted to be a professional napper. She said, 'You've been training for years \u2014 I'm just proud you finally found a job you can do with your eyes closed.'"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
