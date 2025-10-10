#_________________________________Typing_____________________________
import time
import sys

def typ(str, textSpeed = 0.03):
  """
  Prints a string in a way that it looks like its being typed
  Syntax: type(\"Hello World\") or type(\"Hello World Slower\", 0.01)
  """
  for c in str + '\n':
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(textSpeed)




#_____________________________frm_input________________________
def input_frm(string, type, alt = "Not the right format"):
  """
  Keeps asking for input until a certain type is give
  Syntax: input_frm(\"Whats your age: \", int)
  """
  ans = None
  while isinstance(ans, type) == False:
    ans = input(string)
    try:
      if type == str:
        ans = str(ans)
        
      elif type == float:
        ans = float(ans)
        
      elif type == int:
        ans = int(ans)
    except:
      print('\033[0;31m' + alt + '\033[0m')
  return ans




#__________________________Clock__________________________

class clock:
  clock = time.localtime(time.time())
  days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  
  months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  
  
  if clock.tm_mday == 1:
    ending = "st"
  elif clock.tm_mday == 2:
    ending = "nd"
  elif clock.tm_mday == 3:
    ending = "rd"
  else:
    ending = "th"
  
  year      = clock.tm_year
  month     = months[clock.tm_mon - 1]
  month_day = str(clock.tm_mday) + ending
  week_day  = days[clock.tm_wday]
  hour      = clock.tm_hour
  min       = clock.tm_min
  sec       = clock.tm_sec



    
#___________________________________Colour_____________________________________

class clr_code:
  """
  Returns a ascii code used to change the format of text
  Syntax: clr_code.red
  """
  red = '\033[0;31m'
  green = '\033[0;32m'
  orange = '\033[0;33m'
  blue = '\033[0;34m'
  purple = '\033[0;35m'
  cyan = '\033[0;36m'
  white = '\033[0;37m' 
  
  brt_black = '\033[0;90m'
  brt_black_red = '\033[0;91m'
  brt_green = '\033[0;92m'
  brt_yellow = '\033[0;93m'
  brt_blue = '\033[0;94m'
  brt_magenta = '\033[0;95m'
  brt_cyan = '\033[0;96m'
  
  cyan_bg = '\033[0;46m'
  purple_bg = '\033[0;45m'
  white_bg = '\033[0;47m'
  blue_bg = '\033[0;44m'
  orange_bg = '\033[0;43m'
  green_bg = '\033[0;42m'
  pink_bg = '\033[0;41m'
  grey_bg = '\033[0;40m'
  
  bold = '\033[1m'
  underline = '\033[4m'
  italic = '\033[3m'
  darken = '\033[2m'
  invisible ='\033[08m'
  high_contrast ='\033[07m'
  
  reset ='\033[0m'







class clr:
  """
  Returns a string with a changed format
  Syntax: clr.red(\"Hello World in red\")
  """
  def red(text):
    return clr_code.red + text + clr_code.reset
  
  def green(text):
    return clr_code.green + text + clr_code.reset
  
  def orange(text):
    return clr_code.orange + text + clr_code.reset
  
  def blue(text):
    return clr_code.bold + text + clr_code.reset
  
  def purple(text):
    return clr_code.purple + text + clr_code.reset
  
  def cyan(text):
    return clr_code.cyan + text + clr_code.reset
  
  def white(text):
    return clr_code.white + text + clr_code.reset
  
  def grey(text):
    return clr_code.brt_black + text + clr_code.reset
  
  def pink(text):
    return clr_code.brt_red + text + clr_code.reset
  
  def brt_green(text):
    return clr_code.brt_green + text + clr_code.reset
  
  def yelo(text):
    return clr_code.brt_yellow + text + clr_code.reset
  
  def brt_blue(text):
    return clr_code.brt_blue + text + clr_code.reset
  
  def brt_magenta(text):
    return clr_code.brt_magenta + text + clr_code.reset
  
  def brt_cyan(text):
    return clr_code.brt_cyan + text + clr_code.reset
  
  def cyan_bg(text):
    return clr_code.cyan_bg + text + clr_code.reset
  
  def purple_bg(text):
    return clr_code.purple_bg + text + clr_code.reset
  
  def white_bg(text):
    return clr_code.white_bg + text + clr_code.reset
  
  def blue_bg(text):
    return clr_code.blue_bg + text + clr_code.reset
  
  def orange_bg(text):
    return clr_code.orange_bg + text + clr_code.reset
  
  def green_bg(text):
    return clr_code.green_bg + text + clr_code.reset
  
  def pink_bg(text):
    return clr_code.pink_bg + text + clr_code.reset
  
  def grey_bg(text):
    return clr_code.grey_bg + text + clr_code.reset
  
  def bold(text):
    return clr_code.bold + text + clr_code.reset
  
  def underline(text):
    return clr_code.underline + text + clr_code.reset
  
  def italic(text):
    return clr_code.italic + text + clr_code.reset
  
  def darken(text):
    return clr_code.darken + text + clr_code.reset
  
  def invisible(text):
    return clr_code.invisible + text + clr_code.reset
  
  def high_contrast(text):
    return clr_code.high_contrast + text + clr_code.reset