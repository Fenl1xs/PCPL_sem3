from collections.abc import Iterable


class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items_iter = iter(items)
        self.used_elements = set()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self.items_iter)
            
            # Ключ для сравнения в множестве
            if self.ignore_case and isinstance(item, str):
                check_item = item.lower()
            else:
                check_item = item

            if check_item not in self.used_elements:
                self.used_elements.add(check_item)
                return item


if __name__ == '__main__':
    from gen_random import gen_random

    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print("data1:", list(Unique(data1)))

    data2 = gen_random(10, 1, 3)
    print("data2 (генератор):", list(Unique(data2)))

    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print("data3 (ignore_case=False):", list(Unique(data3)))
    print("data3 (ignore_case=True):", list(Unique(data3, ignore_case=True)))