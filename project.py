import spacy
from spellchecker import SpellChecker
from language_tool_python import LanguageTool
from diff_match_patch import diff_match_patch
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.align import Align

import sys


nlp = spacy.load("en_core_web_sm")
spell = SpellChecker()
tool = LanguageTool('en-US')
console = Console()
dmp = diff_match_patch()

# Mistake(s) count
spelling_errors = 0
grammar_errors = 0

def main():
    text = Prompt.ask("Text", default="Hello World").strip()

    if text.isdigit():
        sys.exit("Expected WORDS NOT NUMBERS")

    corrected_spelling = spell_check(text)
    corrected_grammar = grammar_check(corrected_spelling)

    highlight(text, corrected_grammar)


def spell_check(text: str) -> str:
    """ Corrects spelling mistakes in the given text. """
    global spelling_errors
    words = text.split()
    corrected_words = []

    for word in words:
        if word in spell.unknown(words):
            corrected = spell.correction(word)
            if corrected:
                corrected_words.append(corrected)
                spelling_errors += 1
            else:
                corrected_words.append(word)
        else:
            corrected_words.append(word)

    return " ".join(corrected_words)


def grammar_check(text: str) -> str:
    """ Corrects grammatical mistakes in the given text. """
    global grammar_errors
    matches = tool.check(text)
    grammar_errors += len(matches)
    return tool.correct(text)


def highlight(original: str, corrected: str):
    """ Highlights changes in the text. """
    diff = dmp.diff_main(original, corrected)
    dmp.diff_cleanupSemantic(diff)
    colored_diff = []

    for op, data in diff:
        if op == diff_match_patch.DIFF_EQUAL:
            colored_diff.append(data)
        elif op == diff_match_patch.DIFF_INSERT:
            colored_diff.append(f"[green]{data}[/]")
        elif op == diff_match_patch.DIFF_DELETE:
            colored_diff.append(f"[red]{data}[/]")

    colored_output = "".join(colored_diff)

    console.print("\n", Align.center(colored_output), "\n")
    console.print(Panel(Text(f'Spelling Mistakes: {spelling_errors}', justify="center", style="red")))
    console.print(Panel(Text(f'Grammar Mistakes: {grammar_errors}', justify="center", style="red")))


if __name__ == "__main__":
    main()
    tool.close()
