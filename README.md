**StringAugmentor** is a Python script that offers various ways to manipulate and transform strings. It’s particularly useful for creating unique variations of text, which can be used for password generation, adding creative effects to text, or creating hidden messages.

### Features

The script includes the following string transformations:

1. **Reversed String** — Displays the text in reverse order.
2. **Concatenated Words** — Joins all words into a single string without spaces.
3. **Removed Random Characters** — Randomly removes 2-3 characters from words.
4. **Replaced Random Characters** — Replaces 2-3 characters with random special symbols.
5. **Random Case** — Randomly converts letters to uppercase or lowercase.
6. **Inserted Random Characters** — Inserts random special symbols or numbers between each character.
7. **Leet Transformation** — Converts text into leet format (a hacker-style text transformation).
8. **Swapped Adjacent Words** — Swaps adjacent words in the string.

Each transformation is returned as a separate string within a dictionary.

### Example Usage

```python
# Example input string
input_str = "Hello мир! Привіт мир! Älä usko; ñándõ hęll."
results = augment_string(input_str)

# Output the results
for key, value in results.items():
    print(f"{key}: {value}")
```

### Output

Each transformation is returned as a dictionary element with a corresponding key. Here’s a brief description of each key:

- **reversed** — the reversed string
- **concatenated** — the string with concatenated words
- **removed_chars** — the string with removed random characters
- **replaced_chars** — the string with replaced random characters
- **random_case** — the string with randomized case
- **inserted_chars** — the string with inserted random special symbols
- **leet** — the string transformed into leet format
- **swapped** — the string with adjacent words swapped
