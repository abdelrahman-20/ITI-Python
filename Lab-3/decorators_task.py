# 7) Decorators Task
#    - Create a decorator called "log_time" that:
#         - Records the execution time of any function.
#         - Saves the function name and runtime into "execution_log.txt".
#    - Apply this decorator to at least two tasks (e.g., Math Automation & Regex Log Cleaner).
#    - Verify that the log file contains entries after running.

import time


# Decorator Function:
def log_time(func):
    def wrapper(*args, **kwargs):
        print("*" * 75 + "\n")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        runtime = end - start

        # Log function name and runtime into file
        with open("execution_log.txt", "a") as f:
            f.write(f"{func.__name__} => {runtime:.6f} Seconds\n")
            f.close()
        print(f"\nResult is: {result}, in Time: {runtime}")
        print("*" * 75 + "\n")
        return result

    return wrapper
