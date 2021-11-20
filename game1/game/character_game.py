import random
class characters:
    name=''
    blood=1000
    magic=1000
    money=500
    skill_damage=100
    experience_point=0
    skill1_damage =100
    skill2_damage = 200
    skill3_damage = 300
    skill_damage = ['skill1_damage','skill2_damage','skill3_damage']

    level=0
    roles=''
    status=''

    #Adjust the attributes of a hero after being assigned with a specific role
    def attributes_adjust(self):
        a=self.roles
        if a=='tank':
           self.blood+=500
           return str(self.blood)
        elif a=='assistant':
             self.skill1_damage-=50
             self.skill2_damage-=100
             self.skill3_damage -=100
             return str(self.skill1_damage)
        elif a=='hunter':
             self.skill1_damage += 50
             self.skill2_damage += 80
             self.skill3_damage += 100
             return str(self.skill1_damage)
        elif a=='mage':
             self.magic+=300
             return str(self.magic)
        elif a=='ADC':
             self.experience_point+=200
             self.blood-=200
             return str(self.blood)


    def __init__(self,name1,blood1,magic1,money1,experience_point1):
        self.name=name1
        self.blood=blood1
        self.magic=magic1
        self.money=money1
        self.experience_point=experience_point1

    # when a hero attacks another hero, he gets Ex and money but loses magic.
    def attack(self):
        self.magic -= 80
        self.experience_point += 100
        self.money += 150
    # randomly select a skill to attack others
    def select_skill(self):
        a = random.choice(self.skill_damage)
        if a==self.skill_damage[0]:
           return self.skill1_damage
        elif a==self.skill_damage[1]:
           return self.skill2_damage
        elif a==self.skill_damage[2]:
           return self.skill3_damage
    # when a hero is attacked by another hero, he loses blood.
    def being_attack(self,x):
        self.blood -= x
        return self.blood

    # Check the current status of the hero after each attack
    def herostatus_check(self):
        a=self.blood
        if a<=0:
           self.status='dead'
        else:
            self.status='alive'
        return self.status











