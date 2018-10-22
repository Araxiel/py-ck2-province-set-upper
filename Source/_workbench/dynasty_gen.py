starting_date = list((806, 6, 16))


class Character(object):

    def generate_death(self):
        import random
        death_ages_container = [random.randint(0, 20)]
        for x in range(0, 8):
            death_ages_container.append(random.randint(20, 60))
        for x in range(0, 2):
            death_ages_container.append(random.randint(60, 80))
        final_age = random.choice(death_ages_container)
        death_year = self.birth[0] + final_age
        self.death = daterizer(death_year)

    def __init__(self, name=False, dynasty=756, culture='saxon', religion='catholic', birth=(1025, 1, 2),
                 death=(1066, 10, 14), female=False, game_id=60000):
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
        self.generate_death()

    def generate_child(self, female=False):
        import random
        has_child_age = random.randint(16, get_final_age(self.birth, self.death))
        child_birth_date = daterizer(self.birth[0] + has_child_age)
        child_id = assign_id('guys')
        global character_list
        character_list[child_id] = Character()
        character_list[child_id].birth = child_birth_date
        character_list[child_id].father = self
        character_list[child_id].culture = self.culture
        character_list[child_id].religion = self.religion
        if len(self.spouses_list) > 0:
            for index, item in enumerate(self.spouses_marry_dates_list):
                print(self.spouses_list[index])
                if item[0] > child_birth_date[0]:
                    character_list[child_id].mother = self.spouses_list[index]
                    break
        global global_game_id
        global_game_id += 1
        character_list[child_id].game_id = global_game_id
        self.children_list.append(character_list[child_id])
        character_list[child_id].female = female

    def generate_wife(self, last_wive_death_date=(0, 0, 0)):
        import random
        # If there was no previous wife
        if last_wive_death_date[0] is 0:
            # Will check if person dies before they're 30, so we don't have corpse bride
            death_age = get_final_age(self.birth, self.death)
            if death_age > 30:
                thirty_or_less = 30
            else:
                thirty_or_less = death_age
            var1 = random.randint(10, thirty_or_less)
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
        # father and mother might go here
        self.spouses_list.append(character_list[wife_id])
        self.spouses_marry_dates_list.append(marry_date)


def daterizer(year_in=starting_date[0]):
    import random
    month = random.randint(1, 12)
    day = random.randint(1, 30)
    date = list((year_in, month, day))
    return date


def get_final_age(birth, death):
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


def gen_new_guy(name=False, dynasty=756, culture='saxon', religion='catholic', birth=(1025, 1, 2), death=(1066, 10, 14),
                female=False, game_id=60000):
    import random
    char_number = assign_id('guys')
    character_list[char_number] = Character(name, dynasty, culture, religion, birth, death, female, game_id)
    character_list[char_number].generate_wife()
    for x in range(0, random.randint(1, 8)):
        character_list[char_number].generate_child()


name_ids = {
    'guys': 1,
    'gals': 300,
    'other': 800
}
global_game_id = 60000
character_list = {}

gen_new_guy()


def init_province_set_up():
    from _workbench import configs
    config_obj = configs.configs()
    last_file_id = config_obj.read_config('Last_Setup', 'Last_File_ID')
    rel_path = "Output\\common\\province_setup\\%(number)s_province_setup.txt" % {'number': last_file_id}
    import os
    os.makedirs(os.path.dirname(rel_path), exist_ok=True)
    open(rel_path, "w")
    import logging
    logging.info("Init province-setup %s", rel_path)


def province_set_up(province_dict, current_id=6, terrain="plains"):
    from _workbench import configs
    config_obj = configs.configs()
    last_file_id = config_obj.read_config('Last_Setup', 'Last_File_ID')
    rel_path = "Output\\common\\province_setup\\%(number)s_province_setup.txt" % {'number': last_file_id}
    import os
    os.makedirs(os.path.dirname(rel_path), exist_ok=True)
    with open(rel_path, "a") as file:
        file.write(str(current_id) + " = {\n")
        file.write("    title = c_" + province_dict.get("county").lower().replace(" ", "_") + "\n")
        file.write("    max_settlements = " + str(len(province_dict.keys()) - 1) + "\n")
        file.write("    terrain = " + terrain + "\n}\n")
    import logging
    logging.info("Province-Setup: c_%s", province_dict.get("county").lower().replace(" ", "_"))