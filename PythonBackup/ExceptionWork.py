from configparser import ConfigParser

# Created object of Configparser class
config = ConfigParser()

# To read data from config file
config.read("./InputFiles/Config.cfg")

print(config.get("Section", "username",))

