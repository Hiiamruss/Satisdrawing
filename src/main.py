import pygame


class Screen:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((600, 400))
        self.project_name = "Nuke Simulator"

        self.title = pygame.display.set_caption("Nuke Simulator")
        self.background = pygame.image.load("assets/background_img.png")
        self.running = True


    def gameloop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.blit(self.background, (0,0))

            pygame.display.flip()







if __name__ == '__main__':
    sb = Screen()
    sb.gameloop()


