class province():
    class read():
        def dictionary_creation(province_line):
            "Takes one line and turns it into a dictionary"
            province_elements = province_line.split(';')
            province_dict = dict(
                county = province_elements[0],
                barony_1 = province_elements[1],
            )
            num = 2
            for x in province_elements[2:]:
                if x == "x":
                    break
                province_dict["barony_" + str(num)] = province_elements[num]
                num += 1
            return province_dict;

        class flags():

            def shuffle_flag_list():
                import os
                import random
                flag_list_original = os.listdir("Databases\\Flags")
                global flag_list_current
                flag_list_current = flag_list_original.copy()
                random.shuffle(flag_list_current)
                global current_flag_number
                current_flag_number = 0

    class write():

        class history():

            def history_province(province_dict, current_id=6, culture = "norse", religion = "catholic", is_tribal = False, terrain = None):
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

            def comment_overflow_baronies(province_dict,file,is_tribal=False):
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
                history_titles_filename = "c_" + province_dict.get("county").lower().replace(" ", "_")
                rel_path = "Output\\history\\titles\\" + history_titles_filename + ".txt"
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                open(rel_path, "w")

        class common():

            def init_province_set_up():
                rel_path = "Output\\common\\province_setup\\90_province_setup.txt"
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                open(rel_path, "w")

            def province_set_up(province_dict, current_id=6, terrain="plains"):
                rel_path = "Output\\common\\province_setup\\90_province_setup.txt"
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                with open(rel_path, "a") as file:
                    file.write(str(current_id) + " = {\n")
                    file.write("    title = c_" + province_dict.get("county").lower().replace(" ", "_") + "\n")
                    file.write("    max_settlements = " + str(len(province_dict.keys())-1) + "\n")
                    file.write("    terrain = " + terrain + "\n}\n")

            def init_landed_titles():
                rel_path = "Output\\common\\landed_titles\\90_landed_titles.txt"
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                open(rel_path, "w")

            def landed_titles(province_dict, rgb_basis = (255, 102, 0) ):
                rgb_value = randomise.randomise_colors(rgb_basis)
                rel_path = "Output\\common\\landed_titles\\90_landed_titles.txt"
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

        class loc():

            def init_loc():
                rel_path = "Output\\localisation\\90_province_setup.csv"
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                open(rel_path, "w")
                with open(rel_path, "a") as file:
                    file.write("#CODE;ENGLISH;FRENCH;GERMAN;;SPANISH;;;;;;;;;x\n")

            def locs(province_dict,current_id):
                rel_path = "Output\\localisation\\90_province_setup.csv"
                import os
                os.makedirs(os.path.dirname(rel_path), exist_ok=True)
                with open(rel_path, "a") as file:
                    county_name = province_dict.get("county")
                    county_name_adj = province.write.loc.adjective(county_name)
                    file.write("PROV"+str(current_id)+";"+county_name+";"+county_name+";"+county_name+";;"+county_name+";;;;;;;;;\n")
                    file.write("c_"+ county_name.lower().replace(" ", "_")+";"+county_name+";"+county_name+";"+county_name+";;"+county_name+";;;;;;;;;\n")
                    file.write("c_"+ county_name.lower().replace(" ", "_")+"_adj;"+county_name_adj+";"+county_name_adj+";"+county_name_adj+";;"+county_name_adj+";;;;;;;;;\n")
                    num = 1
                    for x in province_dict:
                        province_dict_instance = province_dict.get("barony_" + str(num))
                        if province_dict_instance is None:
                            break
                        file.write("b_" + province_dict_instance.lower().replace(" ", "_") + ";"+province_dict_instance+";"+province_dict_instance+";"+province_dict_instance+";;"+province_dict_instance+";;;;;;;;;\n")
                        num += 1

            def adjective(name):
                adj_final = name + "n"
                return adj_final

        class flags():

            def select_flag():
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

            def assign_flag(province_dict):
                import shutil
                import os
                flag_file_name = "c_" + province_dict.get("county").lower().replace(" ", "_") + ".tga"
                rel_path = "Output\\gfx\\flags\\"
                rel_file_path = rel_path + flag_file_name
                os.makedirs(os.path.dirname(rel_file_path), exist_ok=True)
                current_flag = province.write.flags.select_flag()
                shutil.copyfile("flags\\" + current_flag, rel_file_path)

        def underscore_name(object_name) -> object:
            return object_name.replace(" ", "_").lower()

class utilities():
    def randomise_color(value = 100):
        import random
        if value < 50:
            rng_up_ceiling = 60
        else:
            rng_up_ceiling = 20
        v_up = random.randrange(0, rng_up_ceiling, 1)
        if value > 235:
            rng_down_ceiling = 60
        else:
            rng_down_ceiling = 20
        v_down = random.randrange(0, rng_down_ceiling, 1)
        v_down *= -1
        value += v_up + v_down
        if value > 255:
                value = 255
        if value < 0:
                value = 0
        return value
    def randomise_colors(rgb_basis):
        r_base = rgb_basis[0]
        r = utilities.randomise_color(r_base)
        g_base = rgb_basis[1]
        g = utilities.randomise_color(g_base)
        b_base = rgb_basis[2]
        b = utilities.randomise_color(b_base)
        rgb_value = tuple((r,g,b))
        return rgb_value
        
class execute():
    def write(fileName, startID=6, culture="Norse", religion="Catholic",  is_tribal=False,  terrain="Plains",  rgb_basis=(255, 102, 0)):
        province.write.common.init_province_set_up()
        province.write.common.init_landed_titles()
        province.write.loc.init_loc()
        province.read.flags.shuffle_flag_list()
        rgb_basis_tuple = tuple((255, 102, 0))
        spreadsheet = open(fileName, "r")
        current_id = startID
        provinces = spreadsheet.readlines()
        for x in provinces:
            province_dict = province.read.dictionary_creation(x)
            province.write.history.history_province(province_dict, current_id, culture.lower(), religion.lower(), is_tribal, terrain.lower())
            province.write.history.history_titles(province_dict)
            province.write.common.province_set_up(province_dict, current_id, terrain)
            province.write.common.landed_titles(province_dict,rgb_basis_tuple)
            province.write.loc.locs(province_dict,current_id)
            province.write.flags.assign_flag(province_dict)
            current_id += 1