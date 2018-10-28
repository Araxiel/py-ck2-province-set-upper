# Ugh...this is a complete effing mess and will require a huge cleanup...but already addressed that in #37.
# Also needs to have the validator run through this; so many errors and problematic code

class province():
    class read():
        def dictionary_creation(province_line):
            """
            Takes one line and turns it into the current dictionary.
            """
            province_elements = province_line.split(';')
            province_elements.remove('\n')
            province_elements = [x for x in province_elements if x]
            province_dict = dict(
                county = province_elements[0],
                barony_1 = province_elements[1],
            )
            num = 2
            for x in province_elements[2:]:
                province_dict["barony_" + str(num)] = province_elements[num]
                num += 1
            return province_dict;

        class flags():

            def shuffle_flag_list():
                """
                Creates a list of all flags in the database and shuffles them.
                """
                import os
                import random
                flag_list_original = os.listdir("Databases\\Flags")
                global flag_list_current
                flag_list_current = flag_list_original.copy()
                random.shuffle(flag_list_current)
                global current_flag_number
                current_flag_number = 0
                import logging
                logging.info("Flag Order %s", flag_list_current)

    class write():

        class history():

            def history_province(province_dict, current_id=6, culture = "norse", religion = "catholic", is_tribal = False, terrain = None):
                """
                Writes the history/provinces file.
                """
                underscored_name = province.write.underscore_name(province_dict.get("county"))
                history_provinces_filename = str(current_id) + " - " + underscored_name
                rel_path = "Output\\history\\provinces\\" + history_provinces_filename + ".txt"
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                with open(rel_path, "w") as file:
                    file.write("# " + str(current_id) + " - " + province_dict.get("county") + "\n\n# County Title\n")
                    file.write("title = c_" + underscored_name + "\n\n")
                    file.write("# Settlements\nmax_settlements = " + str(len(province_dict.keys())-1) + "\n")
                    if ( is_tribal == True ):
                        file.write("b_" + province_dict.get("barony_1").lower().replace(" ", "_") + " = is_tribal\n\n")
                        province.write.comment_overflow_baronies(province_dict,file,is_tribal)
                    else:
                        file.write("b_" + province_dict.get("barony_1").lower().replace(" ", "_") + " = castle\n")
                        file.write("b_" + province_dict.get("barony_2").lower().replace(" ", "_") + " = city\n")
                        file.write("b_" + province_dict.get("barony_3").lower().replace(" ", "_") + " = temple\n\n")
                        province.write.history.comment_overflow_baronies(province_dict,file,is_tribal)
                    file.write("\n# Misc\nculture = " + culture + "\nreligion = " + religion + "\n")
                    if terrain is not None:
                        file.write("terrain = " + terrain + "\n")
                    file.write("\n# History\n")
                import logging
                logging.info("Province History written: %s", rel_path)

            def comment_overflow_baronies(province_dict,file,is_tribal=False):
                """
                Appends the commented-out baronies.
                """
                if ( is_tribal == True ):
                    num = 2
                else:
                    num = 4
                for x in province_dict:
                    province_dict_instance = province_dict.get("barony_" + str(num))
                    if province_dict_instance is None:
                        break
                    file.write("#b_" + province_dict_instance.lower().replace(" ", "_") + "\n")
                    num += 1

            def history_titles(province_dict):
                """
                Creates (empty) history/titles files.
                """
                history_titles_filename = "c_" + province_dict.get("county").lower().replace(" ", "_")
                rel_path = "Output\\history\\titles\\" + history_titles_filename + ".txt"
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                open(rel_path, "w")

        class common():

            def init_province_set_up():
                """
                Creates the common/province setup file.
                """
                from _workbench import configs
                config_obj = configs.configs()
                last_file_id = config_obj.read_config('Last_Setup', 'Last_File_ID')
                rel_path = "Output\\common\\province_setup\\%(number)s_province_setup.txt" %{'number':last_file_id}
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                open(rel_path, "w")
                import logging
                logging.info("Init province-setup %s", rel_path)

            def province_set_up(province_dict, current_id=6, terrain="plains"):
                """
                Writes to the common/province setup file.
                """
                from _workbench import configs
                config_obj = configs.configs()
                last_file_id = config_obj.read_config('Last_Setup', 'Last_File_ID')
                rel_path = "Output\\common\\province_setup\\%(number)s_province_setup.txt" %{'number':last_file_id}
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                with open(rel_path, "a") as file:
                    file.write(str(current_id) + " = {\n")
                    file.write("    title = c_" + province_dict.get("county").lower().replace(" ", "_") + "\n")
                    file.write("    max_settlements = " + str(len(province_dict.keys())-1) + "\n")
                    file.write("    terrain = " + terrain + "\n}\n")
                import logging
                logging.info("Province-Setup: c_%s", province_dict.get("county").lower().replace(" ", "_"))

            def init_landed_titles():
                """
                Creates the common/landed titles file.
                """
                from _workbench import configs
                config_obj = configs.configs()
                last_file_id = config_obj.read_config('Last_Setup', 'Last_File_ID')
                rel_path = "Output\\common\\landed_titles\\%(number)s_landed_titles.txt" %{'number':last_file_id}
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                open(rel_path, "w")
                import logging
                logging.info("Init landed titles %s", rel_path)

            def landed_titles(province_dict, rgb_basis = (255, 102, 0)):
                """
                Writes to the common/landed titles.
                """
                from _workbench import configs
                config_obj = configs.configs()
                last_file_id = config_obj.read_config('Last_Setup', 'Last_File_ID')
                rel_path = "Output\\common\\landed_titles\\%(number)s_landed_titles.txt" %{'number':last_file_id}
                rgb_value = utilities.randomise_colors(rgb_basis)
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                with open(rel_path, "a") as file:
                    file.write("c_" + province_dict.get("county").lower().replace(" ", "_") + " = {\n")
                    num = 1
                    for x in province_dict:
                        province_dict_instance = province_dict.get("barony_" + str(num))
                        if province_dict_instance is None:
                            break
                        file.write("    b_" + province_dict_instance.lower().replace(" ", "_") + " = { }\n")
                        num += 1
                    file.write("    color = { " + str(rgb_value[0]) +" "+ str(rgb_value[1]) +" "+ str(rgb_value[2]) + " }  # rgb" + str(rgb_value) + "\n")
                    file.write("    color2 = { " + str(rgb_basis[0]) +" "+ str(rgb_basis[1]) +" "+ str(rgb_basis[2]) + " } \n")
                    file.write("}\n")
                import logging
                logging.info("Landed Titles for %s - RGB: %s", province_dict.get("county"), rgb_value)

        class loc():

            def init_loc():
                """
                Writes the localisation file.
                """
                from _workbench import configs
                config_obj = configs.configs()
                last_file_id = config_obj.read_config('Last_Setup', 'Last_File_ID')
                rel_path = "Output\\localisation\\%(number)s_province_setup.csv" %{'number':last_file_id}
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                open(rel_path, "w")
                with open(rel_path, "a") as file:
                    file.write("#CODE;ENGLISH;FRENCH;GERMAN;;SPANISH;;;;;;;;;x\n")
                import logging
                logging.info("Init localisation %s", rel_path)

            def locs(province_dict,current_id):
                """
                Populate the localisation file.
                """
                from _workbench import configs
                config_obj = configs.configs()
                last_file_id = config_obj.read_config('Last_Setup', 'Last_File_ID')
                rel_path = "Output\\localisation\\%(number)s_province_setup.csv" %{'number':last_file_id}
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                with open(rel_path, "a") as file:
                    county_name = province_dict.get("county")
                    county_name_adj = province.write.loc.adjective(county_name)
                    file.write("PROV"+str(current_id)+";"+county_name+";"+county_name+";"+county_name+";;"+county_name+";;;;;;;;;\n")
                    file.write("c_"+ county_name.lower().replace(" ", "_")+";"+county_name+";"+county_name+";"+county_name+";;"+county_name+";;;;;;;;;\n")
                    file.write("c_"+ county_name.lower().replace(" ", "_")+"_adj;"+county_name_adj+";"+county_name_adj+";"+county_name_adj+";;"+county_name_adj+";;;;;;;;;\n")
                    loc_lines_added = 3
                    num = 1
                    for each in province_dict:
                        province_dict_instance = province_dict.get("barony_" + str(num))
                        if province_dict_instance is None:
                            break
                        file.write("b_" + province_dict_instance.lower().replace(" ", "_") + ";"+province_dict_instance+";"+province_dict_instance+";"+province_dict_instance+";;"+province_dict_instance+";;;;;;;;;\n")
                        num += 1
                        loc_lines_added += 1
                import logging
                logging.info("Localisation %s lines=%i", rel_path, loc_lines_added)

            def adjective(name):
                """
                Adds an appropiate adjective to the end based on the word's ending.
                """
                import random
                if name[-2:] in "ia" or name[-2:] in "um":
                    adj_final = name[:-2]
                    if adj_final[-1:] is "l" or adj_final[-1:] is "i":
                        adj_final = adj_final + "an"
                elif name[-2:] in "en" or name[-1:] in "t" or name[-1:] in "n":
                    adj_final = name + "er"
                elif name[-1:] in "i":
                    endings = tuple(("n", "an"))
                    adj_final = name + random.choice(endings)
                elif name[-1:] in "o":
                    endings = "nian"
                    adj_final = name + endings
                elif name[-1:] in "k" or name[-1:] in "s" or name[-1:] in "c":
                    endings = "ian"
                    adj_final = name + endings
                elif name[-2:] in "?a" and not (name[-2:] in "ia"):
                    endings = tuple(("ni", "nian", "n", "ese"))
                    adj_final = name + random.choice(endings)
                elif name[-1:] in "e":
                    endings = tuple(("ch", "an"))
                    select_ending = random.choice(endings)
                    if select_ending in "ch":
                        name = name[:-2]
                    else:
                        pass
                    adj_final = name + select_ending
                elif name[-1:] in "y":
                    endings = tuple(("ssios", "ian", "ese"))
                    select_ending = random.choice(endings)
                    if select_ending in "ese":
                        name = name[:-1]
                    else:
                        pass
                    adj_final = name + select_ending
                else:
                    adj_final = name
                return adj_final

        class flags():

            def select_flag():
                """
                Reads the current list of flags, moves it along by 1; checks if at the end and creates new list.
                """
                global current_flag_number
                global flag_list_current
                if current_flag_number < len(flag_list_current):
                    current_flag = flag_list_current[current_flag_number]
                    current_flag_number += 1
                    return current_flag
                else:
                    province.read.flags.shuffle_flag_list()
                    current_flag = province.write.flags.select_flag()
                    return current_flag

            def assign_flag(province_dict,flag_removal):
                """
                Creates the flag.
                """
                import shutil
                import os
                import logging
                flag_file_name = "c_" + province_dict.get("county").lower().replace(" ", "_") + ".tga"  # c_carcossa.tga
                rel_path = "Output\\gfx\\flags\\"
                rel_file_path = rel_path + flag_file_name   #  "Output\\gfx\\flags\\c_carcossa.tga"
                os.makedirs(os.path.dirname(rel_file_path), exist_ok=True)  # create folder
                current_flag = province.write.flags.select_flag()   # "placeholder_7.tga"
                copy_file_location = ("Databases\\Flags\\" + current_flag)  # "Databases\\Flags\\placeholder7.tga"
                shutil.copyfile(copy_file_location, rel_file_path)  # copies "Databases\\Flags\\placeholder7.tga" as "Output\\gfx\\flags\\c_carcossa,tga"
                if flag_removal is True:
                    rel_path = "Databases\\Flags\\Removed\\"
                    rel_file_path = rel_path + flag_file_name  # "Databases\\Flags\\Removed\\c_carcossa.tga"
                    os.makedirs(os.path.dirname(rel_file_path), exist_ok=True)  # create folder
                    print(copy_file_location + " ~~~ " +  rel_file_path)
                    os.replace(copy_file_location, rel_file_path)  # moves-renames "Databases\\Flags\\placeholder7.tga" as "Databases\\Flags\\Removed\\c_carcossa.tga"
                logging.info("%s was used for %s", current_flag, province_dict.get("county"))


        def underscore_name(object_name) -> object:
            """
            Tiny utility that simply turns spaces into underlines.
            """
            return object_name.replace(" ", "_").lower()

