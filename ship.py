import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load the ship image and get its rect
        self.image = pygame.image.load("images/pngwing.com (1).png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottm center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.bottom = 400

        # store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # move flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False  # scott added
        self.moving_down = False  # scott added

    def update(self):
        """update the ship's position based on the movement flag"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor

        if (
            self.moving_down and self.rect.bottom < self.screen_rect.bottom
        ):  # scott added
            self.rect.centery += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.ai_settings.ship_speed_factor

        if self.moving_up and self.rect.top > 0:  # scott added
            self.rect.centery -= self.ai_settings.ship_speed_factor

        # # update rect object from self.center
        # self.rect.centerx = self.center

    def blitme(self):
        """draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
