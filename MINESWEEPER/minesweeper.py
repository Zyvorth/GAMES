import pygame
import time
import json 
import minesweeper_back
from supabase import create_client
url = "https://povqbyyplyqdntdnowfv.supabase.co"
key = "sb_publishable_1mtsCxMXYITJMNVofwzZdg_UasPvA5f"
supabase = create_client(url, key)

pygame.init()
hover_img=pygame.image.load("IMAGES/minesweeper_tiles/masked_tile_hover.png")
hover_img_1 = pygame.transform.scale(hover_img,(40, 40))
hover_img_2 = pygame.transform.scale(hover_img,(35, 35))
hover_img_3 = pygame.transform.scale(hover_img,(30,30))

def hover(mode,cell,stat):
  if stat==False:
    if mode==1:
      for i in cell:
        tile=pygame.Rect(i["x_pos"],i["y_pos"],40,40)
        keys = pygame.key.get_pressed()
        if tile.collidepoint(pygame.mouse.get_pos()) and (i["mine"]==0 or i["mine"]==1) and  i["revealed"]==0 and i["flag"]==0 and keys[pygame.K_f]==False:
          win.blit(hover_img_1,(i["x_pos"],i["y_pos"]))
        
    elif mode==2:
  
      for i in cell:
        tile=pygame.Rect(i["x_pos"],i["y_pos"],35,35)
        keys = pygame.key.get_pressed()
        if tile.collidepoint(pygame.mouse.get_pos()) and (i["mine"]==0 or i["mine"]==1) and  i["revealed"]==0 and i["flag"]==0 and keys[pygame.K_f]==False:
          win.blit(hover_img_2,(i["x_pos"],i["y_pos"]))
    
    elif mode==3:
      for i in cell:
        tile=pygame.Rect(i["x_pos"],i["y_pos"],30,30)
        keys = pygame.key.get_pressed()
        if tile.collidepoint(pygame.mouse.get_pos()) and (i["mine"]==0 or i["mine"]==1) and  i["revealed"]==0 and i["flag"]==0 and keys[pygame.K_f]==False:
          win.blit(hover_img_3,(i["x_pos"],i["y_pos"]))
  else:
    return 
    

def draw_again():
  FONT1=pygame.font.SysFont("Consolas",32,bold=True)
  FONT1.set_underline(True)
  FONT2=pygame.font.SysFont("Consolas",20)
  
  title = FONT1.render("MINESWEEPER", True, (0,255,0))
  win.fill((0,0,0))
  win.blit(title,(400,40))
  l1="Welcome To Minesweeper !"
  l2="Please Chose the level you want to play at"
  p1 = FONT2.render(l1,True,(255,255,255))
  p2=FONT2.render(l2,True,(255,255,255))
  win.blit(p1,(200,130))
  win.blit(p2,(200,170))
  pygame.display.update()
  
  

