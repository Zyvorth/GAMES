#* Beginner → 9×9 grid with 10 mines
#* Intermediate → 16×16 grid with 40 mines
#* Expert → 30×16 grid with 99 mines
import pygame
import secrets 
pygame.init()
cell=[]
mine=[]

#MOST OF THE IMAGES LOADED
flag=pygame.image.load("IMAGES/minesweeper_tiles/masked_tile_flag.png")
flag_1=pygame.transform.scale(flag,(40,40))
flag_2=pygame.transform.scale(flag,(35,35))
flag_3=pygame.transform.scale(flag,(30,30))
img_0=pygame.image.load("IMAGES/minesweeper_tiles/revealed_tile.png")
img_0_1= pygame.transform.scale(img_0, (40,40))
img_0_2= pygame.transform.scale(img_0, (35,35))
img_0_3= pygame.transform.scale(img_0, (30,30))

img_1=pygame.image.load("IMAGES/minesweeper_tiles/revealed_tile_1.png")
img_1_1= pygame.transform.scale(img_1, (40,40))
img_1_2= pygame.transform.scale(img_1, (35,35))
img_1_3= pygame.transform.scale(img_1, (30,30))

img_2=pygame.image.load("IMAGES/minesweeper_tiles/revealed_tile_2.png")
img_2_1= pygame.transform.scale(img_2, (40,40))
img_2_2= pygame.transform.scale(img_2, (35,35))
img_2_3= pygame.transform.scale(img_2, (30,30))

img_3=pygame.image.load("IMAGES/minesweeper_tiles/revealed_tile_3.png")
img_3_1= pygame.transform.scale(img_3, (40,40))
img_3_2= pygame.transform.scale(img_3, (35,35))
img_3_3= pygame.transform.scale(img_3, (30,30))

img_4=pygame.image.load("IMAGES/minesweeper_tiles/revealed_tile_4.png")
img_4_1= pygame.transform.scale(img_4, (40,40))
img_4_2= pygame.transform.scale(img_4, (35,35))
img_4_3= pygame.transform.scale(img_4, (30,30))

img_5=pygame.image.load("IMAGES/minesweeper_tiles/revealed_tile_5.png")
img_5_1= pygame.transform.scale(img_5, (40,40))
img_5_2= pygame.transform.scale(img_5, (35,35))
img_5_3= pygame.transform.scale(img_5, (30,30))

img_6=pygame.image.load("IMAGES/minesweeper_tiles/revealed_tile_6.png")
img_6_1= pygame.transform.scale(img_6, (40,40))
img_6_2= pygame.transform.scale(img_6, (35,35))
img_6_3= pygame.transform.scale(img_6, (40,40))

img_7=pygame.image.load("IMAGES/minesweeper_tiles/revealed_tile_7.png")
img_7_1= pygame.transform.scale(img_7, (40,40))
img_7_2= pygame.transform.scale(img_7, (35,35))
img_7_3= pygame.transform.scale(img_7, (30,30))

img_8=pygame.image.load("IMAGES/minesweeper_tiles/revealed_tile_8.png")
img_8_1= pygame.transform.scale(img_8, (40,40))
img_8_2= pygame.transform.scale(img_8, (35,35))
img_8_3= pygame.transform.scale(img_8, (30,30))
#def blast(mode,win,n_x,n_y,tile_no):
  
    

