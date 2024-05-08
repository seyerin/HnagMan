import pygame

pygame.init()

# 내갸 쓸 rgb 포맷
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = [400, 300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("game title")

running = True 
clock = pygame.time.Clock()


# count=0

# text
def textFunc(txt, font):
  textSurface = font.render(txt, True, BLUE)
  return textSurface, textSurface.get_rect()


count = 0

# butthon
def buttonFunc(txt, x, y, w, h, color):
  # mouse = pygame.mouse.get_pos() #마우스 좌표
  click = pygame.mouse.get_pressed() #마우스 클릭

  if click[0] == 1:
    # action()
    global count
    count += 1

  pygame.draw.rect(screen, color, (x,y,w,h))

  fontSize = pygame.font.SysFont("malgungothic", 20)
  textSurf, textRect = textFunc(txt, fontSize)
  textRect.center = ((x+(w/2)), (y+(h/2)))
  screen.blit(textSurf, textRect)  


font = pygame.font.Font(None, 36)
#main
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill((255, 255, 255))

  
  cntTxt = font.render(f"Score: {count}", True, RED)

  screen.blit(cntTxt, (190, 100))
  buttonFunc("click!", 175, 150, 50, 40, GREEN)

  # pygame.display.update()
  pygame.display.flip()
    
