class HasTable:
    def __init__(self, size: int = 7) -> None:
        self.size: int = size
        self.data_map: list = [None] * self.size

    def print_table(self) -> None:
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def __hash(self, key: str):
        my_hash: int = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % self.size
        return my_hash

    def set(self, key: str, value: int) -> None:
        index: int = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get(self, key: str) -> int | None:
        index: int = self.__hash(key)
        if self.data_map[index] is None:
            return None
        for data in self.data_map[index]:
            if data[0] == key:
                return data[1]
        return None

    def keys(self) -> list:
        all_keys: list = []
        for data in self.data_map:
            if data is not None:
                for key in data:
                    all_keys.append(key[0])
        return all_keys


# leetcode question
def item_in_common(list1: list, list2: list) -> bool:
    """le meilleur solution est de faire un hash table"""
    ht: HasTable = (
        HasTable()
    )  # On peut utiliser un dictionaire, c'est le hastable natif
    for i in list1:
        ht.set(str(i), True)  # O(1)
    for j in list2:
        if ht.get(str(j)):  # O(1)
            return True
    return False


def main():
    ht: HasTable = HasTable()
    ht.set("hello", 10)
    ht.set("bolts", 100),
    ht.set("washers", 1000)
    ht.print_table()
    print(ht.get("hello"))
    print(ht.get("washers"))
    print(ht.keys())


if __name__ == "__main__":
    main()
