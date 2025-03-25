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
    assert root.search(word)

root.search("adwahiudwa")

# =======================================================
# =======================================================
