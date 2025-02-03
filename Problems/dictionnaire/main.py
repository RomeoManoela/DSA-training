import typing
from numbers import Number


def word_max(words: dict) -> str:
    max_word: int = 0
    result: str = ""
    for word in words:
        if words[word] > max_word:
            max_word = words[word]
            result = word
    return result

def reverse_dic(dic: dict) -> None:
    new_dic = {}
    for key, value in dic.items():
        new_dic[value] = key

def main():
    my_dict: dict = {'romeo': 12, 'man': 2, 'akory': 13}
    print(word_max(my_dict))
    reverse_dic(my_dict)
    print(my_dict)
if __name__ == '__main__':
    main()
