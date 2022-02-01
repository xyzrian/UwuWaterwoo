# Character definitons, names, color codes
define ma = Character('Alyssa', color="#c60079")
define ahs = Character('Annie', color="#146f68")
define art = Character('Kaori', color="#e16738")
define env = Character('Neve', color="#a1aa11")
define eng = Character('Nicole', color="#4f00b4")
define sci = Character('Sachi', color="#147acc")
define anon = Character('Unknown', color="#ffffff") # When an unknown character is speaking
define dar = Character('Darren', color="#180896")

# Character "points" variables - influence menu options in the game
define ma_points = 0
define ahs_points = 0
define art_points = 0
define env_points = 0
define eng_points = 0
define sci_points = 0

label start:
    scene bg day 1 with fade
    pause
    scene bg uw outside with fade

    "Tomorrow is my first day at Waterloo as a male CS student."
    "I'm awfully terrified, but I've made the decision to walk around campus to see if I could find any potential friends..."
    "...although I know how unlikely that is."
    "I mean, there's never been anything special about me."
    $ name = renpy.input("What's my name again, anyway?")
    if name == "":
        "Please enter a name"
    "Ever since I was young, people only ever referred to me as the \'smart kid', never anything more."
    "Needless to say, I've never even been in a relationship, or felt the feeling of equally returned love."
    "I'm hoping university will be different for me. But, of course, I should not get my hopes up too much."
    "Looking around me, there aren't many girls in my field of view, and even if there were, I'd be the last person they would talk to."
    "Whatever. Might as well listen to music."
    "I reach into my pocket and find my phone, however..."
    "CRAP! I lost my WatCard - my student ID - and it isn't even my first day yet!"
    "How could I be so stupid?"
    "I begin to retrace my steps, frantically looking around for my lost card, when I hear a voice."

    anon "Hey, are you [name]?"

    show mathgirl at right with dissolve

    "I come face to face with a girl wearing glasses and a pink sweater."

    name "Yeah, I am. Who are you?"

    show mathgirl happy

    ma "I'm Alyssa. Did you lose your WatCard?"

    show mathgirl

    "Oh no. Out of all the boys on this campus... why did a pretty girl find my card?"
    "I feel my face going red."

    name "Yeah..... I did! I've been searching for it."

    "How embarrassing."

    show mathgirl happy

    ma "Well, here you go."

    "She hands me my card."

    show mathgirl

menu:
    "Say thank you and walk away.":
        jump walk_away

    "Say thanks and ask her what program she's in.":
        jump ask_her

label walk_away:
    name "Thank you for returning my card. I'll be on my way now."
    jump hold_up

label ask_her:
    name "Thank you for returning my card. By the way, what program are you in?"
    ma "I'm in Year 2 Math, majoring in Math Finance. What about you?"
    name "Tomorrow I start Computer Science."
    ma "So we're in the same faculty! Cool."
    name "Yeah, that is!"
    jump conversation_club

label hold_up:
    show mathgirl confused
    ma "What do you mean you'll be on your way? Who do you think you are?"
    name "Uh, I'm sorry?"
    show mathgirl happy
    ma "I'm messing with you, [name]. You're obviously a First Year so this is hilarious to me."
    "Hilarious? Oh my god. This girl must think I'm another CS code-monkey. Crap."
    name "Oh, yeah. Tomorrow is my first day in the Computer Science program."
    ma "Computer science, huh? I'm also in the Math faculty! In Year 2 now, decided to major in Math Finance."
    name "That's awesome."
    jump conversation_club

label conversation_club:
    ma "Have you looked into any clubs or teams you want to join?"
    name "Well... I'm not really sure. There are a few clubs that interest me."
    show mathgirl confused
    ma "Like what?"

menu:
    "Tell her you're interested in the CTRL-A (Anime) Club.":
        jump anime_club
    "Tell her you're interested in the Concert Band Club.":
        jump concert_band
    "Tell her you're busy and need to be on your way now.":
        jump goodbye

