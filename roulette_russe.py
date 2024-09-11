import random
import os

class Player:
    def __init__(self):
        self.pv = 4
        self.items = [] # Bière / Cigarette / Couteau / Menotte / Miroir
        self.name = ""
        self.is_menoted = [False, 0]

class Game:
    def __init__(self):
        self.player_1 = Player()
        self.player_1.name = input("Comment veux-tu t'appeller joueur n°1 ?\n")
        self.player_2 = Player()
        self.player_2.name = input("Comment veux-tu t'appeller joueur n°2 ?\n")
        pv = random.randint(3, 6)
        self.player_1.pv = pv
        self.player_2.pv = pv
        self.canon_sciee = False
        self.player_turn = 1

    def set_up_phase(self):
        self.nbr_balls = random.randint(2, 8)
        self.canon_chamber = []
        for ball in range(self.nbr_balls):
            ball = random.randint(1, 2) == 1
            self.canon_chamber.append(ball)
        if not True in self.canon_chamber:
            self.canon_chamber[random.randint(0, self.nbr_balls)] = True
        elif not False in self.canon_chamber:
            self.canon_chamber[random.randint(0, self.nbr_balls)] = False
        nbr_true = 0
        for ball in self.canon_chamber:
            if ball is True:
                nbr_true += 1
        print(f"\nRechargement...\n{'💣'*nbr_true}{'💨'*(len(self.canon_chamber)-nbr_true)}\n")
        player_1_new_items = [random.choice(["Bière", "Cigarette", "Couteau", "Menotte", "Miroir"]), random.choice(["Bière", "Cigarette", "Couteau", "Menotte", "Miroir"])]
        player_2_new_items = [random.choice(["Bière", "Cigarette", "Couteau", "Menotte", "Miroir"]), random.choice(["Bière", "Cigarette", "Couteau", "Menotte", "Miroir"])]
        self.player_1.items.append(player_1_new_items[0])
        self.player_1.items.append(player_1_new_items[1])
        self.player_2.items.append(player_2_new_items[0])
        self.player_2.items.append(player_2_new_items[1])
        print(f"{self.player_1.name} a reçu les objets suivants :\n- {player_1_new_items[0]}\n- {player_1_new_items[1]}\n")
        print(f"{self.player_2.name} a reçu les objets suivants :\n- {player_2_new_items[0]}\n- {player_2_new_items[1]}\n")

    def phase(self):
        self.set_up_phase()
        while len(self.canon_chamber) > 0:
            if self.player_1.pv <= 0:
                print(f"PARTIE TERMINEE : {self.player_2.name} REMPORTE LA PARTIE")
                return
            elif self.player_2.pv <= 0:
                print(f"PARTIE TERMINEE : {self.player_1.name} REMPORTE LA PARTIE")
                return
            if self.player_turn == 1:
                if self.player_2.is_menoted == [True, 0]:
                    self.player_2.is_menoted = [True, 1]
                elif self.player_2.is_menoted == [True, 1]:
                    self.player_2.is_menoted = [False, 0]
                    print(f"{self.player_2.name} casse enfin ses menottes et se libére\n")
                if self.player_1.is_menoted == [True, 0]:
                    self.player_1.is_menoted = [True, 1]
                    self.player_turn = 2
                    print(f"{self.player_1.name} à toujours ses menottes, il saute son tour !\n")
                    self.tour(self.player_2, self.player_1)
                elif self.player_1.is_menoted == [True, 1]:
                    self.player_1.is_menoted = [False, 0]
                    print(f"{self.player_1.name} casse enfin ses menottes et se libére juste à temps pour son tour\n")
                    self.tour(self.player_1, self.player_2)
                else:
                    self.tour(self.player_1, self.player_2)
            elif self.player_turn == 2:
                if self.player_1.is_menoted == [True, 0]:
                    self.player_1.is_menoted = [True, 1]
                elif self.player_1.is_menoted == [True, 1]:
                    self.player_1.is_menoted = [False, 0]
                    print(f"{self.player_1.name} casse enfin ses menottes et se libére\n")
                if self.player_2.is_menoted == [True, 0]:
                    self.player_2.is_menoted = [True, 1]
                    self.player_turn = 1
                    print(f"{self.player_2.name} à toujours ses menottes, il saute son tour !\n")
                    self.tour(self.player_1, self.player_2)
                elif self.player_2.is_menoted == [True, 1]:
                    self.player_2.is_menoted = [False, 0]
                    print(f"{self.player_2.name} casse enfin ses menottes et se libére juste à temps pour son tour\n")
                    self.tour(self.player_2, self.player_1)
                else:
                    self.tour(self.player_2, self.player_1)
        self.phase()

    def tour(self, player, opponent):
        choice = input(f"Le joueur {self.player_1.name} a encore {self.player_1.pv} PV\nLe joueur {self.player_2.name} a encore {self.player_2.pv} PV\n{player.name}, choisissez une action :\n- Tirer sur l'adversaire [1]\n- Tirer sur soi [2]\n- Utiliser un item [3]\n") if player.items else input(f"{player.name}, choisissez une action :\n- Tirer sur l'adversaire [1]\n- Tirer sur soi [2]\n")
        os.system('cls')
        if choice == "1":
            if self.canon_chamber[-1] is True:
                print("C'est une vraie cartouche 💀")
                if self.canon_sciee is True:
                    opponent.pv -= 2
                    self.canon_sciee = False
                else:
                    opponent.pv -= 1
            else:
                print("C'est une balle à blanc...")
            self.player_turn = 1 if self.player_turn == 2 else 2
            self.canon_chamber.pop()
        elif choice == "2":
            if self.canon_chamber[-1] is True:
                print("C'est une vraie cartouche 💀")
                if self.canon_sciee is True:
                    player.pv -= 2
                    self.canon_sciee = False
                else:
                    player.pv -= 1
                self.player_turn = 1 if self.player_turn == 2 else 2
            else:
                print("C'est une balle à blanc...\nREJOUEZ")
            self.canon_chamber.pop()
        elif choice == "3" and player.items:
            self.show_items(player, opponent)
        else:
            self.tour(player, opponent)
            
    def show_items(self, player, opponent):
        all_items = ""
        for i in range(len(player.items)):
            all_items += f"- Utiliser l'item {player.items[i]} [{i+1}]\n"
        choice = input(f"Quel objet voulez-vous utiliser ?\n{all_items}- Quitter le menu [N'importe quelle autre touche]\n")
        try:
            if int(choice) <= len(player.items) + 1 and int(choice) > 0:
                os.system('cls')
                self.use_item(player, opponent, int(choice)-1)
        except:
            pass
        self.tour(player, opponent)
    
    def use_item(self, player, opponent, item_index):
        if player.items[item_index] == "Bière":
            ball = self.canon_chamber.pop()
            print("Glouglouglou...\nVous avez enlevé une vraie cartouche 💣") if ball is True else print("Glouglouglou...\nVous avez enlevé une balle à blanc 💨")
        elif player.items[item_index] == "Cigarette":
            player.pv = player.pv + 1 if player.pv < 4 else player.pv
            print("Hffffff... Vous tirez une taffe et vous soignez 1 pv")
        elif player.items[item_index] == "Couteau":
            self.canon_sciee = True
            print("Tchak tchak tchak... Le canon de fusil a été scié")
        elif player.items[item_index] == "Menotte":
            if opponent.is_menoted[0]:
                print(f"{opponent.name} est déjà menotté, vous ne pouvez pas lui mettre deux paires de menottes à la fois")
            else:
                opponent.is_menoted = [True, 0]
                print(f"Clic clac, vous passez les menottes à {opponent.name} qui va sauter son prochain tour")
        elif player.items[item_index] == "Miroir":
            print(f"Hmmm intéressant, la prochaine cartouche est vraie 💣") if self.canon_chamber[-1] is True else print(f"Hmmm intéressant, la prochaine balle est à blanc 💨")
        player.items.pop(item_index)

if __name__ == "__main__":
    jeu = Game()
    jeu.phase()