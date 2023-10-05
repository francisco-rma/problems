def sum_prefix_score(words: list[str]) -> list[int]:
    answer = []

    def is_prefix(target: str, comparison: str) -> bool:
        if len(comparison) < len(target):
            return False

        is_prefix = True

        i = 0

        while i < len(target):
            if target[i] == comparison[i]:
                i += 1
                continue
            else:
                i += 1
                is_prefix = False
                break

        return is_prefix

    def find_prefix_score(words: list[str], index: int) -> int:
        score = 0
        target = words[index]
        for i, word in enumerate(words):
            if is_prefix(target=target, comparison=word):
                score += 1
        return score

    for i, word in enumerate(words):
        score = find_prefix_score(words=words, index=i)
        if score > 0:
            answer.append(score)

    return answer


words = ["abc", "ab", "bc", "b"]

answer = sum_prefix_score(words)
print(answer)
