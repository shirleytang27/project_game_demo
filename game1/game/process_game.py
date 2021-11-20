import random
from game import character_game

#create 10 heros with its initial amount of blood,magic,money and EXpoints
hero_one = character_game.characters('hero1', 1000, 1000, 500,0)
hero_two = character_game.characters('hero2', 1000, 1000, 500,0)
hero_three = character_game.characters('hero3', 1000, 1000, 500,0)
hero_four = character_game.characters('hero4', 1000, 1000, 500,0)
hero_five = character_game.characters('hero5', 1000, 1000, 500,0)
hero_six = character_game.characters('hero6', 1000, 1000, 500,0)
hero_seven = character_game.characters('hero7', 1000, 1000, 500,0)
hero_eight = character_game.characters('hero8', 1000, 1000, 500,0)
hero_nine = character_game.characters('hero9', 1000, 1000, 500,0)
hero_ten = character_game.characters('hero10', 1000, 1000, 500,0)
herolist1 = [hero_one,hero_two,hero_three,hero_four,hero_five,hero_six,hero_seven,hero_eight,hero_nine,hero_ten]
team_one = [hero_one, hero_two, hero_three, hero_four, hero_five]
team_two = [hero_six, hero_seven, hero_eight, hero_nine, hero_ten]
role_list=['tank','assistant','mage','hunter','ADC']
role_list1=['tank','assistant','mage','hunter','ADC']


# randomly assign the type of role to team members and adjust its attributes
def team1_role():
  ret=''
  for i in range(0,len(team_one),1):

    a=random.choice(role_list)
    team_one[i].roles = a
    role_list.remove(a)
    team_one[i].attributes_adjust()
    ret+= 'Team_one '+team_one[i].name+'\t'+'is '+str(a)+',Current blood is '+str(team_one[i].blood)+'. Current magic is '+str(team_one[i].magic)+'. Damage of skill one is '+str(team_one[i].skill1_damage)+'. Ex_point of the hero is '+str(team_one[i].experience_point)+'\n'+'\n'

  return ret

def team2_role():
  ret=''
  for i in range(0,len(team_two),1):

    a=random.choice(role_list1)
    team_two[i].roles = a
    role_list1.remove(a)
    team_two[i].attributes_adjust()
    ret+= 'Team_two '+team_two[i].name+'\t'+'is '+str(a)+',Current blood is '+str(team_two[i].blood)+'. Current magic is '+str(team_two[i].magic)+'. Damage of skill one is '+str(team_two[i].skill1_damage)+'. Ex_point of the hero is '+str(team_two[i].experience_point)+'\n\n'
  return ret


#Actions taken by hero1
def hero1click():
   #Check the status of the hero_one before each attack, once he is dead, then he can not attack others.
   if hero_one.status=='dead':
      return hero_one.name+' dead, no more actions.'
   #Check if all members from team_two are killed, if yes, then game over
   if len(team_two) <= 0:
     return 'Game over, Team one won'
   #Randomly attack one of the hero from team_two
   hero_one.attack()
   a = random.choice(team_two)
   #Attack a hero from team two with a randomly chosen skill, causing different damage
   a.being_attack(team_one[0].select_skill())
   #Check the status of the hero being attacked, remove it from team_two if he is dead and attack the rest of members.
   a.herostatus_check()
   if a.status=='dead':
      team_two.remove(a)
   return a.name+' :was attacked by hero1 & current status is '+a.herostatus_check()+', has '+str(a.blood)+' blood '+'\n'+'hero1:the current EX is '+str(hero_one.experience_point)+' current amount of money is '+str(hero_one.money)

#Actions taken by hero2
def hero2click():
    #Check the status of the hero_two before each attack, once he is dead, then he can not attack others.
    if hero_two.status == 'dead':
        return hero_two.name + ' dead, no more actions.'
    if len(team_two) <= 0:
        return 'Game over, Team one won'
    hero_two.attack()
    # Randomly attack one of the hero from team_two
    a = random.choice(team_two)
    a.being_attack(team_one[1].select_skill())
    a.herostatus_check()
    if a.status == 'dead':
       team_two.remove(a)
    return a.name + ' :was attacked by hero2 & current status is ' + a.herostatus_check() + ', has ' + str(a.blood) + ' blood ' + '\n' + 'hero2:the current EX is ' + str(hero_two.experience_point) + ' current amount of money is ' + str(hero_two.money)


#Actions taken by hero3
def hero3click():
    # Check the status of the hero_three before each attack, once he is dead, then he can not attack others.
    if hero_three.status == 'dead':
        return hero_three.name + ' dead, no more actions.'
    if len(team_two) <= 0:
        return 'Game over, Team one won'
    hero_three.attack()
    # Randomly attack one of the hero from team_two
    a = random.choice(team_two)
    a.being_attack(team_one[2].select_skill())
    a.herostatus_check()
    if a.status == 'dead':
       team_two.remove(a)
    return a.name + ' :was attacked by hero3 & current status is ' + a.herostatus_check() + ', has ' + str(a.blood) + ' blood ' + '\n' + 'hero3:the current EX is ' + str(hero_three.experience_point) + ' current amount of money is ' + str(hero_three.money)

