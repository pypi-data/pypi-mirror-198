import math,time,os
def rgbf(r, g, b): 
  return f"\u001b[38;2;{r};{g};{b}m"

def rgbb(r, g, b): 
  return f"\u001b[48;2;{r};{g};{b}m"

RESET = "\u001b[0m"

def cprint(text,fg=(255,255,255),bg=None,**kwargs):
  if bg != None:
    print(rgbf(*fg)+rgbb(*bg)+text+RESET,**kwargs)
  else:
    print(rgbf(*fg)+text+RESET,**kwargs)

class color:
  white = (255,255,255)
  black = (0,0,0)
  red = (255,0,0)
  green = (0,255,0)
  blue = (0,191,255)

  darkblue = (0,0,255)


  yellow = (255,255,0)
  teal = (0,255,255)
  purple = (255,0,255)

  orange = (255,125,0)
  pink = (255,0,145)


  warn = (255,204,0)

block = "█"
mdot = "·"

lup = "\u001b[1E"
ldown = "\u001b[1F"

def init():
  if os.name == 'nt':
    os.system("color")

class determinate:
  def __init__(self,format="[%bar]",char=block,l=50,fill=" ",lead=None,fg=(255,255,255),bg=None):
    self.format = format
    self.char = char
    self.fill = fill
    self.len = l
    if lead != None:
      self.lead = lead
    else:
      self.lead = char
    self.fg = fg
    
    self.bg = bg
    self.init = 0
    self.logmsg = ""
    if self.len != "full":
      if self.len <= 0:
        raise ValueError("bar must have length")
    self.freeze= False
  def update(self,pd=-1,done=-1,total=-1,rate=0.1):

    print('\033[?25l', end="")
    print(end="\x1b[2K")

    global cchar
    if pd==-1:
      pd = done//total

    
    if self.len == "full":
      le,_ = os.get_terminal_size(0)
      fmt = self.format.replace("%perc","10%").replace("%frac",f"{done}/{total}").replace("%log",self.logmsg)
      le -= len(fmt)
    else:
      le = self.len
    csx = math.floor(pd * le)
    if csx>1:
      cstr = ""
      for i in range(csx-1):
        cstr += self.char
      cstr += self.lead
      for i in range(le - csx):
        cstr += self.fill
    else:
      cstr = self.fill * le
    print("\r", end="", flush=True)
    
    perc = f"{round(pd*100)}%"
    res = self.format.replace("%bar",cstr).replace("%perc",perc).replace("%frac",f"{done}/{total}").replace("%log",self.logmsg)
    if not self.freeze:
      cprint(res,self.fg,self.bg,end="\r")
    print('\033[?25h', end="")
    time.sleep(rate)
  def stop(self,msg="Done!"):
    print(end="\x1b[2K")
    print('\033[?25h', end="") 
    cprint(f"\r{msg}" ,self.fg,self.bg)
  def error(self,msg,fg=(255,0,0),bg=(0,0,0)):
    print('\033[?25h', end="") 
    
    cprint(f"\r{msg}",fg,bg,flush=True)
    os._exit(1)
  def log(self,msg,):
    self.logmsg= msg

indeterminate_modes = {
  "classic":["|","/","-","\\"],
  "arrow":[ "▹▹▹▹▹","▸▹▹▹▹","▹▸▹▹▹","▹▹▸▹▹","▹▹▹▸▹","▹▹▹▹▸"
],
  "dots": ["   ",".  ",".. ","..."],
  "x+": ["×","+","×","+"],
  "spindots":["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"],
  "spindots2":["⣾","⣽","⣻","⢿","⡿","⣟","⣯","⣷"],
  "spindots3":["⠁","⠂","⠄","⡀","⢀","⠠","⠐","⠈"],
  "hamburger":["☱","☲","☴"],
  "vdots": [".",":"," ",],
  "c2in": ["||","/\\","--","\\/"],
  "c2out": ["||","\\/","--","/\\"],
  "c2s": ["||","//","--","\\\\"],
  "letter": ["b",'d','q','p'],
  "rundots": ['·   ',"··  ","··· ","····"," ···","  ··","   ·","    "],
  "expand": ["  ··  "," ···· ","······",'      '],
  "missing": [" ·····","· ····","·· ···","··· ··","···· ·","····· ","······"],
  "cycle": ['···   '," ···  ","  ··· ","   ···","·   ··","··   ·"],
}

class indeterminate_spin:
  def __init__(self,mode="classic",pre="",post="",fg=(255,255,255),bg=None):
    if type(mode) == str:
      self.mode = mode
      self.arr = indeterminate_modes[self.mode]
    elif type(mode) == list:
      self.mode = "custom"
      self.arr = mode

    self.freeze = False
    self.ind = 0

    self.pre = pre
    self.post = post
    self.fg = fg
    self.bg = bg
    self.logmsg = ""
    
  def update(self,rate=0.1):
    print('\033[?25l', end="") 
    if not self.freeze:
      pr = self.pre.replace("%log",self.logmsg)
      ps = self.post.replace("%log",self.logmsg)
      cprint(pr+self.arr[self.ind]+ps,self.fg,self.bg,end="\r",flush=True)
    self.ind += 1 
    self.ind %= len(self.arr)
    time.sleep(rate*(4/len(self.arr)))
    
  def stop(self,msg = "DONE!"):
    print(end="\x1b[2K")
    print(end="\x1b[2K")

    cprint("\r"+msg,self.fg,self.bg)
    print('\033[?25h', end="") 
  def error(self,msg,fg=(255,0,0),bg=(0,0,0)):
      print('\033[?25h', end="") 
      print(end="\x1b[2K")
      cprint(f"\r{msg}",fg,bg,flush=True)
      os._exit(1)

  def log(self,msg):
    self.logmsg= msg
class indeterminate_bar:
  def __init__(self,format="%bar",l=50,bar="<-->",fill=mdot,fg=(255,255,255),bg=None):
    self.len = l
    self.bar = bar
    self.fill = fill
    self.prog = 0
    self.format = format
    self.add = +1
    self.fg = fg
    self.bg = bg
    self.freeze = False
    self.logmsg = ""
    if len(self.bar) > self.len:
      raise ValueError("moving bar must not be longer than big bar")
    if len(self.bar) <= 0 or self.len <= 0:
      raise ValueError("both bars must have length")
  def update(self,rate=0.1):
    print('\033[?25l', end="") 
    s = [self.fill for _ in range(self.len)]
    for n in range(len(self.bar)):
      try:
        s[n+self.prog] = self.bar[n]
      except:
        pass
    self.prog += self.add
    if self.prog > self.len-len(self.bar)-1:
      self.add = -1
    if self.prog<1:
      self.add = +1
    s = ''.join(s)
    if not self.freeze:
      cprint(self.format.replace("%bar",s).replace("%log",self.logmsg),self.fg,self.bg,end="\r",flush=True)
    time.sleep(rate)
  def stop(self,msg="Done!"):
    print('\033[?25h', end="") 
    print(end="\x1b[2K")

    cprint(f"\r{msg}",self.fg,self.bg)
  def error(self,msg,fg=(255,0,0),bg=(0,0,0)):
      print('\033[?25h', end="") 
      print(end="\x1b[2K")
      cprint(f"\r{msg}",fg,bg,flush=True)
      os._exit(1)

  def log(self,msg,):
    self.logmsg= msg
