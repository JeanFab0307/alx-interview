#!/usr/bin/python3
""" prime game with the functions searchPrimes and isWinner"""


def searchPrime(n):
  """return a list of prime numbers from 0 to n
  n: the biggest number"""
  num = 2
  prime = [True for i in range(n+1)]
  primeList = []
  
  while (num * num < n):
    if prime[num] is True:
      for i in range (num + num, n+1, num):
        prime[i] = False
    num += 1

  for i in range(2, n+1):
    if prime[i] is True:
      primeList.append(i)

  return primeList

def isWinner(x, nums):
  """Determine the winner of the prime game
  x: the number of rounds played
  nums: a list of the numbers they will play with
  
  there are 2 players: Maria and Ben, Maria begins the game"""
  Maria = 0
  Ben = 0
  for i in range(x):
    # The winner is determined by the number of prime numbers
    # if the count is impair Ben will win else Maria will win
    numberCount = len(searchPrime(nums[i]))
    print(numberCount)
    if numberCount % 2 == 0:
      Ben += 1
    else:
      Maria +=1
    if Ben > x/2:
      return "Ben"
    elif Maria > x/2:
      return "Maria"
  
  return None
