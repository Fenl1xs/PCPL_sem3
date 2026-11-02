def field(items, *args):
    assert len(args) > 0, "Необходимо указать хотя бы одно поле"

    if len(args) == 1:
        key = args[0]
        for item in items:
            val = item.get(key)
            if val is not None:
                yield val
    else:
        for item in items:
            filtered = {k: item[k] for k in args if k in item and item[k] is not None}
            if len(filtered) > 0:
                yield filtered


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'color': 'blue'},
        {'title': None, 'price': None}
    ]

    print("Один аргумент ('title'):")
    print(list(field(goods, 'title')))

    print("\nНесколько аргументов ('title', 'price'):")
    print(list(field(goods, 'title', 'price')))