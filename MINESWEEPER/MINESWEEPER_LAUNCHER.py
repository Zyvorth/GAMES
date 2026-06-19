from supabase import create_client
import json 
import pygame
from datetime import date
import uuid
import minesweeper


pygame.init()



WIDTH,HEIGHT=1000,800
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("MINE SWEEPER")
clock=pygame.time.Clock()
FONT1=pygame.font.SysFont("Consolas",32,bold=True)
FONT1.set_underline(True)
FONT2=pygame.font.SysFont("Consolas",20)
FONT3=pygame.font.SysFont("Consolas",26,bold=True)
FONT3.set_underline(True)
run=True
title = FONT1.render("MINESWEEPER", True, (0,255,0))
watermark=FONT2.render("Zyvorth_CORE",True,'white')
text_signup=FONT2.render("Zyvorth_CORE",True,'white')
pass_name=False
pass_pass=False
user_name=''
user_gmail=''
user_password=''
show_gmail=FONT2.render("GMAIL :",True,"white")
show_pass=FONT2.render("PASSWORD :",True,"white")
show_name=FONT2.render("NAME :",True,"white")
sign_up=FONT3.render("SIGN UP",True,"red")
login_in=FONT3.render("LOGIN",True,"red")
request=FONT2.render("Please use a user name with less than 11 characters",True,'white')

try:
    f=open('user_minesweep_data.json','r')
    data = json.load(f)
    last_date=date.fromisoformat(data["last_date"])
    if (date.today()-last_date).days>30:
      run=True
      login=False
      while run:
        clock.tick(60)
        text_gmail=FONT2.render(user_gmail,True,"black")
        gmail_rect = pygame.Rect(
          (300,250),
          (max(400, text_gmail.get_width() + 20), 50))
        text_pass=FONT2.render(user_password,True,"black")
        pass_rect = pygame.Rect(
          (300,350),
          (max(400, text_pass.get_width() + 20), 50))
      
        for event in pygame.event.get():
          if event.type==pygame.QUIT:
            run=False
          if event.type==pygame.KEYDOWN:
            if (event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER) and pass_pass==False and len(user_gmail)!=0:
              pass_pass=True
            elif pass_pass==False and (event.key==pygame.K_DELETE or event.key==pygame.K_BACKSPACE):
              user_gmail=user_gmail[:-1]
            elif pass_pass==False:
              user_gmail+=event.unicode
              
            elif pass_pass==True :
              if (event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER) and len(user_password)!=0:
                if user_gmail==data['gmail'] and user_password==data['password']:
                  
                  login=True
                else:
                  
                  user_gmail = ''
                  user_password = ''
                  pass_pass = False
              elif (event.key==pygame.K_DELETE or event.key==pygame.K_BACKSPACE):
                user_password=user_password[:-1]
              else:
                user_password+=event.unicode
          if login==True:
            data['last_date']=date.today().isoformat()
            f.close()
            f=open('user_minesweep_data.json','w') 
            json.dump(data,f)
            f.close()
            run=False
            minesweeper.main()
          else:
            
            win.fill((0,0,0))
            win.blit(title,(400,40))
            win.blit(watermark,(20,20))
            win.blit(login_in,(440,200))
            pygame.draw.rect(win,(255, 233, 200),gmail_rect,0,5)
            pygame.draw.rect(win,(255,255,255),gmail_rect,1,5)
            win.blit(show_gmail,(180,265))
            win.blit(text_gmail, (300 + (gmail_rect.width - text_gmail.get_width()) // 2, 250 + (50 - text_gmail.get_height()) // 2))

            pygame.draw.rect(win,(255, 233, 200),pass_rect,0,5)
            pygame.draw.rect(win,(255,255,255),pass_rect,1,5)
            win.blit(show_pass,(180,365))
            win.blit(text_pass, (300 + (pass_rect.width - text_pass.get_width()) // 2, 350 + (50 - text_pass.get_height())//2))
            pygame.display.update()  
    else:
      minesweeper.main() 
    pygame.quit()
    
except FileNotFoundError:
  f=open('user_minesweep_data.json','w')
  current_date = date.today()
  run=True
  while run:
      clock.tick(60)
      text_gmail=FONT2.render(user_gmail,True,"black")
      gmail_rect = pygame.Rect(
        (300,250),
        (max(400, text_gmail.get_width() + 20), 50))
      text_pass=FONT2.render(user_password,True,"black")
      pass_rect = pygame.Rect(
        (300,350),
        (max(400, text_pass.get_width() + 20), 50))
      text_name=FONT2.render(user_name,True,"black")
      name_rect = pygame.Rect(
        (300,450),
        (max(400, text_name.get_width() + 20), 50))
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          run=False
        if event.type==pygame.KEYDOWN:
          if (event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER) and pass_pass==False and len(user_gmail)!=0:
            
            pass_pass=True
          elif pass_pass==False and (event.key==pygame.K_DELETE or event.key==pygame.K_BACKSPACE):
            user_gmail=user_gmail[:-1]
          elif pass_pass==False:
            user_gmail+=event.unicode
            
          elif pass_pass==True and pass_name==False:
            if (event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER) and len(user_password)!=0:
              
              pass_name=True
            elif  (event.key==pygame.K_DELETE or event.key==pygame.K_BACKSPACE):
              user_password=user_password[:-1]
            else:
              user_password+=event.unicode
              
          elif pass_name==True:
            if (event.key==pygame.K_RETURN or event.key==pygame.K_KP_ENTER) and len(user_name)!=0:
              
              pass_name==False
              new_id=str(uuid.uuid4())
              data={'gmail':user_gmail,'password':user_password,'name':user_name,'u_id':new_id,'last_date':date.today().isoformat()}
              json.dump(data,f)
              f.close()
              minesweeper.main()
              
              break
            elif  (event.key==pygame.K_DELETE or event.key==pygame.K_BACKSPACE):
              user_name=user_name[:-1]
            else:
              user_name+=event.unicode
              
  
      win.fill((0,0,0))
      win.blit(title,(400,40))
      win.blit(watermark,(20,20))
      win.blit(request,(180,150))
      win.blit(sign_up,(440,200))
      pygame.draw.rect(win,(255, 233, 200),gmail_rect,0,5)
      pygame.draw.rect(win,(255,255,255),gmail_rect,1,5)
      win.blit(show_gmail,(180,265))
      win.blit(text_gmail, (300 + (gmail_rect.width - text_gmail.get_width()) // 2, 250 + (50 - text_gmail.get_height()) // 2))

      pygame.draw.rect(win,(255, 233, 200),pass_rect,0,5)
      pygame.draw.rect(win,(255,255,255),pass_rect,1,5)
      win.blit(show_pass,(180,365))
      win.blit(text_pass, (300 + (pass_rect.width - text_pass.get_width()) // 2, 350 + (50 - text_pass.get_height())//2))
      pygame.draw.rect(win,(255, 233, 200),name_rect,0,5)
      pygame.draw.rect(win,(255,255,255),name_rect,1,5)
      win.blit(show_name,(180,465))
      win.blit(text_name, (300 + (name_rect.width - text_name.get_width()) // 2, 450 + (50 - text_name.get_height())//2))
            
      pygame.display.update()
  pygame.quit()
