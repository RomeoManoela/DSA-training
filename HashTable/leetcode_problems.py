from main import HasTable


# check if there is a common item in two list
def item_in_common(list1: list, list2: list) -> bool:
    """the best approach is to use a hash table"""
    ht: HasTable = HasTable()  # dict can be used instead of HasTable
    for i in list1:
        ht.set(str(i), True)  # O(1)
    for j in list2:
        if ht.get(str(j)):  # O(1)
            return True
    return False


# find duplicate in a list
def find_duplicate(list1: list) -> list:
    """the best approach is to use a dictionary or hash table"""
    result: list = []
    my_dict: dict = {}  # HasTable can be used instead of dict
    for i in list1:
        if i not in my_dict:
            my_dict[i] = 1
        else:
            result.append(i)
    return result


# First Non-Repeating Character
def first_non_repeating_char(string: str) -> str | None:
    my_dic: dict = {}
    for char in string:
        if char not in my_dic:
            my_dic[char] = 1
        else:
            my_dic[char] += 1

    for char in string:
        if my_dic[char] == 1:
            return char
    return None


def main():
    print(item_in_common([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))
    print(item_in_common([1, 2, 3, 4, 5], [5, 6, 7, 8, 9, 10]))
    print(find_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]))
    print(first_non_repeating_char("aabbccddeef"))
    print(first_non_repeating_char("hello"))
    print(first_non_repeating_char("leetcode"))
    print(first_non_repeating_char("romero"))


if __name__ == "__main__":
    main()