class banner():
  def __init__(self,text,posx,posy,width,height):
    self.text=text
    self.posx=posx
    self.posy=posy
    self.width=width
    self.height=height
  
  def draw_ban(self):
    FONT2=pygame.font.SysFont("Consolas",20)
    banner_rect=pygame.rect.Rect((self.posx,self.posy),(self.width,self.height))
    pygame.draw.rect(win,'black',banner_rect,0,5)
    pygame.draw.rect(win,'red',banner_rect,2,5)
    text_c=self.text.split().copy()
    str_txt=""
    c=5
    for j in text_c:
      test_line=str_txt[:]
      str_txt=str_txt+" "+j
      t=FONT2.render(str_txt,True,'white')
      t_test=FONT2.render(test_line,True,'white')
      if t.get_width()>=(self.width-10):
        win.blit(t_test,((self.posx+((self.width-t_test.get_width())//2)),self.posy+c))
        c+=25
        str_txt=j
    k=FONT2.render(str_txt,True,'white')
    win.blit(k,((self.posx+((self.width-k.get_width())//2)),self.posy+c))
    

def draw():
  text_c = 0
  vol_c=0.1
  for i in range(len(l_text)+1):
    pygame.mixer.music.set_volume(vol_c)
    vol_c+=0.003
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          return
    clock.tick(15)
    title = FONT1.render("MINESWEEPER", True, (0,255,0))
    watermark=FONT2.render("Zyvorth_CORE",True,'white')
    win.fill((0,0,0))
    win.blit(title,(400,40))
    win.blit(watermark,(20,20))
    # first line
    first = l_text[0:min(text_c,l_text_individual[0])]
    p1 = FONT2.render(first, True, (255,255,255))
    win.blit(p1,(200,130))
    # second line
    if text_c > l_text_individual[0]:
        second = l_text[
            l_text_individual[0]:
            text_c]
        p2 = FONT2.render(second, True, (255,255,255))
        win.blit(p2,(200,170))
    if text_c>=sum(l_text_individual):
      break
    text_c += 1
    pygame.display.update()
  title = FONT1.render("MINESWEEPER", True, (0,255,0))
  win.fill((0,0,0))
  win.blit(title,(400,40))
  win.blit(watermark,(20,20))
  l1="Welcome To Minesweeper !"
  l2="Please Chose the level you want to play at"
  p1 = FONT2.render(l1,True,(255,255,255))
  p2=FONT2.render(l2,True,(255,255,255))
  win.blit(p1,(200,130))
  win.blit(p2,(200,170))
  pygame.display.update()
  

class Button():
  def __init__(self,text,x_pos,y_pos,width,height,color,enabled):
    self.text=text
    self.x_pos=x_pos
    self.y_pos=y_pos
    self.width=width
    self.height=height
    self.color=color
    self.enabled=enabled
  def draw_but(self):
    FONT=pygame.font.SysFont("Consolas",20,bold=True)
    button_text=FONT.render(self.text,True,'white')
    button_rect=pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))
    pygame.draw.rect(win,self.color,button_rect,0,5)
    pygame.draw.rect(win,(0,255,0),button_rect,2,5)
    win.blit(button_text,((self.x_pos + (self.width - button_text.get_width()) // 2),(self.y_pos + (self.height - button_text.get_height()) // 2)))
      
    
      
  def button_clicked(self):
    mouse_pose=pygame.mouse.get_pos()
    right_click=pygame.mouse.get_pressed()[2]
    button_rect=pygame.rect.Rect((self.x_pos,self.y_pos),(self.width,self.height))
    if right_click and button_rect.collidepoint(mouse_pose) and self.enabled:
      button_mus=pygame.mixer.Sound('SOUNDS/button.mp3')
      button_mus.play()
      return True
    else:
      return False

#INTIALIZING PART

WIDTH,HEIGHT=1000,800
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("MINESWEEPER")
clock=pygame.time.Clock()
FONT1=pygame.font.SysFont("Consolas",32,bold=True)
FONT1.set_underline(True)
FONT2=pygame.font.SysFont("Consolas",20)
l_text = "Welcome To Minesweeper ! Please Chose the level you want to play at"
l_text_individual = [len("Welcome To Minesweeper !"),len("Please Chose the level you want to play at")]
    
  
def main():
  with open('user_minesweep_data.json', 'r') as f:
        data=json.load(f)
 
  typed_again=True
  pygame.mixer.music.load('SOUNDS/bg.mp3')
  run=True
  typed=False
  win.fill((0,0,0))
  pygame.mixer.music.play(-1)#-1 loops it forever
  pygame.display.update()
  exit_top_10=Button("EXIT",470,740,60,30,'red',True)
  beginner_button=Button("BEGINNER",100,250,200,50,'black',True)
  intermediate_button=Button("INTERMEDIATE",400,250,200,50,'black',True)
  advanced_button=Button("ADVANCED",700,250,200,50,'black',True)
  beginner_banner=banner("9x9 grid with 10 mines which are randomly placed ",
                         100,310,200,250)
  intermediate_banner=banner("16x16 grid with 40 mines which are randomly placed ",
                         400,310,200,250)
  advanced_banner=banner("30x16 grid with 99 mines which are randomly placed ",
                         700,310,200,250)
  
  top_ten=Button("TOP TEN",450,620,100,50,(0,0,255),'True')
  beg_1 = pygame.Rect(30, 220, 300, 40)
  beg_2 = pygame.Rect(30, 270, 300, 40)
  beg_3 = pygame.Rect(30, 320, 300, 40)
  beg_4 = pygame.Rect(30, 370, 300, 40)
  beg_5 = pygame.Rect(30, 420, 300, 40)
  beg_6 = pygame.Rect(30, 470, 300, 40)
  beg_7 = pygame.Rect(30, 520, 300, 40)
  beg_8 = pygame.Rect(30, 570, 300, 40)
  beg_9 = pygame.Rect(30, 620, 300, 40)
  beg_10 = pygame.Rect(30,670, 300, 40)
  
  inter_1 = pygame.Rect(350, 220, 300, 40)
  inter_2 = pygame.Rect(350, 270, 300, 40)
  inter_3 = pygame.Rect(350, 320, 300, 40)
  inter_4 = pygame.Rect(350, 370, 300, 40)
  inter_5 = pygame.Rect(350, 420, 300, 40)
  inter_6 = pygame.Rect(350, 470, 300, 40)
  inter_7 = pygame.Rect(350, 520, 300, 40)
  inter_8 = pygame.Rect(350, 570, 300, 40)
  inter_9 = pygame.Rect(350, 620, 300, 40)
  inter_10 = pygame.Rect(350,670, 300, 40)
  
  adv_1 = pygame.Rect(670, 220, 300, 40)
  adv_2 = pygame.Rect(670, 270, 300, 40)
  adv_3 = pygame.Rect(670, 320, 300, 40)
  adv_4 = pygame.Rect(670, 370, 300, 40)
  adv_5 = pygame.Rect(670, 420, 300, 40)
  adv_6 = pygame.Rect(670, 470, 300, 40)
  adv_7 = pygame.Rect(670, 520, 300, 40)
  adv_8 = pygame.Rect(670, 570, 300, 40)
  adv_9 = pygame.Rect(670, 620, 300, 40)
  adv_10 = pygame.Rect(670,670, 300, 40)
  FONT1=pygame.font.SysFont("Consolas",32,bold=True)
  FONT1.set_underline(True)
  FONT2=pygame.font.SysFont("Consolas",20)
  FONT4=pygame.font.SysFont("Consolas",26,bold=True)
  FONT4.set_underline(True)

  pygame.display.update()
  pygame.mixer.music.load('SOUNDS/bg.mp3')
  pygame.mixer.music.play(-1)
  restart_1=False
  restart_2=False
  restart_3=False
  while run:
    clock.tick(60)
    if not typed:
      watermark=FONT2.render("Zyvorth_CORE",True,'white')
      win.blit(watermark,(20,20))
      draw()
      typed = True
    beginner_button.draw_but()
    intermediate_button.draw_but()
    advanced_button.draw_but()
    top_ten.draw_but()
    beginner_banner.draw_ban()
    intermediate_banner.draw_ban()
    advanced_banner.draw_ban()
    exit_top=False
    if top_ten.button_clicked():
      while exit_top==False:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            return
        clock.tick(60)
        win.fill((0,0,0))
        exit_top_10.draw_but()
        if exit_top_10.button_clicked():
          exit_top=True
          title = FONT1.render("MINESWEEPER", True, (0,255,0))
          watermark=FONT2.render("Zyvorth_CORE",True,'white')
          win.fill((0,0,0))
          win.blit(title,(400,40))
          win.blit(watermark,(20,20))
          l1="Welcome To Minesweeper !"
          l2="Please Chose the level you want to play at"
          p1 = FONT2.render(l1,True,(255,255,255))
          p2=FONT2.render(l2,True,(255,255,255))
          win.blit(p1,(200,130))
          win.blit(p2,(200,170))
          break
        title = FONT1.render("MINESWEEPER", True, (0,255,0))
        top=FONT1.render("TOP 10 GLOBALLY",True,(0,255,0))
        watermark=FONT2.render("Zyvorth_CORE",True,'white')
        time_unit_ten=FONT2.render("The Time is in seconds",True,'white')
        beg_top=FONT4.render("BEGINNER",True,'white')
        inter_top=FONT4.render("INTERMEDIATE",True,'white')
        adv_top=FONT4.render("ADVANCED",True,'white')
        win.blit(title,(400,40))
        win.blit(top,(360,80))
        win.blit(watermark,(20,20))
        win.blit(time_unit_ten,(370,140))
        
        win.blit(beg_top,(115,170))
        win.blit(inter_top,(400,170))
        win.blit(adv_top,(750,170))
        pygame.draw.rect(win, (30, 58, 95), beg_1,0,5)
        pygame.draw.rect(win, (255, 255, 255), beg_1,1,5)
        pygame.draw.rect(win, (30, 58, 95), beg_2,0,5)
        pygame.draw.rect(win, (255, 255, 255), beg_2,1,5)
        pygame.draw.rect(win, (30, 58, 95), beg_3,0,5)
        pygame.draw.rect(win, (255, 255, 255), beg_3,1,5)
        pygame.draw.rect(win, (30, 58, 95), beg_4,0,5)
        pygame.draw.rect(win, (255, 255, 255), beg_4,1,5)
        pygame.draw.rect(win, (30, 58, 95), beg_5,0,5)
        pygame.draw.rect(win, (255, 255, 255), beg_5,1,5)
        pygame.draw.rect(win, (30, 58, 95), beg_6,0,5)
        pygame.draw.rect(win, (255, 255, 255), beg_6,1,5)
        pygame.draw.rect(win, (30, 58, 95), beg_7,0,5)
        pygame.draw.rect(win, (255, 255, 255), beg_7,1,5)
        pygame.draw.rect(win, (30, 58, 95), beg_8,0,5)
        pygame.draw.rect(win, (255, 255, 255), beg_8,1,5)
        pygame.draw.rect(win, (30, 58, 95), beg_9,0,5)
        pygame.draw.rect(win, (255, 255, 255), beg_9,1,5)
        pygame.draw.rect(win, (30, 58, 95), beg_10,0,5)
        pygame.draw.rect(win, (255, 255, 255), beg_10,1,5)
        response_beg = (
            supabase.table("top_ten_beginner")
            .select("*")
            .order("time")
            .execute())
        l_beg=[]
        c_beg=1
        c_beg_y=220
        for j in response_beg.data:
          row_beg=FONT2.render(str(c_beg)+":"+j["player_name"]+":"+str(j["time"]),True,"white")
          win.blit(row_beg,(60,c_beg_y+10))
          c_beg+=1
          c_beg_y+=50
        
        pygame.draw.rect(win, (67, 56, 120), inter_1,0,5)
        pygame.draw.rect(win, (255, 255, 255), inter_1,1,5)
        pygame.draw.rect(win, (67, 56, 120), inter_2,0,5)
        pygame.draw.rect(win, (255, 255, 255), inter_2,1,5)
        pygame.draw.rect(win, (67, 56, 120), inter_3,0,5)
        pygame.draw.rect(win, (255, 255, 255), inter_3,1,5)
        pygame.draw.rect(win, (67, 56, 120), inter_4,0,5)
        pygame.draw.rect(win, (255, 255, 255), inter_4,1,5)
        pygame.draw.rect(win, (67, 56, 120), inter_5,0,5)
        pygame.draw.rect(win, (255, 255, 255), inter_5,1,5)
        pygame.draw.rect(win, (67, 56, 120), inter_6,0,5)
        pygame.draw.rect(win, (255, 255, 255), inter_6,1,5)
        pygame.draw.rect(win, (67, 56, 120), inter_7,0,5)
        pygame.draw.rect(win, (255, 255, 255), inter_7,1,5)
        pygame.draw.rect(win, (67, 56, 120), inter_8,0,5)
        pygame.draw.rect(win, (255, 255, 255), inter_8,1,5)
        pygame.draw.rect(win, (67, 56, 120), inter_9,0,5)
        pygame.draw.rect(win, (255, 255, 255), inter_9,1,5)
        pygame.draw.rect(win, (67, 56, 120), inter_10,0,5)
        pygame.draw.rect(win, (255, 255, 255), inter_10,1,5)
        response_inter = (
            supabase.table("top_ten_intermediate")
            .select("*")
            .order("time")
            .execute())
        c_inter=1
        c_inter_y=220
        for j in response_inter.data:
          row_inter=FONT2.render(str(c_inter)+":"+j["player_name"]+":"+str(j["time"]),True,"white")
          win.blit(row_inter,(380,c_inter_y+10))
          c_inter+=1
          c_inter_y+=50
        
        pygame.draw.rect(win, (110, 45, 90), adv_1,0,5)
        pygame.draw.rect(win, (255, 255, 255), adv_1,1,5)
        pygame.draw.rect(win, (110, 45, 90), adv_2,0,5)
        pygame.draw.rect(win, (255, 255, 255), adv_2,1,5)
        pygame.draw.rect(win, (110, 45, 90), adv_3,0,5)
        pygame.draw.rect(win, (255, 255, 255), adv_3,1,5)
        pygame.draw.rect(win, (110, 45, 90), adv_4,0,5)
        pygame.draw.rect(win, (255, 255, 255), adv_4,1,5)
        pygame.draw.rect(win, (110, 45, 90), adv_5,0,5)
        pygame.draw.rect(win, (255, 255, 255), adv_5,1,5)
        pygame.draw.rect(win, (110, 45, 90), adv_6,0,5)
        pygame.draw.rect(win, (255, 255, 255), adv_6,1,5)
        pygame.draw.rect(win, (110, 45, 90), adv_7,0,5)
        pygame.draw.rect(win, (255, 255, 255), adv_7,1,5)
        pygame.draw.rect(win, (110, 45, 90), adv_8,0,5)
        pygame.draw.rect(win, (255, 255, 255), adv_8,1,5)
        pygame.draw.rect(win, (110, 45, 90), adv_9,0,5)
        pygame.draw.rect(win, (255, 255, 255), adv_9,1,5)
        pygame.draw.rect(win, (110, 45, 90), adv_10,0,5)
        pygame.draw.rect(win, (255, 255, 255), adv_10,1,5)
        response_adv = (
            supabase.table("top_ten_advanced")
            .select("*")
            .order("time")
            .execute())
        c_adv=1
        c_adv_y=220
        for j in response_adv.data:
          row_adv=FONT2.render((str(c_adv)+":"+j["player_name"]+":"+str(j["time"])),True,"white")
          win.blit(row_adv,(700,c_adv_y+10))
          c_adv+=1
          c_adv_y+=50
        pygame.display.update()
      
    if beginner_button.button_clicked() or restart_1==True:
      current_time = time.time()
      restart_1=False
      beginner=True
      cell=minesweeper_back.tile(win,1)
      minesweeper_back.mine_initializer(1)
      mine_status=False
      tile_reveal=True
      first_w=True
      won=False
      while beginner:
        if mine_status==False:
          time_elapsed=round(time.time()-(current_time),2)
        elif mine_status==True and won==True:
          won=False
          response = (
              supabase.table("top_ten_beginner")
              .select("player_id, time")
              .order("time")
              .execute())
          scores = response.data
          print("DATA =", data)
          if len(scores) < 10:
            supabase.table("top_ten_beginner").insert({
              "player_id": data["u_id"],
              "player_name":data["name"],
              "time": time_elapsed
              }).execute()

          else:
            worst_score = scores[-1]["time"]
            if time_elapsed < worst_score:
              worst_player_id = scores[-1]["player_id"]
              supabase.table("top_ten_beginner") \
              .delete() \
              .eq("player_id", worst_player_id) \
              .execute()
              supabase.table("top_ten_beginner").insert({
              "player_id": data["u_id"],
              "player_name": data["name"],
              "time": time_elapsed
              }).execute()
          
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            return
        time_show=FONT2.render(str(time_elapsed),True,'red')
        time_unit=FONT2.render("seconds",True,'red')
        watermark=FONT2.render("Zyvorth_CORE",True,'white')
        win.blit(watermark,(20,20))
        pygame.draw.rect(win, (0, 0, 0), (700, 40, 500, 50))
        win.blit(time_show,(800,40))
        win.blit(time_unit,(900,40))
        beg_banner=pygame.draw.rect(win,'black',[100,100,800,600],0,5)
        pygame.draw.rect(win,'blue',[100,100,800,600],2,5)
        exit_beg=Button("EXIT",300,740,60,30,'red',True)
        exit_beg.draw_but()
        restart_beg=Button("RESTART",600,740,100,30,'green',True)
        restart_beg.draw_but()
        minesweeper_back.tile_placer(win,1)
        right_click=pygame.mouse.get_pressed()[2]
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            return
          if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
              keys = pygame.key.get_pressed()
              if keys[pygame.K_f]:
                n = minesweeper_back.return_tile_no(1)
                if n is not None:
                    minesweeper_back.flagged(n)
        keys = pygame.key.get_pressed()
        if right_click and keys[pygame.K_f]==False:
          if minesweeper_back.mine_result(win,1,0):
            explosion = pygame.mixer.Sound("SOUNDS/explosion.mp3")
            explosion.play()
            mine_status=True
          #minesweeper_back.mine_no(win,1)
        keys = pygame.key.get_pressed()
        if tile_reveal==True and right_click==True and keys[pygame.K_f]==False :
          n=minesweeper_back.return_tile_no(1)
          if n==None:
            pass
          else:
            minesweeper_back.mine_no(win,1,False,n)
            minesweeper_back.reveal_zero(1,win,n,True)
          minesweeper_back.tile_placer(win,1)
          
        if mine_status==True:
          minesweeper_back.mine_result(win,1,1)
        hover(1,cell,mine_status)
        if first_w and minesweeper_back.win(1) :
          won=True
          w_sound = pygame.mixer.Sound("SOUNDS/won.mp3")
          w_sound.play()
          FONT1=pygame.font.SysFont("Consolas",50,bold=True)
          you_won = FONT1.render("YOU WON", True, (255,255,255))
          you_won_can=pygame.draw.rect(win,(0,255,0),(300,25,400,50),0,5)
          pygame.draw.rect(win,(255,255,255),(300,25,400,50),2,5) 
          win.blit(you_won,(300+((400-you_won.get_width())//2),25+((50-you_won.get_height())//2)))
          mine_status=True
          first_w=False
        elif first_w==False:
          FONT1=pygame.font.SysFont("Consolas",50,bold=True)
          you_won = FONT1.render("YOU WON", True, (255,255,255))
          you_won_can=pygame.draw.rect(win,(0,255,0),(300,25,400,50),0,5)
          pygame.draw.rect(win,(255,255,255),(300,25,400,50),2,5) 
          win.blit(you_won,(300+((400-you_won.get_width())//2),25+((50-you_won.get_height())//2)))
          
        pygame.display.update()
        if restart_beg.button_clicked():
          win.fill((0,0,0))
          minesweeper_back.cell.clear()
          restart_1 = True
          beginner = False
          mine_status = False
          first_w = True
          pygame.time.wait(150)
          break
          
        
        if exit_beg.button_clicked():
          typed_again=True
          mine_status=False
          tile_reveal=False
          break

    
    if intermediate_button.button_clicked() or restart_2==True:
      won=False
      current_time=time.time()
      restart_2=False
      pygame.time.wait(200)
      mine_status=False
      intermediate=True 
      cell=minesweeper_back.tile(win,2)
      minesweeper_back.mine_initializer(2)
      tile_reveal=True
      first_w=True
      while intermediate:
        if mine_status==False:
          time_elapsed=round(time.time()-(current_time),2)
        elif mine_status==True and won==True:
          won=False
          response = (
              supabase.table("top_ten_intermediate")
              .select("player_id, time")
              .order("time")
              .execute())
          scores = response.data
          if len(scores) < 10:
            supabase.table("top_ten_intermediate").insert({
              "player_id": data["u_id"],
              "player_name":data["name"],
              "time": time_elapsed
              }).execute()

          else:
            worst_score = scores[-1]["time"]
            if time_elapsed < worst_score:
              worst_player_id = scores[-1]["player_id"]
              supabase.table("top_ten_intermediate") \
              .delete() \
              .eq("player_id", worst_player_id) \
              .execute()
              supabase.table("top_ten_intermediate").insert({
              "player_id": data["u_id"],
              "player_name": data["name"],
              "time": time_elapsed
              }).execute()
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            minesweeper_back.cell.clear()
            pygame.quit()
            return
        time_show=FONT2.render(str(time_elapsed),True,'red')
        time_unit=FONT2.render("seconds",True,'red')
        watermark=FONT2.render("Zyvorth_CORE",True,'white')
        win.blit(watermark,(20,20))
        pygame.draw.rect(win, (0, 0, 0), (700, 40, 500, 50))
        win.blit(time_show,(800,40))
        win.blit(time_unit,(900,40))
        inter_banner=pygame.draw.rect(win,'black',[100,100,800,600],0,5)
        pygame.draw.rect(win,'blue',[100,100,800,600],2,5)
        exit_inter=Button("EXIT",300,740,60,30,'red',True)
        exit_inter.draw_but()
        restart_int=Button("RESTART",600,740,100,30,'green',True)
        restart_int.draw_but()
        minesweeper_back.tile_placer(win,2)
        right_click=pygame.mouse.get_pressed()[2]
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            return
          if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
              keys = pygame.key.get_pressed()
              if keys[pygame.K_f]:
                n = minesweeper_back.return_tile_no(2)
                if n is not None:
                    minesweeper_back.flagged(n)
        keys = pygame.key.get_pressed()
        if right_click and keys[pygame.K_f]==False:
          if minesweeper_back.mine_result(win,2,0):
            explosion = pygame.mixer.Sound("SOUNDS/explosion.mp3")
            explosion.play()
            mine_status=True
        if tile_reveal==True and right_click==True and keys[pygame.K_f]==False:
          n=minesweeper_back.return_tile_no(2)
          if n==None:
            pass
          else:
            minesweeper_back.mine_no(win,2,False,n)
            minesweeper_back.reveal_zero(2,win,n,True)
          minesweeper_back.tile_placer(win,2)
        if mine_status==True:
          minesweeper_back.mine_result(win,2,1)
        hover(2,cell,mine_status)
        if first_w and minesweeper_back.win(2) :
          won=True
          w_sound = pygame.mixer.Sound("SOUNDS/won.mp3")
          w_sound.play()
          FONT1=pygame.font.SysFont("Consolas",50,bold=True)
          you_won = FONT1.render("YOU WON", True, (255,255,255))
          you_won_can=pygame.draw.rect(win,(0,255,0),(300,25,400,50),0,5)
          pygame.draw.rect(win,(255,255,255),(300,25,400,50),2,5) 
          win.blit(you_won,(300+((400-you_won.get_width())//2),25+((50-you_won.get_height())//2)))
          mine_status=True
          first_w=False
        elif first_w==False:
          FONT1=pygame.font.SysFont("Consolas",50,bold=True)
          you_won = FONT1.render("YOU WON", True, (255,255,255))
          you_won_can=pygame.draw.rect(win,(0,255,0),(300,25,400,50),0,5)
          pygame.draw.rect(win,(255,255,255),(300,25,400,50),2,5) 
          win.blit(you_won,(300+((400-you_won.get_width())//2),25+((50-you_won.get_height())//2)))
        pygame.display.update()
        if restart_int.button_clicked():
          win.fill((0,0,0))
          minesweeper_back.cell.clear()
          restart_2 = True
          beginner = False
          mine_status = False
          first_w = True
          pygame.time.wait(150)
          break
          
        if exit_inter.button_clicked():
          minesweeper_back.cell.clear()
          typed_again=True
          mine_status=False
          tile_reveal=False
          break 
    if advanced_button.button_clicked() or restart_3==True:
      current_time=time.time()
      restart_3=False
      pygame.time.wait(200)
      advanced=True
      cell=minesweeper_back.tile(win,3)
      minesweeper_back.mine_initializer(3)
      mine_status=False
      tile_reveal=True
      first_w=True
      won=False
      while advanced:
        if mine_status==False:
          time_elapsed=round(time.time()-(current_time),2)
        elif mine_status==True and won==True:
          won=False
          response = (
              supabase.table("top_ten_advanced")
              .select("player_id, time")
              .order("time")
              .execute())
          scores = response.data
          if len(scores) < 10:
            supabase.table("top_ten_advanced").insert({
              "player_id": data["u_id"],
              "player_name":data["name"],
              "time": time_elapsed
              }).execute()

          else:
            worst_score = scores[-1]["time"]
            if time_elapsed < worst_score:
              worst_player_id = scores[-1]["player_id"]
              supabase.table("top_ten_advanced") \
              .delete() \
              .eq("player_id", worst_player_id) \
              .execute()
              supabase.table("top_ten_advanced").insert({
              "player_id": data["u_id"],
              "player_name": data["name"],
              "time": time_elapsed
              }).execute()
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            return
        time_show=FONT2.render(str(time_elapsed),True,'red')
        time_unit=FONT2.render("seconds",True,'red')
        watermark=FONT2.render("Zyvorth_CORE",True,'white')
        win.blit(watermark,(20,20))
        pygame.draw.rect(win, (0, 0, 0), (700, 40, 500, 50))
        win.blit(time_show,(800,40))
        win.blit(time_unit,(900,40))
        adv_banner=pygame.draw.rect(win,'black',[0,100,1000,600],0,5)
        pygame.draw.rect(win,'blue',[0,100,1000,600],2,5)
        exit_adv=Button("EXIT",300,740,60,50,'red',True)
        exit_adv.draw_but()
        restart_adv=Button("RESTART",600,740,100,30,'green',True)
        restart_adv.draw_but()
        minesweeper_back.tile_placer(win,3)
        right_click=pygame.mouse.get_pressed()[2]
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            pygame.quit()
            return
          if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 3:
              keys = pygame.key.get_pressed()
              if keys[pygame.K_f]:
                n = minesweeper_back.return_tile_no(3)
                if n is not None:
                    minesweeper_back.flagged(n)
        keys = pygame.key.get_pressed()
        if right_click and keys[pygame.K_f]==False:
          if minesweeper_back.mine_result(win,3,0):
            explosion = pygame.mixer.Sound("SOUNDS/explosion.mp3")
            explosion.play()
            mine_status=True
        if tile_reveal==True and right_click==True and mine_status==False and keys[pygame.K_f]==False:
          n=minesweeper_back.return_tile_no(3)
          if n==None:
            pass
          else:
            minesweeper_back.mine_no(win,3,False,n)
            minesweeper_back.reveal_zero(3,win,n,True)
          minesweeper_back.tile_placer(win,3)
        if mine_status==True:
          minesweeper_back.mine_result(win,3,1)
        hover(3,cell,mine_status)
        if first_w and minesweeper_back.win(3) :
          w_sound = pygame.mixer.Sound("SOUNDS/won.mp3")
          w_sound.play()
          FONT1=pygame.font.SysFont("Consolas",50,bold=True)
          you_won = FONT1.render("YOU WON", True, (255,255,255))
          you_won_can=pygame.draw.rect(win,(0,255,0),(300,25,400,50),0,5)
          pygame.draw.rect(win,(255,255,255),(300,25,400,50),2,5) 
          win.blit(you_won,(300+((400-you_won.get_width())//2),25+((50-you_won.get_height())//2)))
          mine_status=True
          first_w=False
        elif first_w==False:
          FONT1=pygame.font.SysFont("Consolas",50,bold=True)
          you_won = FONT1.render("YOU WON", True, (255,255,255))
          you_won_can=pygame.draw.rect(win,(0,255,0),(300,25,400,50),0,5)
          pygame.draw.rect(win,(255,255,255),(300,25,400,50),2,5) 
          win.blit(you_won,(300+((400-you_won.get_width())//2),25+((50-you_won.get_height())//2)))
        pygame.display.update()
        if restart_adv.button_clicked():
          win.fill((0,0,0))
          minesweeper_back.cell.clear()
          restart_3 = True
          beginner = False
          mine_status = False
          first_w = True
          pygame.time.wait(150)
          break
        if exit_adv.button_clicked():
          minesweeper_back.cell.clear()
          typed_again=True
          mine_status=False
          tile_reveal=False
          break
  
    if typed_again:
        draw_again()
        watermark=FONT2.render("Zyvorth_CORE",True,'white')
        win.blit(watermark,(20,20))
        typed_again = False
    pygame.display.update()
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
  pygame.quit()
if __name__=="__main__":
  main()
