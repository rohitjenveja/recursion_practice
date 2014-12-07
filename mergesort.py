#!/usr/bin/python

def merge_sort(elements):
  if len(elements) <= 1:
    return elements

  else:
    mid = len(elements)/2
    left = merge_sort(elements[:mid])
    right = merge_sort(elements[mid:])
    return merge(left, right)


def merge(left, right):
  x=[]
  while len(left) and len(right):
    if left[0] < right[0]:
      x.append(left[0])
      left.pop(0)
    else:
      x.append(right[0])
      right.pop(0)
  if left:
   x.extend(left)
  if right:
   x.extend(right)
  return x

if __name__ == '__main__':
  print merge_sort([3,2,5])
