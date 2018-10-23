def characters_file_set_up():
    # super basic, will need logging and config and integration and UI and more
    rel_path = "Output\\history\\characters\\gen_characters.txt"
    import os
    os.makedirs(os.path.dirname(rel_path), exist_ok=True)
    open(rel_path, "w+")


def characters_file_writing(char_dictionary):
    rel_path = "Output\\history\\characters\\gen_characters.txt"
    import os
    os.makedirs(os.path.dirname(rel_path), exist_ok=True)
    with open(rel_path, "a") as file:
        file.write("# Generated\n")
        for char in char_dictionary:
            file.write("%s = {\n" % char_dictionary[char].game_id)
            file.write("    name = \"%s\"\n" % char_dictionary[char].name)
            file.write("    dynasty = \"%s\"\n" % char_dictionary[char].dynasty)
            file.write("    culture = \"%s\"\n" % char_dictionary[char].culture)
            if char_dictionary[char].father is False:
                pass
            else:
                file.write("    father = %i\n" % int(char_dictionary[char].father.game_id))
            if char_dictionary[char].mother is False:
                pass
            else:
                file.write("    mother = %i\n" % int(char_dictionary[char].mother.game_id))
            if char_dictionary[char].female is False:
                pass
            else:
                file.write("    female = yes\n")
            birth_date = char_dictionary[char].birth
            file.write("    %s.%s.%s = {\n        birth = yes\n" % (birth_date[0], birth_date[1], birth_date[2]))
            file.write("    }\n")
            if len(char_dictionary[char].spouses_list) > 0:
                for index, spouse in enumerate(char_dictionary[char].spouses_list):
                    marry_date = char_dictionary[char].spouses_marry_dates_list[index]
                    file.write("    %s.%s.%s = {\n        add_spouse = %s\n" % (
                        marry_date[0], marry_date[1], marry_date[2], spouse.game_id))
                    file.write("    }\n")
            file.write("    %s.%s.%s = {\n        death = yes\n" % (
                char_dictionary[char].death[0], char_dictionary[char].death[1], char_dictionary[char].death[2]))
            file.write("    }\n")
            file.write("}\n\n")


def title_holder_file_set_up():
    rel_path = "Output\\history\\characters\\__title_holder_placeholder.txt"
    import os
    os.makedirs(os.path.dirname(rel_path), exist_ok=True)
    open(rel_path, "w+")


def title_holder_file_writing(char_dictionary):
    rel_path = "Output\\history\\characters\\__title_holder_placeholder.txt"
    import os
    os.makedirs(os.path.dirname(rel_path), exist_ok=True)
    with open(rel_path, "a") as file:
        file.write("# Generated\n")
        for char in char_dictionary:
            if char_dictionary[char].title_holder is True:
                if char_dictionary[char].founder is True:
                    birth_date = char_dictionary[char].birth
                    file.write("%s.%s.%s = {\n" % (birth_date[0], birth_date[1], birth_date[2]))
                else:
                    birth_date = char_dictionary[char].father.death
                    file.write("%s.%s.%s = {\n" % (birth_date[0], birth_date[1], birth_date[2]))
                file.write("    holder = %i     # %s %s\n" % (char_dictionary[char].game_id, char_dictionary[char].name, char_dictionary[char].dynasty_name))
                file.write("}\n\n")
            pass
