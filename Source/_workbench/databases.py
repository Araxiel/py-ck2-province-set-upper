class geodata():
    global geonames_username
    geonames_username = 'ck2_setupper'
    def get_towns(country):
        import geocoder
        global geonames_username
        a = geocoder.geonames(country, key=geonames_username)
        #print("a:   " +str(a))
        b = geocoder.geonames(a.geonames_id, key=geonames_username, method='children')
        #print(list(b))
        import random
        b_r = random.choice(b)
        #print("b:   " +str(b_r))
        c = geocoder.geonames(b_r.geonames_id, key=geonames_username, method='children')
        #print(list(c))
        if c:
            c_r = random.choice(c)
            #print("c list:  " + str(list(c)))
            #print("c:    " + str(c_r))
            d = geocoder.geonames(c_r.geonames_id, key=geonames_username, method='children')
            if d:
                d = geocoder.geonames(c_r.geonames_id, key=geonames_username, method='children')
                if d:
                    d_r = random.choice(d)
                    #print("d list:  "+str(list(d)))
                    #print("d:    " + str(d_r))
                    e = geocoder.geonames(d_r.geonames_id, key=geonames_username, method='children')
                    #print(list(e))
                    return list(e)
                else:
                    return list(d)
            else:
                return list(c)
        else:
            return list(b)

    def smallest_child(towns):
        import geocoder
        import random
        import workbench
        global geonames_username
        if towns:
            municipality = random.choice(towns)
            print("municipality:   "+str(municipality))
            villages = geocoder.geonames(municipality.geonames_id, key=geonames_username, method='children')
            if villages:
                #print(list(villages))
                village = random.choice(villages)
                #print("village:   "+str(village))
                return village
            else:
                return municipality
        else:
            return towns

    def random_replacer(entry_list,country):
        import workbench
        province_elements = workbench.province.read.dictionary_creation(entry_list)
        for value in province_elements:
            if province_elements[value] not in "!R":
                pass
            else:
                entry = geodata.smallest_child(geodata.get_towns(country))
                entry = workbench.utilities.remove_bracket(entry)
                province_elements[value] = str(entry)
        return province_elements


debug_list_string = "Miskatonic;Arkhem;Salem;Ipswich;!R;!R"
country = 'United Kingdom'

print(geodata.random_replacer(debug_list_string,country))