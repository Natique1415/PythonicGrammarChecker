# CS50 Final Project - PythonicGrammarChecker

#### Video Demo: <https://youtu.be/5-No6oaCl6Y>

#### Description: I always used Grammarly to figure out my errors while writing my school assignments or any such event that might show up. After learning Python, I figured maybe I could implement a similar program in Python.

---

## Libraries Used

- [**spaCy**](https://spacy.io/) (open-source software library for advanced natural language processing)
- [**rich**](https://rich.readthedocs.io/en/stable/introduction.html) (writing colored text to the terminal)
- [**pyspellchecker**](https://pyspellchecker.readthedocs.io/en/latest/) (library responsible for finding misspelled words)
- [**language-tool-python**](https://pypi.org/project/language-tool-python/) (responsible for pointing out potential grammatical errors)
- [**diff-match-patch**](https://pypi.org/project/diff-match-patch/) (finds the difference between two given strings)

---

## How Does It Work?

### `def main()`

> The main function prompts the user for a sentence or a paragraph (depending on the use case).

- Other functionalities of the main function:
  - Strips leading and trailing whitespace from the user-provided input.
  - Calls out the user if **only** digits are provided.
  - Once the input is cleaned, it calls a series of functions that process the text for spelling and grammar corrections.

---

### `def spell_()`

> Expects a sentence or paragraph and corrects the spelling mistakes in the input.

- **How it works:**
  - A variable called **spelling_e** keeps track of spelling errors.
  - The function uses **spaCy** to tokenize the input for better accuracy.
  - The input is broken down into words, and each word is checked against a dictionary.
  - If a word is incorrect, it is replaced with the closest correct match.

  ```python
  correct_text = []
  for word in words_list:
      correct_text.append(spell.correction(word))
      if word != spell.correction(word):
          spelling_e += 1
  ```
  - Finally, the function returns the corrected text with spelling errors fixed.

---

### `def grammar_()`

> Expects a sentence or paragraph and corrects grammatical errors.

- **How it works:**
  - A variable called **grammar_e** keeps track of grammatical errors.
  - Uses **language-tool-python** to analyze and correct grammar mistakes.

    ```python
    grammar_e += len(tool.check(para))
    return tool.correct(para)
    ```

---

### `def highlight()`

> Uses the **rich** library to highlight corrections and display them in a neat, color-coded format.

- **How changes are detected:**
  - The **diff-match-patch** library compares the original and corrected text.
  - Semantic comparison is used to determine differences.

    ```python
    diff = dmp.diff_main(old, new)
    dmp.diff_cleanupSemantic(diff)
    ```
  - The differences are then formatted:
    ```python
    for op, data in diff:
        if op == diff_match_patch.DIFF_EQUAL:
            colored_diff.append(data)
        if op == diff_match_patch.DIFF_INSERT:
            colored_diff.append(f"[green]{data}[/]")
    ```
  - Words that were changed are highlighted in **green**.

---

### **Implementation of the Rich Library**

- Used to display corrections with formatting and colors.
- Highlights spelling and grammar mistakes:

  ```python
  console.print(Align.center(colored_diff))
  ```
  - **Aligns** output in the center.
  - Recognizes `[green]...[/]` formatting to color the corrected text.

- Displays mistake counts:

  ```python
  spell_p = Panel(Text(f'Spelling Mistake(s): {spelling_e}', justify="center", style="red"))
  grammar_p = Panel(Text(f'Grammar Mistake(s): {grammar_e}', justify="center", style="red"))
  ```

---

### **Downsides**

- The corrections may not always be 100% accurate.
- Capitalization changes can sometimes be flagged as errors.
- The program takes a longer runtime due to the use of multiple libraries.

---

### **Possible Improvements**

- Implement **multithreading** to improve performance.
- Train a better NLP model for improved grammar correction.
- Allow users to choose between different correction modes.

---
