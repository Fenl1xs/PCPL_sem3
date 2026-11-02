import json
import sys
import os

from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique
from field import field
from gen_random import gen_random

# Путь к файлу передается аргументом командной строки или берется data_light.json по умолчанию
path = sys.argv[1] if len(sys.argv) > 1 else 'data_light.json'

if not os.path.exists(path):
    # Фоллбэк на поиск в текущей директории, если скрипт запущен из корня проекта
    alt_path = os.path.join(os.path.dirname(__file__), path)
    if os.path.exists(alt_path):
        path = alt_path

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    return sorted(list(Unique(field(arg, 'job-name'), ignore_case=True)), key=lambda s: s.lower())


@print_result
def f2(arg):
    return list(filter(lambda s: s.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    return list(map(lambda s: f"{s} с опытом Python", arg))


@print_result
def f4(arg):
    salaries = gen_random(len(arg), 100000, 200000)
    return [f"{job}, зарплата {salary} руб." for job, salary in zip(arg, salaries)]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))