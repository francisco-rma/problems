import random
from string import ascii_lowercase


def rabin_karp(s: str, t: str) -> bool:
    idx = len(s) - 1

    ps = horner_rule(s)
    ts = horner_rule(t[: idx + 1])
    if ps == ts and t[idx - len(s) + 1 : idx + 1] == s:
        print("\nmatch!")
        print(f"{t[idx - len(s)+1 : idx+1]} ->  {ts}")
        print(f"{s} ->  {ps}")
        return True
    idx += 1

    while idx < len(t):
        ts = 10 * (ts - 10 ** (len(s) - 1) * ord(t[idx - len(s)])) + ord(t[idx])
        if ps == ts and t[idx - len(s) + 1 : idx + 1] == s:
            print("\nmatch!")
            print(f"{t[idx - len(s)+1 : idx+1]} ->  {ts}")
            print(f"{s} ->  {ps}")
            return True
        idx += 1

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


result = rabin_karp("dero", "o rato roeu a roupa do rei de roma")

print(result)


def test_rabin_karp():
    attempts = 10000
    i = 0
    size = 100
    target_size = 5
    while i < attempts:
        target = "".join(random.choices(population=ascii_lowercase, k=target_size))
        target_set = set(target)

        sample = "".join(
            random.choices(
                population=list(filter(lambda x: x not in target_set, ascii_lowercase)), k=size
            )
        )

        control = bool(random.choices(population=[True, False], k=1)[0])
        control = True
        if control:
            sample = target + sample

        test = rabin_karp(s=target, t=sample)

        assert test == control
        i += 1


test_rabin_karp()
