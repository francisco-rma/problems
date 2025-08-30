from strings.rabin_karp import horner_rule, rabin_karp
from string import ascii_lowercase
import random


def test_horner_rule():
    attempts = 10000
    i = 0
    size = 100
    while i < attempts:
        sample = random.choices(population=ascii_lowercase, k=size)
        control = sum([ord(sample[i]) * (10 ** (size - i - 1)) for i in range(size)])
        test = horner_rule(sample)

        assert test == control
        i += 1


def test_rabin_karp(attempts: int = 10000, sample_size: int = 1000, target_size: int = 15):
    i = 0
    while i < attempts:
        target = "".join(random.choices(population=ascii_lowercase, k=target_size))
        target_set = set(target)

        sample = "".join(
            random.choices(
                population=list(filter(lambda x: x not in target_set, ascii_lowercase)),
                k=sample_size,
            )
        )

        control = bool(random.choices(population=[True, False], k=1)[0])

        if control:
            match random.choice([0, 1, 2]):
                case 0:
                    sample = target + sample
                case 1:
                    sample += target
                case 2:
                    sample = sample[: len(sample) // 2] + target + sample[len(sample) // 2 :]

        test = rabin_karp(pattern=target, text=sample)

        assert test == control
        i += 1
