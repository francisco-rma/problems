from array import array

SIZE = 100
BITS = 8


def pre_hash(key):
    value = int(bytes(key, encoding="utf-8").hex(), 16)
    return value


def division_hash(key: int, m=SIZE) -> int:
    return key % m


def multiplication_hash(key: int, a: int = SIZE, w: int = BITS, r: int = 2) -> int:
    return ((a * key) % (2**w)) >> (w - r)


class dictionary:
    def __init__(self):
        self.size = SIZE
        self.table = array("b", [0] * self.size)
        self.method: str = "multiplication"

    def generate_hash(self, key: str | int) -> int:
        match self.method:
            case "division":
                hash_key = division_hash(pre_hash(key))
            case "multiplication":
                hash_key = multiplication_hash(pre_hash(key))
            case _:
                hash_key = division_hash(pre_hash(key))
        assert hash_key < self.size
        return hash_key

    def insert(self, key: str | int, value: int):
        hash_key = self.generate_hash(key)
        print(hash_key)
        self.table[hash_key] = value

    def search(self, key):
        hash_key = self.generate_hash(key)
        return self.table[hash_key]


source = "hello world"
key = pre_hash(source)
print(f"source: {source} --> {key}")

d = dictionary()
d.insert("key1", 1)
d.insert("key2", 2)
d.insert("key3", 3)
d.insert("key4", 4)
d.insert("adfkohgsighsiuhfiu", 5)
d.insert("asdforf", 5)