class utilities():
    def randomise_color(value = 100):
        """
        Creates a single randomised RGB value.
        """
        import random
        if value < 50:
            rng_up_ceiling = 45
        else:
            rng_up_ceiling = 20
        v_up = random.randrange(0, rng_up_ceiling, 1)
        if value > 235:
            rng_down_ceiling = 45
        else:
            rng_down_ceiling = 20
        v_down = (random.randrange(0, rng_down_ceiling, 1))*-1
        value += v_up + v_down
        if value > 255:
                value = 255
        if value < 0:
                value = 0
        return value
    def randomise_colors(rgb_basis):
        """
        Randomised a whole RGB colour.
        """
        r_base = rgb_basis[0]
        r = utilities.randomise_color(r_base)
        g_base = rgb_basis[1]
        g = utilities.randomise_color(g_base)
        b_base = rgb_basis[2]
        b = utilities.randomise_color(b_base)
        rgb_value = tuple((r,g,b))
        return rgb_value

class execute():

    def write(fileName, startID=6, culture="Norse", religion="Catholic",  is_tribal=False,  terrain="Plains",  rgb_basis=(255, 102, 0),flag_removal = False):
        """
        The actual script compiling all the other stuff.
        """
        import logging
        province.write.common.init_province_set_up()
        province.write.common.init_landed_titles()
        province.write.loc.init_loc()
        province.read.flags.shuffle_flag_list()
        spreadsheet = open(fileName, "r")
        current_id = startID
        provinces = spreadsheet.readlines()
        for x in provinces:
            province_dict = province.read.dictionary_creation(x)
            logging.info("Started with  %s", x[:-2])
            province.write.history.history_province(province_dict, current_id, culture.lower(), religion.lower(), is_tribal, terrain.lower())
            province.write.history.history_titles(province_dict)
            province.write.common.province_set_up(province_dict, current_id, terrain)
            province.write.common.landed_titles(province_dict,rgb_basis)
            province.write.loc.locs(province_dict,current_id)
            province.write.flags.assign_flag(province_dict,flag_removal)
            current_id += 1
            logging.info("Finished with  %s", province_dict)

        logging.info('-- Finished Writing -- ')