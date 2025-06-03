# =======================================================
# Test harness
# =======================================================

import urllib.request
from trie import Trie

# =======================================================
# Word Trie
# =======================================================

path = "https://www.mit.edu/~ecprice/wordlist.10000"
response = urllib.request.urlopen(url=path)

words = response.read().decode().splitlines()
print(f"Source array has {len(words)} words")
root = Trie()

for word in words:
    root.insert(word)

for word in words:
    result: str = root.search(word)
    print(f"Found {result}/{word}")
    assert result == word

word = "adwahiudwa"
result = root.search(word)
print(f"Found {result}/{word}")

# =======================================================
# =======================================================
