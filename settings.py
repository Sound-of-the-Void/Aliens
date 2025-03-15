class Settings():

    def initialize_dynamic_speed(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.fleet_direction = 1.0

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

    def __init__(self):

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 50, 230)
        self.speedup_scale = 1.1
        self.ship_limit = 3
        self.alien_speed = 1
        self.alien_points = 50
        self.ship_speed = 2
        self.fleet_drop_speed = 5
        self.bullet_speed = 1.5
        self.bullet_width = 50
        self.bullet_height = 10
        self.bullet_color = (250, 10, 10)
        self.bullets_allowed = 5
        self.initialize_dynamic_speed()


