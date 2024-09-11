import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import threading
from icecream import ic

class Player:
    def __init__(self):
        self.max_pv = 4
        self.pv = 4
        self.items = [] # Bière / Cigarette / Couteau / Menotte / Miroir
        self.name = ""
        self.is_menoted = [False, 0]

class Game:
    def __init__(self):
        self.player_1 = Player()
        self.player_2 = Player()
        self.canon_sciee = False
        self.player_turn = 1
        self.using_item = False
        self.actual_player = self.player_1
        self.actual_opponent = self.player_2
        threading_start = threading.Thread(target=self.show_ui)
        threading_start.start()

    def start(self):
        if self.nom_joueur_1_entry.get().strip() and self.nom_joueur_2_entry.get().strip() and int(self.pv_range_1_entry.get().isdigit()) and int(self.pv_range_2_entry.get().isdigit()):
            self.player_1.name = self.nom_joueur_1_entry.get()
            self.player_2.name = self.nom_joueur_2_entry.get()
            pv = random.randint(int(min(self.pv_range_1_entry.get(), self.pv_range_2_entry.get())), int(max(self.pv_range_1_entry.get(), self.pv_range_2_entry.get())))
            self.player_1.pv, self.player_1.max_pv, self.player_2.pv, self.player_2.max_pv = pv, pv, pv, pv
            self.settings_frame.destroy()
            self.settings_frame_2.destroy()
            self.enter_infos_button.destroy()
            
            self.rechargement_infos_label = Label(self.frame)
            self.rechargement_infos_label.grid(row=0, column=0, columnspan=2)

            self.info_action_label = Label(self.frame)
            self.info_action_label.grid(row=1, column=0, columnspan=2)
            if not self.hide_pv_checkbutton_var.get():
                self.info_action_label.config(text=f"Vous avez {self.player_1.pv} PV chacun.")

            self.menottes_info_label = Label(self.frame)
            self.menottes_info_label.grid(row=2, column=0, columnspan=2)

            self.game_infos_label = Label(self.frame)
            self.game_infos_label.grid(row=3, column=0, columnspan=2)

            self.player_1_frame = LabelFrame(self.frame, text=f"Infos joueur 1 ({self.player_1.name}) :")
            self.player_1_frame.grid(row= 4, column=0, padx=20, pady=10)

            if self.hide_pv_checkbutton_var.get():
                self.player_1_pv_label = Label(self.player_1_frame, text=f"Points de vie restants :\n{'➕'*self.player_1.pv}", justify="left")
                self.player_1_pv_label.grid(row=0, column=0, sticky="w")
            all_items = ""
            for i in range(len(self.player_1.items)):
                all_items += f"- {self.player_1.items[i]}\n"
            self.player_1_infos_label = Label(self.player_1_frame, text=f"Items :\n{all_items}", justify="left")
            self.player_1_infos_label.grid(row=1, column=0, sticky="w")

            self.player_1_combobox = ttk.Combobox(self.player_1_frame, values=[], state="disabled", justify="left", width=25)
            self.player_1_combobox.grid(row=2, column=0)

            self.player_1_selectionner_action = Button(self.player_1_frame, text="CONFIRMER", state="disabled", command=self.action_choosed)
            self.player_1_selectionner_action.grid(row=3, column=0, sticky="news", padx=20, pady=10)

            for widget in self.player_1_frame.winfo_children():
                widget.grid_configure(padx=10, pady=5)
            
            self.player_2_frame =LabelFrame(self.frame, text=f"Infos joueur 2 ({self.player_2.name}) :")
            self.player_2_frame.grid(row=4, column=1, padx=20, pady=10)
            
            if self.hide_pv_checkbutton_var.get():
                self.player_2_pv_label = Label(self.player_2_frame, text=f"Points de vie restants :\n{'➕'*self.player_2.pv}", justify="left")
                self.player_2_pv_label.grid(row=0, column=0, sticky="w")
            all_items = ""
            for i in range(len(self.player_2.items)):
                all_items += f"- {self.player_2.items[i]}\n"
            self.player_2_infos_label = Label(self.player_2_frame, text=f"Items :\n{all_items}", justify="left")
            self.player_2_infos_label.grid(row=1, column=0, sticky="w")
            
            self.player_2_combobox = ttk.Combobox(self.player_2_frame, values=[], state="disabled", justify="left", width=25)
            self.player_2_combobox.grid(row=2, column=0)

            self.player_2_selectionner_action = Button(self.player_2_frame, text="CONFIRMER", state="disabled", command=self.action_choosed)
            self.player_2_selectionner_action.grid(row=3, column=0, sticky="news", padx=20, pady=10)

            for widget in self.player_2_frame.winfo_children():
                widget.grid_configure(padx=10, pady=5)

            self.generate_chamber()

        else:
            pass

    def generate_chamber(self):
        try:
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
        except Exception as e:
            ic(e, self.nbr_balls, self.canon_chamber)
            return self.generate_chamber()
        print(f"\nRechargement...\n{'\u2B24'*nbr_true}{'○'*(len(self.canon_chamber)-nbr_true)}\n")
        self.rechargement_infos_label.config(text=f"\nRechargement...\n{'\u2B24'*nbr_true}{'○'*(len(self.canon_chamber)-nbr_true)}\n")
        if self.use_item_checkbutton_var.get():
            player_1_new_items = [random.choice(["Bière", "Cigarette", "Couteau", "Menotte", "Miroir"]), random.choice(["Bière", "Cigarette", "Couteau", "Menotte", "Miroir"])]
            player_2_new_items = [random.choice(["Bière", "Cigarette", "Couteau", "Menotte", "Miroir"]), random.choice(["Bière", "Cigarette", "Couteau", "Menotte", "Miroir"])]
            self.player_1.items.append(player_1_new_items[0])
            self.player_1.items.append(player_1_new_items[1])
            self.player_2.items.append(player_2_new_items[0])
            self.player_2.items.append(player_2_new_items[1])
            print(f"{self.player_1.name} a reçu les objets suivants :\n- {player_1_new_items[0]}\n- {player_1_new_items[1]}\n")
            print(f"{self.player_2.name} a reçu les objets suivants :\n- {player_2_new_items[0]}\n- {player_2_new_items[1]}\n")
            all_items = ""
            for i in range(len(self.player_1.items)):
                all_items += f"- {self.player_1.items[i]}\n"
            self.player_1_infos_label.config(text=f"Items :\n{all_items}")
            all_items = ""
            for i in range(len(self.player_2.items)):
                all_items += f"- {self.player_2.items[i]}\n"
            self.player_2_infos_label.config(text=f"Items :\n{all_items}")
            if len(self.player_1.items) > 8:
                self.supprimer_items(1)
            elif len(self.player_2.items) > 8:
                self.supprimer_items(2)
            else:
                self.phase()
        else:
            self.phase()

    def supprimer_items(self, player : int):
        if player == 1:
            all_items = ""
            for i in range(len(self.player_1.items)):
                all_items += f"- Supprimer l'item {self.player_1.items[i]} [{i+1}]\n"
            self.game_infos_label.config(text=f"{self.player_1.name} tu as trop d'objets, quel objet voulez-vous supprimer ?\n{all_items}\n")
            self.player_1_combobox["values"] = all_items.split("\n")[:-1]
            self.player_1_combobox["state"] = "readonly"
            self.player_1_combobox.current(0)
            self.player_1_selectionner_action.config(state="normal", command= lambda: self.supprimer_objet(1))
        else:
            all_items = ""
            for i in range(len(self.player_2.items)):
                all_items += f"- Supprimer l'item {self.player_2.items[i]} [{i+1}]\n"
            self.game_infos_label.config(text=f"{self.player_2.name} tu as trop d'objets, quel objet voulez-vous supprimer ?\n{all_items}\n")
            self.player_2_combobox["values"] = all_items.split("\n")[:-1]
            self.player_2_combobox["state"] = "readonly"
            self.player_2_combobox.current(0)
            self.player_2_selectionner_action.config(state="normal", command= lambda: self.supprimer_objet(2))

    def phase(self):
        if self.player_1.pv <= 0:
            messagebox.showinfo(title="PARTIE TERMINEE", message=f"{self.player_2.name} REMPORTE LA PARTIE")
            print(f"PARTIE TERMINEE : {self.player_2.name} REMPORTE LA PARTIE")
            self.root.destroy()
            return
        elif self.player_2.pv <= 0:
            messagebox.showinfo(title="PARTIE TERMINEE", message=f"{self.player_1.name} REMPORTE LA PARTIE")
            print(f"PARTIE TERMINEE : {self.player_1.name} REMPORTE LA PARTIE")
            self.root.destroy()
            return
        self.player_1_combobox["state"] = "disabled"
        self.player_1_selectionner_action["state"] = "disabled"
        self.player_2_combobox["state"] = "disabled"
        self.player_2_selectionner_action["state"] = "disabled"
        if self.player_turn == 1:
            if self.player_2.is_menoted == [True, 0]:
                self.player_2.is_menoted = [True, 1]
            if self.player_2.is_menoted == [True, 1]:
                self.player_2.is_menoted = [False, 0]
                self.menottes_info_label.config(text=f"{self.player_2.name} casse enfin ses menottes et se libére\n")
                print(f"{self.player_2.name} casse enfin ses menottes et se libére\n")
                self.player_2_combobox["state"] = "readonly"
                self.player_2_selectionner_action["state"] = "normal"
                self.tour(self.player_2, self.player_1)
            elif self.player_1.is_menoted == [True, 0]:
                self.player_1.is_menoted = [True, 1]
                self.menottes_info_label.config(text=f"{self.player_1.name} à toujours ses menottes, il saute son tour !\n")
                print(f"{self.player_1.name} à toujours ses menottes, il saute son tour !\n")
                self.player_2_combobox["state"] = "readonly"
                self.player_2_selectionner_action["state"] = "normal"
                self.tour(self.player_2, self.player_1)
            elif self.player_1.is_menoted == [True, 1]:
                self.player_1.is_menoted = [False, 0]
                self.menottes_info_label.config(text=f"{self.player_1.name} casse enfin ses menottes et se libére juste à temps pour son tour\n")
                print(f"{self.player_1.name} casse enfin ses menottes et se libére juste à temps pour son tour\n")
                self.player_1_combobox["state"] = "readonly"
                self.player_1_selectionner_action["state"] = "normal"
                self.tour(self.player_1, self.player_2)
            else:
                self.player_1_combobox["state"] = "readonly"
                self.player_1_selectionner_action["state"] = "normal"
                self.tour(self.player_1, self.player_2)
        elif self.player_turn == 2:
            if self.player_1.is_menoted == [True, 0]:
                self.player_1.is_menoted = [True, 1]
            if self.player_1.is_menoted == [True, 1]:
                self.player_1.is_menoted = [False, 0]
                self.menottes_info_label.config(text=f"{self.player_1.name} casse enfin ses menottes et se libére\n")
                print(f"{self.player_1.name} casse enfin ses menottes et se libére\n")
                self.player_1_combobox["state"] = "readonly"
                self.player_1_selectionner_action["state"] = "normal"
                self.tour(self.player_1, self.player_2)
            elif self.player_2.is_menoted == [True, 0]:
                self.player_2.is_menoted = [True, 1]
                self.menottes_info_label.config(text=f"{self.player_2.name} à toujours ses menottes, il saute son tour !\n")
                print(f"{self.player_2.name} à toujours ses menottes, il saute son tour !\n")
                self.player_1_combobox["state"] = "readonly"
                self.player_1_selectionner_action["state"] = "normal"
                self.tour(self.player_1, self.player_2)
            elif self.player_2.is_menoted == [True, 1]:
                self.player_2.is_menoted = [False, 0]
                self.menottes_info_label.config(text=f"{self.player_2.name} casse enfin ses menottes et se libére juste à temps pour son tour\n")
                print(f"{self.player_2.name} casse enfin ses menottes et se libére juste à temps pour son tour\n")
                self.player_2_combobox["state"] = "readonly"
                self.player_2_selectionner_action["state"] = "normal"
                self.tour(self.player_2, self.player_1)
            else:
                self.player_2_combobox["state"] = "readonly"
                self.player_2_selectionner_action["state"] = "normal"
                self.tour(self.player_2, self.player_1)

    def action_choosed(self):
        if not self.hide_rechargement_checkbutton_var.get():
            self.rechargement_infos_label.config(text="")
        self.info_action_label.config(text="")
        self.menottes_info_label.config(text="")
        if not self.using_item:
            self.action_resolution()
        else:
            self.use_item()

    def supprimer_objet(self, player : int):
        item_index = self.player_1_combobox["values"].index(self.player_1_combobox.get()) if player == 1 else self.player_2_combobox["values"].index(self.player_2_combobox.get())
        if player == 1:
            self.player_1.items.pop(item_index)
            all_items = ""
            for i in range(len(self.player_1.items)):
                all_items += f"- {self.player_1.items[i]}\n"
            self.player_1_infos_label.config(text=f"Items :\n{all_items}")
        else:
            self.player_2.items.pop(item_index)
            all_items = ""
            for i in range(len(self.player_2.items)):
                all_items += f"- {self.player_2.items[i]}\n"
            self.player_2_infos_label.config(text=f"Items :\n{all_items}")
        self.player_1_combobox["state"] = "disabled"
        self.player_1_selectionner_action.config(state="disabled", command=self.action_choosed)
        self.player_2_combobox["state"] = "disabled"
        self.player_2_selectionner_action.config(state="disabled", command=self.action_choosed)
        if len(self.player_1.items) > 8:
            self.supprimer_items(1)
        elif len(self.player_2.items) > 8 :
            self.supprimer_items(2)
        else:
            self.phase()

    def tour(self, player : Player, opponent : Player):
        self.game_infos_label.config(text=f"{player.name}, choisissez une action :\n- Tirer sur l'adversaire [1]\n- Tirer sur soi [2]\n- Utiliser un item [3]" if player.items else f"{player.name}, choisissez une action :\n- Tirer sur l'adversaire [1]\n- Tirer sur soi [2]")
        self.player_1_combobox["values"] = self.game_infos_label.cget("text").split("\n")[1:]
        self.player_2_combobox["values"] = self.game_infos_label.cget("text").split("\n")[1:]
        self.player_1_combobox.current(0)
        self.player_2_combobox.current(0)
        print(f"{player.name}, choisissez une action :\n- Tirer sur l'adversaire [1]\n- Tirer sur soi [2]\n- Utiliser un item [3]") if player.items else print(f"{player.name}, choisissez une action :\n- Tirer sur l'adversaire [1]\n- Tirer sur soi [2]")
        self.actual_player = player
        self.actual_opponent = opponent

    def action_resolution(self):
        self.using_item = False
        choice = self.player_1_combobox.get() if self.actual_player == self.player_1 else self.player_2_combobox.get()
        if choice == "- Tirer sur l'adversaire [1]":
            if self.canon_chamber[-1] is True:
                self.info_action_label.config(text="C'est une vraie cartouche 💀")
                print("C'est une vraie cartouche 💀")
                if self.canon_sciee is True:
                    self.actual_opponent.pv -= 2
                    if self.hide_pv_checkbutton_var.get():
                        self.player_1_pv_label.config(text=f"Points de vie restants :\n{'➕'*self.player_1.pv}")
                        self.player_2_pv_label.config(text=f"Points de vie restants :\n{'➕'*self.player_2.pv}")
                    self.canon_sciee = False
                else:
                    self.actual_opponent.pv -= 1
                    if self.hide_pv_checkbutton_var.get():
                        self.player_1_pv_label.config(text=f"Points de vie restants :\n{'➕'*self.player_1.pv}")
                        self.player_2_pv_label.config(text=f"Points de vie restants :\n{'➕'*self.player_2.pv}")
            else:
                self.info_action_label.config(text="C'est une balle à blanc...")
                print("C'est une balle à blanc...")
                self.canon_sciee = False
            self.player_turn = 1 if self.player_turn == 2 else 2
            self.canon_chamber.pop()
            if self.hide_rechargement_checkbutton_var.get():
                nbr_true = 0
                for ball in self.canon_chamber:
                    if ball is True:
                        nbr_true += 1
                print(f"\n{'\u2B24'*nbr_true}{'○'*(len(self.canon_chamber)-nbr_true)}\n")
                self.rechargement_infos_label.config(text=f"\n{'\u2B24'*nbr_true}{'○'*(len(self.canon_chamber)-nbr_true)}\n")
            if len(self.canon_chamber) > 0:
                self.phase()
            else:
                self.generate_chamber()
        elif choice == "- Tirer sur soi [2]":
            if self.canon_chamber[-1] is True:
                self.info_action_label.config(text="C'est une vraie cartouche 💀")
                print("C'est une vraie cartouche 💀")
                if self.canon_sciee is True:
                    self.actual_player.pv -= 2
                    if self.hide_pv_checkbutton_var.get():
                        self.player_1_pv_label.config(text=f"Points de vie restants :\n{'➕'*self.player_1.pv}")
                        self.player_2_pv_label.config(text=f"Points de vie restants :\n{'➕'*self.player_2.pv}")
                    self.canon_sciee = False
                else:
                    self.actual_player.pv -= 1
                    if self.hide_pv_checkbutton_var.get():
                        self.player_1_pv_label.config(text=f"Points de vie restants :\n{'➕'*self.player_1.pv}")
                        self.player_2_pv_label.config(text=f"Points de vie restants :\n{'➕'*self.player_2.pv}")
                self.player_turn = 1 if self.player_turn == 2 else 2
            else:
                self.info_action_label.config(text="C'est une balle à blanc...\nREJOUEZ")
                print("C'est une balle à blanc...\nREJOUEZ")
                self.canon_sciee = False
            self.canon_chamber.pop()
            if self.hide_rechargement_checkbutton_var.get():
                nbr_true = 0
                for ball in self.canon_chamber:
                    if ball is True:
                        nbr_true += 1
                print(f"\n{'\u2B24'*nbr_true}{'○'*(len(self.canon_chamber)-nbr_true)}\n")
                self.rechargement_infos_label.config(text=f"\n{'\u2B24'*nbr_true}{'○'*(len(self.canon_chamber)-nbr_true)}\n")
            if len(self.canon_chamber) > 0:
                self.phase()
            else:
                self.generate_chamber()
        elif choice == "- Utiliser un item [3]" and self.actual_player.items:
            self.show_items()
        else:
            self.tour(self.actual_player, self.actual_opponent)
            
    def show_items(self):
        self.using_item = True
        all_items = ""
        for i in range(len(self.actual_player.items)):
            all_items += f"- Utiliser l'item {self.actual_player.items[i]} [{i+1}]\n"
        menu = all_items.split("\n")[:-1]
        menu.append(f"- Quitter le menu [{i+2}]")
        self.player_1_combobox["values"] = menu
        self.player_2_combobox["values"] = menu
        self.player_1_combobox.current(0)
        self.player_2_combobox.current(0)
        self.game_infos_label.config(text=f"{self.actual_player.name}, quel objet voulez-vous utiliser ?\n{all_items}- Quitter le menu [{i+2}]\n")
        print(f"{self.actual_player.name}, quel objet voulez-vous utiliser ?\n{all_items}- Quitter le menu [{i+2}]\n")
    
    def use_item(self):
        self.using_item = False
        item_index = self.player_1_combobox["values"].index(self.player_1_combobox.get()) if self.actual_player == self.player_1 else self.player_2_combobox["values"].index(self.player_2_combobox.get())
        try:
            if self.actual_player.items[item_index] == "Bière":
                ball = self.canon_chamber.pop()
                self.info_action_label.config(text="Glouglouglou...\nVous avez enlevé une vraie cartouche 💣" if ball is True else "Glouglouglou...\nVous avez enlevé une balle à blanc 💨")
                print("Glouglouglou...\nVous avez enlevé une vraie cartouche 💣") if ball is True else print("Glouglouglou...\nVous avez enlevé une balle à blanc 💨")
                if self.hide_rechargement_checkbutton_var.get():
                    nbr_true = 0
                    for ball in self.canon_chamber:
                        if ball is True:
                            nbr_true += 1
                    print(f"\n{'\u2B24'*nbr_true}{'○'*(len(self.canon_chamber)-nbr_true)}\n")
                    self.rechargement_infos_label.config(text=f"\n{'\u2B24'*nbr_true}{'○'*(len(self.canon_chamber)-nbr_true)}\n")
            elif self.actual_player.items[item_index] == "Cigarette":
                if self.actual_player.pv == self.actual_player.max_pv:
                    self.info_action_label.config(text="Vous ne pouvez pas vous soigner plus, vous êtes déjà au maximum de points de vie")
                    print("Vous ne pouvez pas vous soigner plus, vous êtes déjà au maximum de points de vie")
                    return self.tour(self.actual_player, self.actual_opponent)
                else:
                    self.actual_player.pv += 1
                    if self.hide_pv_checkbutton_var.get():
                        self.player_1_pv_label.config(text=f"Points de vie restants :\n{'➕'*self.player_1.pv}")
                        self.player_2_pv_label.config(text=f"Points de vie restants :\n{'➕'*self.player_2.pv}")
                    self.info_action_label.config(text="Hffffff... Vous tirez une taffe et vous soignez 1 pv")
                    print("Hffffff... Vous tirez une taffe et vous soignez 1 pv")
            elif self.actual_player.items[item_index] == "Couteau":
                self.canon_sciee = True
                self.info_action_label.config(text="Tchak tchak tchak... Le canon de fusil a été scié")
                print("Tchak tchak tchak... Le canon de fusil a été scié")
            elif self.actual_player.items[item_index] == "Menotte":
                if self.actual_opponent.is_menoted[0]:
                    self.info_action_label.config(text=f"{self.actual_opponent.name} est déjà menotté, vous ne pouvez pas lui mettre deux paires de menottes à la fois")
                    print(f"{self.actual_opponent.name} est déjà menotté, vous ne pouvez pas lui mettre deux paires de menottes à la fois")
                    return self.tour(self.actual_player, self.actual_opponent)
                else:
                    self.actual_opponent.is_menoted = [True, 0]
                    self.info_action_label.config(text=f"Clic clac, vous passez les menottes à {self.actual_opponent.name} qui va sauter son prochain tour")
                    print(f"Clic clac, vous passez les menottes à {self.actual_opponent.name} qui va sauter son prochain tour")
            elif self.actual_player.items[item_index] == "Miroir":
                self.info_action_label.config(text=f"Hmmm intéressant, la prochaine cartouche est vraie 💣" if self.canon_chamber[-1] is True else f"Hmmm intéressant, la prochaine balle est à blanc 💨")
                print(f"Hmmm intéressant, la prochaine cartouche est vraie 💣") if self.canon_chamber[-1] is True else print(f"Hmmm intéressant, la prochaine balle est à blanc 💨")
        except IndexError:
            return self.tour(self.actual_player, self.actual_opponent)
        self.actual_player.items.pop(item_index)
        all_items = ""
        for i in range(len(self.player_1.items)):
            all_items += f"- {self.player_1.items[i]}\n"
        self.player_1_infos_label.config(text=f"Items :\n{all_items}")
        all_items = ""
        for i in range(len(self.player_2.items)):
            all_items += f"- {self.player_2.items[i]}\n"
        self.player_2_infos_label.config(text=f"Items :\n{all_items}")
        self.tour(self.actual_player, self.actual_opponent)

    def show_ui(self):
        self.root = Tk()
        self.root.title("Buckshot Roulette de wish")

        self.frame = Frame(self.root)
        self.frame.pack()

        self.settings_frame =LabelFrame(self.frame)
        self.settings_frame.grid(row= 0, column=0, padx=20, pady=10)

        self.nom_joueur_1_label = Label(self.settings_frame, text="Pseudo joueur 1 :")
        self.nom_joueur_1_label.grid(row=0, column=0)
        self.nom_joueur_1_entry = Entry(self.settings_frame)
        self.nom_joueur_1_entry.insert(0, "Joueur 1")
        self.nom_joueur_1_entry.grid(row= 1, column=0, padx=20, pady=10)
        
        self.nom_joueur_2_label = Label(self.settings_frame, text="Pseudo joueur 2 :")
        self.nom_joueur_2_label.grid(row=0, column=1)
        self.nom_joueur_2_entry = Entry(self.settings_frame)
        self.nom_joueur_2_entry.insert(0, "Joueur 2")
        self.nom_joueur_2_entry.grid(row= 1, column=1, padx=20, pady=100)

        for widget in self.settings_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)
        
        self.settings_frame_2 =LabelFrame(self.frame)
        self.settings_frame_2.grid(row= 1, column=0, padx=20, pady=10)
        
        self.use_item_checkbutton_var = BooleanVar()
        self.use_item_checkbutton_var.set(True)
        self.use_item_checkbutton = Checkbutton(self.settings_frame_2, text="Utiliser les items ?", variable=self.use_item_checkbutton_var)
        self.use_item_checkbutton.grid(row= 0, column=0, padx=20, pady=10)
        
        self.hide_pv_checkbutton_var = BooleanVar()
        self.hide_pv_checkbutton_var.set(True)
        self.hide_pv_checkbutton = Checkbutton(self.settings_frame_2, text="Afficher les PV ?", variable=self.hide_pv_checkbutton_var)
        self.hide_pv_checkbutton.grid(row= 0, column=1, padx=20, pady=10)
        
        self.pv_range_label = Label(self.settings_frame_2, text="Mettez dans les deux cases les PV max et min.\nLes PV vont être choisi entre ces deux nombres (inclus).")
        self.pv_range_label.grid(row=1, column=0, columnspan=2)
        self.pv_range_1_entry = Entry(self.settings_frame_2)
        self.pv_range_1_entry.insert(0, "4")
        self.pv_range_1_entry.grid(row= 2, column=0, padx=20, pady=10)
        self.pv_range_2_entry = Entry(self.settings_frame_2)
        self.pv_range_2_entry.insert(0, "4")
        self.pv_range_2_entry.grid(row= 2, column=1, padx=20, pady=10)

        self.hide_rechargement_checkbutton_var = BooleanVar()
        self.hide_rechargement_checkbutton_var.set(False)
        self.hide_rechargement_checkbutton = Checkbutton(self.settings_frame_2, text="Afficher le nombre\nde balles restantes ?", variable=self.hide_rechargement_checkbutton_var)
        self.hide_rechargement_checkbutton.grid(row= 3, column=0, padx=20, pady=10)

        for widget in self.settings_frame_2.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        self.enter_infos_button = Button(self.frame, text="Commencer", command=self.start)
        self.enter_infos_button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

        self.root.mainloop()

if __name__ == "__main__":
    jeu = Game()