from reviews.text_utils.anagram import is_anagram
from reviews.text_utils.reverse import reverse


def test_reverse():
    assert reverse("hello") == "olleh"
    assert reverse("") == ""
    assert reverse("a") == "a"
    assert reverse("racecar") == "racecar"
    assert reverse("12345") == "54321"
    assert reverse("12341") == "54321"


def test_is_anagram():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("Triangle", "Integral") is True
    assert is_anagram("apple", "pale") is False
    assert is_anagram("aabbcc", "abcabc") is True
    assert is_anagram("abcd", "abce") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "a") is True
    assert is_anagram("a", "b") is False
