import pygame
import numpy as np

pygame.init()
screen_width, screen_height = 500, 500
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Physics Engine Simulation")
background_color = (0, 0, 0)
white = (255, 255, 255)
num_movers = 1

class Mover:
    def __init__(self, screen):
        self.screen = screen
        self.radius = 30.0
        self.mass = 1
        self.loc = np.array([screen_width // 2, 0], dtype=float)
        self.vel = np.array([0.0, 0.0], dtype=float)  # initial velocity of object in x and y
        self.acc = np.array([0.0, 0.0], dtype=float)

    def display(self):
        el_size = int(self.mass * 20)
        ellipse_rect = (self.loc[0] - el_size // 2, self.loc[1] - el_size // 2, el_size, el_size)
        pygame.draw.ellipse(self.screen, white, ellipse_rect)

    def update(self):
        self.vel += self.acc
        self.loc += self.vel.copy()
        self.acc = np.array([0.0, 0.0], dtype=float)
        if np.linalg.norm(self.vel) < 0.1:
            self.vel = np.array([0.0, 0.0], dtype=float)

    def applyForce(self, force):
        f = force / self.mass
        self.acc += f

    def edges(self):
        if self.loc[0] + 10 < 0 or self.loc[0] + 10 > screen_width:
            self.vel[0] *= -1
        if self.loc[1] + 10 < 0 or self.loc[1] + 10 > screen_height:
            self.vel[1] *= -1

m = [Mover(screen) for _ in range(num_movers)]
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    screen.fill(background_color)

    for mover in m:
        # Display the movers
        mover.display()

        # Drag force
        # drag = mover.vel
        # drag_magnitude = np.linalg.norm(drag)
        # c = -0.002
        # drag *= c * drag_magnitude
        # drag = np.nan_to_num(drag, nan=0.0)
        # mover.applyForce(drag)

        # Gravity force
        # gravity = np.array([0.0, 0.3])
        # gravity *= mover.mass
        # mover.applyForce(gravity)

        # Friction force
        friction = mover.vel
        friction_magnitude = np.linalg.norm(friction)
        c = -0.1
        friction *= c * friction_magnitude
        # mover.applyForce(friction)


        # Wind force
        mouse_state = pygame.mouse.get_pressed()
        if mouse_state[0]:
            wind = np.array([0.2, 0.0])
            mover.applyForce(friction)


        mover.update()
        mover.edges()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
