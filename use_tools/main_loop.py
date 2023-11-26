import pygame as pg


class MainLoop:
    def __init__(self, uf=None, df=None, fps=60):
        """
        uf - update function, take 1 argument - events;
        df - draw function, no argument;
        fps - FPS (count cycles per second.
        """
        self._update = uf if uf else lambda x: None
        self._draw = df if df else lambda: None
        self._fps = fps

        self._clock = pg.time.Clock()
        self.__running = True

    def run(self):
        while self.__running:
            events = pg.event.get()
            self._update(events)
            self._draw()

            self._clock.tick(self._fps)

    def exit(self):
        self.__running = False
