# without dp
import time


def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


# with memorization
def fib_memo(n: int, cache={}) -> int:
    if n < 2:
        return n
    if n not in cache:
        cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)
    return cache[n]


if __name__ == "__main__":
    print(fib(600))
    start_time = time.time()
    print(fib_memo(900))
    print(f"end:{time.time() - start_time}")
