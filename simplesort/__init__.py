def simplesort(s):
    a = s.split(' ')
    a = [float(i) for i in a]
    a = sorted(a)
    a = ["{:.3f}".format(k) for k in a]
    return ' '.join(a)

__all__ = ['simplesort']
