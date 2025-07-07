from strings.string_matching import naive_string_match


def test_naive_string_match_exact():
    text = "hello world"
    pattern = "world"
    result = naive_string_match(text, pattern)

    print(result)
    assert result == [6]


def test_naive_string_match_no_match():
    text = "abcdefg"
    pattern = "xyz"
    result = naive_string_match(text, pattern)
    print(result)
    assert result == []


def test_naive_string_match_multiple():
    text = "abcabcabc"
    pattern = "abc"
    result = naive_string_match(text, pattern)
    print(result)
    assert result == [0, 3, 6]  # Only first non-overlapping match due to break


def test_naive_string_match_empty_pattern():
    text = "abc"
    pattern = ""
    result = naive_string_match(text, pattern)
    print(result)
    assert result == []
