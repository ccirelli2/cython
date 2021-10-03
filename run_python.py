'''Natural python functions
'''

def build_list(size):
    nlist = []
    for i in range(0, size):
        nlist.append(i)
    return nlist


def test(x):
    y = 1
    for i in range(1, x +1):
        y += i
    return y




