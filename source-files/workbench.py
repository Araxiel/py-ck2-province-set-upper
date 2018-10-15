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
            rel_path = "Output\\history\\provinces\\" + history_provinces_filename + ".txt"
            import os
            os.makedirs(os.path.dirname(rel_path), exist_ok=True)
            with open(rel_path, "w") as file:
                file.write("# " + str(current_id) + " - " + province_dict.get("county") + "\n\n# County Title\n")
                file.write("title = c_" + province_dict.get("county").lower() + "\n\n")
                file.write("# Settlements\nmax_settlements = " + str(len(province_dict.keys())-1) + "\n")
                if ( tribal == 1 ):
                    file.write(province_dict.get("barony_1") + " = tribal\n\n")
                    province.write.comment_overflow_baronies(province_dict,file)
                else:
                    file.write(province_dict.get("barony_1") + " = castle\n")
                    file.write(province_dict.get("barony_2") + " = city\n")
                    file.write(province_dict.get("barony_3") + " = temple\n\n")
                    province.write.comment_overflow_baronies(province_dict,file)
                file.write("\n# Misc\nculture = " + culture + "\nreligion = " + religion + "\n")
                if terrain is not None:
                    file.write("terrain = " + terrain + "\n")
                file.write("\n# History\n")

        def comment_overflow_baronies(province_dict,file):
            num = 4
            for x in province_dict:
                province_dict_instance = province_dict.get("barony_" + str(num))
                if province_dict_instance is None:
                    break
                file.write("#" + province_dict_instance + "\n")
                num += 1


## Input
in_province_line = "Carcossa;b_carcossa;b_arkham;b_rylhe;b_stratham;x"
in_start_id = 12
in_culture = "norse"
in_religion = "catholic"
in_tribal = 0

## Execution
province_dict = province.read.dictionary_creation(in_province_line)
print(province_dict)
province.write.history_province(province_dict, in_start_id, in_culture, in_religion, in_tribal, terrain = "steppes")