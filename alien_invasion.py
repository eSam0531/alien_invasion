# alien_invasion.py
# Esmeralda Samarripa
# CISA 4359 Spring 2021
# Project 1 - From Textbook: Python Crash Course 2nd edition
#
# In Alien Invasion, the player controls a rocket ship that appears
# at the bottom center of the screen. The player can move the ship
# right and left using the arrow keys and shoot bullets using the
# spacebar. Whe the game begins, a fleete of aliens fills the sky
# and moves across and down the screen. The player shoots and destroys
# the aliens. If the play shoots all the aliens, a new fleet appears
# that moves faster than the previous fleet. If any alien hits the 
# player's ship or reaches the bottom of the screen, the player
# loses a ship. If the player loses three ships, the game ends.
#
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    '''Overall class to manage game assets and behavior.'''
    def __init__(self):
        '''Initialize the game, and create game resources.'''
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((\
            self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        # Set the background color
        self.bg_color = (self.settings.bg_color)
        # Create an instance of the ship
        self.ship = Ship(self)
        # Create a bullet Group to manage bullets fired
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        'Start the main loop for the game.'
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            
    def _check_events(self):
        '''Respond to keypresses and mouse events'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        '''Respond to keypresses.'''
        if event.key == pygame.K_RIGHT:
            # Move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        '''Respond to key releases.'''
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        '''Update positionof bullets and get rid of old bullets.'''
        #Update bullet positions.
        self.bullets.update()

        #Get rid of bullets that have disappeard.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            #used to test if bullets were being removed
            #print(len(self.bullets))

    def _update_screen(self):
        '''Update images on the screen, and flip tot he new screen.'''
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
            
        # Make the most recently drawn screen visible.
        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()