label anime_club:
    $ ma_points += 1
    name "I really like the CTRL-A Club. I think I might join it."
    show mathgirl looking away
    ma "CTRL-A? What are you, some sort of weeb?"
    name "... This is why I didn't want to tell you."
    show mathgirl happy
    ma "I'm kidding! I've been part of CTRL-A since my first week at uWaterloo!"
    name "Really? That makes me feel a lot better about it."
    show mathgirl happy blush
    "She giggles slightly, and only then do I realize what I've just said."
    ma "Well, if you plan on joining, I can introduce you, if you want."
    name "That would be awesome. When is the first meet?"
    ma "In two days, at 6 o'clock."
    name "I'll be there, then."
    ma "Let's exchange numbers so we can talk more, okay?"
    name "Uh- okay, sure."
    "We exchange numbers."
    ma "I'm going to V1 to meet with some of my friends. Talk soon?"
    name "Of course. Have fun. And thanks for finding my card."
    ma "Don't lose it again. I rarely ever walk past here. Anyway, see ya."
    show mathgirl
    hide mathgirl with dissolve
    "Did I... did I just talk to a girl?"
    "This can't be real. Never have I had someone approach me so proactively like that."
    "And now I have her number too? Maybe I do have a chance here at uWaterloo!"
    jump where_to

label concert_band:
    name "Since I did play in the band at my high school, I think I'm going to join the Concert Band Club."
    show mathgirl happy
    ma "Oh, that's awesome. I have a few friends in the club and they really enjoy it."
    name "Cool. When do rehearsals start?"
    show mathgirl looking away
    ma "I believe on September 23, at 7 pm."
    name "Alright, thanks. Are you in any clubs?"
    show mathgirl happy
    ma "Yeah, a few. My favourite is CTRL-A though, haha. I'm a bit of a weeb."

menu:
    "I am too!":
        ma "Oh, seriously! Haha, maybe consider joining CTRL-A then."
        name "I'll think about it."
        jump closing
    "Respectable, considering we are at uWaterloo.":
        show mathgirl looking away
        ma "I guess we do have the reputation for that sort of thing."
        jump closing

label goodbye:
    show mathgirl
    name "I'd talk more, but there's some things I need to get done."
    name "Thanks for returning my card back to me. I'll see you around."
    show mathgirl happy
    ma "Anytime. Have a good day."
    show mathgirl
    hide mathgirl with dissolve
    "Well, that was interesting."
    jump where_to

label closing:
        show mathgirl happy
        ma "Anyway, I'm going to V1 to visit some friends before class starts tomorrow. See ya around."
        name "Have fun. And thanks for finding my card."
        ma "Yeah, you're welcome. Don't lose it again."
        show mathgirl
        hide mathgirl with dissolve
        jump where_to

label where_to:
    "What should I do now?"

menu:
    "Get Bubble Tea.":
        "I'm craving BBT right now. Off to Coco's."
        jump bbt
    "Go back to dorm.":
        "That's enough socializing for the day. I'm going to head back to my room."
        jump dorm

label bbt:
    scene bg cocos_cashier with fade
    "Ahh, finally at Coco's."
    anon "Hi there, what could I get for you today?"

menu:
    "Order Grass Jelly Roasted Milk Tea.":
        name "Hi, I'll take a medium Grass Jelly Roasted Milk Tea."
        jump order
    "Order a Strawberry Latte.":
        name "Hi, I'll take a medium Strawberry Latte."
        jump order
    "Order Brown Sugar Milk Tea with extra sugar, red beans, and tapioca":
        $ ahs_points += 1
        name "Hi, I'll take a medium Brown Sugar Milk Tea with extra sugar, red beans, and tapioca."
        name "And I mean, a lot of tapioca."
        jump special_order

label order:
    anon "Alright, anything else?"
    name "Nope, that's everything."
    jump after_order

label special_order:
    "The cashier's face scrunches up as she gives me an interesting look."
    "Is she annoyed with my picky order? No... she's smiling."
    "It seems as though she wants to say something, but settles for a:"
    anon "Is that all?"
    name "Yep, that's everything."
    "Weird. I feel like I know this girl from somewhere."
    jump after_order

label after_order:
    "She makes my drink for me and I pause for a moment, wondering whether I want to have my drink in the store"
    "or head back to my dorm."
    menu:
        "Stay in the store.":
            "I decide to take a seat in the store and browse Reddit as I sip away at my beverage."
            jump sit_store
        "Go back to dorm.":
            "I'm getting tired, so I'll go back to my dorm for now."
            jump dorm

label sit_store:
    scene cocos_seating with fade
    "Let's see what's on the uWaterloo subreddit today. Afterall, classes do start tomorrow, so hopefully there's something worth reading."
    show phone with fade
    "I begin to scroll through my new school's Reddit page."
    "As usual, I see the typical NSFW drawings posted by the {i}wonderful{/i} artists here at UW."
    "It may seem strange, but the uWaterloo x UofT tsundere drawings are almost... attractive to me?"
    "Don't get the wrong idea: it's not the drawings that are turning me on of course.."
    "more so just imagining the possibilities that await for me here at this school."
    "Aha, who am I kidding? I'm a CS kid. No one, girl nor guy, would have interest in me."
    "I'm about to laugh at myself, but just then, I hear a group of four students walk into Coco's and my heart drops."
    "I recognize two of them from OWeek. The other two are their girlfriends... oh crap."
    "They were the same kids that made fun of me for..."
    "well... I need to act fast. They're bound to look this way any second now."

