"""Grading app"""
n_students = int(input("How many num of student: "))

i = 0

from func import *
while i < n_students:
  name = input("Names: ")
  score = float(input("Score? "))

  scores(score)
  i += 1