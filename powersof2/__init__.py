def powersof2(n):
  """
  >>> powersof2(0)
  False
  >>> powersof2(-1)
  False
  >>> powersof2(1)
  True
  >>> powersof2(2)
  True
  >>> powersof2(3)
  False
  >>> powersof2(4)
  True
  """
  if n <= 0:
    return False
  else:
    return (n & -n) == n
