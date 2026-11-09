from pico2d import (
    SDL_KEYDOWN, SDL_QUIT, SDLK_SPACE, clear_canvas,
    get_canvas_height, get_canvas_width, get_events, load_image, update_canvas,
)

import game_framework

image = None


def init():
    global image
    image = load_image('title.png')


def finish():
    global image
    image = None


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            import play_mode
            game_framework.change_mode(play_mode)
            return


def update():
    pass


def render():
    clear_canvas()
    width, height = get_canvas_width(), get_canvas_height()
    image.draw(width // 2, height // 2, width, height)
    update_canvas()
