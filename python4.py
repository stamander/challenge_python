from random import randint

def get_anser():
  while True:
    ans = input("High(H) or Low(L)>")
    if ans.upper() == "H" or ans.upper()== "L":
      break
  return ans.upper()


def main():
  player_count = 0
  computer_count = 0

  while player_count < 5 and computer_count <5:
    player_number = randint(1,13)
    print("Your number:{}".format(player_number))
    computer_number = randint(1,13)
    print("Computer number:?")
    anser = get_anser()
    balance = computer_number - player_number
    if balance == 0:
      print("even")
