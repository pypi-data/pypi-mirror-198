from functools import wraps
import time

def timeit(func):
	@wraps
	def timeit_wrapper(*args, **kwargs):
        start_time_r = time.perf_counter()
        start_time_p = time.process_time()
        # run function
        result = func(*args, **kwargs)
        end_time_r = time.perf_counter()
        end_time_p = time.process_time()
        elapsed_r = end_time_r - start_time_r
        elapsed_p = end_time_p - start_time_p
        print(f"Function {func.__name__}{args} {kwargs} Took {elapsed_r:.4f} seconds (real) / {elapsed_p:.4f} (cpu)")
        return result
	return timeit_wrapper

def default_decorator_func(arg):
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			pass
			result = func(*args, **kwargs)
			pass
			return result

		return wrapper
	return decorator