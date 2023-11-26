import pygame as pg
from use_tools.main_loop import MainLoop


class App:
    def __init__(self, w: int, h: int):
        pg.init()

        self.w = w
        self.h = h
        self.screen = pg.display.set_mode((self.w, self.h))

        self.main_loop = MainLoop(self.update, self.draw)
        self.__updates = []

    def run(self):
        self.main_loop.run()

    def update(self, events):
        for event in events:
            if event.type == pg.QUIT:
                self.exit()

        for i in self.__updates:
            i()

    def draw(self):
        pass

    def exit(self):
        self.main_loop.exit()

    def add_update_function(self, func):
        self.__updates.append(func)

    def remove_update_function(self, func):
        if func in self.__updates:
            self.__updates.remove(func)


if __name__ == '__main__':
    my_app = App(800, 600)
    my_app.run()
