"""플레이 위에서 동작하는 아이템 창. 모드 스택을 교체하거나 정지하지 않는다."""

from pico2d import SDL_KEYDOWN, SDLK_i


active = False


def init():
    global active
    active = False


def finish():
    global active
    active = False


def handle_event(event, boy):
    """아이템 창이 처리한 입력만 소비하고 나머지는 플레이에 전달한다."""
    global active
    if event.type == SDL_KEYDOWN and event.key == SDLK_i:
        active = not active
        return True
    return False
