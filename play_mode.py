from pico2d import *
import game_framework
import game_world
import item_mode
from boy import Boy
from grass import Grass


def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import logo_mode
            game_framework.change_mode(logo_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            import pause_mode
            game_framework.push_mode(pause_mode)
            return
        elif item_mode.handle_event(event, boy):
            # 창을 열어도 같은 프레임의 이동·발사·키 해제를 계속 처리한다.
            continue
        else:
            boy.handle_event(event)



def init():
    global boy

    item_mode.init()
    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)



def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    item_mode.render()
    update_canvas()


def pause():
    global pause_started_at
    pause_started_at = get_time()


def resume():
    # 정지 중 흐른 시간은 소년의 대기 시간에 포함하지 않는다.
    boy.idle_started_at += get_time() - pause_started_at

    # 정지 중 놓은 방향키가 계속 눌린 것으로 남지 않도록 확인한다.
    keys = SDL_GetKeyboardState(None)
    for key in tuple(boy.pressed_keys):
        if not keys[SDL_GetScancodeFromKey(key)]:
            event = Event(SDL_KEYUP)
            event.key = key
            boy.handle_event(event)


def finish():
    global boy
    item_mode.finish()
    game_world.clear()
    boy = None


