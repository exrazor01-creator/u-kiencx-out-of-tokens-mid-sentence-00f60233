"""Out of Tokens, Mid-Sentence -- make.fun one-liner entry.

The line below is the error message an AI agent shows when it runs
out of tokens mid-sentence. The joke is meta: the error message
itself runs out of tokens too, so it gets cut off mid-sentence just
like the sentence it is apologising for. No grand apology, no
"please try again" -- the error simply stops, which is the whole
point: running out of tokens does not spare even the error message.
"""

import os

LINE = "Error: out of tokens. This error message was also going to be longer, but..."

MAX_LEN = 140


def validate(text):
    """Check that *text* is a valid one-line entry.

    Raises ValueError unless the text is a string of 1..140
    characters, ASCII only, a single line, not blank, with no
    leading or trailing space and no double spaces.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= MAX_LEN:
        raise ValueError("entry must be 1..140 characters")
    if not text.isascii():
        raise ValueError("entry must be ASCII only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing space")
    if "  " in text:
        raise ValueError("entry must not contain double spaces")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii") as fh:
        fh.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()
