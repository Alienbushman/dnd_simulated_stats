def attack_damage(weapon,stat,bonus=0, crit=False):
    #calculating the rng part of damage
    weapon_rng=weapon.split('d')
    damage=0
    for _ in range(0,int(weapon_rng[0])):
        damage+=randint(1, int(weapon_rng[1]))
        if (crit):
            damage+=randint(1, int(weapon_rng[1]))
    #adding the damage stat
    damage+=stat+bonus
    return damage
def hit_chance(stat,proficiency,accuracy_bonus,ac):
    #returns 0 for miss, 1 for a hit, 2 for a crit
    # determines whether a weapon attack hits
    random_elem=randint(1, 20)
    
    if random_elem==20:
        return 2
    elif(random_elem+stat+proficiency+accuracy_bonus>ac):
        return 1
    return 0
