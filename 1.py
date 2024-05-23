import pygame
import sys
import random
pygame.init()

pygame.key.set_repeat(1,1) #주기적으로 키를 다시 검사(무슨 킨지 모름 찾아봐야함)

screen = pygame.display.set_mode((1200,700)) #게임 스크린 정의
pygame.display.set_caption("HANG MAN")
clock = pygame.time.Clock() #fps 설정
running = True


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
heart = 5 #목숨
topic = "fruit" #주제 나중에 배열로 만들 예정
words = ["APPLE", "BANANA", "ORANGE", "MANDARIN", "MELON"] #게임 단어
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y","Z"]
# randomWord =words[random.randint(0, len(words)-1)] # 랜덤 숫자
randomWord = "ORANGE"
wordLen = len(randomWord) #단어 길이

userAns = []

def emptyWord(len): #정답 보여줌
  for i in range(0, len):
    global userAns
    userAns.append("_")
  return userAns
  # print(" ".join(userAns))


def alphaCheck(userInput): #남아있는 알파벳 체크 함수
  temp = []
  temp2 = []
  temp3 = []
  global alpha
  userIdx =  list(filter(lambda n: alpha[n] == userInput, range(len(alpha)))) #사용자가 입력한 알파벳의 idx 배열로 들어옴 

  if len(userIdx) != 0:
    print(userIdx)
    for i in userIdx: 
      alpha[i] = " "
  
  for i in range(len(alpha)):  #남은 알파벳을 사용자에게 출력
    if i < 10:
      temp.append(alpha[i])
    elif i < 19:
      temp2.append(alpha[i])
    else:
      temp3.append(alpha[i])
  # print(temp)
  # print(temp2)
  return [temp, temp2, temp3]


def ansCheck(userInput): # 정답 체크
  global randomWord
  global heart
  global gameCnt
  flag = False
  for i in range(wordLen):
    if randomWord.find(userInput) != -1:
      checkIdx = randomWord.find(userInput) # 랜덤 단어에서 사용자가 입력한 알파벳이 있으면
      # print(ch)
      # userAns[checkIdx] = userInput # 정답의 __를 사용자 입력값으로 바꿈
      # print(userAns)
      randomWord = randomWord.replace(userInput, "0", 1) # 기존에 있는 알파벳 배열에서 사용자가 입력한 알파벳을 지워줌
      flag = True
      gameCnt+=1

  print(" ".join(userAns))
  if not flag:
    heart -= 1
      

def paint(heart): #행맨 그리기 아마 나중에는 그림 그리는 메소드 이용 예정
  if(heart == 5):
    print("남은 목숨 {}개".format(heart-1))
  elif(heart == 4):
    print("남은 목숨 {}개".format(heart-1))
  elif(heart == 3):
    print("남은 목숨 {}개".format(heart-1))
  elif(heart == 2):
    print("남은 목숨 {}개".format(heart-1))
  else:
    print("남은 목숨 {}개".format(heart-1))


userInput = ""

arr = emptyWord(wordLen)



#------------------------------------------------pygame main

while running:
  # clock.tick(10)
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      key = pygame.key.name(event.key)
      keyNum=pygame.key.key_code(key)
      if(97 <= keyNum and 122 >= keyNum):
        userInput = key.upper()
    #----------------------------------------------------사용자 입력 받기

      if event.key == pygame.K_RETURN:
        # print(userInput)
        ansCheck(userInput)
        userInput = ""

    if event.type == pygame.QUIT: 
      running=False 
      #------------------------------------------ 창 닫기 
    # if event.type == pygame.KEYDOWN:
      # if event.key == 



  screen.fill(WHITE)
  # while(heart != 0 or game):
  #   if(gameCnt == wordLen) :
  #     break

  font = pygame.font.SysFont("malgungothic", 35)

  remainHeart = font.render("목숨 {}/5".format(heart), True, BLACK)
  screen.blit(remainHeart, (50, 50)) 
  #------------------------------------------------목숨 출력


  font = pygame.font.SysFont("malgungothic", 75)
  defaultAns = font.render(" ".join(arr), True, BLACK)
  screen.blit(defaultAns, (1200/2 -(len(arr)*29), 350))
  #------------------------------------------------ 빈칸 출력
  
  
  remainAlphaArr = alphaCheck(userInput)
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
  
  #------------------------------------------------------사용자 입력
    # userInput = input("알파벳을 적어주세요 ").upper()
    # ansCheck(userInput)
  
  pygame.display.flip()
