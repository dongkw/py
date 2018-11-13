# -*- coding: utf-8 -*-
# !/usr/bin/python


ss="A8 E3 E7 71 33 58 37 3A 71 6E 31 81 21 B8 5B E7 31 EB 50 18 61 B6 DC 9B E0 9E 69 53 5B C2 EA AD 98 3A A6 1B 79 93 FB 35 4F BA 49 A8 11 8D 4D D0 80 5E D3 39 0A 99 76 C4 12 BE 6D 78 64 28 62 6C 72 86 59 8B 27 5B 80 3F F6 88 BE EC 39 90 A0 90 18 DD B7 02 A1 61 C6 0B A4 D9 53 81 49 5B 6E 5D 7A 88 21 82 98 7D 6D 2E AC 72 EE BD 27 3A 69 93 21 3A 4F FA 61 07 80 78 C4 F5 33 05 FC B1 45 5C 4C 10 06 28 2E 6E 99 A6 3B 55 13 B7 62 65 12 BE 8D F1 06 A3 10 D0 D6 54 4F AB 8E 8E 01 EA 59 FD AC BD EF 03 12 31 CD 02 49 82 27 3E 6B 54 38 3F D4 69 C7 79 E4 07 E8 4B 79 A5 4C FA 1D B4 F3 2A 48 84 F8 D0 41 09 FA A5 EF 0B 94 C5 5A B1 0D 0D 53 0B 8F DB 26 46 40 85 59 00 FB 3B C5 57 F8 45 8C C7 FA 77 B4 55 DA B4 11 7F 6C 4F 87 24 4A 35 84 C9 34 8D 7B F0 3F 1C CD EE 16 78 F2 CF A6 2B"


def GetCmd(hexString):
  hexString = hexString.replace(" ", "");
  if ((len(hexString)  % 2) != 0):
    hexString += " ";
  bits = ""
  for x in range(0, len(hexString), 2):
    bits += chr(int(hexString[x:x+2], 16))
  return bits;


print(GetCmd(ss))