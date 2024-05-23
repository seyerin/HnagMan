import pygame
import random
import time
pygame.init()

screen = pygame.display.set_mode((1200,700)) #게임 스크린 정의
pygame.display.set_caption("HANG MAN")
clock = pygame.time.Clock() #fps 설정
running = True
pi = 3.141592653589793


# 내갸 쓸 rgb 포맷
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)



# -----------------------------------------------------------
# 게임 준비
game = False
gameCnt = 0
heart = 10 #목숨
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y","Z"]
topic = "fruit" #주제 나중에 배열로 만들 예정
words = ["APPLE", "BANANA", "ORANGE", "MANDARIN", "MELON", "GRAPE", "GRAPEFRUIT", "ABOCADO", "BLUEBERRY", "COCONUT", "LEMON", "KIWI", "MANGO", "PAPAYA", "PEACH", "PEAR", "PLUM", "TANGERINE"] #게임 단어
# randomWord =words[random.randint(0, len(words)-1)] # 랜덤 숫자
randomWord = "APPLE"
wordLen = len(randomWord) #단어 길이

userAns = []
userInput = ""


def emptyWord(len): #정답 보여줌
  for i in range(0, len):
    global userAns
    userAns.append("_")
  return userAns


def alphaCheck(userInput): #남아있는 알파벳 체크 함수
  temp = []
  temp2 = []
  temp3 = []
  global alpha
  userIdx =  list(filter(lambda n: alpha[n] == userInput, range(len(alpha)))) #사용자가 입력한 알파벳의 idx 배열로 들어옴 

  if len(userIdx) != 0:
    for i in userIdx: 
      alpha[i] = " "
  
  for i in range(len(alpha)):  #남은 알파벳을 사용자에게 출력
    if i < 10:
      temp.append(alpha[i])
    elif i < 19:
      temp2.append(alpha[i])
    else:
      temp3.append(alpha[i])
  return [temp, temp2, temp3]


def ansCheck(userInput): # 정답 체크
  global randomWord
  global heart
  global gameCnt
  flag = False
  for i in range(wordLen):
    if randomWord.find(userInput) != -1:
      checkIdx = randomWord.find(userInput) # 랜덤 단어에서 사용자가 입력한 알파벳이 있으면
      userAns[checkIdx] = userInput # 정답의 __를 사용자 입력값으로 바꿈\
      randomWord = randomWord.replace(userInput, "0", 1) # 기존에 있는 알파벳 배열에서 사용자가 입력한 알파벳을 지워줌
      flag = True
      gameCnt+=1

  if not flag: 
    heart -= 1
      

def paint(heart): #행맨 그리기 아마 나중에는 그림 그리는 메소드 이용 예정
  if heart < 10:
    pygame.draw.circle(screen, BLACK, (555, 190), 30, 5)#머리
  if heart < 9:
    pygame.draw.line(screen, BLACK, (555, 220), (555, 290), 5) #몸
  if heart < 8:
    pygame.draw.line(screen, BLACK, (555, 220), (530, 300), 5) #팔1
  if heart < 7:
    pygame.draw.line(screen, BLACK, (555, 220), (580, 300), 5) #팔2
  if heart < 6:
    pygame.draw.line(screen, BLACK, (555, 290), (530, 370), 5) #다리1
  if heart < 5:
    pygame.draw.line(screen, BLACK, (555, 290), (580, 370), 5) #다리2
  if heart < 4:
    pygame.draw.line(screen, BLACK, (540, 175), (550, 190), 5)
    pygame.draw.line(screen, BLACK, (550, 175), (540, 190), 5) # 눈
  if heart < 3:
    pygame.draw.line(screen, BLACK, (560, 175), (570, 190), 5)
    pygame.draw.line(screen, BLACK, (570, 175), (560, 190), 5) # 눈
  if heart < 2:
    pygame.draw.line(screen, BLACK, [540,195], [570, 195], 3) #입
  if heart < 1:
    pygame.draw.arc(screen, BLACK, [555, 180, 10, 30], pi,3*pi/2, 2)
    pygame.draw.arc(screen, BLACK, [555, 180, 15, 30], 3*pi/2, 2*pi, 2) #혀



def clicked():
  global running
  if event.type == pygame.MOUSEBUTTONDOWN:
    running = False

def popup(txt, fontSize, px):
    pygame.draw.rect(screen, BLACK, [300, 150, 600, 350])
    font2 = pygame.font.SysFont("none", fontSize)
    endText = font2.render(txt, True, WHITE)
    screen.blit(endText, (px,240))
    pygame.draw.rect(screen, BLUE, [450, 380, 300, 80])
    font2 = pygame.font.SysFont("malgungothic", 50)
    endText = font2.render("나가기", True, WHITE)
    screen.blit(endText, (520,390))

    if event.type == pygame.MOUSEBUTTONDOWN:
      clicked()


arr = emptyWord(wordLen)
remainAlphaArr = alphaCheck(userInput)


#------------------------------------------------pygame main

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      running=False 
      #------------------------------------------ 창 닫기 
    if heart > 0 and "".join(userAns).find("_") != -1:
      if event.type == pygame.KEYDOWN:
        key = pygame.key.name(event.key)
        keyNum=pygame.key.key_code(key)
        if(97 <= keyNum and 122 >= keyNum):
          userInput = key.upper()
    #----------------------------------------------------사용자 입력 받기
        if event.key == pygame.K_RETURN:
          if userInput != "":
            ansCheck(userInput)
            remainAlphaArr = alphaCheck(userInput)
            userInput = ""
    #----------------------------------------------------- enter키 누를 때 답안 체크

  screen.fill(WHITE)

  font = pygame.font.SysFont("malgungothic", 35)

  topicText = font.render("주제: {}".format(topic), True, BLACK)
  screen.blit(topicText, (490,40))

  #------------------------------------------------------주제 출력

  remainHeart = font.render("목숨 {}/10".format(heart), True, BLACK)
  screen.blit(remainHeart, (50, 40)) 
  #------------------------------------------------목숨 출력


  font = pygame.font.SysFont("malgungothic", 75)
  defaultAns = font.render(" ".join(arr), True, BLACK)
  screen.blit(defaultAns, (1200/2 -(len(arr)*35), 350))
  #------------------------------------------------ 빈칸 출력
  
  
  font2 = pygame.font.SysFont("none", 45);
  py= 500
  px =100
  tmp = 55
  for i in range(len(remainAlphaArr)):
    for j in range(len(remainAlphaArr[i])):
      remainAlpha1 = font2.render("".join(remainAlphaArr[i][j]), True, BLACK)
      screen.blit(remainAlpha1, (px, py))
      px += 55
    px = px/len(remainAlphaArr[i]) + tmp
    tmp+=55
    py+=55
  #-------------------------------------------남은 알파벳 출력

  font = pygame.font.SysFont("malgungothic", 35)
  inputText = font.render("답: {}".format(userInput), True, BLACK)
  screen.blit(inputText, (800, 480))
  #--------------------------------------------------------사용자 답 출력

  pygame.draw.line(screen, BLACK, (460, 130), (460, 130+230), 10)
  pygame.draw.line(screen, BLACK, (457, 134), (457+100, 134), 10)
  pygame.draw.line(screen, BLACK, (552, 134), (552, 134+30), 10)

  
  
  paint(heart)
  
  if heart == 0:
    popup(randomWord, 80, 1200/2 - (len(randomWord) * 20))

  if "".join(userAns).find("_") == -1:
    popup("YOU WIN !", 150, 345)
  
  pygame.display.flip()
