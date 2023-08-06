import pygame as pg
import threading as thr
from .Sprites import *


class Screen:
    def __init__(self, width, height, fps=60):
        self.objects = dict()
        self.objects_order = []
        self.raw_draw = dict()
        self.blit_arr = []
        self.width, self.height = width, height
        self.screen = None
        self.pressed_obj_ind = None
        self.fps = 0
        self.pressed_keys = []
        self.curr_obj = None
        self.clock = pg.time.Clock()
        self.max_fps = fps
        self.bg_color = (0,0,0)

        self.mouse_delta = [0, 0]
        self.process_btn_clk = 0
        self.pressed_obj = None
        self.released_obj = None
        self.dragged_obj = None
        self.old_mouse_pos = [0, 0]
        self.mouse_wheel_pos = 0
        self.mouse_pos = [0, 0]
        self.mouse_state = [0, 0]
        self.initialized = False
        self.in_separate_thread = False
        self.force_stop = False
        self.del_queue = []
        self.cicle_finished = True
        self.pause_update = thr.Lock()

    def lunch_separate_thread(self):
        self.in_separate_thread=True
        self.thread = thr.Thread(target=self.as_thread)
        self.thread.start()

    def as_thread(self):
        self.init()
        self.run()

    def __getitem__(self, item):
        if item in self.objects:
            return self.objects[item]
        else:
            raise AttributeError("No object named", item)

    def add_fps_indicator(self, x=0, y=0, font=10, color=(255,255,255)):
        Text(self, name="fps", x=x, y=y, inp_text=self.get_fps, font='serif', font_size=font, color=color)


    def init(self):
        pg.init()
        self.screen = pg.display.set_mode((self.width, self.height))
        self.initialized = True


    def step(self):
        if self.running:
            self.handle_events()
            self.update_mouse()
            self.update_objects()
            self.draw_objects()
            pg.display.update()
            pg.display.flip()
            self.clock.tick(self.max_fps)
            self.fps = self.clock.get_fps()
            self.post_processes()
            self.cicle_finished = True

    def run(self):
        while self.running:
            self.pause_update.acquire()
            self.step()
            self.pause_update.release()
        pg.quit()

    def end(self):
        self.running = False
        pg.quit()


    @property
    def running(self):
        if self.in_separate_thread:
            return thr.main_thread().is_alive()
        else:
            return not self.force_stop
    @running.setter
    def running(self, val):
        self.force_stop = val

    def wait_step(self):
        self.cicle_finished = False
        while not self.cicle_finished:
            pass

    def get_fps(self):
        return round(self.fps, 2)

    def update_mouse(self):
        self.mouse_pos = pg.mouse.get_pos()
        self.mouse_delta = [self.old_mouse_pos[0] - self.mouse_pos[0], self.old_mouse_pos[1] - self.mouse_pos[1]]
        self.old_mouse_pos = self.mouse_pos[:]


    def handle_events(self):
        for obj_name in self.objects_order[::-1]:
            obj = self.objects[obj_name]
            if obj.rect.collidepoint(self.mouse_pos) and not obj.transparent_for_mouse:
                self.curr_obj = obj
                break
            self.curr_obj = None

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.running = False
                    return
                else:
                    self.pressed_keys.append(event.key)
            elif event.type == pg.KEYUP:
                if event.key in self.pressed_keys:
                    self.pressed_keys.pop(self.pressed_keys.index(event.key))
            elif event.type == pg.MOUSEWHEEL:
                self.mouse_wheel_pos += event.y
            elif event.type == pg.MOUSEBUTTONDOWN:
                self.update_mouse()
                self.mouse_state = [event.button, 1]
                self.pressed_obj = self.curr_obj
            elif event.type == pg.MOUSEBUTTONUP:
                self.mouse_state = [event.button, 0]
                self.released_obj = self.curr_obj
                self.dragged_obj = None


    def add_object(self, obj):
        if obj.name in self.objects:
            raise ValueError("Duplicate object")
        self.objects[obj.name] = obj
        self.objects_order.append(obj.name)

    def del_object(self, obj):
        if isinstance(obj, str):
            obj_name =obj
        else:
            obj_name =obj.name
        self.del_queue.append(obj_name)

    def post_processes(self):
        if self.del_queue:
            for i in self.del_queue:
                del self.objects[i]
                self.objects_order.pop(self.objects_order.index(i))
            self.del_queue = []


    def add_raw(self, func, name, *args):
        self.raw_draw[name] = [func, args]

    def add_blit(self, img, pos):
        self.blit_arr.append((img, pos))
    def update_objects(self):

        if self.pressed_obj:
            pomop = self.pressed_obj.convert_to_local(self.mouse_pos)
            self.pressed_obj.pressed(mouse_pos=pomop, btn_id=self.mouse_state[0])
            self.pressed_obj = None
        if self.released_obj:
            pomop = self.released_obj.convert_to_local(self.mouse_pos)
            self.released_obj.release(mouse_pos=pomop, btn_id=self.mouse_state[0])
            self.released_obj = None
        if self.dragged_obj:
            curr_obj_mouse_pos = self.dragged_obj.convert_to_local(self.mouse_pos)
            if (self.mouse_delta[0] or self.mouse_delta[1]) and self.mouse_state[1]:
                self.dragged_obj.dragged(mouse_pos=curr_obj_mouse_pos,
                                      btn_id=self.mouse_state[0],
                                      mouse_delta=self.mouse_delta)
        if self.curr_obj:
            if (self.mouse_delta[0] or self.mouse_delta[1]) and self.mouse_state[1] and not self.dragged_obj:
                self.dragged_obj = self.curr_obj
            else:
                curr_obj_mouse_pos = self.curr_obj.convert_to_local(self.mouse_pos)
                self.curr_obj.hover(mouse_pos=curr_obj_mouse_pos)

        for obj in self.objects_order:
            self.objects[obj].update()

    def draw_objects(self):
        self.screen.fill(self.bg_color)
        for img, pos in self.blit_arr:
            self.screen.blit(img, pos)
        self.blit_arr = []
        for obj_name in self.objects_order:
            if self.objects[obj_name].visible:
                self.objects[obj_name].draw()
        for func, args in self.raw_draw.values():
            func(self.screen, *args)
        self.raw_draw = dict()

    def sprite(self, sprite_obj):
        while not self.initialized:
            pass
        self.add_object(sprite_obj)
        return self.objects[sprite_obj.name]
