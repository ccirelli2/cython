cpdef list build_list(int size):
    cdef list nlist = []
    cdef int i
    for i in range(0, size):
        nlist.append(i)
    return nlist

cpdef int test(int x):
    cdef int y = 1
    cdef int i
    for i in range(1, x + 1):
        y += 1
    return y



