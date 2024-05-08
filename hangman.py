import pygame
import random
# import 
# pygame.init()

# 내갸 쓸 rgb 포맷
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# BLUE = (0, 0, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)

# size = [800, 700]
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("game title")

# running = True 
# clock = pygame.time.Clock()
# font = pygame.font.Font(None, 36)

# -----------------------------------------------------------
# 게임 준비
heart = 5 #목숨
topic = "fruit" #주제 나중에 배열로 만들 예정
words = ["APPLE", "BANANA", "ORANGE", "MANDARIN", "MELON"] #게임 단어
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X","Y","Z"]
# randomWord =words[random.randint(0, len(words)-1)] # 랜덤 숫자
randomWord = "APPLE"
wordLen = len(randomWord) #단어 길이

userAns = []

def emptyWord(len):
  for i in range(0, len):
    global userAns
    userAns.append("__")
  # print(" ".join(userAns))

def alphaCheck(userInput):
  temp = ""
  temp2 = ""
  global alpha
  if alpha.index(userInput) != -1:
    alpha[alpha.index(userInput)] = ""
  
  for i in range(len(alpha)):
    if i < len(alpha) / 2:
      temp += alpha[i]+ " "
    else:
      temp2 += alpha[i]+ " "
  # print(temp)
  # print(temp2)

def ansCheck(userInput): # 정답 체크
  global randomWord
  for i in range(wordLen):
    if randomWord.find(userInput) != -1:
      checkIdx = randomWord.find(userInput)
      userAns[checkIdx] = userInput
      randomWord = randomWord.replace(userInput, "0", 1)
      print(" ".join(userAns))
      

def paint(heart): #행맨 그리기 아마 나중에는 그림 그리는 메소드 이용 예정
  if(heart == 5):
    print()
  elif(heart == 4):
    paint()
  elif(heart == 3):
    print()
  elif(heart == 2):
    print()
  else:
    print()


emptyWord(wordLen) #단어 길이 만큼 빈칸 만들기
alphaCheck("P") #알파벳 보기 담당
ansCheck("P")

# print(alpha.index("A"))


#main
# while running:
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       running = False

#   screen.fill(WHITE)



#   pygame.display.flip()
    