#Actions taken by hero4
def hero4click():
    # Check the status of the hero_four before each attack, once he is dead, then he can not attack others.
    if hero_four.status == 'dead':
        return hero_four.name + ' dead, no more actions.'
    if len(team_two) <= 0:
        return 'Game over, Team one won'
    hero_four.attack()
    # Randomly attack one of the hero from team_two
    a = random.choice(team_two)
    a.being_attack(team_one[3].select_skill())
    a.herostatus_check()
    if a.status == 'dead':
       team_two.remove(a)
    return a.name + ' :was attacked by hero4 & current status is ' + a.herostatus_check() + ', has ' + str(a.blood) + ' blood ' + '\n' + 'hero4:the current EX is ' + str(hero_four.experience_point) + ' current amount of money is ' + str(hero_four.money)


#Actions taken by hero5
def hero5click():
    # Check the status of the hero_five before each attack, once he is dead, then he can not attack others.
    if hero_five.status == 'dead':
        return hero_five.name + ' dead, no more actions.'
    if len(team_two) <= 0:
        return 'Game over, Team one won'
    hero_five.attack()
    # Randomly attack one of the hero from team_two
    a = random.choice(team_two)
    a.being_attack(team_one[4].select_skill())
    a.herostatus_check()
    if a.status == 'dead':
       team_two.remove(a)
    return a.name + ' :was attacked by hero5 & current status is ' + a.herostatus_check() + ', has ' + str(a.blood) + ' blood ' + '\n' + 'hero5:the current EX is ' + str(hero_five.experience_point) + ' current amount of money is ' + str(hero_five.money)


#Actions taken by hero6
def hero6click():
    # Check the status of the hero_six before each attack, once he is dead, then he can not attack others.
    if hero_six.status == 'dead':
        return hero_six.name + ' dead, no more actions.'
    # Check if all members from team_one are killed, if yes, then game over
    if len(team_one) <= 0:
        return 'Game over, Team two won'
    # Randomly attack one of the hero from team_one
    hero_six.attack()
    a = random.choice(team_one)
    # Attack a hero from team two with a randomly chosen skill, causing different damage
    a.being_attack(team_two[0].select_skill())
    # Check the status of the hero being attacked, remove it from team_one if he is dead and attack the rest of members.
    a.herostatus_check()
    if a.status == 'dead':
        team_one.remove(a)
    return a.name + ' :was attacked by hero6 & current status is ' + a.herostatus_check() + ', has ' + str(a.blood) + ' blood ' + '\n' + 'hero6:the current EX is ' + str(hero_six.experience_point) + ' current amount of money is ' + str(hero_six.money)

#Actions taken by hero7
def hero7click():
    # Check the status of the hero_seven before each attack, once he is dead, then he can not attack others.
    if hero_seven.status == 'dead':
        return hero_seven.name + ' dead, no more actions.'
    if len(team_one) <= 0:
        return 'Game over, Team two won'
    hero_seven.attack()
    # Randomly attack one of the hero from team_one
    a = random.choice(team_one)
    a.being_attack(team_two[1].select_skill())
    a.herostatus_check()
    if a.status == 'dead':
        team_one.remove(a)
    return a.name + ' :was attacked by hero7 & current status is ' + a.herostatus_check() + ', has ' + str(a.blood) + ' blood ' + '\n' + 'hero7:the current EX is ' + str(hero_seven.experience_point) + ' current amount of money is ' + str(hero_seven.money)

#Actions taken by hero8
def hero8click():
    # Check the status of the hero_eight before each attack, once he is dead, then he can not attack others.
    if hero_eight.status == 'dead':
        return hero_eight.name + ' dead, no more actions.'
    if len(team_one) <= 0:
        return 'Game over, Team two won'
    hero_eight.attack()
    # Randomly attack one of the hero from team_one
    a = random.choice(team_one)
    a.being_attack(team_two[2].select_skill())
    a.herostatus_check()
    if a.status == 'dead':
        team_one.remove(a)
    return a.name + ' :was attacked by hero8 & current status is ' + a.herostatus_check() + ', has ' + str(a.blood) + ' blood ' + '\n' + 'hero8:the current EX is ' + str(hero_eight.experience_point) + ' current amount of money is ' + str(hero_eight.money)


#Actions taken by hero9
def hero9click():
    # Check the status of the hero_nine before each attack, once he is dead, then he can not attack others.
    if hero_nine.status == 'dead':
        return hero_nine.name + ' dead, no more actions.'
    if len(team_one) <= 0:
        return 'Game over, Team two won'
    hero_nine.attack()
    # Randomly attack one of the hero from team_one
    a = random.choice(team_one)
    a.being_attack(team_two[3].select_skill())
    a.herostatus_check()
    if a.status == 'dead':
        team_one.remove(a)
    return a.name + ' :was attacked by hero9 & current status is ' + a.herostatus_check() + ', has ' + str(a.blood) + ' blood ' + '\n' + 'hero9:the current EX is ' + str(hero_nine.experience_point) + ' current amount of money is ' + str(hero_nine.money)

#Actions taken by hero10
def hero10click():
    # Check the status of the hero_ten before each attack, once he is dead, then he can not attack others.
    if hero_ten.status == 'dead':
        return hero_ten.name + ' dead, no more actions.'
    if len(team_one) <= 0:
        return 'Game over, Team two won'
    hero_ten.attack()
    # Randomly attack one of the hero from team_one
    a = random.choice(team_one)
    a.being_attack(team_two[4].select_skill())
    a.herostatus_check()
    if a.status == 'dead':
        team_one.remove(a)
    return a.name + ' :was attacked by hero10 & current status is ' + a.herostatus_check() + ', has ' + str(a.blood) + ' blood ' + '\n' + 'hero10:the current EX is ' + str(hero_ten.experience_point) + ' current amount of money is ' + str(hero_ten.money)

