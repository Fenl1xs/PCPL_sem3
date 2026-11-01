from operator import itemgetter


class Lib:
    def __init__(self, id, name, size, lang_id):
        self.id = id
        self.name = name
        self.size = size
        self.lang_id = lang_id


class Lang:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class LibLang:
    def __init__(self, lang_id, lib_id):
        self.lang_id = lang_id
        self.lib_id = lib_id


langs = [
    Lang(1, "Python"),
    Lang(2, "C++"),
    Lang(3, "JavaScript"),
    Lang(11, "Python (Embedded)"),
    Lang(22, "C++ (Modern)"),
    Lang(33, "JavaScript (Node.js)"),
]

libs = [
    Lib(1, "Asyncio", 420, 1),
    Lib(2, "Axios", 310, 3),
    Lib(3, "Actix", 850, 2),
    Lib(4, "NumPy", 15200, 1),
    Lib(5, "Boost", 28000, 2),
]

libs_langs = [
    LibLang(1, 1),
    LibLang(3, 2),
    LibLang(2, 3),
    LibLang(1, 4),
    LibLang(2, 5),
    LibLang(11, 1),
    LibLang(33, 2),
    LibLang(22, 3),
    LibLang(11, 4),
    LibLang(22, 5),
]


def main():
    one_to_many = [
        (l.name, l.size, lang.name)
        for lang in langs
        for l in libs
        if l.lang_id == lang.id
    ]

    many_to_many_temp = [
        (lang.name, ll.lang_id, ll.lib_id)
        for lang in langs
        for ll in libs_langs
        if lang.id == ll.lang_id
    ]

    many_to_many = [
        (l.name, l.size, lang_name)
        for lang_name, lang_id, lib_id in many_to_many_temp
        for l in libs
        if l.id == lib_id
    ]

    print("Задание В1")
    res_11 = [
        (lib_name, lang_name)
        for lib_name, _, lang_name in one_to_many
        if lib_name.startswith("А") or lib_name.startswith("A")
    ]
    print(res_11)

    print("\nЗадание В2")
    res_12_unsorted = []
    for lang in langs:
        lang_libs = list(filter(lambda i: i[2] == lang.name, one_to_many))
        if len(lang_libs) > 0:
            lang_sizes = [size for _, size, _ in lang_libs]
            lang_size_min = min(lang_sizes)
            res_12_unsorted.append((lang.name, lang_size_min))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1))
    print(res_12)

    print("\nЗадание В3")
    res_13 = sorted(
        [(lib_name, lang_name) for lib_name, _, lang_name in many_to_many],
        key=itemgetter(0),
    )
    print(res_13)


if __name__ == "__main__":
    main()
