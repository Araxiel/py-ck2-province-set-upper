class configs(object):
    import os
    import configparser
    configfile_name = "config.ini"
    # Check if there is already a configurtion file
    if not os.path.isfile(configfile_name):
        print("Setting Up Config")
        import logging
        logging.info('Created Config')
        # Create the configuration file as it doesn't exist yet
        cfgfile = open(configfile_name, 'w')
        # Add content to the file
        config = configparser.ConfigParser()
        config.add_section('Basic')
        config.set('Basic', 'Version', '1.3.0')
        config.set('Basic', 'User', 'Willhelm')
        config.add_section('Last_Setup')
        config.set('Last_Setup', 'startID', '16')
        config.set('Last_Setup', 'Culture', 'Norse')
        config.set('Last_Setup', 'Religion', 'Catholic')
        config.set('Last_Setup', 'is_tribal', 'false')
        config.set('Last_Setup', 'terrain', 'Plains')
        config.set('Last_Setup', 'RGB_Basis', '(250,105,6)')
        config.set('Last_Setup', 'Last_File_ID', '50')
        config.set('Last_Setup', 'Last_fileName', 'None')
        config.write(cfgfile)
        cfgfile.close()

    def read_config(self,section,key):
        import configparser
        config = configparser.ConfigParser()
        config.read('config.ini')
        return config.get(section, key)

    def edit_config(self,section,key,new_value):
        import configparser
        config = configparser.ConfigParser()
        config.read('config.ini')
        config.set(section, key, new_value)
        with open('config.ini', 'w+') as configfile:
            config.write(configfile)