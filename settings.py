class Settings:
    """存储设置"""

    def __init__(self):
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.ba_color = (20, 230, 230)
        # ship setting
        self.ship_limit = 3
        # bullet setting
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3
        # alien setting
        self.fleet_drop_speed = 5
        # accelerate
        self.speedup_scale = 2
        self.score_scale = 10
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        self.alien_points = 50

        self.fleet_direction = -1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points*self.score_scale)