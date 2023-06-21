#Game by Jan Lupus Reimann
import time
import random
character={}
    #"Alice":{
    #    "mood":-1,
    #    "description": ""#https://www.verywellhealth.com/generalized-anxiety-disorder-5092814
    #},
    #"Emma":{
    #   "mood":1,
    #   "description": ""#https://www.verywellhealth.com/pica-5083875
    #},
    #"George":{
    #   "mood":0,
    #   "description": ""#https://www.verywellhealth.com/schizophrenia-5078641
    #},
    #"Niklas":{
    #   "mood":0,
    #   "description": ""#https://www.verywellhealth.com/obsessive-compulsive-disorder-ocd-5084138
    #},
    #"Alastair":{
    #   "mood":0,
    #   "description": ""#https://www.verywellhealth.com/complex-ptsd-5094628
    #},
    #"Manasses":{
    #   "mood":random.randint(0,1),
    #    "description": ""#https://www.verywellhealth.com/bipolar-disorder-5090253
    #}
#https://www.verywellhealth.com/top-mental-health-disorders-a-mental-illness-list-5210092


won=False

def intro():
    print("You got invited to a dating-show, that offered a weird service\nYou would have to pick out one person, asking them three questions and answering their three questions.\nAfter these questions you can ask them for their number and if they don't give you their number, you have to move over to the next person.")
    time.sleep(3)
    print("The special part about this show: Once you found someone, the show covers the cost of three visits to a therapist your choice, who will have individual sessions with you, your partner and one session with the two of you.\n")
    time.sleep(3)
    tutorial()

def tutorial():
    print("You will be given 3 options at the same time, pick from them using the numbers indicated.(1,2,3)")
    #time.sleep(3)
    #print('If you think that you already found a match, you can enter "!number" at anytime during the show, to ask for the number of your date.')
    time.sleep(3)
    print("Note: This game is not intended to reference any existing people or to be used as simulation for any social interactions.")
    time.sleep(2)
    print("\n\n\n██████╗ ███████╗ █████╗ ██████╗ ██╗   ██╗██████╗ ██████╗ \n██╔══██╗██╔════╝██╔══██╗██╔══██╗╚██╗ ██╔╝╚════██╗╚════██╗ \n██████╔╝█████╗  ███████║██║  ██║ ╚████╔╝   ▄███╔╝  ▄███╔╝\n██╔══██╗██╔══╝  ██╔══██║██║  ██║  ╚██╔╝    ▀▀══╝   ▀▀══╝ \n██║  ██║███████╗██║  ██║██████╔╝   ██║     ██╗     ██╗   \n╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═════╝    ╚═╝     ╚═╝     ╚═╝   \n\n\n")
    time.sleep(2)
    print("\n\n██████╗ \n╚════██╗\n █████╔╝\n ╚═══██╗\n██████╔╝\n╚═════╝ \n\n")
    time.sleep(2)
    print("\n\n██████╗ \n╚════██╗\n █████╔╝\n██╔═══╝ \n███████╗\n╚══════╝\n\n")
    time.sleep(2)
    print("\n\n ██╗\n███║\n╚██║\n ██║\n ██║\n ╚═╝\n\n")
    time.sleep(3)
    print("\n\n\n██╗     ███████╗████████╗    ████████╗██╗  ██╗███████╗    ██████╗  █████╗ ████████╗██╗███╗   ██╗ ██████╗     ██████╗ ███████╗ ██████╗ ██╗███╗   ██╗██╗\n██║     ██╔════╝╚══██╔══╝    ╚══██╔══╝██║  ██║██╔════╝    ██╔══██╗██╔══██╗╚══██╔══╝██║████╗  ██║██╔════╝     ██╔══██╗██╔════╝██╔════╝ ██║████╗  ██║██║\n██║     █████╗     ██║          ██║   ███████║█████╗      ██║  ██║███████║   ██║   ██║██╔██╗ ██║██║  ███╗    ██████╔╝█████╗  ██║  ███╗██║██╔██╗ ██║██║\n██║     ██╔══╝     ██║          ██║   ██╔══██║██╔══╝      ██║  ██║██╔══██║   ██║   ██║██║╚██╗██║██║   ██║    ██╔══██╗██╔══╝  ██║   ██║██║██║╚██╗██║╚═╝\n███████╗███████╗   ██║          ██║   ██║  ██║███████╗    ██████╔╝██║  ██║   ██║   ██║██║ ╚████║╚██████╔╝    ██████╔╝███████╗╚██████╔╝██║██║ ╚████║██╗\n╚══════╝╚══════╝   ╚═╝          ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝\n\n\n")
    character["cast"]=["Alastair","Alice","Emma","George","Manasses","Niklas"]
    charaIntro()
    #Danke an https://www.patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=1 fuer die tolle Schrift :)

