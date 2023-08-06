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

def color(text,fg=(255,255,255),bg=None,**kwargs):
	if bg != None:
		return(rgbf(*fg)+rgbb(*bg)+text+RESET)
	else:
		return(rgbf(*fg)+text+RESET)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

yellow = (255,255,0)
teal = (0,255,255)
purple = (255,0,255)

orange = (255,125,0)
pink = (255,0,145)


warn = (255,204,0)
