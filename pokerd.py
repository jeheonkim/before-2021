import random
redflush = 0
def game():
    hand = []
    handcolor = []
    colors = ["C", "H", "D", "S"]
    for i in range(5):
        hand.append(random.randint(7,14))
        handcolor.append(random.choice(colors))
    avail = ["0", "1", "2", "3", "4"]
    answer = ""
    while answer != -1:
        print(hand)
        print(handcolor)
        print(avail)
        answer = int(input("You can change each card once. Input the number that corresponds to the card you want to switch. If you are done switching, input -1."))
        if avail[answer]!= "X" and answer != -1:
            avail[answer] = "O"
            hand[answer] = random.randint(7,14)
            handcolor[answer] = random.choice(colors)
    hand = sorted(hand)
    print(hand)
    straight = True
    for i in range(4):
        if hand[i] + 1 != hand[i+1]:
            straight = False
    flush = (handcolor[0] == handcolor[1] == handcolor[2] == handcolor[3] == handcolor[4])
    if (flush) and (straight == True):
        print('straightflush')
    elif (hand[0] == hand[4]):
        print('fivecards')
    elif (hand[0] == hand[3] or hand[1] == hand[4]):
        print('fourcards')
    elif (hand[0] == hand[2] and hand[3] == hand[4]) or (hand[0] == hand[1] and hand[2] == hand[4]):
        print('fullhouse')
    elif (flush):
        print('flush')
        if handcolor[0] == "H":
            redflush += 1
    elif (straight):
        print('straight')
    elif (hand[0] == hand[2] or hand[1] == hand[3] or hand[2] == hand[4]):
        print('triple')
    elif ((hand[0] == hand[1] and hand[2] == hand[3]) or (hand[0] == hand[1] and hand[3] == hand[4]) or (hand[1] == hand[2] and hand[3] == hand[4])):
        print('twopair')
    elif (hand[0] == hand[1] or hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]):
        print('onepair')
    else:
        print('Top card')
for i in range(5):
    game()
