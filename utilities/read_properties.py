import configparser

config = configparser.RawConfigParser()  # Create a RawConfigParser object to read the configuration file
config.read('./config.ini')

class ReadConfig:

    @staticmethod
    def get_base_url(app_name, env=None):
        return config.get(app_name, env)
    
    
    
    