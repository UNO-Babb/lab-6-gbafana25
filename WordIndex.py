#WordIndex.py
#Name:
#Date:
#Assignment:

def main():
  textFile = open("fish.txt", 'r')
  
  words = {} #create an empty dictionary
  
  
  #print ("fish" in words) #is a word already in the dictionary?
  #words["fish"] = [2]     #add a list to the dictionary
  #print ("fish" in words) #is the word there now?
  #words["fish"].append(5) #add to an existing list
  #print(words)
  linenum = 1
  for line in textFile:
    for w in line.replace("\n", "").split(" "):
      if w not in words:
        words[w] = [linenum]
      else:
        if linenum not in words[w]:
          words[w].append(linenum)
    linenum += 1

  print(words)


if __name__ == '__main__':
  main()
