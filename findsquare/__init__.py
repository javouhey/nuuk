import types
import decimal
from itertools import combinations

__author__ = 'Gavin Bong'

class SlopeInterceptEquation(object):
    def __init__(self, slope, b):
        if type(slope) != decimal.Decimal:
            raise ValueError('slope must be a decimal.Decimal')
        self.slope = slope
        if type(b) != decimal.Decimal:
            b = decimal.Decimal(b)
        self.b = b

    def y(self, x):
        if type(x) != decimal.Decimal:
            x = decimal.Decimal(x)
        return (self.slope * x) + self.b

def len_slope(p1, p2):
    return decimal.Decimal(pow(p1[0]-p2[0], 2) + pow(p1[1]-p2[1], 2)).sqrt()

def dot_product(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1]

def is_perpendicular_at(intersect, point1, point2):
    if intersect == point1 or intersect == point2 or point1 == point2:
        return (False, -8)

    try:
        slope1 = find_slope(intersect, point1)
        len1 = len_slope(intersect, point1)
        #print '\t1 len: ==>', len1, 'slope1 ', slope1
        #print '\tcheck slope2'
        try:
            slope2 = find_slope(intersect, point2, indent=True)
            len2 = len_slope(intersect, point2)
            #print '\t2 len2: ==>', len2, 'slope2 ', slope2

            if (len1.to_integral() == len2.to_integral()):
                # do dot products in linear algebra
                v1 = (intersect[0]-point1[0], intersect[1]-point1[1]) 
                v2 = (point2[0]-intersect[0], point2[1]-intersect[1]) 
                dpres = dot_product(v1, v2)
                #print "dotproduct=", str(dpres)
                return (abs(dpres) == 0, len1.to_integral())
            else:
                return (False, -2)

        except ZeroDivisionError:
            try:
                if slope1 != 0:
                    raise RuntimeError('')
                #print '\tCANDIDATE:', intersect, 'and', point1, 'MIGHT BE perpendicular with', point2
                length_point2 = abs(intersect[1] - point2[1]) # vertical
                #print '\t\tlength of sides', len1, 'vs', length_point2
                return (len1 == length_point2, len1)
            except:
                #print intersect, 'and', point1, 'are NOT perpendicular with', point2
                return (False, -1)


    except ZeroDivisionError:
        # EXPECT: the line intersect->point1 is vertical
        # Thus, we need the slope for (intersect, point2) to be zero. 
        try:
            slope2 = find_slope(intersect, point2, indent=True)
            if slope2 != 0:
                raise RuntimeError('expected to be zero')
        except:
            #print intersect, 'and', point1, 'are NOT perpendicular with', point2
            return (False, -3)

        #print '\tCANDIDATE:', intersect, 'and', point1, 'ARE perpendicular with', point2
        length_point1 = abs(intersect[1] - point1[1]) # vertical
        length_point2 = abs(intersect[0] - point2[0]) # horizontal
        #print '\t\tlength of sides', length_point1, 'vs', length_point2
        return (length_point1 == length_point2, length_point1)

def find_slope(point1, point2, indent=False):
    """
    changeinY divided by changeinX

    If we get a ZeroDivisionError, means line is vertical.
    If slope is zero, it is a horintal line.

    :raises ZeroDivisionError: 
    """
    #if indent:
    #    print '\tfind_slope', point1, point2
    #else:
    #    print 'find_slope', point1, point2

    numerator = decimal.Decimal(point1[0] - point2[0])
    if numerator == decimal.Decimal('0'):
        raise ZeroDivisionError('zero division')

    return decimal.Decimal(point1[1] - point2[1]) / numerator

def search_square(intersect, atuple, points, leftover):
    """
    :param intersect: a point e.g. (1,5)
    :param atuple: index into `points` e.g. (0, 3)
    :param points: a dict
    :param leftover: a set of index of length one e.g. [2]
    """
    pos_1 = points[atuple[0]]
    pos_2 = points[atuple[1]]
    ch1 = is_perpendicular_at(intersect, pos_1, pos_2)
    if ch1[0]:
        pos_3 = points[leftover.pop()]
        if pos_3 == intersect:
            return False, 'dup'

        ch2 = is_perpendicular_at(pos_3, pos_1, pos_2)
        if ch2[0]:
            if ch1[1] == ch2[1]:
                return True, 'Found a square with len = ' + str(ch2[1])

        return False, 'nothing to see'
    else:
        return False, 'no hope. Bail'

def issquare(line):
    """
    :param: line
        e.g. (1,6), (6,7), (2,7), (9,1)
    """
    retval = False
    inp = [eval(k) for k in line.strip().split(', ')]

    A, B, C, D = range(4) 
    names = [A, B, C, D]

    # Keys - A, B, C, D. Values - 2D coords
    points = dict(zip(names, inp)) 

    set_names = set(names)

    should_continue = True
    for b in set_names:
        if not should_continue:
            break
        pos_b = points[b] # e.g. (1,6)   
        temp_names = set_names - set([b])
        pairs = list(combinations(set_names - set([b]), 2))
        for t in pairs:
            h = temp_names - set([j for j in t])
            found, msg = search_square(pos_b, t, points, h)
            if found:
                retval = True
                should_continue = False
                break

    return retval

__all__ = ['issquare']
