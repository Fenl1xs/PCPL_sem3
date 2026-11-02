import time
from contextlib import contextmanager


class cm_timer_1:
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = time.perf_counter() - self.start_time
        print(f"time: {elapsed:.2f}")


@contextmanager
def cm_timer_2():
    start_time = time.perf_counter()
    try:
        yield
    finally:
        elapsed = time.perf_counter() - start_time
        print(f"time: {elapsed:.2f}")


if __name__ == '__main__':
    print("Тестирование cm_timer_1:")
    with cm_timer_1():
        time.sleep(1.5)

    print("\nТестирование cm_timer_2:")
    with cm_timer_2():
        time.sleep(1.5)