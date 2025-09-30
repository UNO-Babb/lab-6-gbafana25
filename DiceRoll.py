#DiceRoll.py
#Name: Gareth Moodley
#Date: 9-30-25
#Assignment: Dice Roll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(len(rolls)):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    #find the sum total of the two dice
    sum = dice1 + dice2
    rolls[r] = sum
  
  #print statictics for dice rolls
  roll_stats = {}
  for r in rolls:
    if r in roll_stats.keys():
      roll_stats[r] += 1
    else:
      roll_stats[r] = 1
  for k in roll_stats.keys():
    print(str(k)+": Count = "+str(roll_stats[k])+", Percent: "+str(round((roll_stats[k]/len(rolls))*100))+"%")

if __name__ == '__main__':
  main()
