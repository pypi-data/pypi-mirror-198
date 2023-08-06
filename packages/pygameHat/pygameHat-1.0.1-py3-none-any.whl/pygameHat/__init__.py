import pygame, sys, time
from text_format import TextFormat

#pygame initialization
print("Additional hello from pygameHat :D")
pygame.init()
pygame.font.init()
try:
    pygame.mixer.init()
except:
    print("WARNING: Failed to initialize audio!")

#main objects
class Object:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprite = None
    
    def draw(self):
        draw_sprite(self.sprite, self.x, self.y)
    
    def step(self):
        pass
    def key_just_pressed(self, key):
        pass
    def key_just_released(self, key):
        pass
    def is_colliding(self, object):
        pass

class Room():
    def __init__(self, background=(0, 0, 0), layers={"default": []}, instances=[]):
        self.background = background
        self.layers = layers
        self.instances = instances

class Sprite():
    def __init__(self, index, spritesheet_data, speed=60, collision=False):
        self.index = pygame.image.load(index).convert_alpha()
        self.speed = speed
        self.x_size, self.y_size, self.x_frames, self.y_frames = spritesheet_data
        self.current_x_frame = 0
        self.current_y_frame = 0
        self.timer = 1/self.speed

        self.collision = collision
        self.collision_shape = self.index.get_rect(width=self.index.get_width()/(self.x_frames+1), height=self.index.get_height()/(self.y_frames+1))
    
    def animate(self):
        self.timer -= delta_time
        if self.timer <= 0:
            if self.current_x_frame < self.x_frames:
                self.current_x_frame += 1
            elif self.current_y_frame < self.y_frames:
                self.current_x_frame = 0
                self.current_y_frame += 1
            else:
                self.current_y_frame = 0
                self.current_x_frame = 0
            self.timer = 1/self.speed

#game settings
version = "Alpha 1.0.0"
settings = {
    "screen_size": (1200, 700),
    "window_title": "pygameHat "+version,
    "icon": "playground_assets/pghat.png",
    "enable_console": True,
    "fps": 60,

    "shameless_ad": False,
}

#first initializations
debug_font = pygame.font.Font(None, 25)
console_opened = False
console = TextFormat()
delta_time = 0

screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_icon(pygame.image.load(settings["icon"]))
pygame.display.set_caption(settings["window_title"])
if settings["shameless_ad"]:
    screen.blit(pygame.transform.scale(pygame.image.load("playground_assets/pghat.png").convert(), (1000, 1000)), (0, 0))
    pygame.display.flip()
    time.sleep(1.5)
current_room = Room()

def add_object_instance(x, y, object, layer):
    object.x = x
    object.y = y
    current_room.layers[layer].append(object)

def collide_objects(object1, object2):
    if object1 != object2 and object1.sprite and object1.sprite.collision and object2.sprite and object2.sprite.collision:
        object1_shape = object1.sprite.collision_shape
        object1_shape.x = object1.x
        object1_shape.y = object1.y
        object2_shape = object2.sprite.collision_shape
        object2_shape.x = object2.x
        object2_shape.y = object2.y
        if object1_shape.colliderect(object2_shape):
            return object2

def draw_sprite(sprite, x, y):
        if sprite:
            screen.blit(sprite.index, (x, y), (sprite.x_size*sprite.current_x_frame, sprite.y_size*sprite.current_y_frame, sprite.x_size, sprite.y_size))
            sprite.animate()

def change_room(room):
    global current_room

    current_room = room

#debug fuctions
def switch_console():
    global console_opened
    
    if console_opened:
        console_opened = False
        console.clear()
    else:
        console_opened = True

def start():
    global delta_time

    screen = pygame.display.set_mode(settings["screen_size"])
    pygame.display.set_caption(settings["window_title"])
    pygame.display.set_icon(pygame.image.load(settings["icon"]))

    while True:
        delta_time = pygame.time.Clock().tick(settings["fps"])/1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            
            elif event.type == pygame.KEYDOWN:
                #console management
                if console_opened:
                    console.text += event.unicode
                    if event.key == pygame.K_RETURN:
                        try:
                            exec(console.text)
                            console.clear()
                        except:
                            print("Something went wrong")
                    elif event.key == pygame.K_BACKSPACE:
                        console.delete_from_end()
                if event.key == pygame.K_F10 and settings["enable_console"]:
                    switch_console()
                #handling keypresses for objects
                for layer in current_room.layers:
                    for instance in current_room.layers[layer]:
                        instance.key_just_pressed(event.key)

            elif event.type == pygame.KEYUP:
                #handling keyups for objects
                for layer in current_room.layers:
                    for instance in current_room.layers[layer]:
                        instance.key_just_released(event.key)

        screen.fill(current_room.background)

        #console rendering
        if console_opened:
            screen.blit(debug_font.render(">>"+console.text, True, (255, 255, 255)), (0, 0))
    
        #object handling
        for layer in current_room.layers:
            for instance in current_room.layers[layer]:
                #object drawing and processing
                instance.draw()
                instance.step()
                #collision processing
                for layer2 in current_room.layers:
                    for instance2 in current_room.layers[layer2]:
                        obj = collide_objects(instance, instance2)
                        if obj:
                            instance.is_colliding(obj)

        pygame.display.flip()
