#lab 8
#This program is an AI that simulates human emotions and responses
#emotionalai.py

#variables
emo1 = 'happy'
emo2= 'sad'
emo3 = 'angry'
emo4 = "disgusted"
emo5 = "afraid"
emo6 = "surprised"
emo7 = "playful"
responses =[['reward', emo7,emo6, emo6, emo3, emo1, emo1, emo1],
            ['punish', emo2, emo2, emo3, emo2, emo2, emo3, emo2],
            ["threaten", emo5, emo5, emo3, emo3, emo2, emo2, emo3],
            ['joke', emo7, emo3, emo4, emo3, emo6, emo1, emo7]]

curEmo = emo1

def output(curEmo, emo1, emo2, emo3, emo4, emo5, emo6, emo7):
#Show emotion
#prints current emotion
#return emotion in current state
    
    if curEmo == emo1:
        print("Yay, now I'm", emo1)
    if curEmo == emo2:
        print("Oh... now I'm", emo2)
    if curEmo ==emo3:
        print("Argh, you've done it now! Now I'm", emo3)
    if curEmo == emo4:
        print("Eugh! Now I'm", emo4)
    if curEmo == emo5:
        print("Aahhh! I'm", emo5)
    if curEmo == emo6:
        print("Whoa, I'm", emo6)
    if curEmo == emo7:
        print("Ha ha! I'm feeling", emo7)
            
    return curEmo

def userInput(curEmo, action, rew, pun, thr, lol):
    action = ""
    rew= ""
    pun = ""
    thr = ""
    lol = ""
    print("Right now, I'm", curEmo)
    print("")
    print("What would you like to do?")
    action = str(input("Reward, punish, threaten, joke, or quit?:"))
    if action == 'reward':
        action = rew
    elif action == 'punish':
          action = pun
    elif action == "threaten":
          action = thr
    elif action =='joke':
          action = lol
    elif action =='quit':
          action = 'quit'    
    else:
        print("I didn't understand that action. Try again?")
        action = userInput(curEmo, action, rew, pun, thr, lol)

    return action

def currentEmotion(rew, pun, thr, lol, action, curEmo):
    #lookup new appropriate reaction
    responses =[['reward', emo7,emo6, emo6, emo3, emo1, emo1, emo1],
            ['punish', emo2, emo2, emo3, emo2, emo2, emo3, emo2],
            ['threaten', emo5, emo5, emo3, emo3, emo2, emo2, emo3],
            ['joke', emo7, emo3, emo4, emo3, emo6, emo1, emo7]]
    #take in users input, return new emotional state
    if action == rew:
        if curEmo == emo1:
           curEmo = (responses[0][1])
        elif curEmo == emo2:
            curEmo = (responses[0][2])
        elif curEmo == emo3:
            curEmo = (responses[0][3])
        elif curEmo == emo4:
            curEmo = (responses[0][4])
        elif curEmo == emo5:
            curEmo = (responses[0][5])
        elif curEmo == emo6:
            curEmo = (responses[0][6])
        elif curEmo == emo7:
            curEmo =(responses[0][7])

    if action == pun:
        if curEmo == emo1:
            curEmo =(responses[1][1])
        if curEmo == emo2:
            curEmo = (responses[1][2])
        if curEmo == emo3:
            curEmo=(responses[1][3])
        if curEmo == emo4:
            curEmo =(responses[1][4])
        if curEmo == emo5:
            curEmo =(responses[1][5])
        if curEmo == emo6:
            curEmo =(responses[1][6])
        if curEmo == emo7:
            curEmo =(responses[1][7])          

    if action == thr:
        if curEmo == emo1:
            curEmo =(responses[2][1])
        if curEmo == emo2:
            curEmo =(responses[2][2])
        if curEmo == emo3:
            curEmo =(responses[2][3])
        if curEmo == emo4:
            curEmo =(responses[2][4])
        if curEmo == emo5:
            curEmo =(responses[2][5])
        if curEmo == emo6:
            curEmo =(responses[2][6])
        if curEmo == emo7:
            curEmo =(responses[2][7])

            
    if action == lol:
        if curEmo == emo1:
            curEmo =(responses[3][1])
        if curEmo == emo2:
            curEmo =(responses[3][2])
        if curEmo == emo3:
            curEmo =(responses[3][3])
        if curEmo == emo4:
            curEmo =(responses[3][4])
        if curEmo == emo5:
            curEmo =(responses[3][5])
        if curEmo == emo6:
            curEmo =(responses[3][6])
        if curEmo == emo7:
            curEmo =(responses[3][7])

    return curEmo
           
            
        
def main():
    #intro
    print("Hello, I'm an AI programmed with emotional reponses to your actions!")
    print("")
    curEmo = emo1
    action = ""
    rew= ""
    pun = ""
    thr = ""
    lol = ""
    #primary loop
    while action != "quit":
        action = userInput(curEmo, action, rew, pun, thr, lol)
        curEmo = currentEmotion(rew, pun, thr, lol, action, curEmo)
        output(curEmo, emo1, emo2, emo3, emo4, emo5, emo6, emo7)
    else:
        print("Goodbye!")    
main()    
