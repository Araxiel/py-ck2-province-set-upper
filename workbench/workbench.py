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
    class write():
        def history_province(province_dict, current_id=6, culture = "norse", religion = "catholic", is_tribal = 0, terrain = None):
            history_provinces_filename = str(current_id) + " - " + province_dict.get("county").lower()
            rel_path = "output\\history\\provinces\\" + history_provinces_filename + ".txt"
            import os
            os.makedirs(os.path.dirname(rel_path), exist_ok=True)
            with open(rel_path, "w") as file:
                file.write("# " + str(current_id) + " - " + province_dict.get("county") + "\n\n# County Title\n")
                file.write("title = c_" + province_dict.get("county").lower() + "\n\n")
                file.write("# Settlements\nmax_settlements = " + str(len(province_dict.keys())-1) + "\n")
                if ( is_tribal == 1 ):
                    file.write("b_" + province_dict.get("barony_1").lower() + " = is_tribal\n\n")
                    province.write.comment_overflow_baronies(province_dict,file,is_tribal)
                else:
                    file.write("b_" + province_dict.get("barony_1").lower() + " = castle\n")
                    file.write("b_" + province_dict.get("barony_2").lower() + " = city\n")
                    file.write("b_" + province_dict.get("barony_3").lower() + " = temple\n\n")
                    province.write.comment_overflow_baronies(province_dict,file,is_tribal)
                file.write("\n# Misc\nculture = " + culture + "\nreligion = " + religion + "\n")
                if terrain is not None:
                    file.write("terrain = " + terrain + "\n")
                file.write("\n# History\n")

        def comment_overflow_baronies(province_dict,file,is_tribal=0):
            if ( is_tribal == 1 ):
                num = 2
            else:
                num = 4
            for x in province_dict:
                province_dict_instance = province_dict.get("barony_" + str(num))
                if province_dict_instance is None:
                    break
                file.write("#b_" + province_dict_instance.lower() + "\n")
                num += 1

        def history_titles(province_dict):
            history_titles_filename = "c_" + province_dict.get("county").lower()
            rel_path = "output\\history\\titles\\" + history_titles_filename + ".txt"
            import os
            os.makedirs(os.path.dirname(rel_path), exist_ok=True)
            open(rel_path, "w")

        def init_province_set_up():
            rel_path = "output\\common\\province_setup\\0x_province_setup.txt"
            import os
            os.makedirs(os.path.dirname(rel_path), exist_ok=True)
            open(rel_path, "w")

        def province_set_up(province_dict, current_id=6, terrain="plains"):
            rel_path = "output\\common\\province_setup\\0x_province_setup.txt"
            import os
            os.makedirs(os.path.dirname(rel_path), exist_ok=True)
            with open(rel_path, "a") as file:
                file.write(str(current_id) + " = {\n")
                file.write("    title = c_" + province_dict.get("county").lower() + "\n")
                file.write("    max_settlements = " + str(len(province_dict.keys())-1) + "\n")
                file.write("    terrain = " + terrain + "\n}\n")

        def init_landed_titles():
            rel_path = "output\\common\\landed_titles\\0x_landed_titles.txt"
            import os
            os.makedirs(os.path.dirname(rel_path), exist_ok=True)
            open(rel_path, "w")

        def landed_titles(province_dict, rgb_basis = (255, 102, 0) ):
            rgb_value = randomise.randomise_colors(rgb_basis)
            rel_path = "output\\common\\landed_titles\\0x_landed_titles.txt"
            import os
            os.makedirs(os.path.dirname(rel_path), exist_ok=True)
            with open(rel_path, "a") as file:
                file.write("c_" + province_dict.get("county").lower() + " = {\n")
                num = 1
                for x in province_dict:
                    province_dict_instance = province_dict.get("barony_" + str(num))
                    if province_dict_instance is None:
                        break
                    file.write("    b_" + province_dict_instance.lower() + " = { }\n")
                    num += 1
                file.write("    color = { " + str(rgb_value[0]) +" "+ str(rgb_value[1]) +" "+ str(rgb_value[2]) + " }  # rgb" + str(rgb_value) + "\n")
                file.write("    color2 = { " + str(rgb_basis[0]) +" "+ str(rgb_basis[1]) +" "+ str(rgb_basis[2]) + " } \n")
                file.write("}\n")

class randomise():
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
        return value
    def randomise_colors(rgb_basis):
        r_base = rgb_basis[0]
        r = randomise.randomise_color(r_base)
        g_base = rgb_basis[1]
        g = randomise.randomise_color(g_base)
        b_base = rgb_basis[2]
        b = randomise.randomise_color(b_base)
        rgb_value = tuple((r,g,b))
        return rgb_value