def tile(win,mode):
  cell.clear()
  if mode==1:#cell.append({'x_pos':c_x,'y_pos':c_y,'width':40,'height':40,'stat':0,"tile_no_x":c_tile,"tile_no_y":c_title_y})
    first_x=100+((800-(40*9))//2) #i hardcoded this 🗣️
    first_y=100+((600-(40*9))//2)
    c_x=first_x
    c_y=first_y #800*600
    c_tile_x=1
    c_tile_y=1
    for i in range(81):
      cell.append({'x_pos':c_x,'y_pos':c_y,'width':40,'height':40,'stat':0,"tile_no_x":c_tile_x,"tile_no_y":c_tile_y,"mine":0,"revealed":0,"count":0,"flag":0})
      c_x=c_x+40
      c_tile_x+=1
      if c_tile_x==10:
        c_tile_y+=1
        c_x=first_x
        c_tile_x=1
        c_y=c_y+40
  elif mode==2:
    first_x=100+((800-(35*16))//2) #i hardcoded this 🗣️
    first_y=100+((600-(35*16))//2)
    c_x=first_x
    c_y=first_y #win=800*600
    c_tile_x=1
    c_tile_y=1
    for k in range(16*16):
      cell.append({'x_pos':c_x,'y_pos':c_y,'width':35,'height':35,'stat':0,"mine":0,"tile_no_x":c_tile_x,"tile_no_y":c_tile_y,"revealed":0,"count":0,"flag":0})
      c_x=c_x+35
      c_tile_x+=1
      if c_tile_x==17:
        c_tile_y+=1
        c_x=first_x
        c_tile_x=1
        c_y=c_y+35
  elif mode==3:
    first_x=100+((800-(30*30))//2) #i hardcoded this 🗣️
    first_y=100+((600-(30*16))//2)
    c_x=first_x
    c_y=first_y #win=800*600
    c_tile_x=1
    c_tile_y=1
    for _ in range(30*16):
      cell.append({'x_pos':c_x,'y_pos':c_y,'width':30,'height':30,'stat':0,"tile_no_x":c_tile_x,"tile_no_y":c_tile_y,"mine":0,"revealed":0,"count":0,"flag":0})
      c_x=c_x+30
      c_tile_x+=1
      if c_tile_x==31:
        c_tile_y+=1
        c_x=first_x
        c_tile_x=1
        c_y=c_y+30
  return cell
  
  
def tile_placer(win,mode):
  if mode==1:
    tile = pygame.image.load("IMAGES/minesweeper_tiles/masked_tile.png")
    tile = pygame.transform.scale(tile, (40, 40))
    for i in cell:
      if i["flag"]==1:
        win.blit(flag_1,(i["x_pos"],i["y_pos"]))
      elif i["revealed"]==0:
        win.blit(tile,(i["x_pos"],i["y_pos"]))
      else:
        if i["count"]==0:
          win.blit(img_0_1,(i["x_pos"],i["y_pos"]))
        if i["count"]==1:

          win.blit(img_1_1,(i["x_pos"],i["y_pos"]))
        if i["count"]==2:

          win.blit(img_2_1,(i["x_pos"],i["y_pos"]))
        if i["count"]==3:

          win.blit(img_3_1,(i["x_pos"],i["y_pos"]))
        if i["count"]==4:

          win.blit(img_4_1,(i["x_pos"],i["y_pos"]))
        if i["count"]==5:

          win.blit(img_5_1,(i["x_pos"],i["y_pos"]))
        if i["count"]==6:

          win.blit(img_6_1,(i["x_pos"],i["y_pos"]))
        if i["count"]==7:

          win.blit(img_7_1,(i["x_pos"],i["y_pos"]))
        if i["count"]==8:

          win.blit(img_8_1,(i["x_pos"],i["y_pos"]))
        
  elif mode==2:
    tile = pygame.image.load("IMAGES/minesweeper_tiles/masked_tile.png")
    tile = pygame.transform.scale(tile, (35, 35))
    for i in cell:
      if i["flag"]==1:
        win.blit(flag_2,(i["x_pos"],i["y_pos"]))
      elif i["revealed"]==0:
        win.blit(tile,(i["x_pos"],i["y_pos"]))
      else:
        if i["count"]==0:
          win.blit(img_0_2,(i["x_pos"],i["y_pos"]))
        if i["count"]==1:

          win.blit(img_1_2,(i["x_pos"],i["y_pos"]))
        if i["count"]==2:

          win.blit(img_2_2,(i["x_pos"],i["y_pos"]))
        if i["count"]==3:

          win.blit(img_3_2,(i["x_pos"],i["y_pos"]))
        if i["count"]==4:

          win.blit(img_4_2,(i["x_pos"],i["y_pos"]))
        if i["count"]==5:

          win.blit(img_5_2,(i["x_pos"],i["y_pos"]))
        if i["count"]==6:

          win.blit(img_6_2,(i["x_pos"],i["y_pos"]))
        if i["count"]==7:

          win.blit(img_7_2,(i["x_pos"],i["y_pos"]))
        if i["count"]==8:

          win.blit(img_8_2,(i["x_pos"],i["y_pos"]))
  elif mode==3:
    tile= pygame.image.load("IMAGES/minesweeper_tiles/masked_tile.png")
    tile = pygame.transform.scale(tile, (30,30))
    for i in cell:
      if i["flag"]==1:
        win.blit(flag_3,(i["x_pos"],i["y_pos"]))
      elif i["revealed"]==0:
        win.blit(tile,(i["x_pos"],i["y_pos"])) 
      else:
        if i["count"]==0:
          win.blit(img_0_3,(i["x_pos"],i["y_pos"]))
        if i["count"]==1:

          win.blit(img_1_3,(i["x_pos"],i["y_pos"]))
        if i["count"]==2:

          win.blit(img_2_3,(i["x_pos"],i["y_pos"]))
        if i["count"]==3:

          win.blit(img_3_3,(i["x_pos"],i["y_pos"]))
        if i["count"]==4:

          win.blit(img_4_3,(i["x_pos"],i["y_pos"]))
        if i["count"]==5:

          win.blit(img_5_3,(i["x_pos"],i["y_pos"]))
        if i["count"]==6:

          win.blit(img_6_3,(i["x_pos"],i["y_pos"]))
        if i["count"]==7:

          win.blit(img_7_3,(i["x_pos"],i["y_pos"]))
        if i["count"]==8:

          win.blit(img_8_3,(i["x_pos"],i["y_pos"])) 


def mine_initializer(mode):
  mine.clear()
  if mode==1:
    c=0
    mine_l=[]
    while c<10:
      x_no=secrets.randbelow(9)+1
      y_no=secrets.randbelow(9)+1
      for i in mine_l:
        if i[0]==x_no and i[1]==y_no:
          break
      else:#cell.append({'x_pos':c_x,'y_pos':c_y,'width':40,'height':40,'stat':0,"tile_no_x":c_tile,"tile_no_y":c_title_y})
          mine_l.append([x_no,y_no])
          c_no=(y_no-1)*9+x_no
          mine.append(c_no)
          cell[c_no-1]["mine"]=1
          c+=1
          
  elif mode==2:
    mine_l=[]
    c=0
    while c<40:
      x_no=secrets.randbelow(16)+1
      y_no=secrets.randbelow(16)+1
      for i in mine_l:
        if i[0]==x_no and i[1]==y_no:
          break
      else:
        c+=1
        mine_l.append([x_no,y_no])
        c_no=(y_no-1)*16+x_no
        mine.append(c_no)
        cell[c_no-1]["mine"]=1
        
  elif mode==3:
    c=0
    mine_l=[]
    while c<99:
      x_no=secrets.randbelow(30)+1
      y_no=secrets.randbelow(16)+1
      for i in mine_l:
        if i[0]==x_no and i[1]==y_no:
          break
      else:
        c+=1
        mine_l.append([x_no,y_no])
        c_no=(y_no-1)*30+x_no
        mine.append(c_no)
        cell[c_no-1]["mine"]=1

  


def mine_result(win,mode,res):
  if res==0:
    if mode==1:
      mine_img = pygame.image.load("IMAGES/minesweeper_tiles/tile_exploded.png")
      mine_img = pygame.transform.scale(mine_img, (40,40))
      for i in cell:
        tile=pygame.Rect(i["x_pos"],i["y_pos"],40,40)
        if tile.collidepoint(pygame.mouse.get_pos()) and i["mine"]==1:
          for j in mine:
            win.blit(mine_img,(cell[j-1]["x_pos"],cell[j-1]["y_pos"]))
          return True 
    elif mode==2:
      mine_img = pygame.image.load("IMAGES/minesweeper_tiles/tile_exploded.png")
      mine_img = pygame.transform.scale(mine_img, (35,35))
      for i in cell:
        tile=pygame.Rect(i["x_pos"],i["y_pos"],35,35)
        if tile.collidepoint(pygame.mouse.get_pos()) and i["mine"]==1:
          for j in mine:
            win.blit(mine_img,(cell[j-1]["x_pos"],cell[j-1]["y_pos"])) 
          return True        
    elif mode==3:
      mine_img = pygame.image.load("IMAGES/minesweeper_tiles/tile_exploded.png")
      mine_img = pygame.transform.scale(mine_img, (30,30))
      for i in cell:
        tile=pygame.Rect(i["x_pos"],i["y_pos"],30,30)
        if tile.collidepoint(pygame.mouse.get_pos()) and i["mine"]==1:
          for j in mine:
            win.blit(mine_img,(cell[j-1]["x_pos"],cell[j-1]["y_pos"]))         
          return True
  elif res==1:
    FONT1=pygame.font.SysFont("Consolas",50,bold=True)
    you_lost = FONT1.render("YOU LOST", True, (255,255,255))
    if mode==1:
      mine_img = pygame.image.load("IMAGES/minesweeper_tiles/tile_exploded.png")
      mine_img = pygame.transform.scale(mine_img, (40,40))
      for i in cell:
        tile=pygame.Rect(i["x_pos"],i["y_pos"],40,40)
        if i["mine"]==1:
          for j in mine:
            win.blit(mine_img,(cell[j-1]["x_pos"],cell[j-1]["y_pos"]))
            you_lost_can=pygame.draw.rect(win,(255,0,0),(300,25,400,50),0,5)
            pygame.draw.rect(win,(255,255,255),(300,25,400,50),2,5) 
            win.blit(you_lost,(300+((400-you_lost.get_width())//2),25+((50-you_lost.get_height())//2)))
      
    elif mode==2:
      mine_img = pygame.image.load("IMAGES/minesweeper_tiles/tile_exploded.png")
      mine_img = pygame.transform.scale(mine_img, (35,35))
      for i in cell:
        tile=pygame.Rect(i["x_pos"],i["y_pos"],35,35)
        if i["mine"]==1:
          for j in mine:
            win.blit(mine_img,(cell[j-1]["x_pos"],cell[j-1]["y_pos"])) 
            you_lost_can=pygame.draw.rect(win,(255,0,0),(300,25,400,50),0,5)
            pygame.draw.rect(win,(255,255,255),(300,25,400,50),2,5) 
            win.blit(you_lost,(300+((400-you_lost.get_width())//2),25+((50-you_lost.get_height())//2)))         
    elif mode==3:
      mine_img = pygame.image.load("IMAGES/minesweeper_tiles/tile_exploded.png")
      mine_img = pygame.transform.scale(mine_img, (30,30))
      for i in cell:
        tile=pygame.Rect(i["x_pos"],i["y_pos"],30,30)
        if i["mine"]==1:
          for j in mine:
            win.blit(mine_img,(cell[j-1]["x_pos"],cell[j-1]["y_pos"]))
            you_lost_can=pygame.draw.rect(win,(255,0,0),(300,25,400,50),0,5)
            pygame.draw.rect(win,(255,255,255),(300,25,400,50),2,5) 
            win.blit(you_lost,(300+((400-you_lost.get_width())//2),25+((50-you_lost.get_height())//2))) 



def mine_no(win,mode,inside,k):
  i=cell[k-1]
  if mode==1:
      tile=pygame.Rect(i["x_pos"],i["y_pos"],40,40)
      if inside:
        mouse=True
      else:
        mouse=tile.collidepoint(pygame.mouse.get_pos())
      n_x=i["tile_no_x"]
      n_y=i["tile_no_y"]

      if mouse and i["mine"]==0  and i["flag"]==0:
        i["revealed"]=1
        if n_x>1 and n_x<9 and n_y>1 and n_y<9:
          c_mine=0
          n_index=((n_y-1)*9+n_x)-1
          if cell[n_index+1]["mine"]==1 :
            c_mine+=1
          if cell[n_index-1]["mine"]==1 :
            c_mine+=1
          if cell[n_index-9]["mine"]==1  :
            c_mine+=1
          if cell[n_index+9]["mine"]==1:
            c_mine+=1
          if cell[n_index-9+1]["mine"]==1 :
            c_mine+=1
          if cell[n_index-9-1]["mine"]==1 :
            c_mine+=1
          if cell[n_index+9+1]["mine"]==1 :
            c_mine+=1
          if cell[n_index+9-1]["mine"]==1 :
            c_mine+=1
          i["count"]=c_mine 

          i["around"]=[n_index+1+1,n_index-1+1,n_index-9+1,n_index+9+1,n_index-9+1+1,n_index-9-1+1,n_index+9+1+1,n_index+9-1+1]
        else:
          if n_y==1 and n_x>1 and n_x<9:
            c_mine=0
            n_index=((n_y-1)*9+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-1]["mine"]==1:
              c_mine+=1
            if cell[n_index+9]["mine"]==1:
              c_mine+=1
            if cell[n_index+9+1]["mine"]==1:
              c_mine+=1
            if cell[n_index+9-1]["mine"]==1:
              c_mine+=1
            i["count"]=c_mine

            i["around"]=[n_index+1+1,n_index-1+1,n_index+9+1,n_index+9+1+1,n_index+9-1+1]
          elif n_y==9 and n_x>1 and n_x<9:
            c_mine=0
            n_index=((n_y-1)*9+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-9]["mine"]==1 :
              c_mine+=1
            if cell[n_index-9+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-9-1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index+1+1,n_index-1+1,n_index-9+1,n_index-9-1+1,n_index-9+1+1]
          elif n_x==1 and n_y>1 and n_y<9:
            c_mine=0
            n_index=((n_y-1)*9+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-9]["mine"]==1 :
              c_mine+=1
            if cell[n_index+9]["mine"]==1 :
              c_mine+=1
            if cell[n_index-9+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index+9+1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine

            i["around"]=[n_index+1+1,n_index-9+1,n_index+9+1,n_index-9+1+1,n_index+9+1+1]
          elif n_x==9 and n_y>1 and n_y<9:
            c_mine=0
            n_index=((n_y-1)*9+n_x)-1
            if cell[n_index-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-9]["mine"]==1 :
              c_mine+=1
            if cell[n_index+9]["mine"]==1 :
              c_mine+=1
            if cell[n_index-9-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index+9-1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index-1+1,n_index-9+1,n_index+9+1,n_index-9-1+1,n_index+9-1+1]
          elif n_x==1 and n_y==1:
            c_mine=0
            n_index=((n_y-1)*9+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index+9]["mine"]==1 :
              c_mine+=1
            if cell[n_index+9+1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index+1+1,n_index+9+1,n_index+9+1+1]
          elif n_x==9 and n_y==1:
            c_mine=0
            n_index=((n_y-1)*9+n_x)-1
            if cell[n_index-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index+9]["mine"]==1 :
              c_mine+=1
            if cell[n_index+9-1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index-1+1,n_index+9+1,n_index+9-1+1]
          elif n_x==1 and n_y==9:
            c_mine=0
            n_index=((n_y-1)*9+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-9]["mine"]==1 :
              c_mine+=1
            if cell[n_index-9+1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index+1+1,n_index-9+1,n_index-9+1+1]
          elif n_x==9 and n_y==9:
            c_mine=0
            n_index=((n_y-1)*9+n_x)-1
            if cell[n_index-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-9]["mine"]==1 :
              c_mine+=1
            if cell[n_index-9-1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine 
            i["around"]=[n_index-1+1,n_index-9+1,n_index-9-1+1]          
            
          
        
  if mode==2:
    tile=pygame.Rect(i["x_pos"],i["y_pos"],35,35)
    if inside:
      mouse=True
    else:
      mouse=tile.collidepoint(pygame.mouse.get_pos())
    n_x=i["tile_no_x"]
    n_y=i["tile_no_y"]
    if mouse and i["mine"]==0 and i["flag"]==0  :
      i["revealed"]=1
      if n_x>1 and n_x<16 and n_y>1 and n_y<16:
          c_mine=0
          n_index=((n_y-1)*16+n_x)-1
          if cell[n_index+1]["mine"]==1 :
            c_mine+=1
          if cell[n_index-1]["mine"]==1 :
            c_mine+=1
          if cell[n_index-16]["mine"]==1  :
            c_mine+=1
          if cell[n_index+16]["mine"]==1:
            c_mine+=1
          if cell[n_index-16+1]["mine"]==1 :
            c_mine+=1
          if cell[n_index-16-1]["mine"]==1 :
            c_mine+=1
          if cell[n_index+16+1]["mine"]==1 :
            c_mine+=1
          if cell[n_index+16-1]["mine"]==1 :
            c_mine+=1
          i["count"]=c_mine 
          i["around"]=[n_index+1+1,n_index-1+1,n_index-16+1,n_index+16+1,n_index-16+1+1,n_index-16-1+1,n_index+16+1+1,n_index+16-1+1]
      else:
          if n_y==1 and n_x>1 and n_x<16:
            c_mine=0
            n_index=((n_y-1)*16+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-1]["mine"]==1:
              c_mine+=1
            if cell[n_index+16]["mine"]==1:
              c_mine+=1
            if cell[n_index+16+1]["mine"]==1:
              c_mine+=1
            if cell[n_index+16-1]["mine"]==1:
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index+1+1,n_index-1+1,n_index+16+1,n_index+16+1+1,n_index+16-1+1]
          elif n_y==16 and n_x>1 and n_x<16:
            c_mine=0
            n_index=((n_y-1)*16+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-16]["mine"]==1 :
              c_mine+=1
            if cell[n_index-16+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-16-1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index+1+1,n_index-1+1,n_index-16+1,n_index-16-1+1,n_index-16+1+1]
          elif n_x==1 and n_y>1 and n_y<16:
            c_mine=0
            n_index=((n_y-1)*16+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-16]["mine"]==1 :
              c_mine+=1
            if cell[n_index+16]["mine"]==1 :
              c_mine+=1
            if cell[n_index-16+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index+16+1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index+1+1,n_index-16+1,n_index+16+1,n_index-16+1+1,n_index+16+1+1]
          elif n_x==16 and n_y>1 and n_y<16:
            c_mine=0
            n_index=((n_y-1)*16+n_x)-1
            if cell[n_index-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-16]["mine"]==1 :
              c_mine+=1
            if cell[n_index+16]["mine"]==1 :
              c_mine+=1
            if cell[n_index-16-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index+16-1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index-1+1,n_index-16+1,n_index+16+1,n_index-16-1+1,n_index+16-1+1]
          elif n_x==1 and n_y==1:
            c_mine=0
            n_index=((n_y-1)*16+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index+16]["mine"]==1 :
              c_mine+=1
            if cell[n_index+16+1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index+1+1,n_index+16+1,n_index+16+1+1]
          elif n_x==16 and n_y==1:
            c_mine=0
            n_index=((n_y-1)*16+n_x)-1
            if cell[n_index-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index+16]["mine"]==1 :
              c_mine+=1
            if cell[n_index+16-1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index-1+1,n_index+16+1,n_index+16-1+1]
          elif n_x==1 and n_y==16:
            c_mine=0
            n_index=((n_y-1)*16+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-16]["mine"]==1 :
              c_mine+=1
            if cell[n_index-16+1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index+1+1,n_index-16+1,n_index-16+1+1]
          elif n_x==16 and n_y==16:
            c_mine=0
            n_index=((n_y-1)*16+n_x)-1
            if cell[n_index-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-16]["mine"]==1 :
              c_mine+=1
            if cell[n_index-16-1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index-1+1,n_index-16+1,n_index-16-1+1]          
            
  if mode==3:
      tile=pygame.Rect(i["x_pos"],i["y_pos"],30,30)
      if inside:
        mouse=True
      else:
        mouse=tile.collidepoint(pygame.mouse.get_pos())
      n_x=i["tile_no_x"]
      n_y=i["tile_no_y"]

      if mouse and i["mine"]==0 and i["flag"]==0 :
        i["revealed"]=1
        if n_x>1 and n_x<30 and n_y>1 and n_y<16:
          c_mine=0
          n_index=((n_y-1)*30+n_x)-1
          if cell[n_index+1]["mine"]==1 :
            c_mine+=1
          if cell[n_index-1]["mine"]==1 :
            c_mine+=1
          if cell[n_index-30]["mine"]==1  :
            c_mine+=1
          if cell[n_index+30]["mine"]==1:
            c_mine+=1
          if cell[n_index-30+1]["mine"]==1 :
            c_mine+=1
          if cell[n_index-30-1]["mine"]==1 :
            c_mine+=1
          if cell[n_index+30+1]["mine"]==1 :
            c_mine+=1
          if cell[n_index+30-1]["mine"]==1 :
            c_mine+=1
          i["count"]=c_mine 

          i["around"]=[n_index+1+1,n_index-1+1,n_index-30+1,n_index+30+1,n_index-30+1+1,n_index-30-1+1,n_index+30+1+1,n_index+30-1+1]
        else:
          if n_y==1 and n_x>1 and n_x<30:
            c_mine=0
            n_index=((n_y-1)*30+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-1]["mine"]==1:
              c_mine+=1
            if cell[n_index+30]["mine"]==1:
              c_mine+=1
            if cell[n_index+30+1]["mine"]==1:
              c_mine+=1
            if cell[n_index+30-1]["mine"]==1:
              c_mine+=1
            i["count"]=c_mine

            i["around"]=[n_index+1+1,n_index-1+1,n_index+30+1,n_index+30+1+1,n_index+30-1+1]
          elif n_y==16 and n_x>1 and n_x<30:
            c_mine=0
            n_index=((n_y-1)*30+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-30]["mine"]==1 :
              c_mine+=1
            if cell[n_index-30+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-30-1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index+1+1,n_index-1+1,n_index-30+1,n_index-30-1+1,n_index-30+1+1]
          elif n_x==1 and n_y>1 and n_y<16:
            c_mine=0
            n_index=((n_y-1)*30+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-30]["mine"]==1 :
              c_mine+=1
            if cell[n_index+30]["mine"]==1 :
              c_mine+=1
            if cell[n_index-30+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index+30+1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine

            i["around"]=[n_index+1+1,n_index-30+1,n_index+30+1,n_index-30+1+1,n_index+30+1+1]
          elif n_x==30 and n_y>1 and n_y<16:
            c_mine=0
            n_index=((n_y-1)*30+n_x)-1
            if cell[n_index-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-30]["mine"]==1 :
              c_mine+=1
            if cell[n_index+30]["mine"]==1 :
              c_mine+=1
            if cell[n_index-30-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index+30-1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index-1+1,n_index-30+1,n_index+9+1,n_index-9-1+1,n_index+9-1+1]
          elif n_x==1 and n_y==1:
            c_mine=0
            n_index=((n_y-1)*30+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index+30]["mine"]==1 :
              c_mine+=1
            if cell[n_index+30+1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index+1+1,n_index+30+1,n_index+30+1+1]
          elif n_x==30 and n_y==1:
            c_mine=0
            n_index=((n_y-1)*30+n_x)-1
            if cell[n_index-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index+30]["mine"]==1 :
              c_mine+=1
            if cell[n_index+30-1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index-1+1,n_index+30+1,n_index+30-1+1]
          elif n_x==1 and n_y==16:
            c_mine=0
            n_index=((n_y-1)*30+n_x)-1
            if cell[n_index+1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-30]["mine"]==1 :
              c_mine+=1
            if cell[n_index-30+1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index+1+1,n_index-30+1,n_index-30+1+1]
          elif n_x==30 and n_y==16:
            c_mine=0
            n_index=((n_y-1)*30+n_x)-1
            if cell[n_index-1]["mine"]==1 :
              c_mine+=1
            if cell[n_index-30]["mine"]==1 :
              c_mine+=1
            if cell[n_index-30-1]["mine"]==1 :
              c_mine+=1
            i["count"]=c_mine
            i["around"]=[n_index-1+1,n_index-30+1,n_index-30-1+1]
            
                      
def return_tile_no(mode):
  if mode==1:
    for i in cell:
        tile=pygame.Rect(i["x_pos"],i["y_pos"],40,40)
        if tile.collidepoint(pygame.mouse.get_pos()):
          n_x=i["tile_no_x"]
          n_y=i["tile_no_y"]
          return ((n_y-1)*9+n_x)
  if mode==2:
    for i in cell:
        tile=pygame.Rect(i["x_pos"],i["y_pos"],35,35)
        if tile.collidepoint(pygame.mouse.get_pos()):
          n_x=i["tile_no_x"]
          n_y=i["tile_no_y"]
          return ((n_y-1)*16+n_x)     
  if mode==3:
    for i in cell:
        tile=pygame.Rect(i["x_pos"],i["y_pos"],30,30)
        if tile.collidepoint(pygame.mouse.get_pos()):
          n_x=i["tile_no_x"]
          n_y=i["tile_no_y"]
          return ((n_y-1)*30+n_x)


def reveal_zero(mode,win,i,first):
  if mode==1:
    if cell[i-1]["mine"]==1 or cell[i-1]["flag"]==1:
      return
    if cell[i-1]["revealed"]==1 and not first:
      return
    if cell[i-1]["revealed"] == 0 or first==True:
      cell[i-1]["revealed"]=1
      if cell[i-1]["count"]==0 and cell[i-1]["flag"]==0 :
          for j in cell[i-1]["around"]:
            mine_no(win,mode,True,j)
            if cell[j-1]["count"]==0:
              reveal_zero(1,win,j,False)
  if mode==2:
    if cell[i-1]["mine"]==1 or  cell[i-1]["flag"]==1:
      return
    if cell[i-1]["revealed"]==1 and not first:
      return
    if cell[i-1]["revealed"] == 0 or first==True:
      cell[i-1]["revealed"]=1
      if cell[i-1]["count"]==0 and  cell[i-1]["flag"]==0 :
          for j in cell[i-1]["around"]:
            mine_no(win,mode,True,j)
            if cell[j-1]["count"]==0:
              reveal_zero(2,win,j,False) 
  if mode==3:
    if cell[i-1]["mine"]==1 or cell[i-1]["flag"]==1:
      return
    if cell[i-1]["revealed"]==1 and not first:
      return
    if cell[i-1]["revealed"] == 0 or first==True:
      cell[i-1]["revealed"]=1
      if cell[i-1]["count"]==0 and cell[i-1]["flag"]==0:
          for j in cell[i-1]["around"]:
            mine_no(win,mode,True,j)
            if cell[j-1]["count"]==0:
              reveal_zero(3,win,j,False)     



def flagged(n):
    if n is None:
        return
    if cell[n-1]["flag"] == 0:
      cell[n-1]["flag"] = 1
      cell[n-1]["revealed"]=0
    else:
      cell[n-1]["flag"] = 0
      cell[n-1]["revealed"]=0
def win(mode):
  if mode==1:
    c=0
    for i in cell:
      if i["revealed"]==1:
        c+=1
    if c==71:
      return True
  if mode==2:
    c=0
    for i in cell:
      if i["revealed"]==1:
        c+=1
    if c==216:
      return True
  if mode==3:
    c=0
    for i in cell:
      if i["revealed"]==1:
        c+=1
    if c==381:
      return True
         

