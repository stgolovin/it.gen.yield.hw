import sys


class FlatIterator:
    def __init__(self, list_of_list):
        self.main_list = list_of_list

    def __iter__(self):
        self.main_list_cursor = 0
        self.nested_list_cursor = -1
        return self

    def __next__(self):
        self.nested_list_cursor += 1  # [1][2]
        if self.nested_list_cursor is IndexError:
            self.main_list_cursor += 1
            self.nested_list_cursor = 0
        if self.main_list_cursor is IndexError:
            raise StopIteration
        item = self.main_list[self.main_list_cursor][self.nested_list_cursor]
        return item


def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for item in FlatIterator(list_of_lists_1):
        print(item)

    sys.exit()
    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
