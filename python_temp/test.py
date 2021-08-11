import pyautogui
import sys
import time
import datetime

#============================================================
# Note
#============================================================
"""
"""
# open mac authorization
# jp language
# login
# follow the hololive booth



#============================================================
# Global Parameters
#============================================================
CURRENT_OS = sys.platform                               # platform of excuete computer

TESTING     = True
CHECK_LOGIN = False
PASSWARD    = ''
PAYMENT     = ''
SALE_TIME   = '2021-08-11 03:16:00.000'

TAB_NUM     = 2

# Images
IMG_WEB_STATE   = 'web_done_win_24inch_1920_1080.png'
IMG_ADD_TO_CART = 'add_to_cart_win_24inch_1920_1080.png'
IMG_BUY_BUTTON  = 'buy_botton_win_24inch_1920_1080.png'
IMG_PAYMENT     = 'payment_win_24inch_1920_1080.png'
IMG_SHIP_INFO   = 'ship_info_win_24inch_1920_1080.png'
IMG_CONFIRM     = 'confirm_win_24inch_1920_1080.png'

CONFIDENCE = 0.9                                        # match error torrence

# The searching screen shot region. Smaller the region, faster the process
REGION_WEB_STATE   = (   77,  43,   95,   60 )
REGION_ADD_TO_CART = ( 1100,   0, 1450, 1080 )
REGION_BUY_BUTTON  = ( 1030, 500, 1280,  700 )
REGION_PAYMENT     = (  680, 500,  800,  600 )
REGION_SHIP_INFO   = (  650, 790,  810,  850 )
REGION_CONFIRM     = (  870, 860, 1040,  980 )

# Global setting
pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = False



#============================================================
# Functions
#============================================================
def WaitLoading():
    while True:
        state = pyautogui.locateOnScreen( IMG_WEB_STATE, confidence = CONFIDENCE , region = REGION_WEB_STATE )
        if state != None: break
    return


# Refrssh the browser when it starts saling
def Refresh():
    t_now = datetime.datetime.now()
    t_sale = datetime.datetime.fromisoformat( SALE_TIME )
    while True:
        if t_now >= t_sale: break
        t_now = datetime.datetime.now()
        
    if CURRENT_OS == 'darwin':
        pyautogui.hotkey( 'command', 'r' )
    else:
        pyautogui.press( 'f5' )

    pyautogui.press('home')
    pyautogui.press('pagedown')
    return


# switch the screen
def ChangeScreen():
    if CURRENT_OS == 'darwin':
        pyautogui.hotkey( 'command', 'tab' )
    else:
        pyautogui.keyDown( 'alt' )
        pyautogui.press( 'tab', presses = TAB_NUM )
        pyautogui.keyUp( 'alt' )
    return


def MoveOnBotton( search_botton, search_region ):
    buttonlocation = pyautogui.locateOnScreen( search_botton, confidence = CONFIDENCE , region = search_region )
    x, y = pyautogui.center( buttonlocation )
    if CURRENT_OS == 'darwin':
        pyautogui.moveTo(x//2, y//2)
    else:
        pyautogui.moveTo(x, y)
    return


def ClickOnBotton( search_botton, search_region ):
    buttonlocation = pyautogui.locateOnScreen( search_botton, confidence = CONFIDENCE , region = search_region )
    x, y = pyautogui.center( buttonlocation )
    if CURRENT_OS == 'darwin':
        pyautogui.click(x//2, y//2)
    else:
        pyautogui.click(x, y)
    return


# this will choose the most top and most left one buy button
def AddToCart():
    ClickOnBotton( IMG_ADD_TO_CART, REGION_ADD_TO_CART )
    return


def Buy():
    ClickOnBotton( IMG_BUY_BUTTON, REGION_BUY_BUTTON )
    return


def Login():
    return



def Payment():
    pyautogui.click(960, 640)
    ClickOnBotton( IMG_PAYMENT, REGION_PAYMENT )
    return



def ShipInfo():
    ClickOnBotton( IMG_SHIP_INFO, REGION_SHIP_INFO )
    return



def Confirm():
    pyautogui.press('end')
    if TESTING:
        MoveOnBotton( IMG_CONFIRM, REGION_CONFIRM )
    else:
        ClickOnBotton( IMG_CONFIRM, REGION_CONFIRM )
    return



#============================================================
# Main part
#============================================================
ChangeScreen()

Refresh()
WaitLoading()

AddToCart()
WaitLoading()

Buy()
WaitLoading()

if not CHECK_LOGIN: Login()

WaitLoading()
Payment()

WaitLoading()
ShipInfo()

WaitLoading()
Confirm()

