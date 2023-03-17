import random

# Menu

print("Witaj w grze Zombe")
print("1  Rozpocznij")
print("2   Credits")
print("3    Wyjdź z gry")
print("Wersja gry -> Alpha 0.1")

odczyt = input("Wybierz opcje -> ")

# Opcje menu gry
#
# Rozpoczęcie gry
if odczyt == "1":
  print("Wybrana opcja -> Rozpocznij")
  print("Wkrótce...")
  # Gra
  #
  # Hp zombie
  hp_gracza = 100
  hp_zombie=random.randint(120,150)
  while True:
    print("Twoje HP:",hp_gracza,"<-> HP Przeciwnika:",hp_zombie)
    print("1  Zaatakuj przeciwnika")
    print("2   Ucieknij")
    wybor_akcji=input("Wybierz opcję -> ")
    if wybor_akcji == "1":
      dmg=random.randint(25,60)
      dmg=random.randint(10,25)
    elif wybor_akcji == "2":
      szansa_ucieczki=random.randint(0,1)
      if szansa_ucieczki == "1":
        print("Gratulacje! Udało ci się uciec.")
      elif szansa_ucieczki == "0":
        print("Nie udało ci się uciec. Zombie zadał ci obrażenia.")
# Credits
elif odczyt == "2":
  print("Wybrana opcja -> Credits")
  print("Game by \/")
  print("Knifej")
# Wyjście z gry
elif odczyt == "3":
  print("Wybrana opcja -> Wyjdź z gry")
  print("Wyszedłeś z gry.")
# Jeśli liczba jest inna niż 1, 2, 3
else:
  print("Podałeś nie poprawną liczbę spróbuj ponownie.")
