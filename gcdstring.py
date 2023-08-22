def gcdOfStrings(str1: str, str2: str) -> str:
    def find_divisors(term: str):
        divisors = set()
        size = len(term)
        end = term[-1]

        min_index = -1
        while term not in divisors:
            i = min_index + 1
            while i < size:
                if term[i] == end:
                    min_index = i
                    break

                i += 1

            candidate_divisor = term[:i + 1]

            if size % len(candidate_divisor) != 0:
                continue

            division_test = ""
            while len(division_test) != size:
                division_test += candidate_divisor

            if division_test == term:
                divisors.add(candidate_divisor)

        return divisors

    divisors1 = find_divisors((str1))
    divisors2 = find_divisors((str2))

    result_set = divisors1.intersection((divisors2))

    if len(result_set) > 0:
        return max(result_set)
    else:
        return ""


test_string1 = "AA"
test_string2 = "A"

greatest_divisor = gcdOfStrings(test_string1, test_string2)
print(greatest_divisor)
