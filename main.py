from abc import ABC, abstractmethod

class BaseCharacter(ABC):
    def __init__(self, base_hp: int):
        self.__base_hp = base_hp

    @property
    def base_hp(self):
        return self.__base_hp

    @abstractmethod
    def attack_enemy(self):
        pass

    def __add__(self, other):
        if isinstance(other, BaseCharacter):
            return self.__base_hp + other.__base_hp
        return NotImplemented

class Warrior(BaseCharacter):
    def __init__(self, base_hp: int, strength: float):
        super().__init__(base_hp)
        self.strength = strength

    def attack_enemy(self):
        return self.strength * 2.5

class MagicalStance:
    def attack_enemy(self):
        return 150.0

class Spellblade(Warrior, MagicalStance):
    def __init__(self, base_hp: int, strength: float):
        Warrior.__init__(self, base_hp, strength)

    def attack_enemy(self):
        warrior_damage = Warrior.attack_enemy(self)
        magic_damage = MagicalStance.attack_enemy(self)
        return warrior_damage + magic_damage

class VolcanoZone:
    def activate_buff(self, character):
        if hasattr(character, 'strength'):
            character.strength += 10
            print(f"[VolcanoZone] Buff thành công! Strength tăng +10 → {character.strength}")
        else:
            print("[VolcanoZone] Đối tượng không hỗ trợ buff.")

def apply_battleground_effect(environment, character):
    if hasattr(environment, 'activate_buff'):
        environment.activate_buff(character)
    else:
        print("Môi trường không hỗ trợ hiệu ứng buff.")

def main():
    current_hero = None

    while True:
        print("\n========== RPG GAME CORE MENU ==========")
        print("1. Khởi tạo Ma kiếm sĩ Spellblade & Xem cấu trúc MRO")
        print("2. Ra lệnh tấn công & kích hoạt chiến trường (Duck Typing)")
        print("0. Thoát")
        choice = input("Chọn chức năng (1-2): ")

        match choice:
            case "1":
                try:
                    hp = int(input("Nhập HP cơ bản: "))
                    strength = float(input("Nhập Strength: "))

                    current_hero = Spellblade(hp, strength)

                    total_hp = current_hero + current_hero
                    print(f"Tổng HP sau khi tự cộng hưởng: {total_hp}")

                    print("Thứ tự MRO:", [cls.__name__ for cls in Spellblade.__mro__])

                except ValueError:
                    print("Lỗi: Vui lòng nhập số hợp lệ!")

            case "2":
                if current_hero is None:
                    print("Lỗi: Chưa khởi tạo nhân vật!")
                    continue

                damage = current_hero.attack_enemy()
                print(f"Sát thương gây ra (Spellblade): {damage:.1f}")

                volcano = VolcanoZone()
                apply_battleground_effect(volcano, current_hero)

            case "3":
                print("Đã thoát chương trình.")
                break
            case _:
                print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
