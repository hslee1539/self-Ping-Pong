from tkinter import *
import random
e = 1
class MainFrame :
    window = 0
    canvas = 0
    engine = 0
    def __init__ ( self ):
        print(2)
        self.window = Tk()
        self.window.title("이희수 201401985 이희수")
        self.canvas = Canvas ( self.window, height = 600, width = 1200, bg = "Gray" )
        self.canvas.grid ()
        self.engine = GameEngine(self.canvas)
        self.window.bind("<Key>", self.engine.Control)
        self.window.mainloop()
        
class GameEngine ():
    ob = 0
    ThreadWorking = True
    class Point ( ):
        x = 0
        y = 0
    class GraphicsData ( ):
        p1 = 0
        p2 = 0
        def __init__(self):
            self.p1 = GameEngine.Point()
            self.p2 = GameEngine.Point()

    class Object (  ):
        start = 0
        graphics = 0
        width = 0
        c = "#000000"
        def __init__(self):
            self.graphics = GameEngine.GraphicsData ()
            #self.graphics.p1 = GameEngine.Point()
            #self.graphics.p2 = GameEngine.Point()
            self.start = GameEngine.Point()
            self.graphics.p1.x = 0
            self.graphics.p1.y = 0
            self.graphics.p2.x = 0
            self.graphics.p2.y = 0
            self.start.x = 0
            self.start.y = 0 
        def LocationArea ( self ):
            returnData = GameEngine.GraphicsData()
            returnData.p1.x = self.start.x + self.graphics.p1.x
            returnData.p1.y = self.start.y + self.graphics.p1.y
            returnData.p2.x = self.start.x + self.graphics.p2.x
            returnData.p2.y = self.start.y + self.graphics.p2.y
            return returnData
            
    class Table ( Object ):
        def __init__ (self):
            super().__init__()
            self.graphics.p1.x = -600
            self.graphics.p1.y = 0
            self.graphics.p2.x = 600
            self.graphics.p2.y = 0
            self.start.x = 600
            self.start.y = 300
            self.width = 150
            self.c = "#F0F0FF"
            
    class Table_Line ( Object ):
        def __init__ ( self ):
            super().__init__()
            self.graphics.p1.x = 0
            self.graphics.p1.y = -150
            self.graphics.p2.x = 0
            self.graphics.p2.y = 150
            self.start.x = 600
            self.start.y = 300
            self.width = 2
            self.c = "#aaaaaa"
    class Player ( Object ):
        def __init__ ( self ):
            super().__init__()
            self.graphics.p1.x = 0
            self.graphics.p1.y = -30
            self.graphics.p2.x = 0
            self.graphics.p2.y = 30
            self.start.x = 20
            self.start.y = 300
            self.width = 20
            self.c = "#333399"
            self.speed = 0 # 플레이어 이동에 관한 가속력 ( 스칼라값 )
            self.speed_sticky = 1
        def move ( self ):
            if self.speed != 0:
                self.start.y = self.speed * self.speed_sticky + self.start.y
                self.speed = self.speed - 1
    class Player_Line ( Player, Object ):
        def __init__ ( self ):
            super().__init__()
            self.graphics.p1.y = -75
            self.graphics.p2.y = 75
            self.c = "#aaaaFF"


    class Ball ( Object ):
        def __init__ ( self ):
            super().__init__()
            self.graphics.p1.x = -10
            self.graphics.p1.y = 0
            self.graphics.p2.x = 10
            self.graphics.p2.y = 0
            self.start.x = 40
            self.start.y = 300
            self.width = 20
            self.c = "#333333"
            # Ball 전용
            self.speed = 0
            self.speed_sticky = 1
            self.size = self.width/2
            
        def move ( self , allObject):
            #self.graphics.p2.x = self.size * 10  / (self.speed + 9)
            #self.graphics.p1.x = -self.graphics.p2.x
            self.start.x = self.start.x + self.speed * self.speed_sticky
            if self.speed > 0:
                self.speed = self.speed - 0.2
            else:            # 패배
                self.speed = 0
                self.start.x = 40
            if self.size > self.start.x and self.speed_sticky == -1:
                self.speed_sticky = -self.speed_sticky
            if self.start.x > 1200 - self.size and self.speed_sticky == 1:
                 self.speed_sticky = -self.speed_sticky
                 allObject.g.ColorChange(allObject.table_line2,"#4466cc", allObject.table.c, 3 )
                 self.start.y = random.randint( 245,355 )
                 allObject.g.ColorChange(allObject.ball_line,"#000033", allObject.ball_line.c, 3 )
    class Ball_Line ( Ball, Object ):
        def __init__ ( self ):
            super().__init__()
            self.graphics.p1.x = -600
            self.graphics.p2.x = 600
            self.start.x = 600
        def move(self, obj):
            #ob = GameEngine()
            self.start.y = obj.ball.start.y
    class EffectBall (  ):
        def __init__ ( self ):
            self.ball1 = GameEngine.Ball()
            self.ball2 = GameEngine.Ball()
            self.ball3 = GameEngine.Ball()
            self.ball4 = GameEngine.Ball()
            self.ball1.c = "#000044"
            self.ball2.c = "#444488"
            self.ball3.c = "#8888cc"
            self.ball4.c = "#aaaaff"
        def move (self ,ball ):
            self.ball4.start.x = self.ball3.start.x
            self.ball3.start.x = self.ball2.start.x
            self.ball2.start.x = self.ball1.start.x
            self.ball1.start.x = ball.start.x
            self.ball4.start.y = self.ball3.start.y
            self.ball3.start.y = self.ball2.start.y
            self.ball2.start.y = self.ball1.start.y
            self.ball1.start.y = ball.start.y

            

    class Graphics ():
        g = Canvas
        def __init__ ( self, canvas ):
            self.g = canvas
        def Draw ( self, ob ):
            ob1 = GameEngine.Object()
            ob1 = ob
            self.g.create_line ( ob1.start.x + ob1.graphics.p1.x, ob1.start.y + ob1.graphics.p1.y, ob1.start.x + ob1.graphics.p2.x, ob1.start.y + ob1.graphics.p2.y, fill = ob1.c ,width = ob1.width )
        def GraphicsTheadStart ( self, AllObjects):
            obs = AllObjects
            self.g.delete ("all")
            self.Draw ( obs.table )
            self.Draw ( obs.ball_line )
            self.Draw ( obs.bestScor )
            self.Draw ( obs.table_line )
            self.Draw ( obs.table_line2 )
            self.Draw ( obs.player_line )
            self.Draw ( obs.effectball.ball1 )
            self.Draw ( obs.effectball.ball2 )
            self.Draw ( obs.effectball.ball3 )
            self.Draw ( obs.effectball.ball4 )
            self.Draw ( obs.ball )
            self.Draw ( obs.player )
            a = 0 
        def __ColorChange ( self, obj , color, nextColor, frame ,nowFrame):
            nowFrame = nowFrame + 1
            R = int(nextColor[1:3], 16)
            G = int(nextColor[3:5], 16)
            B = int(nextColor[5:7], 16)

            preR = int(color[1:3], 16)
            preG = int(color[3:5], 16)
            preB = int(color[5:7], 16)

            nextR = hex(int(preR - (preR - R )*nowFrame/frame))[2:4]
            nextG = hex(int(preG - (preG - G )*nowFrame/frame))[2:4]
            nextB = hex(int(preB - (preB - B )*nowFrame/frame))[2:4]

            obj.c = "#" + nextR + nextG + nextB 
            if nowFrame != frame :
                ( self.g._root() ).after ( 60 , self.__ColorChange , obj, color,nextColor, frame,nowFrame )

        def ColorChange ( self, obj, color, nextColor, frame ):
            ( self.g._root() ).after ( 0 , self.__ColorChange , obj, color,nextColor, frame,0 )

    def ThreadStart ( self ):
        (self.g.g._root()).after ( 0 , self.__Thread )
       
    def __Thread ( self ):
        #### 뼈대 생성
        self.effectball.move(self.ball)
        self.player.move()
        self.ball.move(self)
        self.ball_line.move(self)
        if self.ball.speed == 0:
            self.player.start.x = 20
            self.player_line.start.x = 20
        #### 그래픽작업
        self.g.GraphicsTheadStart(self)
        (self.g.g._root()).after ( 15 , self.__Thread )

    def Control ( self, event ):
        if event.keysym == "Up":
            if 270 < self.player.start.y:
                self.player.speed = self.player.speed + 7
                self.player.speed_sticky = -1
            else:
                self.player.start.y = 260
                self.player.speed = 0
        elif event.keysym == "Down":
            if 330 > self.player.start.y:
                self.player.speed = self.player.speed + 7
                self.player.speed_sticky = 1
            else:
                self.player.start.y = 340
                self.player.speed = 0
        elif event.keysym == "Right":
            self.g.ColorChange(self.player_line,"#7777AA",self.player_line.c , 4)
            self.g.ColorChange(self.player,"#FFFFFF",self.player.c , 4)
            LocationArea = self.player.width/2 + self.ball.width/2
            #print("Ball area x1 = ", LocationArea.p1.x)
            #print("Ball area x2 = ", LocationArea.p2.x)
            if self.ball.start.x-1  < self.player.start.x + LocationArea + self.ball.speed and self.player.start.x - LocationArea < self.ball.start.x:
                LocationArea = self.player.LocationArea()
                if self.ball.start.y < LocationArea.p2.y and self.ball.start.y > LocationArea.p1.y:
                    self.g.ColorChange(self.table,"#000000",self.table.c , 4)
                    self.ball.speed_sticky = 1
                    self.player.start.x = self.player.start.x + 5  +self.ball.speed
                    self.player_line.start.x = self.player_line.start.x + 5 +self.ball.speed
                    self.g.ColorChange(self.table,"#2233aa",self.table.c , 4)
                    if self.bestScor.start.x < self.player.start.x:
                        self.bestScor.start.x = self.player.start.x - 5
                        self.g.ColorChange(self.table,"#000066",self.table.c , 4)
                    else:
                        self.g.ColorChange(self.table,"#000000",self.table.c , 4)
                    if self.ball.speed > 15:
                        self.ball.speed = self.ball.speed + 15
                    else:
                        self.ball.speed =  31 + self.ball.speed

            self.player.start.x = self.player.start.x - 5
            self.player_line.start.x = self.player_line.start.x - 5


    def __init__ ( self, canvas ):
        self.ob = self.Object()
        self.table = self.Table()
        self.table_line = self.Table_Line()
        self.player = self.Player()
        self.bestScor = self.Player_Line()
        self.bestScor.c = "#CCCCDD"
        self.player_line = self.Player_Line()
        self.table_line2 = self.Player_Line()
        self.table_line2.c = "#DDDDFF"
        self.table_line2.start.x = 1190
        self.ball = self.Ball()
        self.ball_line = self.Ball_Line()
        self.ball_line.c = self.table.c
        self.effectball = self.EffectBall()
        self.g = self.Graphics(canvas )


        self.ThreadStart()

윈도우=MainFrame ()