def game():
    q1()
    print("\n")
    time.sleep(2)
    q2()
    print("\n")
    time.sleep(2)
    q3()
    print("\n")
    time.sleep(2)
    q4()
    print("\n")
    time.sleep(2)
    q5()
    print("\n")
    time.sleep(2)
    q6()
    print("\n")
    time.sleep(2)
    askNum()

def askNum():
    print("You ask",character["choice"]["name"],"for their number...")
    time.sleep(6)
    if(character[character["choice"]["num"]]["mood"]>=5):
        print("+49 01463 7846592")
        end()
    else:
        print("...but you don't get any response.")
        character.pop(character["choice"]["num"])
        character["cast"].remove(character["choice"]["name"])
        print("You date leaves the show and you have to pick someone again\n")
        charaIntro()

def isOverOne(num):
    if(num>1):
        return num
    else:
        return 1
    
def isOdd(num):
    if(num%2!=0):
        return True
    else:
        return False

def charaIntro():
    for x in range(len(character["cast"])):
        character[x+1]={}
    character["choice"]={}
    if("Alastair" in character["cast"]):
        print("Charakter Nummer 1 | Alastair.\n This very tall, slender figure walks swiftly towards the table, their eyes scanning the entirety of the room as they do so. They are wearing a purple oversized hoodie and black thin shorts.")
        character[1]["mood"]=0
    if("Alice" in character["cast"]):
        print("Charakter Nummer 2 | Alice.\n A short brunett, wearing a short white summer-dress, who is looking around the place with her tired looking hazelbrown eyes wide open. Her fingers are twitching as she rests them onto the table.")
        character[2]["mood"]=-1
    if("Emma" in character["cast"]):
        print("Charakter Nummer 3 | Emma.\n A woman with wild ginger hair, braided losely together. She's wearing a bright yellow top and a knee  long dark brown skirt. Her smile immediately fills the room with warmth.")
        character[3]["mood"]=1
    if("George" in character["cast"]):
        print("Charakter Nummer 4 | George.\n A shorter guy with medium dark hair, wearing a tight black T-shirt and blue suit pants. He looks around the place with big blue eyes and mumbles something quietly as he approaches")
        character[4]["mood"]=0
    if("Manasses" in character["cast"]):
        print("Charakter Nummer 5 | Manasses.\n This short black haired Person, is wearing a multitude of small silver piercings and a black leather fortified 17th century british military uniform. They look rather tired and slowly walk towards the table")
        character[5]["mood"]=random.randint(0,1)
    if("Niklas" in character["cast"]):
        print("Charakter Nummer 6 | Niklas.\n A  tall young man with blond short hair, wearing a blue shirt and beige shorts. His broad shoulders and muscular arms stretching the shirt a little. He sighs visible as he approaches the table and rests his big hands on it.")
        character[6]["mood"]=0
    charaChoice=int(input("Who would you like to meet?\nYou: "))
    if(isOverOne(charaChoice)==1):
        character["choice"]["num"]=1
        character["choice"]["name"]="Alastair"
    elif(isOverOne(charaChoice)==2):
        character["choice"]["num"]=2
        character["choice"]["name"]="Alice"
    elif(isOverOne(charaChoice)==3):
        character["choice"]["num"]=3
        character["choice"]["name"]="Emma"
    elif(isOverOne(charaChoice)==4):
        character["choice"]["num"]=4
        character["choice"]["name"]="George"
    elif(isOverOne(charaChoice)==5):
        character["choice"]["num"]=5
        character["choice"]["name"]="Manasses"
    elif(isOverOne(charaChoice)==6):
        character["choice"]["num"]=6
        character["choice"]["name"]="Niklas"
    else:
        print("Please ")
    game()

