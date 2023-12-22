from exercises.palindrome import is_palindrome


def test_palindrome_true():
    assert is_palindrome("A man, a plan, a canal, Panama") is True


def test_palindrome_false():
    assert is_palindrome("Hello, World!") is False


def test_palindrome_empty_string():
    assert is_palindrome("") is True


def test_palindrome_single_character():
    assert is_palindrome("a") is True


def test_palindrome_whitespace():
    assert is_palindrome("   A  Santa at NASA ") is True
