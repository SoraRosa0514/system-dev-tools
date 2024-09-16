import time

def example_function():
    total = 0
    for i in range(1, 1000000):
        total += i
    return total

start_time = time.time()
result = example_function()
end_time = time.time()

real_time = end_time - start_time

print(f"Result: {result}")
print(f"Real time: {real_time:.6f} seconds")