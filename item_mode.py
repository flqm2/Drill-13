"""플레이 위에서 동작하는 아이템 창. 모드 스택을 교체하거나 정지하지 않는다."""

from pico2d import (
    SDL_KEYDOWN, SDLK_i, SDLK_0, SDLK_1, SDLK_2,
    get_canvas_width, get_canvas_height, load_image,
)


active = False
OPTIONS = {SDLK_0: 0, SDLK_1: 1, SDLK_2: 2}
panel = None
small_ball = None
large_ball = None


def load_images():
    global panel, small_ball, large_ball
    if panel is None:
        panel = load_image('item_select.png')
        small_ball = load_image('ball21x21.png')
        large_ball = load_image('ball41x41.png')


def init():
    global active
    active = False


def finish():
    global active, panel, small_ball, large_ball
    active = False
    panel = None
    small_ball = None
    large_ball = None


def handle_event(event, boy):
    """아이템 창이 처리한 입력만 소비하고 나머지는 플레이에 전달한다."""
    global active
    if event.type == SDL_KEYDOWN and event.key == SDLK_i:
        active = not active
        if active:
            load_images()
        return True
    if active and event.type == SDL_KEYDOWN and event.key in OPTIONS:
        boy.ball_scale = OPTIONS[event.key]
        active = False
        return True
    return False


def render():
    if not active:
        return
    x = get_canvas_width() - panel.w / 2 - 20
    y = get_canvas_height() - panel.h / 2 - 20
    panel.draw(x, y)
    # 안내 이미지의 기존 공 그림 영역을 같은 배경색으로 덮고 실제 공 PNG를 표시한다.
    panel.clip_draw(0, 0, 1, 1, x + 90, y - 37.5, 92, 140)
    small_ball.draw(x + 85, y - 1, small_ball.w, small_ball.h)
    large_ball.draw(x + 85, y - 66, small_ball.w * 2, small_ball.h * 2)
