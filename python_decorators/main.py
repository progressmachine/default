import time


# This is our decorator
def log_time(func):
    def wrapper(*args, **kwargs):
        print(f"⏳ Running '{func.__name__}'...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"✅ Finished '{func.__name__}' in {end - start:.4f} seconds.\n")
        return result

    return wrapper


# Let's decorate this function
@log_time
def slow_add(a, b):
    time.sleep(1)
    return a + b


@log_time
def say_hello(name):
    time.sleep(0.5)
    print(f"Hello, {name}!")


if __name__ == "__main__":
    result = slow_add(5, 3)
    print(f"Result: {result}")

    say_hello("Pranish")