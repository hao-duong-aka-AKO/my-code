import random
import time
def slow_print(text, delay=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
slow_print("Hello, i'm Hào, i like to write/draw stories but, my best friend Phúc Anh hates the story named Triple Eyes, i don't know why he hates it, but i think it's a good story, so i will write it anyway, so i and him start a battle.")
slow_print("Phúc Anh: I hate this story, it's so boring and cliche.")
slow_print("Hào: But it's a good story, it has a lot of action and adventure.")
slow_print("Phúc Anh: But the characters are so one-dimensional and the plot is so predictable.")
slow_print("Hào: But it's a good story, it has a lot plot twist, chat gpt,copilot,... loves it.")
slow_print("Phúc Anh: Let's se who will win , i'm Yin/Yang, and you are Lyako.")
slow_print("Hào: I will win, because i have the power of the story.")
slow_print("Phúc Anh: But i have the power of the reader.")
slow_print("Hào: But i have the power of the writer.")
# LyAko class with skills
class LyAko:
    def __init__(self):
        self.hp = 100
        self.max_hp = 100

    def angel_chaos_overload(self):
        damage = random.randint(50, 100)
        print(f"LyAko uses Angel Chaos Overload! Deals {damage} damage.")
        return damage

    def trio_eyes_power(self):
        heal = random.randint(20, 40)
        self.hp = min(self.hp + heal, self.max_hp)
        print(f"LyAko uses Trio Eyes Power! Heals for {heal} HP. Current HP: {self.hp}")
        return heal

    def goddness_form(self):
        self.hp = self.max_hp
        print(f"LyAko transforms into G0DDN33s form! HP fully restored: {self.hp}")
        return 0  # No damage but restores HP

# Phúc Anh (Âm Dương) class with skills (Bot)
class PhucAnh:
    def __init__(self):
        self.hp = 100
        self.max_hp = 100

    def am_duong_vo_cuc(self):
        # Âm Dương Vô Cực skill that balances attack or heal
        if random.choice([True, False]):
            damage = random.randint(50, 80)
            print(f"Phúc Anh uses Âm Dương Vô Cực! Deals {damage} damage.")
            return damage
        else:
            heal = random.randint(30, 50)
            self.hp = min(self.hp + heal, self.max_hp)
            print(f"Phúc Anh uses Âm Dương Vô Cực to heal! Heals for {heal} HP. Current HP: {self.hp}")
            return -heal

    def lo_bat_quai(self):
        # A strategic skill that might confuse or damage
        action = random.choice(["confuse", "damage"])
        if action == "confuse":
            print("Phúc Anh uses Lò Bát Quái! LyAko is confused!")
            return 0  # No damage, but confusion could make LyAko miss an attack
        else:
            damage = random.randint(30, 50)
            print(f"Phúc Anh uses Lò Bát Quái! Deals {damage} damage.")
            return damage

    def hac_bach_vo_thuong(self):
        # Offensive or defensive stance change
        stance = random.choice(["offensive", "defensive"])
        if stance == "offensive":
            damage = random.randint(40, 70)
            print(f"Phúc Anh uses Hắc Bạch Vô Thường in offensive stance! Deals {damage} damage.")
            return damage
        else:
            heal = random.randint(15, 30)
            self.hp = min(self.hp + heal, self.max_hp)
            print(f"Phúc Anh uses Hắc Bạch Vô Thường in defensive stance! Heals for {heal} HP. Current HP: {self.hp}")
            return -heal

# Game loop for LyAko vs Phúc Anh (Bot)
def game_loop():
    ly_ako = LyAko()
    phuc_anh = PhucAnh()

    while ly_ako.hp > 0 and phuc_anh.hp > 0:
        # LyAko's turn (Player input)
        print("\nLyAko's turn...")
        print("Choose LyAko's skill:")
        print("1. Angel Chaos Overload")
        print("2. Trio Eyes Power")
        print("3. G0DDN33s Form")
        skill_choice = input("Enter 1, 2, or 3: ")

        if skill_choice == "1":
            damage = ly_ako.angel_chaos_overload()
            phuc_anh.hp -= damage
        elif skill_choice == "2":
            heal = ly_ako.trio_eyes_power()
        elif skill_choice == "3":
            ly_ako.goddness_form()

        # Phúc Anh's turn (Bot makes a random move)
        print("\nPhúc Anh's turn...")
        bot_skill_choice = random.choice([1, 2, 3])
        print(f"Phúc Anh chooses skill {bot_skill_choice}.")

        if bot_skill_choice == 1:
            effect = phuc_anh.am_duong_vo_cuc()  # This skill is key!
            ly_ako.hp -= effect
        elif bot_skill_choice == 2:
            effect = phuc_anh.lo_bat_quai()
            ly_ako.hp -= effect
        elif bot_skill_choice == 3:
            effect = phuc_anh.hac_bach_vo_thuong()
            if effect < 0:
                phuc_anh.hp -= effect  # Heal Phúc Anh if defensive

        # Show HP after both turns
        print(f"\nLyAko HP: {ly_ako.hp} | Phúc Anh HP: {phuc_anh.hp}")
        time.sleep(1)

    # Determine winner
    if ly_ako.hp <= 0:
        print("\nLyAko has been defeated!")
        slow_print("Phúc Anh: I won, you can't write the story.")
    elif phuc_anh.hp <= 0:
        print("\nPhúc Anh has been defeated!")
        slow_print("Hào: I won, i will write the story anyway.")
# Run the game loop
game_loop()

