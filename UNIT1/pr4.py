call_count_naive = 0
call_count_memo = 0


def fib_naive(n):
    global call_count_naive
    call_count_naive += 1
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


memo = {}


def fib_memo(n):
    global call_count_memo
    call_count_memo += 1
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]


for test_n in [10, 20, 30]:

    call_count_naive = 0
    call_count_memo = 0
    memo = {}

    result_naive = fib_naive(test_n)
    result_memo = fib_memo(test_n)

    print(f'n={test_n}: fib={result_naive}')
    print(f'  Naive calls : {call_count_naive}')
    print(f'  Memoized calls: {call_count_memo}')
    print()