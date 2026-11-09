from pico2d import SDL_KEYDOWN, SDL_QUIT, SDLK_p, get_events

import game_framework
import play_mode


def init():
    pass


def finish():
    pass


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_mode()
            return


def update():
    # 게임 객체를 갱신하지 않아 위치와 애니메이션 프레임이 그대로 유지된다.
    pass


def render():
    play_mode.render()
