from workbench import workbench
from ui import MainWindow, UI_MainWindow

## Input
start_id = 12
in_culture = "norse"
in_religion = "catholic"
in_is_tribal = 0
in_terrain = "plains"
rgb_basis = (255, 102, 0)

## Execution
workbench.province.write.init_province_set_up()
workbench.province.write.init_landed_titles()
spreadsheet = open("provinces.csv", "r")
current_id = start_id
provinces = spreadsheet.readlines()
for x in provinces:
    province_dict = workbench.province.read.dictionary_creation(x)
    workbench.province.write.history_province(province_dict, current_id, in_culture, in_religion, in_is_tribal, in_terrain)
    workbench.province.write.history_titles(province_dict)
    workbench.province.write.province_set_up(province_dict, current_id, in_terrain)
    workbench.province.write.landed_titles(province_dict,rgb_basis)
    current_id += 1
