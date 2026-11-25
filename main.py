# Emit one UTF-8 line for the make.fun scorer.
import os
from pathlib import Path

TEXT = "The meeting could've been an email, but you can't attach a hostage."


if __name__ == "__main__":
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="\n") as entry_file:
        entry_file.write(TEXT + "\n")
    print(len(TEXT))