menu:
    "Go back to dorm.":
        "Screw this, I'm going back to CMH now."
        jump dorm
    "Chill out. Talk to them.":
        "Whatever, I can't let people like this get to me."
        "Hell, if they look my way, I might as well talk to them for the fun of it."
        jump darren

label darren:
    "As the group makes their way into the line, the tallest of the bunch - Darren - locks eyes with me for a moment."
    "A smile begins to stretch across his face."
    show darren at right with dissolve
    dar "Hey, it's [name]! What's up, man?"
    "I get up from my seat, toss my empty beverage container into the recycling bin, and make my way over to the group."
    name "Nothing much, just thought I'd chill at Coco's for a bit before everything gets hectic tomorrow."
    dar "All by yourself? C'mon man, that's lame! Where are your friends at?"
    "I begin to think of Alyssa, the only other person I've held a conversation with today."
    name "Yeah, I was with some friends earlier, but they're off somewhere else now."
    dar "Makes sense. Hey, have you met my girlfriend yet?"
    show envgirl at left with dissolve
    "I make eye contact with the brunette wearing her hair braided to the side."
    env "Hi, nice to meet you. I'm Neve."
    "She gives me a friendly smile."
    name "Hi, I'm [name]."

menu:
    "Compliment her hair.":
        $ env_points += 1
        name "Your hair looks really great."
        dar "Woah there, I know she's pretty, but keep it to yourself man."
        "Neve looks away, blushing."
        name "Ahaha, I'm messing with you. You guys are too cute."
        jump party
    "Joke around with her.":
        $ env_points += 1
        name "What's a girl like you doing with a guy like him?"
        "They both laugh."
        dar "You know what they say - love works in mysterious ways."
        name "That's damn right. How long have y'all been together?"
        env "Well, I guess since Grade 10, although we've both had our ups and downs."
        dar "Wouldn't wanna have it any other way."
        "They share a look with each other. Perhaps an affectionate one? I really wouldn't know."
        jump party
    "She has a boyfriend, bro. Say less.":
        name "You guys in the same program?"
        env "Nah, math is definitely not my forte. I'm in Planning!"
        "Oh jeez, an Environment girl. I best be careful."
        name "That's awesome. Your co-op sequences are different though, no?"
        dar "Yeah.. we'll be together for 1A, 1B, and 2A... but after that we'll be apart for a long time."
        env "It sucks, but I think in the long run it'll be better for us to explore our own career paths."
        jump party

label party:
    dar "Anyway man, we're actually planning on hosting a party this Saturday. You down to come?"
    "Party?.. I've never been to anything remotely close to a party."
    "What do I do?"

menu:
    "Go for it. It'll be fun.":
        name "Oh hell yeah, I'm down. Where at?"
        dar "In REV, at 9 pm. Sauce me your number and I'll text you the details."
        name "Sounds good man."
        "We exchange numbers."
        dar "Alright, sick. We're gonna go place an order now. See ya around man."
        name "Take care."
    "School is my main focus right now.":
        name "That sounds nice, but I think I want to narrow my focus onto my school work right now. Sorry."
        dar "No worries man. If you change your mind, you can come by. We'll be in REV."
    "I'm too socially inept for parties.":
        name "Well... I've never really been to a party. My social skills are lacking."
        dar "Bro, you're in Uni now. I'll introduce you to some people, maybe some hot chicks if that's what you're in to."
        "A grin spreads across my face. Maybe this won't be so awful."
        name "Alright, fine, only if I can meet some girls."
        "Darren and Neve both share a laugh with me."
        dar "Awesome, Sauce me your number and I'll text you the details."
        "We exchange numbers."
        dar "Alright, sick. We're gonna go place an order now. See ya around man."
        env "Yeah! I'll introduce you to some of my friends hopefully."
        name "Haha, take care guys."

label dorm:
    scene bg black with fade
    scene bg cmh dorm with fade
    "Ahh, home sweet home. Or at least, close enough."
    "I never really liked being at home anyway. This change feels good, almost too good."
    "I can go, do, and eat whatever and whenever I want. Even sleep whenever I want."
    "And although I should shower first, I'm gonna hit the sheets now. I'm exhausted. My shower can wait."
    scene bg black with fade
    "[name], just like most other teens their age, experiences many {i}real life{/i} issues."
    "For this reason, this game includes content that may be not safe for work (NSFW)."
    "In order to continue reading this story, you must agree to enable NSFW content."
    "Not enabling NSFW will end the story."
    "Would you like to enable NSFW content?"

