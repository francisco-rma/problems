# =======================================================
# Test harness
# =======================================================


# =======================================================
# Levenshtein distance
# =======================================================

from levenshtein_distance import lev, random_words

source = "aksdjfofweg"
target = "dfargstrdt"

result = lev(p=source, q=target)

print(result)

for i in range(100, 1000, 100):
    random_words(size=1000)


# =======================================================
# =======================================================
