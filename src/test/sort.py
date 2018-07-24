# -*- coding: utf-8 -*-
# !/usr/bin/python


def bubble_sort(list):
  for i in range(0, len(list)):
    for j in range(i, len(list) - 1):
      if list[i] > list[j + 1]:
        k = list[i]
        list[i] = list[j + 1]
        list[j + 1] = k
  print('bubble', list)


def direct_sort(list):
  for i in range(0, len(list)):
    for j in range(0, i):
      if list[i] < list[j]:
        list.insert(j, list[i])
        list.pop(i + 1)
        print(list)
        break
  print('direct', list)


def selection_sort(list):
  for i in range(0, len(list) - 1):
    num = i
    for j in range(i + 1, len(list)):
      if (list[num] > list[j]):
        num = j
    k = list[num]
    list[num] = list[i]
    list[i] = k
  print('simple', list)


def shell_sort(list):
  gap = int(len(list) / 2)
  while gap > 0:
    for g in range(0, gap):
      for i in range(0, len(list), gap):
        for j in range(0 + g, i + g, gap):
          if (list[i + g] < list[j + g]):
            list.insert(j + g, list[i + g])
            list.pop(i + g + 1)
            print(list)
            break;
    gap = int(gap / 2)
    print('gap', gap, list)


if __name__ == "__main__":
  list = [21, 1, 7, 5, 4, 11, 9, 12, 13, 56, 23, 14, 10, 3, 4, 2, 1, 5, 6, 3]
  print(list)
  # bubble_sort(list)
  # direct_sort(list)
  # selection_sort(list)
  shell_sort(list)
