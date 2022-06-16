# -*- coding: utf-8 -*-
height = 1.75
weight = 80.5
bmi = weight/(height * height)

if bmi < 18.5:
  print('too light')
elif bmi>=18.5 and bmi <25:
  print("normal")
elif bmi>=25 and bmi<28:
  print("too high")
elif bmi>=28 and bmi<32:
  print("fat")
else:
  print("very fat")