menu:
    "Enable NSFW content.":
        "You have enabled NSFW content. Enjoy the rest of the game!"
        jump day_1
    "Keep NSFW content disabled.":
        "Click to return to the main menu."
        return

label day_1:
    scene bg sept 7 with fade
    "It's 6 am. My first day as a Waterloo CS student."
    "My first class, Math 135, isn't even until 10:30, but my thoughts kept me awake for most the night."
    "The transition from high school to university is difficult for everyone of course, but I feel that this might be an even bigger challenge for me in particular."
    show bg sc usa
    "You see, I am originally from the United States, born in South Carolina."
    show bg family
    "I spent the first five years of my life living with my mother and father in our small townhouse home."
    "While we were by no means rich, we usually had enough to get by, and as a young child, I couldn't comprehend that there was anything wrong with my living situation."
    "There were times where I would be playing with toys in my room, or watching TV in the living room, or going to grab a snack, or doing anything a small child typically does with their time"
    show bg fighting
    "and I would begin to hear shouting. Doors being slammed. Objects thrown. Crying. Lots of crying."
    "Sometimes I would hide behind a door and watch. Other times I would simply cover my ears and distract myself with other activities."
    "This was normal for me."
    "But everything changed the day of the accident."
    show bg july 5th
    "July 5th, 2005, is a day I will remember forever."
    "I was sitting on my bedroom floor, flipping through the pages of the picturebook my mother had signed out for me from the library earlier that day"
    "when I began to hear my parents break into yet another fight, this time in the kitchen while my mother was preparing dinner."
    show bg money
    "As I grew older, I came to know that they were arguing over money."
    "My father was a gambling addict, and with rent long overdue, my mother was demanding from him the monthly payment."
    "The arguing went on for what felt like hours."
    "I had never heard my mother this angry in all of my life before. I just wanted this to be over."
    "An ear-piercing shriek."
    "Crying."
    show bg murder
    "I bolted down the stairs to discover a butcher knife planted deep inside my father's chest."
    "My mother, knife in her hand, kneeling over my father, both in a pool of blood."
    "I began to cry and shout, but my mother took almost no notice of me, being in her own hysterical bubble, realizing what she had just done in an act of anger."
    "And so, I did what I was always told to do if someone was hurt - I called 911."
    show bg crime
    "My father was announced dead at the scene, and my mother was charged with murder in the first degree just days after."
    show bg plane
    "With no relatives here in South Carolina, I was made to leave everything behind and live with my mom's brother in the city of Lloydminster, in Alberta, Canada."
    "My Uncle Chase had no wife nor kids, and I had never even met him prior to the accident, but here I was, being put in his care for the rest of my childhood."
    "There was a long journey ahead of me."
    scene bg black

if ma_points > 0:
    label text_message:
        "I hear my phone vibrate on the desk beside me and open my eyes."
        scene bg holding_phone with fade
        "I have a... text?"
        "Oh! It's from Alyssa!"
        "\"Hey [name]! Just wanted to wish you good luck on your first day of classes. If you need anything, let me know.
        \n - Alyssa\""

        "This message should make me feel good. There is someone actively watching out for me."
        "Yet, still, I feel uneasy when I go to reply to her text."
        "After all, why is she even doing this?"
        "I'm just another student at this god forsaken university."
        "Does she feel good about herself for helping someone like me?"
        "Whatever."

    menu:
        "Respond to her text.":
            $ ma_points += 1
            "\"Thanks Alyssa. Want to meet up later today?\""
            "I hope that's not a weird response."
            "Either way, I don't expect this to go anywhere, but it would be nice to have a familiar face for the first CTRL-A meeting."
            "Anyway, I still need to shower. I don't want to be the stereotypical CS kid first day in."
            jump first_class
        "Forget it. Take a shower.":
            "I don't have time for this. I'm going to take my shower and get ready for class."
            jump first_class

else:
    label alarm:
        "I wake up to the sound of my 7 am alarm."
        "Did I really just spend the last hour plauged with thoughts of the past?"
        "Oh well. There is nothing I can do now. There was never a single thing I could do."
        "Today is the big day. I need to take a shower first, so that's what I'll do."



label first_class:
    scene bg outside
    "Okay. First class done. Not too bad."
    "We only really went over introductory content of course, but I have high hopes for this course."
