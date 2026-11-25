import os

LINE = "Automatic reply: I quit to work as a barista and will not be returning. I still take orders all day — when I hallucinate one now, a real person has to drink it."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
