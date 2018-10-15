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
        def history_province(province_dict, current_id=6, culture = "norse", religion = "catholic", tribal = 0, terrain = None):
            history_provinces_filename = str(current_id) + " - " + province_dict.get("county").lower()
            rel_path = "output\\history\\provinces\\" + history_provinces_filename + ".txt"
            import os
            os.makedirs(os.path.dirname(rel_path), exist_ok=True)
            with open(rel_path, "w") as file:
                file.write("# " + str(current_id) + " - " + province_dict.get("county") + "\n\n# County Title\n")
                file.write("title = c_" + province_dict.get("county").lower() + "\n\n")
                file.write("# Settlements\nmax_settlements = " + str(len(province_dict.keys())-1) + "\n")
                if ( tribal == 1 ):
                    file.write("b_" + province_dict.get("barony_1").lower() + " = tribal\n\n")
                    province.write.comment_overflow_baronies(province_dict,file,tribal)
                else:
                    file.write("b_" + province_dict.get("barony_1").lower() + " = castle\n")
                    file.write("b_" + province_dict.get("barony_2").lower() + " = city\n")
                    file.write("b_" + province_dict.get("barony_3").lower() + " = temple\n\n")
                    province.write.comment_overflow_baronies(province_dict,file)
                file.write("\n# Misc\nculture = " + culture + "\nreligion = " + religion + "\n")
                if terrain is not None:
                    file.write("terrain = " + terrain + "\n")
                file.write("\n# History\n")

        def comment_overflow_baronies(province_dict,file,tribal=0):
            if ( tribal == 1 ):
                num = 2
            else:
                num = 4
            for x in province_dict:
                province_dict_instance = province_dict.get("barony_" + str(num))
                if province_dict_instance is None:
                    break
                file.write("#b_" + province_dict_instance.lower() + "\n")
                num += 1

## Input
start_id = 12
in_culture = "norse"
in_religion = "catholic"
in_tribal = 0
in_terrain = None

## Execution
spreadsheet = open("provinces.csv", "r")
current_id = start_id
provinces = spreadsheet.readlines()
for x in provinces:
    province_dict = province.read.dictionary_creation(x)
    province.write.history_province(province_dict, current_id, in_culture, in_religion, in_tribal, in_terrain)
    current_id += 1