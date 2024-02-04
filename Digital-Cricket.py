import random
import sys

r1, r2, r3, r4, r5 = 0, 0, 0, 0, 0  # random functions variables
l1, l2, l3, l4, l5, l6, l7, l8 = 0, 0, 0, 0, 0, 0, 0, 0  # tie variables
s1, s2, s3, s4, s5, s6, s7, s8 = 0, 0, 0, 0, 0, 0, 0, 0  # match1 variables
t1, t2, t3, t4, t5, t6, t7, t8 = 0, 0, 0, 0, 0, 0, 0, 0  # match2 variables

print("\n")
print("*** Welcome to the Digital Cricket World ***")
print("\n")


def random_num():
  return random.randint(0, 10)


def comp_HorT():
  r2 = random.randint(0, 2)
  if r2 == 0:
    print("Computer Choose Batting")
  elif r2 == 1:
    print("Computer Choose Bowling")


def coin_comp():
  r1 = random.randint(0, 2)
  if r1 == 0:
    print("Coin tossed by Computer and Head camed")
  elif r1 == 1:
    print("Coin tossed by Computer and Tail camed")


def match_tie():
  i = 1

  while i < 7:
    l3 = int(input("Enter your number : "))
    if 0 <= l3 < 11:
      pass
    else:
      print("Please enter a proper number between (0 to 10)")
      sys.exit(0)

    print("Computer turn to Bat ...")
    l1 = random_num()
    print("Computer Hitted : ", l1)

    l2 = l2 + l1

    if l3 != l1:
      print("Computer Total Score : ", l2)
      print("\n")
      i += 1
    elif l3 == l1:
      l4 = l2 - l1 + 1
      print("\n")
      print("Computer got Out by Score : ", l4 - 1)
      print("Your Target Score : ", l4)
      print("\n")
      print("Now, Its Your turn to Bat ...")
      print("\n")
      break
    else:
      sys.exit(0)

  while i < 7:

    l8 = int(input("Enter your number : "))
    if 0 <= l8 < 11:
      pass
    else:
      print("Please enter a proper number between (0 to 10)")
      sys.exit(0)

    l6 = l6 + l8

    l5 = random_num()
    print("Computer Hitted : ", l5)

    if l6 > l4 or l6 == l4:
      print("Your Total Score : ", l6)
      print("\n")
      print("*** You Won the Match ***")
      sys.exit(0)
    elif l5 != l8:
      print("Your Total Score : ", l6)
      print("\n")
      i += 1
    elif l5 == l8:
      l7 = l6 - l8 + 1
      if l6 > l4:
        print("Your Total Score : ", l7)
        print("\n")
        print("*** You Won the Match ***")
        sys.exit(0)
      elif l6 < l4:
        print("Your Total Score : ", l7 - 1)
        print("\n")
        print("*** Computer Won the Match ***")
        sys.exit(0)
      elif l6 == l4:
        print("Your Total Score : ", l7 - 1)
        print("\n")
        print("*** Its Tie ***")
        print("\n")
        match_tie()
    else:
      sys.exit()


def match_coin():
  print("Its time for Coin tossing ...")
  r4 = int(input("Choose Head[0] or Tail[1] : "))

  if r4 == 0:
    print("You Choose Head")
    print("\n")
  elif r4 == 1:
    print("You Choose Tail")
    print("\n")
  else:
    print("Enter Proper Head or Tail")
    print("\n")
    sys.exit()

  coin_comp()

  if r4 == r1:
    print("You Won the Toss")
    print("\n")
    r5 = int(input("Choose Batting[0] or Bowling[1] : "))
    if r5 == 0:
      print("You Choose Batting")
      print("\n")
      match1()
    elif r5 == 1:
      print("You Choose Bowling")
      print("\n")
      match2()
    else:
      print("Enter Proper Number")
      print("\n")
      sys.exit()

  elif r4 != r1:
    print("You Loose the Toss")
    print("\n")
    r2 = int(random.randint(0, 2))
    if r2 == 0:
      print("Computer Choose Batting")
      print("\n")
      match2()
    elif r2 == 1:
      print("Computer Choose Bowling")
      print("\n")
      match1()


