import os
from pathlib import Path

from pico2d import close_canvas, open_canvas

import game_framework
import logo_mode


def main():
    # 기존 게임 오브젝트도 실행 위치에 관계없이 이미지 파일을 찾는다.
    os.chdir(Path(__file__).resolve().parent)
    open_canvas()
    try:
        game_framework.run(logo_mode)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
