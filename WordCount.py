#WordCount.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  lines = 0
  wc = 0
  chrs = 0
  for line in textFile:
    lines += 1
    wc += len(line.split(" "))
    chrs += len(line)

  print("Lines: "+str(lines))
  print("Words: "+str(wc))
  print("Characters: "+str(chrs))

if __name__ == '__main__':
  main()
