import pygame
class Screen:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((600, 400))
        self.project_name = "Relaxation Blocks"

        self.title = pygame.display.set_caption(self.project_name)
        self.background = pygame.image.load("assets/background_img.jpeg")
        self.running = True




    def gameloop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            mx, my = pygame.mouse.get_pos()
            cursor = pygame.image.load("assets/cursor.png")
            x = mx
            y = my
            pygame.transform.scale(cursor, (1, 1))
            self.screen.blit(cursor, (x, y))
















            pygame.display.flip()







if __name__ == '__main__':
    sb = Screen()
    sb.gameloop()


