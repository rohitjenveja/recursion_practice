#!/usr/bin/python

def quicksort(elements):
  if len(elements) <=1:
    return elements
  else:
    less, equal, greater = [], [], []
    for i in xrange(0, len(elements)):
      if elements[i] < elements[0]:
        less.append(elements[i])
      elif elements[i] > elements[0]:
        greater.append(elements[i])
      else:
        equal.append(elements[i])
    return quicksort(less) + equal + quicksort(greater)

if __name__ == "__main__":
  print quicksort([5,3,4,5])
