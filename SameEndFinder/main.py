#-*-coding:utf8;-*-
#qpy:3
#qpy:console

import sameendfinder
def main():
 while True:
  print("\n\nEnter 'q' to quit")
  str = input("Enter your input:")
  if 'q'==str:
   break
  print(sameendfinder.sameEnds(str))
if __name__=='__main__':
 main()