import dynasty_write

class Character(object):

    def generate_death(self, essential=True):
        import random
        if essential is False:
            min_age = 0
        else:
            # print(self.name + " es: " + str(essential))
            min_age = 18
        death_ages_container = [random.randint(min_age, min_age + 8)]
        for x in range(0, 8):
            death_ages_container.append(random.randint(25, 60))
        for x in range(0, 2):
            death_ages_container.append(random.randint(65, 80))
        # print(self.name + " dc: " + str(death_ages_container))
        final_age = random.choice(death_ages_container)
        # print(self.name + " fa: " + str(final_age))
        death_year = self.birth[0] + final_age
        self.death = daterizer(death_year)

    def __init__(self, name=False, dynasty=756, culture='saxon', religion='catholic', birth=(1025, 1, 2),
                 death=(1066, 10, 14), female=False, game_id=60000, essential=True, main_heir=None):
        if birth is None:
            birth = [1025, 1, 2]
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
        self.spouses_list = []
        self.spouses_marry_dates_list = []
        self.children_list = []
        self.essential = essential
        self.generate_death(essential=essential)
        self.main_heir = main_heir
        self.last_child_date = None

    def generate_child(self, female=False, essential=False):
        import random
        if not self.children_list:
            print("No Kids")
            has_first_child_age = random.randint(17, get_age_to_death(self.birth, self.death))
            child_birth_date = daterizer(self.birth[0] + has_first_child_age)
        else:
            print("Already has Kids")
            var = random.randint(4, get_age_to_death(self.last_child_date, self.death))
            child_birth_date = daterizer(self.last_child_date[0] + var)
        child_id = assign_id('guys')
        global character_list
        character_list[child_id] = Character(essential=essential)
        character_list[child_id].birth = child_birth_date
        character_list[child_id].father = self
        character_list[child_id].culture = self.culture
        character_list[child_id].religion = self.religion
        if len(self.spouses_list):
            for index, item in enumerate(self.spouses_marry_dates_list):
                if item[0] < child_birth_date[0]:
                    character_list[child_id].mother = self.spouses_list[index]
                    break
        global global_game_id
        global_game_id += 1
        character_list[child_id].game_id = global_game_id
        self.children_list.append(character_list[child_id])
        character_list[child_id].female = female
        global last_char
        last_char = character_list[child_id]
        self.last_child_date = child_birth_date
        return character_list[child_id]

    def generate_wife(self, last_wive_death_date=None):
        import random
        # If there was no previous wife
        if not last_wive_death_date:
            # Will check if person dies before they're 30, so we don't have corpse bride
            death_age = get_age_to_death(self.birth, self.death)
            if death_age > 20:
                thirty_or_less = 20
            else:
                thirty_or_less = death_age
            var1 = random.randint(10, thirty_or_less + 10)
            marry_year = self.birth[0] + var1
        else:
            marry_year = last_wive_death_date[0] + random.randint(1, 20)
        if marry_year >= self.death[0] - 3:
            marry_year = self.death[0] - (random.randint(3, 8))
        marry_date = daterizer(marry_year)
        wife_age = random.randint(14, 35)  # age when getting married/generated
        wife_birth_date = daterizer(marry_year - wife_age)
        wife_id = assign_id('gals')
        global character_list
        character_list[wife_id] = Character(female=True, birth=wife_birth_date)
        character_list[wife_id].culture = self.culture
        character_list[wife_id].religion = self.religion
        character_list[wife_id].dynasty = 'none'
        global global_game_id
        global_game_id += 1
        character_list[wife_id].game_id = global_game_id
        # father and mother might go here
        self.spouses_list.append(character_list[wife_id])
        self.spouses_marry_dates_list.append(marry_date)
        character_list[wife_id].spouses_list.append(self)
        character_list[wife_id].spouses_marry_dates_list.append(marry_date)
        global last_char
        last_char = character_list[wife_id]
        return character_list[wife_id]


def daterizer(year_in=1025):
    import random
    month = random.randint(1, 12)
    day = random.randint(1, 30)
    date = list((year_in, month, day))
    return date


# noinspection SpellCheckingInspection
def wayback(base_year=1025, backtime=100):
    import random
    var = random.randint(backtime, backtime + 100)
    base_year -= var
    return daterizer(base_year)


def get_age_to_death(birth, death):
    age = death[0] - birth[0]
    return age


def assign_id(id_type):
    global name_ids
    id_var = name_ids[id_type]
    name_ids[id_type] += 1
    return str(id_var)


# noinspection SpellCheckingInspection
def get_random_name(female=False):
    import random
    if female is True:
        name_list = ('Francine', 'Willhelmina', 'Sophia', 'Colette', 'Katerina', 'Brigitte', 'Margeritte')
    else:
        name_list = (
            'Bart', 'Willhelm', 'Harold', 'John', 'Francis', 'Ryan', 'Winston', 'Brian', 'Konrad', 'Jason', 'Homer')
    name = random.choice(name_list)
    return name


def generate_character(name=False, dynasty=756, culture='saxon', religion='catholic', birth=(1025, 1, 2), death=None,
                female=False, game_id=60000, essential=True, founder=False, caller=None):
    if death is None:
        death = starting_date
    import random
    protagonist = caller
    if founder is True:
        char_number = assign_id('guys')
        character_list[char_number] = Character(name=name, dynasty=dynasty, culture=culture, religion=religion, birth=birth,
                                                death=death, female=female, game_id=game_id, essential=essential)
        protagonist = character_list[char_number]
    global last_char
    last_char = protagonist.generate_wife()
    last_char = protagonist.generate_child(essential=True)
    protagonist.main_heir = last_char
    #TODO amount of potential kids somehow tied to death-date
    boys_amount = random.randint(0, 1)
    for x in range(0, boys_amount):
        last_char = protagonist.generate_child()
    random_pick = random.choice(protagonist.children_list)
    random_pick.generate_child()
    girls_amount_weight = (0, 0, 0, 1, 1, 2)
    girls_amount = random.choice(girls_amount_weight)
    for x in range(0, girls_amount):
        last_char = protagonist.generate_child(female=True)
    last_char = protagonist
    return protagonist


global_game_id = 86540
starting_date = list((806, 6, 16))

name_ids = {
    'guys': 1000,
    'gals': 300000,
    'other': 9000000
}
character_list = {}

founder = generate_character(game_id=global_game_id, birth=wayback(starting_date[0], 100),founder=True)
print(len(founder.children_list))
last_char = generate_character(caller=founder.main_heir)
print(last_char.game_id)
print(len(last_char.children_list))

dynasty_write.characters_file_set_up()
dynasty_write.characters_file_writing(character_list)
