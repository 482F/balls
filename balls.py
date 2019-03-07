#17k0107 石川 涼

#自由課題

import random, math, time, pygame, random, ctypes

def product_error(arglist, namelist, message="error"):
    print(message)
    for num, value in enumerate(arglist):
        print(namelist[num], " : ", value)
    K = 1 / 0
def randbetween(b, t, mode="float"):
    K = random.random() * (t - b) + b
    if mode=="int":
        K = int(K)
    elif mode == "float":
        pass
    else:
        product_error([mode], ["mode"], "invalid argument")
    return K
def circ_num(s, e, n):
    K = e - s + 1
    n -= 1
    n %= K
    return n + s
class Handler:
    def __init__(self):
        self.dict = {}
    def assign(self, event, function):
        self.dict[event] = function
    def CaD(self, events):
        for event in events:
            if event.type in self.dict.keys():
                self.dict[event.type](event)
class Timer:
    def starttimer(self):
        import time
        self.STARTT = time.time()
        return(self.STARTT)
    def returntime(self, mode="num"):
        import time
        self.FINISHT = time.time()
        self.ELAPSEDT = (self.FINISHT - self.STARTT)
        if mode=="num":
            return(self.ELAPSEDT)
        elif mode=="str":
            T = self.ELAPSEDT
            S = int(T % 60)
            M = int(T // 60 % 60)
            H = int(T // (60*60))
            S = "0" + str(S) if S < 10 else str(S)
            M = "0" + str(M) if M < 10 else str(M)
            H = "0" + str(H) if H < 10 else str(H)
            return(H+":"+M+":"+S)
class Pos:
    def __init__(self, x, y=None):
        Pos.static_RCList = [Pos, Object, Circle]
        if type(x) in Pos.static_RCList:
            self.x = x.x
            self.y = x.y
        elif type(x) in [int, float]:
            self.x = x
            self.y = y
        else:
            product_error([x, y], ["x", "y"], "invalid argument")
    def move(self, x, y, mode="relative"):
        if mode == "relative":
            self.x = self.x + x
            self.y = self.y + y
        if mode == "absolute":
            self.x = x
            self.y = y
        return self
    def distance(self, other=None):
        other = Pos(0, 0) if other == None else other
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**(1/2)
    def angle_between(self, other):
        return Angle(math.atan2(self.y - other.y, self.x - other.x))
    def deepcopy(self):
        return Pos(self.x, self.y)
    def move_from_point(self, point, dist):
        if type(point) in Object.static_RCList:
            Aself = self.deepcopy()
            Aself -= point
            Aself.value += dist
            Aself += point
            self.x = Aself.x
            self.y = Aself.y
        else:
            product_error([point], ["point"], "invalid argument")
    def __str__(self):
        return str((self.x, self.y))
    def __add__(self, other):
        if type(other) in Pos.static_RCList:
            return Pos(self.x + other.x, self.y + other.y)
        else:
            product_error([other], ["other"], "invalid argument")
    def __sub__(self, other):
        if type(other) in Pos.static_RCList:
            return Pos(self.x - other.x, self.y - other.y)
        else:
            product_error([other], ["other"], "invalid argument")
    def __mul__(self, other):
        if type(other) in Pos.static_RCList:
            return Pos(self.x * other.x, self.y * other.y)
        elif type(other) in [int, float]:
            return Pos(self.x * other, self.y * other)
        else:
            product_error([other], ["other"], "invalid argument")
    def __truediv__(self, other):
        if type(other) in Pos.static_RCList:
            return Pos(self.x / other.x, self.y / other.y)
        elif type(other) in [int, float]:
            return Pos(self.x / other, self.y / other)
        else:
            product_error([other], ["other"], "invalid argument")
    def __neg__(self):
        return Pos(-self.x, -self.y)
    def __int__(self):
        return Pos(int(self.x), int(self.y))
    def __round__(self):
        return Pos(round(self.x), round(self.y))
    def __eq__(self, other):
        if type(other) in Pos.static_RCList:
            return (self.x == other.x) and (self.y == other.y)
        else:
            return object.__eq__(self, other)
    def __ne__(self, other):
        if type(other) in Pos.static_RCList:
            return (self.x != other.x) or (self.y != other.y)
        else:
            return object.__ne__(self, other)
    def __lt__(self, other):
        if type(other) in self.static_RCList:
            return (self.value < other.value)
        elif type(other) in [int, float]:
            return (self.value < other)
    def __le__(self, other):
        if type(other) in self.static_RCList:
            return (self.value <= other.value)
        elif type(other) in [int, float]:
            return (self.value <= other)
    def __gt__(self, other):
        if type(other) in self.static_RCList:
            return (self.value > other.value)
        elif type(other) in [int, float]:
            return (self.value > other)
    def __ge__(self, other):
        if type(other) in self.static_RCList:
            return (self.value >= other.value)
        elif type(other) in [int, float]:
            return (self.value >= other)
    def __getattr__(self, name):
        if name == "angle":
            return Angle(math.atan2(self.y, self.x))
        elif name == "value":
            return (self.x ** 2 + self.y ** 2)**(1/2)
        else:
            product_error([name], ["name"], "invalid attribute")
    def __setattr__(self, name, value):
        if name == "angle":
            if type(value) == Angle:value = value.value
            dist = self.value
            self.x = math.cos(value) * dist
            self.y = math.sin(value) * dist
        elif name == "value":
            dist = self.value
            if dist == 0:return
            self.x = self.x / dist * value
            self.y = self.y / dist * value
        else:
            object.__setattr__(self, name, value)
class Angle:
    def __init__(self, value, sub=None):
        Angle.static_RCList = [Pos, Object]
        if type(value) in Angle.static_RCList:
            if sub == None:
                self.value = value.angle
            elif type(sub) in Angle.static_RCList:
                self.value = value.angle_between(sub).value
            else:
                product_error([value, sub], ["value", "sub"], "invalid argument")
        elif type(value) in [int, float]:
            self.value = value
        else:
            product_error([value, sub], ["value", "sub"], "invalid argument")
        self.value = value
        self.adjust()
    def adjust(self):
            self.value -= math.floor(self.value / (2 * math.pi)) * (2 * math.pi)
            return self
    def deepcopy(self):
        return Angle(self.value)
    def __str__(self):
        return str(self.value / math.pi) + "pi (" + str(self.value) + ")"
    def __add__(self, other):
        if type(other) == Angle:
            return Angle(self.value + other.value)
        elif type(other) in [int, float]:
            return Angle(self.value + other)
        else:
            product_error([other], ["other"], "invalid argument")
    def __sub__(self, other):
        if type(other) == Angle:
            return Angle(self.value - other.value)
        elif type(other) in [int, float]:
            return Angle(self.value - other)
        else:
            product_error([other], ["other"], "invalid argument")
    def __mul__(self, other):
        if type(other) == Angle:
            return Angle(self.value * other.value)
        elif type(other) in [int, float]:
            return Angle(self.value * other)
        else:
            product_error([other], ["other"], "invalid argument")
    def __truediv__(self, other):
        if type(other) == Angle:
            return Angle(self.value / other.value)
        elif type(other) in [int, float]:
            return Angle(self.value / other)
        else:
            product_error([other], ["other"], "invalid argument")
    def __neg__(self):
        return Angle(-self.value)
    def __eq__(self, other):
        return self.value == other.value
    def __ne__(self, other):
        return self.value != other.value
    
class Object(Pos):
    static_Ce = None
    def __init__(self, x, y, vx, vy, weight, lcol="0x000000", fcol="0xffffff"):
        super().__init__(x, y)
        Object.static_Ce = 1
        self.speed = Pos(vx, vy)
        self.weight = weight
        if type(lcol) == str:
            self.lcol = pygame.Color(lcol)
        elif type(lcol) == pygame.Color:
            self.lcol = lcol
        else:
            product_error([lcol], ["lcol"], "invalid argument")
        if type(fcol) == str:
            self.fcol = pygame.Color(fcol)
        elif type(fcol) == pygame.Color:
            self.fcol = fcol
        else:
            product_error([fcol], ["fcol"], "invalid argument")
    def __getattr__(self, name, value):
        if name == "pos":
            return Pos(self)
        else:
            object.__getattr__(self, name, value)
    def __setattr__(self, name, value):
        if name == "pos":
            self.x = value.x
            self.y = value.y
        else:
            object.__setattr__(self, name, value)
    def step(self):
        self.x += self.speed.x
        self.y += self.speed.y
    def deepcopy(self):
        return Object(self.x, self.y, self.speed.x, self.speed.y, self.weight, self.lcol, self.fcol)
    def pulled_from_point(self, point, value):
        K = Pos(1, 1)
        K.value = value
        K.angle = self.angle_between(point)
        self.speed -= K
class Circle(Object):
    static_id = 0
    def __init__(self, x=None, y=None, vx=None, vy=None, radius=None, lcol="0x000000", fcol="0xffffff"):
        x = randbetween(0, Object.static_range.x) if x == None else x
        y = randbetween(0, Object.static_range.y) if y == None else y
        vx = randbetween(-1, 1) if vx == None else vx
        vy = randbetween(-1, 1) if vy == None else vy
        self.radius = randbetween(10, 50, "int") if radius == None else radius
        super().__init__(x, y, vx, vy, math.pi * self.radius * self.radius, lcol, fcol)
        self.image = None
        self.make_image()
        self.corflag = {}
        self.id = "Circle_" + str(Circle.static_id)
        self.traj = [Pos(self) for K in range(6)]
        self.traj[0] = 1
        self.pinned = False
        Circle.static_id += 1
    def deepcopy(self):
        return Circle(self.x, self.y, self.speed.x, self.speed.y, self.radius, self.lcol, self.fcol)
    def judge_cor(self, other):
        if type(other) == Circle:
            return self.distance(other) < self.radius + other.radius
    def do_cor(self, other):
        angle = self.angle_between(other)
        Aself = self.deepcopy()
        Aother = other.deepcopy()
        Aself.speed.angle -= angle
        Aother.speed.angle -= angle
        if picked not in [self, other] or True not in [self.pinned, other.pinned]:
            swap = (Aself.speed.x * Aself.weight * (1 + Circle.static_Ce) + Aother.speed.x * (Aother.weight - Circle.static_Ce * Aself.weight)) / (Aother.weight + Aself.weight)
            Aself.speed.x = (Aother.speed.x * Aother.weight * (1 + Circle.static_Ce) + Aself.speed.x * (Aself.weight - Circle.static_Ce * Aother.weight)) / (Aother.weight + Aself.weight)
            Aother.speed.x = swap
            Aself.speed.angle += angle
            Aother.speed.angle += angle
            self.speed.x = Aself.speed.x
            self.speed.y = Aself.speed.y
            other.speed.x = Aother.speed.x
            other.speed.y = Aother.speed.y
        else:
            if picked == self or self.pinned:
                Aother.speed.x *= -Circle.static_Ce
                Aother.speed.x += Aself.speed.x
                Aother.speed.angle += angle
                other.speed = Aother.speed
            elif picked == other or other.pinned:
                Aself.speed.x *= -Circle.static_Ce
                Aself.speed.x += Aother.speed.x
                Aself.speed.angle += angle
                self.speed = Aself.speed
        exdist = self.radius + other.radius - self.distance(other) + 2
        if picked == self or self.pinned:
            other.move_from_point(self, exdist)
        elif picked == other or other.pinned:
            self.move_from_point(other, exdist)
        else:
            self.move_from_point(other, self.radius * exdist / (other.radius + self.radius))
            other.move_from_point(self, other.radius * exdist / (self.radius + other.radius))
    def make_image(self):
        self.image = pygame.Surface((self.radius * 2, self.radius * 2))
        self.image.fill(pygame.Color("0xffffff"))
        pygame.draw.circle(self.image, self.fcol, (self.radius, self.radius), self.radius, 0)
        pygame.draw.circle(self.image, self.lcol, (self.radius, self.radius), self.radius, 1)
        self.image.set_colorkey(pygame.Color("0xffffff"))
    def draw(self, canvas):
        canvas.blit(self.image, (self.x - self.radius + Circle.static_marg.x, self.y - self.radius + Circle.static_marg.y))
    def step(self):
        self.x += self.speed.x
        self.y += self.speed.y
        if self.x - self.radius < 0:
            self.speed.x = abs(self.speed.x)
            self.x = self.radius
        elif Circle.static_range.x < self.x + self.radius:
            self.speed.x = -abs(self.speed.x)
            self.x = Circle.static_range.x - self.radius
        if self.y - self.radius < 0:
            self.speed.y = abs(self.speed.y)
            self.y = self.radius
        elif Circle.static_range.y < self.y + self.radius:
            self.speed.y = -abs(self.speed.y)
            self.y = Circle.static_range.y - self.radius
    def j_include(self, point):
        return self.distance(point) <= self.radius
    def pinnedfunc(self):
        self.speed.value = 0
    def pickedfunc(self):
        x, y = pygame.mouse.get_pos()
        self.move(x - marg.x, y - marg.y, "absolute")
        self.traj[self.traj[0]] = Pos(self)
        self.traj[0] = circ_num(1, 5, self.traj[0] + 1)
        self.speed = (self.traj[circ_num(1, 5, self.traj[0] - 1)] - self.traj[circ_num(1, 5, self.traj[0])]) / 5
def exit_game(event=None):
    pygame.quit()
def keydown(event):
    if event.key == pygame.K_ESCAPE:
        exit_game()
def mousebuttondown(event):
    pos = Pos(event.pos[0], event.pos[1]) - marg
    if event.button == 1:
        pickball(pos)
    elif event.button == 2:
        gen_gen(pos)
    elif event.button == 3:
        deleteball(pos)
def mousebuttonup(event):
    if event.button == 1:
        unpickball()
def pickball(pos):
    global picked, circles
    for circle in circles + GGens:
        if circle.j_include(pos):
            picked = circle
            picktimer.starttimer()
            return
    circles.append(Circle())
    circles[-1].speed.value = 0
    circles[-1].x, circles[-1].y = pos.x, pos.y
def unpickball():
    global picked
    if picktimer.returntime() < 0.3:
        picked.pinned = True
    picked = None
def gen_gen(pos):
    global GGens
    GGens.append(Circle())
    GGens[-1].speed.value = 0
    GGens[-1].x, GGens[-1].y = pos.x, pos.y
    GGens[-1].radius = 5
def deleteball(pos):
    global circles, GGens
    for circle in circles:
        if circle.j_include(pos):
            if circle.pinned:
                circle.pinned = False
            else:
                circles.remove(circle)
            return
    for GGen in GGens:
        if GGen.j_include(pos):
            GGens.remove(GGen)
            return
handler = Handler()
handler.assign(pygame.QUIT, exit_game)
handler.assign(pygame.KEYDOWN, keydown)
handler.assign(pygame.MOUSEBUTTONDOWN, mousebuttondown)
handler.assign(pygame.MOUSEBUTTONUP, mousebuttonup)
Frange = Pos(1280, 720)
marg = Pos(50, 50)
screen = pygame.display.set_mode((Frange.x, Frange.y))
Frange -= marg * 2
Object.static_range = Frange
Object.static_marg = marg
G = 0.0098
GGens = [Circle(Frange.x / 2, Frange.y / 2, 0, 0, 5, "0x000000", "0x000000")]
frame = pygame.Surface((Frange.x+2, Frange.y+2))
frame.fill(pygame.Color("0x000000"))
pygame.draw.rect(frame, pygame.Color("0xffffff"), (1, 1, Frange.x, Frange.y))
FPS = 120
picktimer = Timer()
clock = pygame.time.Clock()
screen.fill(pygame.Color("0xffffff"))
pygame.display.flip()
NoC = 10
Object(0, 0, 0, 0, 0)
circles = [Circle() for K in range(NoC)]
picked = None
for circle in circles:
    circle.speed.value = randbetween(0.3, 0.5)
while True:
    handler.CaD(pygame.event.get())
    for IoC, circle in enumerate(circles):
        for GGen in GGens:
            circle.pulled_from_point(GGen, G)
            pygame.draw.circle(screen, pygame.Color("0x000000"), (int(GGen.x + marg.x), int(GGen.y + marg.y)), GGen.radius, 0)
            if picked == GGen:picked.pickedfunc()
        if circle.pinned:circle.pinnedfunc()
        if picked == circle:picked.pickedfunc()
        circle.step()
        for Acircle in [K for I, K in enumerate(circles) if IoC < I]:
            if circle.judge_cor(Acircle):circle.do_cor(Acircle)
        circle.draw(screen)
    pygame.display.flip()
    screen.fill(pygame.Color("0xffffff"))
    screen.blit(frame, (marg.x, marg.y))
    clock.tick(FPS)
