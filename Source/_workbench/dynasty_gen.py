starting_date = list((806, 6, 16))

class Character(object):

    def __init__(self, name=False, dynasty=756, culture='saxon', religion='catholic', birth=(1025, 1, 2), death=(1066, 10, 14), female = False, game_id = 60000):
        if name is False:
            self.name = get_random_name(female)
        else:
            self.name = name
        self.dynasty = dynasty
        self.birth = birth
        self.death = death
        self.culture = culture
        self.religion = religion
        self.father = False
        self.mother = False
        self.female = female
        self.game_id = game_id
        self.spouses = { }

    def generate_son(self):
        import random
        has_son_age = random.randint(16, get_final_age(self.birth, self.death))
        son_birthdate = generate_date(birth[0] + has_son_age)
        son_id = assign_id('guys')
        global character_list
        character_list[son_id] = character()
        character_list[son_id].birth = son_birthdate
        character_list[son_id].father = self
        character_list[son_id].culture = self.culture
        character_list[son_id].religion = self.religion
        #mother
        global global_game_id
        global_game_id += 1
        character_list[son_id].game_id = global_game_id

    def generate_wife(self, last_wive_death_date = False):
        import random
        ## If there was no previous wife
        if last_wive_death_date is False:
            ## Will check if person dies before they're 30, so we don't have corpse bride
            death_age = get_final_age(self.birth, self.death)
            if death_age > 30:
                thirty_or_less = 30
            else:
                thirty_or_less = death_age
            var1 = random.randint(10, thirty_or_less)
            marry_year = self.birth[0] + var1
        else:
            marry_year = last_wive_death_date[0]+random.randint(1, 20)
        if marry_year >= self.death[0]-3:
            marry_year = self.death[0]-(random.randint(3, 8))
        marry_date = generate_date(marry_year)
        wife_age = random.randint(14, 35) #age when getting married/generated
        wife_birthdate = generate_date(marry_year-wife_age)
        wife_id = assign_id('gals')
        global character_list
        character_list[wife_id] = character(female = True)
        character_list[wife_id].birth = wife_birthdate
        character_list[wife_id].culture = self.culture
        character_list[wife_id].religion = self.religion
        #father and mother might go here
        spouses[marry_date] = character_list[wife_id]
        character_list[wife_id].spouses[marry_date] = self

    def generate_death(self):
        pass

def generate_date(year_in=starting_date[0]):
    import random
    month = random.randint(1, 12)
    day = random.randint(1, 30)
    date = list((year_in,month,day))
    return date

def get_final_age(birth,death):
    age = death[0]-birth[0]
    return age

def assign_id(id_type):
    global name_ids
    id_var = name_ids[id_type]
    name_ids[id_type] += 1
    return str(id_var)

def get_random_name(female = False):
    import random
    if femalse is True:
        name_list = (('Francine', 'Willhelmina', 'Sophia', 'Colette', 'Katerina', 'Brigitte', 'Margeritte'))
    else:
        name_list = (('Bart', 'Willhelm', 'Harold', 'John', 'Francis', 'Ryan', 'Winston','Brian','Konrad','Jason','Homer'))
    name = random.choice(name_list)
    return name

def gen_new_char():
    pass

name_ids = {
    'guys': 1,
    'gals': 300,
    'other': 800
}
global_game_id = 60000
character_list = {}

gen_new_char()
character_list[assign_id('guys')] = Character(culture='french')