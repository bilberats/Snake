import pygame as pg
from random import randint


class Map():
    def __init__(self,x,y):
        self.xmax = x
        self.ymax = y
        self.grille = [[0 for i in range(x)]for i in range(y)]
        self.screen = pg.display.set_mode((x*30,y*30))
        self.clock = pg.time.Clock()

    def flip(self):
        self.screen.fill((30,30,30))
        for y in range(len(self.grille)):
            for x in range(len(self.grille[1])):
                if self.grille[y][x] == 1:
                    pg.draw.rect(self.screen,(255,0,0),pg.Rect(x*30,y*30,30,30))
                elif self.grille[y][x] > 1:
                    pg.draw.rect(self.screen,(0,255,0),pg.Rect(x*30,y*30,30,30),3)
        pg.display.flip()
        self.clock.tick(13)


class Snake():
    def __init__(self,position):
        self.lon = 3
        self.xvect = 1
        self.yvect = 0
        self.alive = True
        self.x = position[0]
        self.y = position[1]

    def init(self,grille):
        for i in range(self.lon-1):
            grille[self.y][self.x-i] = 2+i
        grille[14][8] = 1
        return grille
    def move(self,grille,mape):
        while self.alive:
            moved = False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.alive = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w and self.yvect != 1 and not moved:
                        self.xvect = 0
                        self.yvect = -1
                        moved = True
                    if event.key == pg.K_a and self.xvect != 1 and not moved:
                        self.xvect = -1
                        self.yvect = 0
                        moved = True
                    if event.key == pg.K_s and self.yvect != -1 and not moved:
                        self.xvect = 0
                        self.yvect = 1
                        moved = True
                    if event.key == pg.K_d and self.xvect != -1 and not moved:
                        self.xvect = 1
                        self.yvect = 0
                        moved = True

            if not(0<=self.y+self.yvect<=mape.ymax-1) or not(0<=self.x+self.xvect<=mape.xmax-1):
                self.alive = False
                print("touche le mur")
                break

            if grille[self.y+self.yvect][self.x+self.xvect] == 1:
                self.lon += 1

                done = False
                while not done:
                    pomx = randint(0,mape.xmax-1)
                    pomy = randint(0,mape.ymax-1)
                    if grille[pomy][pomx] == 0:
                        grille[pomy][pomx] = 1
                        done = True

                print("touche la pomme")

            elif 2 < grille[self.y+self.yvect][self.x+self.xvect] < self.lon+1:
                self.alive = False
                print("se touche")
                break
            
            
            for y in range(len(grille)):
                for x in range(len(grille[1])):
                    if grille[y][x] == 2:
                        grille[self.y+self.yvect][self.x+self.xvect] = 2
                        grille[y][x]+=1
                    if grille[y][x] > self.lon+1:
                        grille[y][x] = 0
                    elif grille[y][x] > 2 :
                        grille[y][x]+=1
            grille[self.y+self.yvect][self.x+self.xvect] = 2
            self.x += self.xvect
            self.y += self.yvect
                
            mape.flip()


def main():
    mape = Map(30,20)
    snake = Snake((10,10))
    snake.move(snake.init(mape.grille),mape)

pg.init()
if __name__ == "__main__":
    main()
    
