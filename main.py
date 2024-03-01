import random

class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.max_hp = 100
        self.attack = 10
        self.defense = 5
        self.xp = 0
        self.inventory = {"health_potion": 0, "attack_potion": 0, "defense_potion": 0}

    def attack_enemy(self, enemy):
        damage = max(0, self.attack - enemy.defense)
        enemy.hp -= damage
        print(f"{self.name} inflige {damage} dégâts à {enemy.name}.")
        if enemy.hp <= 0:
            print(f"{enemy.name} a été vaincu!")
            self.xp += enemy.level * 10
            self.level_up()

    def level_up(self):
        if self.xp >= self.level * 100:
            self.level += 1
            self.max_hp += 20
            self.hp = self.max_hp
            self.attack += 5
            self.defense += 3
            print(f"{self.name} monte au niveau {self.level}!")

    def use_health_potion(self):
        if self.max_hp < self.max_hp:
            if self.inventory["health_potion"] > 0:
                print(f"{self.name} utilise une potion de soin.")
                self.hp = min(self.max_hp, self.hp + 30)
                print(f"{self.name} récupère 30 points de vie.")
                self.inventory["health_potion"] -= 1
            else:
                print("Vous n'avez pas de potion dans votre inventaire.")
        else:
            print("Votre vie est déjà au maximum.")

    def use_attack_potion(self, enemy):
        if self.inventory["attack_potion"] > 0:
            print(f"{self.name} utilise une potion de dégâts.")
            damage = min(enemy.hp, 30)
            enemy.hp -= damage
            print(f"{enemy.name} subit 30 points de dégâts supplémentaires.")
            self.inventory["attack_potion"] -= 1
        else:
            print("Vous n'avez pas de potion de dégâts dans votre inventaire.")

    def use_defense_potion(self):
        if self.inventory["defense_potion"] > 0:
            print(f"{self.name} utilise une potion de bouclier.")
            self.defense += 5
            print(f"{self.name} gagne 5 points de défense.")
            self.inventory["defense_potion"] -= 1
        else:
            print("Vous n'avez pas de potion de bouclier dans votre inventaire.")
    
    def check_inventory(self):
        print("Inventaire:")
        for item, quantity in self.inventory.items():
            print(f"{item.capitalize()}: {quantity}")

    def level_up(self):
        if self.xp >= self.level * 100:
            self.level += 1
            self.hp += 20
            self.attack += 5
            self.defense += 3
            print(f"{self.name} monte au niveau {self.level}!")

class Enemy:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = level * 50
        self.attack = level * 5
        self.defense = level * 2

    def attack_player(self, player):
        damage = max(0, self.attack - player.defense)
        player.max_hp -= damage
        print(f"{self.name} inflige {damage} dégâts à {player.name}.")

def start_game():
    print("Bienvenue dans le jeu!")
    name = input("Entrez votre nom: ")
    player = Player(name)
    print(f"Bienvenue, {player.name}!")
    if input("Voulez-vous commencer une nouvelle partie? (oui/non): ").lower() == "oui":
        print("Vous vous réveillez au milieu d'une forêt sombre...")
        explore_forest(player)
    else:
        print("Partie en cours chargée.")

def explore_forest(player):
    print("Vous marchez à travers la forêt...")
    action = input("Que voulez-vous faire? (Go East, Go North, Go West, Go South): ").lower()
    if action.startswith("go"):
        print("Vous continuez à marcher...")
        encounter = random.choice([True, False])
        if encounter:
            handle_encounter(player)
        else:
            print("Vous ne trouvez rien d'intéressant pour le moment.")
            explore_forest(player)
    elif action == "inventory":
        player.check_inventory()
        explore_forest(player)
    else:
        print("Commande invalide, veuillez entrer une direction valide.")
        explore_forest(player)

def handle_encounter(player):
    print("Vous rencontrez un ennemi!")
    enemy = Enemy("Goblin", player.level)
    print(f"Un {enemy.name} de niveau {enemy.level} apparaît!")
    while player.max_hp > 0 and enemy.hp > 0:
        print(f"\n{player.name}: HP: {player.max_hp}, Level: {player.level}")
        print(f"{enemy.name}: HP: {enemy.hp}, Level: {enemy.level}")
        action = input("Que voulez-vous faire? (Attack, Use Item, Run): ").lower()
        if action == "attack":
            player.attack_enemy(enemy)
            if enemy.hp > 0:
                enemy.attack_player(player)
        elif action == "use item":
            item = input("Quel objet voulez-vous utiliser? (Health Potion, Attack Potion, Defense Potion): ").lower()
            if item == "health potion":
                player.use_health_potion()
            elif item == "attack potion":
                player.use_attack_potion(enemy)
            elif item == "defense potion":
                player.use_defense_potion()
            else:
                print("Objet invalide.")    
        elif action == "run":
            print("Vous prenez la fuite!")
            break
        else:
            print("Action invalide.")

    if player.max_hp <= 0:
        print("Vous avez été vaincu! Game Over.")
        start_game()
    elif enemy.hp <= 0:
        print("Vous avez vaincu l'ennemi!")
        explore_forest(player)

start_game()