# Matches Start from here ................


def match1():
  print("Your Turn to Bat ...")
  n = 1
  i = 0

  s2 = 0
  while i < n:
    s1 = int(input("Enter your number : "))
    if 0 <= s1 < 11:
      pass
    else:
      print("Please enter a proper number between (0 to 10)")
      sys.exit(1)

    s2 = s1 + s2

    s3 = random_num()
    print("Computer Hitted : ", s3)

    if s3 != s1:
      print("Your Total Score : ", s2)
      print("\n")
      n += 1
    elif s3 == s1:
      s7 = s2 - s1 + 1
      print("\n")
      print("You Got Out by Score : ", s7 - 1)
      print("Computer Target Score : ", s7)
      print("\n")
      print("Now, Its Computer turn to Bat...")
      print("\n")
      break
    else:
      sys.exit(1)

  while i < n:

    s4 = int(input("Enter your number : "))
    if 0 <= s4 < 11:
      pass
    else:
      print("Please enter a proper number between (0 to 10)")
      sys.exit(1)

    s5 = random_num()
    print("Computer Hitted : ", s5)
    s6 = s6 + s5

    if s6 > s7 or s6 == :
      print("Computer Total Score : ", s6)
      print("\n")
      print("*** Computer Won the Match ***")
      sys.exit(1)
    elif s5 != s4:
      print("Computer Total Score : ", s6)
      print("\n")
      n += 1
    elif s5 == s4:
      s8 = s6 - s5 + 1
      if s6 > s7:
        print("Computer Total Score : ", s8)
        print("\n")
        print("*** Computer Won the Match ***")
        sys.exit(1)
      elif s6 < s7:
        print("Computer Total Score : ", s8 - 1)
        print("\n")
        print("*** You Won the Match ***")
        sys.exit(1)
      elif s6 == s7:
        print("Computer Total Score : ", s8 - 1)
        print("\n")
        print("*** Its Tie ***")
        match_tie()
    else:
      sys.exit(1)


def match2():
  print("Computer Turn to Bat ...")
  n = 1
  i = 0

  t2 = 0
  while i < n:
    t1 = int(input("Enter your number : "))
    if 0 <= t1 < 11:
      pass
    else:
      print("Please enter a proper number between (0 to 10)")
      sys.exit(2)

    t3 = random_num()
    print("Computer Hitted : ", t3)

    t2 = t2 + t3

    if t3 != t1:
      print("Computer Total Score : ", t2)
      print("\n")
      n += 1
    elif t3 == t1:
      t4 = t2 - t3 + 1
      print("\n")
      print("Computer Got Out by Score : ", t4 - 1)
      print("Your Target Score : ", t4)
      print("\n")
      print("Now, Its Your turn to Bat...")
      print("\n")
      break
    else:
      sys.exit(2)

  t6 = 0
  while i < n:
    t5 = int(input("Enter your number : "))
    if 0 <= t5 < 11:
      pass
    else:
      print("Please enter a proper number between (0 to 10)")
      sys.exit(2)

    t6 = t6 + t5

    t7 = random_num()
    print("Computer Hitted : ", t7)

    if t6 > t4 or t6 == t4:
      print("Your Total Score : ", t6)
      print("\n")
      print("*** You Won the Match ***")
      sys.exit(2)
    elif t5 != t7:
      print("Your Total Score : ", t6)
      print("\n")
      n += 1
    elif t5 == t7:
      t8 = t6 - t5 + 1
      if t6 > t4:
        print("Your Total Score : ", t8)
        print("\n")
        print("*** You Won the Match ***")
        sys.exit(2)
      elif t6 < t4:
        print("Your Total Score : ", t8 - 1)
        print("\n")
        print("*** Computer Won the Match ***")
        sys.exit(2)
      elif t6 == t4:
        print("Your Total Score : ", t8)
        print("\n")
        print("*** Its Tie ***")
        print("\n")
        match_tie()
    else:
      sys.exit(2)


match_coin()
