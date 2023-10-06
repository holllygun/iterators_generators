class FlatIterator:

    def __init__(self, some_list):
        self.main_list = some_list
        self.len_list = len(self.main_list)
        self.cursor = -1

    def __iter__(self):
        self.cursor += 1
        self.nested_list_cursor = 0
        return self

    def __next__(self):
        if self.nested_list_cursor == len(self.main_list[self.cursor]):
            iter(self)
        if self.cursor == self.len_list:
            raise StopIteration
        self.nested_list_cursor += 1
        return self.main_list[self.cursor][self.nested_list_cursor-1]


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()