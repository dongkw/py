# -*- coding: utf-8 -*-
# !/usr/bin/python


# 比10大的最小回文数 2进制 8进制 10进制
def back(num):
  return num[::-1]


num = 10;
while 1:
  num_str = str(num)
  num_2 = bin(num)[2:]
  num_8 = oct(num)[2:]
  if num_str == back(num_str) and num_2 == back(num_2) and num_8 == back(num_8):
    print(num_str)
    break
  num = num + 1
