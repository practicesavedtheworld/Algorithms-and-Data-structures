def is_palindrome(text_: str) -> bool:
    """
    Palindrome is a phrase that reads equal in both side. For e.g "TNT" is palindrome.
    Accept that empty sequence is a palindrome.
    Time complexity is O(n + m), n == len(text), m == len(text with only alphanumeric chars). It can be O(n+n) => O(n)
    Space complexity is O(m + m) => O(m)
    :param text_: str
    :return: bool
    """
    if text_:
        only_letters = [char for char in text_ if char.isalnum()]  # Think, it could be better.
        for i in range(len(only_letters) // 2):
            if only_letters[i] != only_letters[~i]:
                return False
    return True


def main():
    """Testing"""

    assert is_palindrome('qweewq') is True
    assert is_palindrome('   w  e e            e w ') is True
    assert is_palindrome('sefr') is False
    assert is_palindrome('') is True


if __name__ == '__main__':
    main()