def q1():
    name=character["choice"]["name"]
    question=""
    if(name=="Alastair"):
        question="How are you?"
    elif(name=="Alice"):
        question="Are you nervous?"
    elif(name=="Emma"):
        question="How are you?"
    elif(name=="George"):
        question="Have you done something like this before?"
    elif(name=="Manasses"):
        question="What is your goal here?"
    elif(name=="Niklas"):
        question="What are your hobbies?"
    print(name+": "+'"'+question+'"')
    getAnswer(1,question)

def q2():
    name=character["choice"]["name"]
    question={}
    if(name=="Alastair"):
        question[1]="How's the weather up there?"
        question[2]="Are you more of an indoors or outdoors person?"
        question[3]="What about you?"
    elif(name=="Alice"):
        question[1]="What about you?"
        question[2]="Are you here for the first time?"
        question[3]="What are your hobbies?"
    elif(name=="Emma"):
        question[1]="How are you?"
        question[2]="What are your hobbies?"
        question[3]="What do you do for a living?"
    elif(name=="George"):
        question[1]="What about you?"
        question[2]="What is this clothing style?"
        question[3]="What are your hobbies?"
    elif(name=="Manasses"):
        question[1]="Are you alright?"
        question[2]="What are your hobbies?"
        question[3]="What are you looking for in a relationship?"
    elif(name=="Niklas"):
        question[1]="What are your hobbies?"
        question[2]="Why are you wearing gloves?"
        question[3]="Are you nervous?"
    for x in range(1,4):
        print(x,"|",question[x])
    questionOption=int(input("You: "))
    print(name+": "+'"'+getAnswer(2,questionOption)+'"')

def q3():
    name=character["choice"]["name"]
    question=""
    if(name=="Alastair"):
        question="Are you a better listener or a better story teller?"
    elif(name=="Alice"):
        question="What do you do in your past time?"
    elif(name=="Emma"):
        question="Does your job take up a big portion of your time?"
    elif(name=="George"):
        question="What are your hobbies?"
    elif(name=="Manasses"):
        question="If you could have the answer to any one question, what question would you want the answer to?"
    elif(name=="Niklas"):
        question="What are you looking for in a person?"
    print(name+": "+'"'+question+'"')
    getAnswer(3,question)

def q4():
    name=character["choice"]["name"]
    question={}
    if(name=="Alastair"):
        question[1]="Would you consider yourself more of an introvert or extrovert? "
        question[2]="What do you work as?"
        question[3]="What are your hobbies?"
    elif(name=="Alice"):
        question[1]="Are you still nervous?"
        question[2]="What do you work as?"
        question[3]="Are you a nightowl or morning person?"
    elif(name=="Emma"):
        question[1]="What are you really good in?"
        question[2]="What are you looking for here?"
        question[3]="Are you a summer or winter person?"
    elif(name=="George"):
        question[1]="What do you work as?"
        question[2]="Are you a night-owl?"
        question[3]="What did you do the past few days?"
    elif(name=="Manasses"):
        question[1]="What do you work as?"
        question[2]="Why are you dressed like that?"
        question[3]="If you could have the answer to any question..."
    elif(name=="Niklas"):
        question[1]="What about you?"
        question[2]="What do you work as?"
        question[3]="What is the weirdest thought you ever had?"
    for x in range(1,4):
        print(x,"|",question[x])
    questionOption=int(input("You: "))
    print(name+": "+'"'+getAnswer(4,questionOption)+'"')

def q5():
    name=character["choice"]["name"]
    question=""
    if(name=="Alastair"):
        question="Do you enjoy going to concerts?"
    elif(name=="Alice"):
        question="Do you have any kids?"
    elif(name=="Emma"):
        question="Do you have any pets?"
    elif(name=="George"):
        question="Are you religious or do you believe in the supernatural?"
    elif(name=="Manasses"):
        question="Do you like your job?"
    elif(name=="Niklas"):
        question="Do you have any weird habbits?"
    print(name+": "+'"'+question+'"')
    getAnswer(5,question)

