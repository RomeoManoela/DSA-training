class HashTable:
    def __init__(self, size = 7):
        self.data_map: list = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def set_item(self, key, value):
        index = self.__hash(key)
        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        for item in self.data_map[index]:
            if item[0] == key:
                return item[1]

    def keys(self):
        key = []
        for items in self.data_map:
            if items is not None:
                for item in items:
                    key.append(item[0])
        return key

    def print_table(self):
        for i, value in enumerate(self.data_map):
            print(f'{i}: {value}')

ht = HashTable(7)
ht.set_item("romeo", 1200)
ht.set_item("rome", 1201)
ht.set_item('gasy', 150)
ht.set_item('bolts', 1400)
ht.set_item('washers', 50)
ht.set_item('lumber', 70)
ht.print_table()
print(f'All keys: {ht.keys()}')
