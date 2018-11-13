# -*- coding: utf-8 -*-
# !/usr/bin/python

import pymongo

conn = pymongo.MongoClient("127.0.0.1", 27017)
db = conn.test
test = db.test
def get(json):
  return test.find(json)


def getAll():
  return test.find()


def set(json):
  test.insert(json)

def upd():
  print()

def main():
  # set({"aa":"aasdf","bb":"12341234"})
  # for arr in getAll():
  for arr in get({"aa":"aasdf"}):
    print(arr)


if __name__ == '__main__':
  main()