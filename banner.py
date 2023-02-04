import os

# System call
os.system("")


# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

bannerDisplay = f"""
+=========================================================+
||  _     _                                              ||
|| | |   | |                            _                ||
|| | |__ | | ____  ____ _   _ ____  ___| |_  ____  ____  ||
|| |  __)| |/ _  |/ ___) | | / _  )/___)  _)/ _  )/ ___) ||
|| | |   | ( ( | | |    \ V ( (/ /|___ | |_( (/ /| |     ||
|| |_|   |_|\_||_|_|     \_/ \____|___/ \___)____)_|     ||
||                  {style.WHITE}  By: Baboucarr Badjie               {style.RESET}||   
||{style.RED}                        Please note this tool uses     {style.RESET}||    
||{style.RED}                    webscraping tools to fetch data.   {style.RESET}||       
||{style.RED}                    By using this tool, you agree      {style.RESET}||   
||{style.RED}                    that you are responsible for any   {style.RESET}||     
||{style.RED}                    violation of rules caused by this  {style.RESET}||         
||{style.RED}                    tool!                              {style.RESET}||  
+=========================================================+                                                
"""