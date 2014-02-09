"""
TODO use a generator yield for a 2nd solution
"""

__author__ = 'Gavin Bong'

def permute(astring):
    #import pdb; pdb.set_trace()
    if len(astring) == 1:
        return [astring]

    ch = astring[0] 
    rest = astring[1:]
    res = []
    permutations = permute(rest)
    # insert ch in every position of the other permutations
    for aperm in permutations:
	aperm = aperm + '_' #fake sentinel character in the last pos.
        for i, v in enumerate(aperm):
            if i == 0:
                res.append(ch + aperm[:-1])
            elif i == len(aperm):
                res.append(aperm[:-1] + ch)
	    else:
                res.append(aperm[:i] + ch + aperm[i:-1])

    return res

__all__ = ['permute']
