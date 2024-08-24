def isPalindrome(s: str) -> bool:
    translation_table = dict.fromkeys(map(ord, "!@#$.,:?;()- "), None)
    value = s.translate(translation_table).lower()

    right = len(value) - 1
    left = 0

    while left <= right:
        left_val = value[left]
        right_val = value[right]
        print(left_val, right_val)
        if value[left] != value[right]:
            return False

        right -= 1
        left += 1

    return True


s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))
