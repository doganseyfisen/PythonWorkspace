print("Player Registering Program")
name = input("Please enter player's name: ")
surname = input("Please enter player's surname: ")
team = input("Please enter player's team: ")
infos = [name,surname,team]
print("Infos saving...")
print("Player's name: {}\nPlayer's surname: {}\n"
      "Player's team: {}".format(infos[0],infos[1],infos[2]))
print("Player's infos are succesfully saved.")
