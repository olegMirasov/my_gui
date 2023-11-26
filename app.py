import pygame as pg


class App:
    def __init__(self, w: int, h: int):
        pg.init()

        self.w = w
        self.h = h
        self.screen = pg.display.set_mode((self.w, self.h))

        self.clock = pg.time.Clock()
        self._running = True

    def run(self):
        while self._running:
            pass

    def exit(self):
        pass


if __name__ == '__main__':
    my_app = App(800, 600)
    my_app.run()
