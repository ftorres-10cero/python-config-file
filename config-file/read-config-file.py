import configparser  # Requiere la instalación de la librería configparser (pip install configparser)

# Load the configuration file
config = configparser.ConfigParser()
config.read('config.ini')

# List all contents
print("List all contents")
print(config.sections())
for section in config.sections():
    print("Section: %s" % section)
    for options in config.options(section):
        print("  %s:::%s:::%s" % (options,
                                  config.get(section, options),
                                  str(type(options))))

# Print some contents
print("\nPrint some contents")
print(config.get('other', 'use_anonymous'))  # Just get the value
print(config.getboolean('other', 'use_anonymous'))  # You know the datatype?