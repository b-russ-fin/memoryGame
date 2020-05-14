http://www.codeskulptor.org/#user43_bNDhxyhy9o_3.py



# implementation of card game - Memory

import simplegui
import random

turns = 0
win = False
# helper function to initialize globals
def new_game():
    global state
    global list
    global exposed
    global turns
    global win
    state = 0
    turns = 0
    win = False
    label.set_text("Turns = " + str(turns))
    
# create cards    
    list = range(1,9) + range(1,9)
    random.shuffle(list)
    print  list
    exposed = dict(enumerate(list))
    for i in exposed:
        exposed[i] = False
    print exposed
    

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state
    global exposed
    global turns
    global card_match1
    global card_match2
    global win
    
    # which card was selected    
    card = int(pos[0] / 50)
    print card
    exposed[card] = True
    
    # is card a match
    if state == 0:
        state = 1
        turns += 1
        card_match1 = card
    elif state == 1:
        if card != card_match1:
            state = 2
        
            card_match2 = card
        
    else:
        if card != card_match1:
            if card != card_match2:
                if list[card_match1] != list[card_match2]:
                    exposed[card_match1] = False
                    exposed[card_match2] = False
                card_match1 = card
                turns += 1
                state = 1
    
    label.set_text("Turns = " + str(turns))
    
    win = True    
    for w in exposed:
        if exposed[w] == False:
            win = False
    

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global list
    global exposed
    
# place cards
    p = 15
    for x in list:
        canvas.draw_text(str(x), (p, 55), 25, 'Gray', 'serif')
        p += 50
   
    for e in exposed:
        if exposed[e] == False:
            canvas.draw_polygon([(e * 50, 0), (50 + e * 50, 0), (50 + e * 50, 100), (e * 50, 100)], 6, 'Grey', 'Blue')
    
    if win == True:
        canvas.draw_text("You Win", (200, 50), 40, 'Red')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
