from functools import wraps
import time
import random

def my_wrapper(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(f.__name__)
        print(f.__doc__)
        return f(*args, **kwargs)

    return decorated_function

def retry_handler(retry_number=3):
    def decorator(f):
        # @wrap(f)
        def decorated_function(*args, **kwargs):
            retry_time = 0
            while True:
                try:
                    return f(*args, **kwargs)
                except Exception as ex:
                    print(ex)
                    retry_time += 1
                    if retry_time >= retry_number:
                        raise ex
                    else:
                        print(f"retry {retry_time}/{retry_number} for function {f.__name__}")
                    time.sleep(2 * random.random())

        return decorated_function
    return decorator



@retry_handler(retry_number=3)
def divide_0(a):
    """This function is to divied 0"""
    return a / 0


def main():
    a = 3
    b = divide_0(a)
    print(b)

if __name__ == '__main__':
    main()

