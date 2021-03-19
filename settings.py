#settings.py
#Alien Invasion settings class file

class Settings:
    '''A class to sotre all settings for Alien Invasion.'''

    def __init__(self):
        '''Inisialize the game's settings.'''
        #Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230,230,230)