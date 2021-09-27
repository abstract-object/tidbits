print ('This is the radix translator. You can convert any number from one integer base to another, if the base is between 2 and 36. The number to be translated must be positive. Please use "." when entering nonintegers.')
 
def getbase(option):
  validinput = False
  while not validinput:
    try:
      if int(option) < 2 or int(option) > 36:
        option = raw_input("Please enter an integer between 2 and 36: ")
      elif int(option) >= 2 and int(option) <= 36:
        validinput = True
    except:
      option = raw_input("Please enter an integer between 2 and 36: ")
  return option
 
def getnumber(option, base, digits):
  validinput = False
  while not validinput:
    option = option.upper()
    x = 0
    point = 0
    while len(option) < 1:
      option = raw_input("Please enter a number in base " + str(base) + ": ")
      option = option.upper()
    while x < len(option):
      validdigit = False
      for y in range (0, int(base)):
        if option[x] == digits[y]:
          validdigit = True
          break
        elif option[x] == "." and x != 0 and x != len(option) - 1:
          point += 1
          if point < 2:
            validdigit = True
            break
      if validdigit:
        x += 1
      else:
        option = raw_input("Please enter a number in base " + str(base) + ": ")
        break
    if validdigit:
      validinput = True
  return option

def separate(number):
  x = 0
  whole = ""
  nonwhole = ""
  while x < len(number):
    if number[x] != ".":
      whole += number[x]
    else:
      x += 1
      while x < len(number):
        nonwhole += number[x]
        x += 1
    x += 1
  return whole, nonwhole
 
def todecimal(number, base, iswhole, digits):
  if iswhole:
    x = len(number) - 1
    p = 0
  else:
    x = 0
    p = -1
  result = 0
  while x >= 0 and x < len(number):
    y = number[x]
    z = 0
    while z < len(digits):
      if y == digits[z]:
        y = z
      z += 1
    result += y * int(base) ** p
    if iswhole:
      p += 1
      x -= 1
    else:
      p -= 1
      x += 1
  return result
 
def fromdecimal(number, base, iswhole, digits):
  result = ""
  if iswhole:
    value = int(number)
    if value == 0:
      result += "0"
    while value != 0:
      remainder = value % int(base)
      value = int(value / int(base))
      z = 0
      while z < len(digits):
        if remainder == z:
          result = digits[z] + result
        z += 1
  else:
    value = float("0." + number)
    while value != 0:
      result += digits[int(float(value * int(base)))]
      value = value * int(base) - int(float(value * int(base)))
  return result
 
d = [str(i) for i in range(0, 10)]
d.extend([chr(i) for i in range(ord("A"), ord("Z") + 1)])

startbase = raw_input("Enter the base from which to translate: ")
startbase = getbase(startbase)
endbase = raw_input("Enter the base to which you wish to translate: ")
endbase = getbase(endbase)
startnum = raw_input("Enter the number in base " + startbase + " to translate: ")
startnum = getnumber(startnum, startbase, d)

wholepart, nonwholepart = separate(startnum)
decvalue = todecimal(wholepart, startbase, True, d)
if len(nonwholepart) > 0:
  decvalue = float(decvalue) + todecimal(nonwholepart, startbase, False, d)

wholepart, nonwholepart = separate(str(decvalue))
finalvalue = fromdecimal(wholepart, endbase, True, d)
if len(nonwholepart) > 0:
  finalvalue += "." + fromdecimal(nonwholepart, endbase, False, d)
 
print(startnum + ", converted from base " + startbase + " to base " + endbase + " is " + finalvalue + ".")