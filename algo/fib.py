from timeit import default_timer as timer

def fib_recursive(n):
    if n <= 2:
        return 1

    return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_memoisation(n, lookup):
    if n <= 2:
        lookup[n] = 1

    if lookup[n] is None:
        lookup[n] = fib_memoisation(n - 1, lookup) + fib_memoisation(n - 2, lookup)

    return lookup[n]


if __name__ == '__main__':
    degree = 42
    delimiter = '----------'
    print(f'Comparing different approaches to computing Fibonacci series.')
    print(f'Computing the {degree}. term:')


    print('\nRecursive:')
    print(delimiter)
    start = timer()
    print(fib_recursive(degree))
    end = timer()
    print(end - start)

    print('\nMemoisation:')
    print(delimiter)
    start = timer()
    print(fib_memoisation(degree, [None]*100))
    end = timer()
    print(end - start)
