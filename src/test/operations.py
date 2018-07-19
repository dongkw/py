# -*- coding: utf-8 -*-
# !/usr/bin/python

#1000-10000拼数游戏 拼写中缀式 中缀式转后缀式 后缀式计算

operator = ["*", "/", "+", "-", ""]


def back(num):
  return str(num)[::-1]


class Stack:
  def __init__(self):
    self.stack = []

  def push(self, obj):
    self.stack.append(obj)

  def isEmpty(self):
    return self.size() == 0

  def peek(self):
    if not self.isEmpty():
      return self.stack[-1]

  def pop(self):
    if not self.isEmpty():
      return self.stack.pop()

  def size(self):
    return len(self.stack)


def compare(peek, cur):
  if ("*" == peek or "/" == peek) and (cur in operator):
    return True
  elif ("+" == peek or "-" == peek) and ("+" == cur or "-" == cur):
    return True
  else:
    return False


def to_post_order(list):
  result = []
  stack = Stack()
  for s in range(0, len(list)):
    if is_num(list[s]):
      result.append(list[s])
    else:
      if list[s] == "(":
        stack.push(list[s])
      elif list[s] == ")":
        while (not stack.peek() == "("):
          result.append(stack.pop())
        stack.pop()
      else:
        while (not stack.isEmpty() and compare(stack.peek(), list[s])):
          result.append(stack.pop())
        stack.push(list[s])
  while not stack.isEmpty():
    result.append(stack.pop())
  return result


def calutate(result):
  stack = Stack()
  for n in result:
    if is_num(n):
      stack.push(int(n))
    else:
      front = int(stack.pop())
      back = int(stack.pop())
      res = 0
      if (n == "+"):
        res = back + front
      elif (n == "-"):
        res = back - front
      elif (n == "*"):
        res = back * front
      elif (n == "/"):
        res = back / front
      stack.push(res)
  return stack.pop()


def is_num(num):
  try:
    float(num)
    return True
  except:
    return False


def to_list(str):
  list = []
  num = ""
  for i in range(0, len(str)):
    if is_num(str[i]):
      num = num + str[i]
    else:
      if num != "":
        list.append(num)
      list.append(str[i])
      num = ""
  if (num != ""):
    list.append(num)
  return list


def main():
  for num in range(1000, 10000):
    num = str(num)
    for m in range(0, len(operator)):
      for k in range(0, len(operator)):
        for o in range(0, len(operator)):
          str1 = num[0] + operator[m] + num[1] + operator[k] + num[2] + \
                 operator[
                   o] + num[3]
          try:
            if (len(str1) > 4):
              #直接用语言自带函数
              # result = eval(str1)

              list = to_list(str1)
              list_post_order = to_post_order(list)
              result = calutate(list_post_order)
              if str(result) == back(num):
                print(str1, result)
          except:
            r = 1


if __name__ == '__main__':
  main()
  # list = to_list("12+(23*3-56+7)*(2+90)/2")
  # print(list)
  # list_post_order = to_post_order(list)
  # print(list_post_order)
  # result = calutate(list_post_order)
  # print(result)