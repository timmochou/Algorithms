def callstack(x):
    if x == 1:
        return 1
    if x > 1:
        return x * callstack(x-1)

print(callstack(5))