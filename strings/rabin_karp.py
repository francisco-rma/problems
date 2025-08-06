from string import ascii_lowercase


def rabin_karp(text: str, pattern: str, d: int = len(ascii_lowercase), q: int = 11) -> bool:
    m = len(pattern)
    n = len(text)
    h = (d ** (m - 1)) % q

    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t and text[s : s + m] == pattern:
            return True
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q

    return False


def horner_rule(text: str, idx: int = None) -> int:
    if idx is None:
        idx = len(text) - 1
    if idx < 0 or idx >= len(text):
        return 0
    ord_val = ord(text[idx])
    hr = horner_rule(text, idx - 1)
    exponent = len(text) - idx - 1
    return (10**exponent) * ord_val + hr
