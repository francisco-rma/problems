from sorting.smallest_missing_number import smallest_missing


def test_smallest_missing_number(n=10000):
    population = list(range(1, n))

    for idx, item in enumerate(population):
        source = population[:idx] + (
            population[idx + 1 :] if idx < len(population) - 1 else []
        )
        print(f"iteration # {idx}...")
        test = smallest_missing(source)
        control = item
        assert test == control
