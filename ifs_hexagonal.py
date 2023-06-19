#!/usr/bin/env python3
# ifs_square.py

from simple_screen import SimpleScreen
from ifs import IteratedFunctionSystem

ifs = IteratedFunctionSystem()


def plot_ifs(ss):
    iterations = 200_000
    x, y = 15, 15

 
    for _ in range(100):
        x, y, color = ifs.transform_point(x, y)

    for _ in range(iterations):
        x, y, color = ifs.transform_point(x, y)
        ss.set_world_pixel(x, y, color)


def main():
    ifs.set_base_frame(0, 0, 30, 30)

    p = 1 / 6

    ifs.add_mapping(0, 0, 15, 0, 0, 15, "blue", p)
    ifs.add_mapping(15, 0, 30, 0, 15, 15, "blue", p)
    ifs.add_mapping(0, 0, 0, 15, 0, 30, "blue", p)
    ifs.add_mapping(15, 15, 30, 15, 15, 30, "blue", p)
    ifs.add_mapping(0, 15, 15, 15, 30, 30, "blue", p)
    ifs.add_mapping(15, 15, 30, 0, 15, 30, "blue", p)

    ifs.generate_transforms()

    ss = SimpleScreen(
        world_rect=((0, 0), (30, 30)),
        screen_size=(900, 900),
        draw_function=plot_ifs,
        title="IFS hexagonal",
    )
    ss.show()


if __name__ == "__main__":
    main()
