import time
import matplotlib.pyplot as plt

def pure_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return pure_fib(n-1) + pure_fib(n-2)

def fib_dynamic(n):
    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n]

n_values = range(10, 101, 10)
pure_execution_times = []
dynamic_execution_times = []

for n in n_values:
    if n > 50:
        n = 50
    start_time = time.time()
    result = pure_fib(n)
    end_time = time.time()
    execution_time = end_time - start_time
    pure_execution_times.append(execution_time)
    print(f"n={n}, result={result}, execution_time={execution_time:.4f} seconds")

for n in n_values:
    start_time = time.time()
    result = fib_dynamic(n)
    end_time = time.time()
    execution_time = end_time - start_time
    dynamic_execution_times.append(execution_time)
    print(f"n={n}, result={result}, execution_time={execution_time:.8f} seconds")


plt.plot(n_values, pure_execution_times, 'o-',label='Recursive')
plt.plot(n_values, dynamic_execution_times,'o-', label='Dynamic')
plt.xlabel('input size')
plt.ylabel('execution Time (seconds)')
plt.legend()
plt.show()