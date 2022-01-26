class Screen:
    def __init__(self) -> None:   
        self.WIDTH = 1000
        self.HEIGHT = 500

        self.x_center = self.WIDTH / 2
        self.y_center = self.HEIGHT / 2
        self.left = self.WIDTH - self.WIDTH
        self.right = self.WIDTH
        self.bottom = self.HEIGHT - self.HEIGHT
        self.top = self.HEIGHT
