import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)
position1 = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.6)
x = position1[0]
y = position1[1]

# Gets message
def get_message():
    global x,y

    position = position1 = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.move(x,y, duration=.05) #duration es para MAC pero por las dudas para ubuntu
    pt.moveTo(x,y,duration= .5)
    pt.moveTo(x + 70,y - 40,duration= .5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("Message: " + whatsapp_message)
    return whatsapp_message

# Tengo que ver las posiciones como conseguirlas si varian.
# Posts 
def post_response():
    global x,y
    position = position1 = pt.locateOnScreen("whatsapp/smiley_paperclip.png", confidence=.6)
    x = position[0]
    y = position[1]
    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    #pt.typewrite("\n",interval=.01) #Hacer el enter para mandar el mensaje OJO ESTO DE COMENTARLO

# Processes response
def process_response(message):
    random_no = random.randrange(3)
    #TODO ver si se puede agregar algo de IA
    if "?" in str(message).lower():
        return "Veamos que hacemos con una pregunta"
    
    #TODO agregar la regex

# Check for new messages
def check_messages():
    pt.moveTo(x + 50, y-35, duration=.5)

    while True:
        try:
            position = pt.locateOnScreen("whatsapp/green_circle.png", confidence=.7)
            
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)
        except(Exception):
            print("No no messages")
        if pt.pixelMatchesColor(int(x + 50), int(y - 35),(255,255,255), tolerance=10):
            print("Is white")
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print("No new messages yet")
        sleep(5)



processed_message = process_response(get_message())
post_response(processed_message)
#post_response()
#get_message()
