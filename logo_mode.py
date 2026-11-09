import game_framework
from pico2d import *

image = None
logo_start_time = 0.0
LOGO_DURATION = 2.0
# 원본의 흰 여백이 비대칭이므로 로고 자체를 중심으로 4:3 영역을 자른다.
LOGO_REGION = (49, 84, 680, 510)

def init():
    global image
    global logo_start_time

    image = load_image('tuk_credit.png')
    logo_start_time = get_time()

def finish():
    global image
    image = None

def update():
    if get_time() - logo_start_time >= LOGO_DURATION:
        import title_mode
        game_framework.change_mode(title_mode)

def render():
    clear_canvas()
    width, height = get_canvas_width(), get_canvas_height()
    image.clip_draw(*LOGO_REGION, width // 2, height // 2, width, height)
    update_canvas()

def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
