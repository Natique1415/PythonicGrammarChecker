from project import spell_, grammar_, highlight


def main():
    test_spell_correct_words()
    test_spell_wrong_words()
    test_grammar_()
    test_highlight()


def test_spell_correct_words():
    """Tests spell_() function with correct spellings."""
    assert spell_("I love my cat") == "I love my cat"
    assert spell_("Hello World") == "Hello World"
    assert spell_("My hometown is in India") == "My hometown is in India"
    assert spell_("You should go to the carnival") == "You should go to the carnival"
    assert (
        spell_("Python is much better than Rust") == "Python is much better than Rust"
    )


def test_spell_wrong_words():
    """Tests spell_() function with incorrect spellings."""
    assert spell_("I loev my cta") == "I love my cat"
    assert spell_("ehllow Wrold") == "hello world"
    assert spell_("My hoemtown is in Indai") == "My hometown is in India"
    assert spell_("You shuold go to the canrival") == "You should go to the carnival"
    assert (
        spell_("pytohn is mchh betetr than rust") == "python is much better than rust"
    )


def test_grammar_():
    """Tests grammar_() function with grammatical mistakes."""
    assert grammar_("He go to school every day.") == "He goes to school every day."
    assert grammar_("She like apples.") == "She likes apples."
    assert grammar_("I has a dog.") == "I have a dog."
    assert grammar_("This are my books.") == "These are my books."
    assert grammar_("He go yesterday.") == "He went yesterday."


def test_highlight():
    """Tests highlight() function to ensure changes are displayed correctly."""
    old = "I loev my cta"
    new = "I love my cat"
    highlight(old, new)

    old = "She like apples."
    new = "She likes apples."
    highlight(old, new)


if __name__ == "__main__":
    main()
