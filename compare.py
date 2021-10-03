import run_python
import run_cpython
import time

num_iters = 10000000
print(f'Number of iterations => {num_iters}')

start = time.time()
run_python.build_list(num_iters)
end = time.time()
py_time = end - start
print(f'Python time => {py_time}')


start = time.time()
run_cpython.build_list(num_iters)
end = time.time()
cpy_time = end - start
print(f'Cython time => {cpy_time}')


# Ratio
print(f'Ratio python to cython => {py_time / cpy_time}')


