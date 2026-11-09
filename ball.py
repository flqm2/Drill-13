from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    images = {}

    def __init__(self, x, y, velocity, scale=1):
        if scale not in (1, 2):
            raise ValueError('공의 배율은 1 또는 2여야 합니다.')
        if not Ball.images:
            Ball.images = {
                1: load_image('ball21x21.png'),
                2: load_image('ball41x41.png'),
            }
        # 발사 시점의 선택값을 공마다 보관해 이후 선택 변경의 영향을 받지 않는다.
        self.scale = scale
        self.image = Ball.images[scale]
        self.width = Ball.images[1].w * scale
        self.height = Ball.images[1].h * scale
        self.x, self.y = x, y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y, self.width, self.height)