def q6():
    name=character["choice"]["name"]
    question={}
    if(name=="Alastair"):
        question[1]="What is your favourite type of music?"
        question[2]="How is your relationship with your family?"
        question[3]="Are you a night-owl or morning person?"
    elif(name=="Alice"):
        question[1]="What is your favourite food?"
        question[2]="Do you believe in astrology?"
        question[3]="Why are you so nervous?"
    elif(name=="Emma"):
        question[1]="What about your job do you love the most?"
        question[2]="Are you excited for the weekend?"
        question[3]="What is the weirdest food you ever tried?"
    elif(name=="George"):
        question[1]="What about you?"
        question[2]="Are you a dog or cat person?"
        question[3]="What are you looking for in a relationship?"
    elif(name=="Manasses"):
        question[1]="What is your favorite food?"
        question[2]="What about you?"
        question[3]="Are you a nightowl or morning person?"
    elif(name=="Niklas"):
        question[1]="Are you a dof or cat person?"
        question[2]="What's your favorite season?"
        question[3]="What the weirdest thing you ever did?"
    for x in range(1,4):
        print(x,"|",question[x])
    questionOption=int(input("You: "))
    print(name+": "+'"'+getAnswer(6,questionOption)+'"')

def getAnswer(questionNum, questionOption):
    name=character["choice"]["name"]
    answer={}
    if(questionNum==1):
        if(name=="Alastair"):
            answer[1]="I'm fine-1"
            answer[2]="Pretty good+0"
            answer[3]="Could be worse+0"
        elif(name=="Alice"):
            answer[1]="Yes!+0"
            answer[2]="A little...+1"
            answer[3]="Not at all.-1"
        elif(name=="Emma"):
            answer[1]="Good.+0"
            answer[2]="A little nervous, but alright+0"
            answer[3]="Very good+1"
        elif(name=="George"):
            answer[1]="Yes, but as you can see I wasn't as successfull yet+1"
            answer[2]="Yeah+0"
            answer[3]="No, this is my first time+0"
        elif(name=="Manasses"):
            answer[1]="To find someone to love-1"
            answer[2]="I mean...it's a dating-show, what do you think?+0"
            answer[3]="Honestly, I've been asking myself the same question+1"
        elif(name=="Niklas"):
            answer[1]="I like to sit myself down alone with a good film or a nice book+0"
            answer[2]="I usually do something with friends+0"
            answer[3]="I love to push myself to my physical and psychological limits in my past time+1"
    elif(questionNum==2):
        if(name=="Alastair"):
            if(questionOption==1):
                answer[0]="funny.-1"
            elif(questionOption==2):
                answer[0]="I'd say both. I do enjoy some time outside, but four walls do give of some comfort.+1"
            elif(questionOption==3):
                answer[0]="I'm alright.+0"
        elif(name=="Alice"):
            if(questionOption==1):
                answer[0]="...-1"
            elif(questionOption==2):
                answer[0]="...no+0"
            elif(questionOption==3):
                answer[0]="...I like listening to music, if that counts+1"
        elif(name=="Emma"):
            if(questionOption==1):
                answer[0]="I'm feeling amazing!+0"
            elif(questionOption==2):
                answer[0]="I love taking the dogs out for a walk around a lake nearby+1"
            elif(questionOption==3):
                answer[0]="I am responsible for the marketing of our local film and media centre+0"
        elif(name=="George"):
            if(questionOption==1):
                answer[0]="Yeah I have, but I ain't the best with people apparently+1"
            elif(questionOption==2):
                answer[0]="...Ohh yeah my washing machine clocked up yesterday, so I had to pick up some old stuff from when I was younger...How do I look?-1"
            elif(questionOption==3):
                answer[0]="I enjoy drawing, crafting and spending some time outside in the wild+0"
        elif(name=="Manasses"):
            if(questionOption==1):
                answer[0]="I am, why shouldn't I?-1"
            elif(questionOption==2):
                answer[0]="I enjoy cooking, shopping and some literature+0"
            elif(questionOption==3):
                answer[0]="Good question, but sadly I can't give you a good answer, maybe that's why I am here+1"
        elif(name=="Niklas"):
            if(questionOption==1):
                answer[0]="I spend my days exercising under the open sky+1"
            elif(questionOption==2):
                answer[0]="...You could say that I like keeping my hands clean.-1"
            elif(questionOption==3):
                answer[0]="Not really. A little perhabs.+0"
    elif(questionNum==3):
        if(name=="Alastair"):
            answer[1]="I'm more of a listener.+0"
            answer[2]="I'm great at telling stories that move people, but I wouldn't consider myself a very bad listener.+1"
            answer[3]="I am as good as a listener as I am a story-teller-1"
        elif(name=="Alice"):
            answer[1]="I don't really have a lot of hobbies, but rather just spend my days in bed exhausted from life and work-1"
            answer[2]="I enjoy a multitude of different activities+0"
            answer[3]="...I like listening to music if that counts-2"
        elif(name=="Emma"):
            answer[1]="Yes. I barely manage to sleep.+0"
            answer[2]="Not really I got a really loose and relaxing schedule, giving me the opportunity to participate in other activities.-1"
            answer[3]="It's okay. I do got some spare-time, but my day is quite busy usually.+1"
        elif(name=="George"):
            answer[1]="I like going outside, it keeps my energised and healthy.+0"
            answer[2]="I like to sit myself down alone with a good film or a nice book.+1"
            answer[3]="I don;t really have a lot of hobbies-1"
        elif(name=="Manasses"):
            answer[1]="The meaning of life-1"
            answer[2]="Difficult question. I don't know.+1"
            answer[3]="The Secret Code on how to get through this python-code instantly+1"
        elif(name=="Niklas"):
            answer[1]="Reliability and Loyalty. If I can't rely on my partner, what is the point in having one at all?+2"
            answer[2]="Kindness and Empathy. Humans are a social-species, we need comfort with the people around us.+0"
            answer[3]="Hardworkingness. I believe that everyone should put in their most in a relationship.-1"
    elif(questionNum==4):
        if(name=="Alastair"):
            if(questionOption==1):
                answer[0]="I would consider myself an introvert. Talking to people is really draning me out.+1"
            elif(questionOption==2):
                answer[0]="I am a receptionist, but I'm thinking about changing career paths soon.+0"
            elif(questionOption==3):
                answer[0]="I enjoy sitting on a horseback and listening to some music.+0"
        elif(name=="Alice"):
            if(questionOption==1):
                answer[0]="...+0"
            elif(questionOption==2):
                answer[0]="I work as a biology research-assistant+1"
            elif(questionOption==3):
                answer[0]="I enjoy the early mornings more than I do the night.+0"
        elif(name=="Emma"):
            if(questionOption==1):
                answer[0]="Uhh...tough question. Maybe planning? I'm really good at keeping things ordered and schedules clean and efficient, but I'm also a quite a good designer. I'd have to think on that longer to give you a good answer, but we'll go with that for now+1"
            elif(questionOption==2):
                answer[0]="For love of course. Just someone to spend some time with and whom I can share my projects with.+0"
            elif(questionOption==3):
                answer[0]="How do I look like? Summer of course!+0"
        elif(name=="George"):
            if(questionOption==1):
                answer[0]="I work as a nurse in the local hospital, but I am still very new.+0"
            elif(questionOption==2):
                answer[0]="I love going home, when the morning-sun rises and the birds start to sing their first songs.+2"
            elif(questionOption==3):
                answer[0]="...Living a med students life, I guess...I don't get to do a lot besides that-1"
        elif(name=="Manasses"):
            if(questionOption==1):
                answer[0]="I am an accountant.-1"
            elif(questionOption==2):
                answer[0]="Because I like the style+0"
            elif(questionOption==3):
                answer[0]="I don't know. Just because I asked you that question doesn't mean that I have an answer. It's just interesting to think about.+1"
        elif(name=="Niklas"):
            if(questionOption==1):
                answer[0]="Respect. It's just frustrating, if your Problems aren't seen as serious due to them not being understood.+1"
            elif(questionOption==2):
                answer[0]="I am an engineer.+0"
            elif(questionOption==3):
                answer[0]="...I can't think of one right now.-2"
    elif(questionNum==5):
        if(name=="Alastair"):
            answer[1]="I love going to concerts.+1"
            answer[2]="I rarely ever do, but it is fun+0"
            answer[3]="I am not really the type of person who goes to concerts.-1"
        elif(name=="Alice"):
            answer[1]="Yes.-3"
            answer[2]="No.+1"
            answer[3]="Why? Want some?-1"
        elif(name=="Emma"):
            answer[1]="Yeah and I love it+1"
            answer[2]="No, but I'm thinking about getting one+1"
            answer[3]="No I am busy enough without a pet-1"
        elif(name=="George"):
            answer[1]="Yes, I am part of a church-1"
            answer[2]="I don't really believe in anything.+0"
            answer[3]="Sometimes I do believe in some things considered supernatural.-1"
        elif(name=="Manasses"):
            answer[1]="There are worse things.+0"
            answer[2]="I love my job.-1"
            answer[3]="I like that it provides me money, that's about everything that I like about it.+1"
        elif(name=="Niklas"):
            answer[1]="No.+0"
            answer[2]="I got some, but I wouldn't consider them all too weird.+0"
            answer[3]="Yes I do, and I can't get rid of them.+1"
    elif(questionNum==6):
        if(name=="Alastair"):
            if(questionOption==1):
                answer[0]="Jazz. I love jazz over everything. It's just so smooth and dynamic.+1"
            elif(questionOption==2):
                answer[0]="....dead-2"
            elif(questionOption==3):
                answer[0]="I'm a night-owl. Wasting my entire sleep, doom-scrolling...+2"
        elif(name=="Alice"):
            if(questionOption==1):
                answer[0]="Cinnamon rolls.+1"
            elif(questionOption==2):
                answer[0]="...No+0"
            elif(questionOption==3):
                answer[0]="...It's actually a medical thing...That's part of why I am here...+3"
        elif(name=="Emma"):
            if(questionOption==1):
                answer[0]="The presentations are the best part, for sure. There's nothing like showing off all the work you did and telling people about your plans and ideas.+1"
            elif(questionOption==2):
                answer[0]="Well I gotta get some chores done, so I can't do too much this weekend.+0"
            elif(questionOption==3):
                answer[0]="...a pair of dirty socks...I got a eating disorder...+2"
        elif(name=="George"):
            if(questionOption==1):
                answer[0]="...No...-2"
            elif(questionOption==2):
                answer[0]="I am a lazy ass bitch. Dogs are a ton of work, so yeah...+1"
            elif(questionOption==3):
                answer[0]="I am looking for someone who can provide me some comfort and stability in my life.+2"
        elif(name=="Manasses"):
            if(questionOption==1):
                answer[0]="As if I could decide. I enjoy cooking too much to limit myself in that regard.+1"
            elif(questionOption==2):
                answer[0]="Yeah nope. I got a master degree in phylosophy and everythin I do all day is reply to e-mails that could very well be replied to by a bot. I hate it.+1"
            elif(questionOption==3):
                answer[0]="Neither. I am tired in the evening and tired in the morning. Most of the time I am even tired during the day.+0"
        elif(name=="Niklas"):
            if(questionOption==1):
                answer[0]="Dog person. I actually had a dog when I was younger. +1"
            elif(questionOption==2):
                answer[0]="Probably autumn. I like just the colours and the colder, but still pleasant temperatures.+1"
            elif(questionOption==3):
                answer[0]="...I have some quite weird habbits...Or tics for that matter...+2"

    if(isOdd(questionNum)):
        for i in range(1,4):
            print(i,"|",answer[i][0:len(answer[i])-2])
        answerOption=int(input("What would you like to say?\nYou:"))
    else:
        answerOption=0
    moodModifier=int(answer[answerOption][-2:])
    character[character["choice"]["num"]]["mood"]+=moodModifier ##https://www.geeksforgeeks.org/python-get-last-n-characters-of-a-string/ taught me how to slice lists in python
    time.sleep(2)
    return answer[answerOption][0:-2]

def end():
    time.sleep(1)
    print("Congrats! You won my game...now please ignore all the bugs, typos and dirtyness of this code and think about that I did this in a little over 24 hours :)")

intro()