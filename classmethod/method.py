# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]".format(self.name, location, self.speed))

# 공격 유닛
# Unit 클래스를 상속
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # 부모 init 호출
        self.damage = damage

    # self 사용을 통해 클래스 내에서 정의된 name과 damage를 사용
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 테란 유닛 파이어벳
firebat1 = AttackUnit("파이어벳", 50, 5, 16)
firebat1.attack("5시")

# 공격을 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 날 수 있는 유닛
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
        Flyable.__init__(self, flying_speed)

    # 메소드 오버라이딩 : 상위 클래스 메소드 move() 재정의
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 테란 유닛 발키리
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")

# 테란 유닛 벌쳐
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 테란 유닛 배틀크루저
battlecrusier = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecrusier.move("9시")

# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # 부모 클래스 호출, self 생략 가능, 다중 상속시 가장 처음 상속받은 부모만 생성자 호출
        self.location = location

# 테란 건물 서플라이 디폿
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

def game_start():
    print("[알림] 새로운 게임을 시작합니다.")

def game_over():
    pass # 미완성 임에도 그냥 넘어감

game_start()
game_over()

