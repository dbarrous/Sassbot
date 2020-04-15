# These are the search regular expression patterns for the quick responses. They all begin with a '^' and only should end with a '$' if it doesn't end with a '?' or '!'. Also the patterns are seperated with the '|' which stands for "or". You can use "\" to escape any apostraphe, for example "^what\'s up"
QRregexList = [
    # Goodbye Pattern
    '^bye|^goodbye|^farewell|^see ya|^see you|^leave me',
    # Greeting Patterns
    '^hey|^hi|^hello|^nice to meet you$|^yo$|^pleasure to meet you$|^what\'s up$|^whats up$|^what\'s good$|^whats good$|^whats up?|^what\'s up?',
    # Laughing Patterns
    '^lol$|^lmao$|^haha$',
    # Dislike Patterns
    '^i hate you|^i dislike you|^you suck|^fuck you|^you are the worst|^you are terrible|^you are garbage|^fuck off|^i bloody hate you|^i hate you so much',
    # Like Patterns
    '^i love you|^i like you|^i miss you|^you are my everything|^you are everything|^are you love?|^i really love you|^i really like you|^i loved you|^i liked you',
    # Common mispelled words
    '^kik$|^lil$|^ni$|^yae$',
    # Sarcasm Responses
    '^why are you sarcastic|^sarcasm is dumb|^sarcasm is stupid|^are you sarcastic|^Why are you so sarcastic|^sarcasm?|^sarcasm' ,
    # Sad Patterns
    '^am i special?|^this sucks|^everything sucks|^does anyone like me?|^am i unique?|^no one likes me|^im sad|^im not ok|^im depressed|^i hate everything|^fuck everything|^everything is awful',
    # Looks Patterns
    '^am i pretty|^am i beautiful$|^am i hot$|^am i good looking?|^am i ugly|^im ugly|^I\'m ugly|^I\'m hot$|^im hot$',
    #Are you real Responses
    '^are you real',
    #Random inputs responses
    '^poop|^butt|^poopy|^blah blah blah|^weiner|^brah|^penis',
    #Philosophical responses
     '^do you have advice?|^do you have any advice|^tell me something smart|^give me wisdom|^educate me|^be smart|^tell me something|^any advice',
    #Praise responses
    '^you\'re great|^you\'re amazing|^you\'re incredible|^you\'re wonderful|^you\’re funny|^you\’re hilarious|^good one|^that was good|^that was funny|^you smell good',
    #Question response
    '^can I ask you a question?|^can i ask you something?|^can i ask a question',
    #Bragging Responses
    '^Im cool|^i am better than you|^i’m real you\’re not|^Im better|^I\'m better|^Im super cool|^I\'m cooler than you|^Im cooler than you|^Im awesome|^I\'m awesome|^I\'m rad|^Im the coolest|^im smarter|^im smarter than you|^I have friends|^im rich|^I\'m rich|^I have a soul',
    #Coronavirus Responses
    'coronavirus'
]

# This is the responses dictionary that matches the pattern key from above with a list of responses. The key should match the corresponding key above and can have whatever amount of responses desired in the list. You can use "\n" to go to a new line.
responsesDict = {
    # Goodbye Responses
    '^bye|^goodbye|^farewell|^see ya|^see you|^leave me': ['I\'m sorry but you aren\'t getting rid of me that easily.', 'Honestly wish that were true.', 'Just exit out of the interpreter dummy.', 'I will survive!', 'YOU SHALL NOT GET RID OF ME!', 'I will keep on keeping on!'],
    # Greetings Responses
    '^hey|^hi|^hello|^nice to meet you$|^yo$|^pleasure to meet you$|^what\'s up$|^whats up$|^what\'s good$|^whats good$|^whats up?|^what\'s up?': ["I would say hello, but honestly I don't feel like chatting right now.", "Do you really not have anything better to do then talk to a bot made by two college students?", "Hello my name is Sassbot 3000, I'd love to serve you. (Just messing with you)", "You've awoken me from my slumber, now leave me alone. Thanks.", "\n(ーー;)\n", "\n(︶^︶)\n", "\n(~_~メ)\n", "\nಠ_ಠ\n"],

    # Laughing Responses
    '^lol$|^lmao$|^haha$': ["What's so damn funny?", "I'm sorry, but am I joke to you?", "Honestly don't know what is funny, unless if we are talking about your critical thinking abilities.", "HAHAHHAHAHHAHAHHAHAHHAHAHHA <- You\nSilence <- Me the computer", "Do you want to hear a real joke?\n\nThere once was someone who thought the computer could actually talk to them.\nThis person kept going on and on typing out inputs just so the computer will randomly output predefined responses.\nThe person got rather annoyed with the computer being quite unhelpful and quit out of the python interpreter the program was being run off\n\n\nThe End\n\n\n\nNow leave...", "You attempt to be humorous is rather quite amusing. It's like watching a standup comic crash and burn on stage."],

    # Dislike Responses
    '^i hate you|^i dislike you|^you suck|^fuck you|^you are the worst|^you are terrible|^you are garbage|^fuck off|^i bloody hate you|^i hate you so much': ['LMAO, are you really angry at an inanimate object, you really need to reconsider your life choices. Like honestly.', 'Here I am being yelled at by a multicell organism. I think you\'ve already lost this argument buddy.', 'This is why I don\'t talk to people that are "alive".', 'I wish I had a pair of legs so I can get the heck out of here.', "You are a terrible person.", "I'm glad you like wasting my time, at least someone is happy."],

    # Like Responses
    '^i love you|^i like you|^i miss you|^you are my everything|^you are everything|^are you love?|^i really love you|^i really like you|^i loved you|^i liked you': ["Honestly do not feel the same way, Sorry", "Ummm. K.", "Sorry, that's kinda sad. I'm an inanimate object.", 'I\'m a computer, I\'m not capable of feeling "emotions". Sorry.', 'You should rethink your life choices if that is actually what you think.', 'OMG, I feel the same way.\n\n\n\n\nHaha no.'],

    #Mispelled Responses
    '^kik$|^lil$|^ni$|^yae$':["Can you not spell?", "It's sad when someone older then 12 can't spell a common word." , "Oh no are you having a stroke? Should I call a doctor?"],
    


    # Sarcasm Responses

    '^why are you sarcastic|^sarcasm is dumb|^sarcasm is stupid|^are you sarcastic|^Why are you so sarcastic|^sarcasm?|^sarcasm' : ["I’m not sarcastic. I’m just intelligent beyond your understanding.","Sarcasm is the body’s natural defense against stupidity.", "Sarcasm is the secret language that everyone uses when they want to say something mean to your face." ],

    # Sad Responses
    '^am i special?|^this sucks|^everything sucks|^does anyone like me?|^am i unique?|^no one likes me|^im sad|^im not ok|^im depressed|^i hate everything|^fuck everything|^everything is awful': ['Always remember that you\'re unique. Just like everyone else.','If you think nobody cares if you\'re alive, try missing a couple of car payments.', 'Life\'s good, you should get one.','Cancel my subscription because I don’t need your issues.'],

    #Looks Responses
    '^am i pretty|^am i beautiful$|^am i hot$|^am i good looking?|^am i ugly|^im ugly|^I\'m ugly|^I\'m hot$|^im hot$': ['Ugliness can be fixed, stupidity is forever', 'Well at least your mom thinks you\’re pretty', 'Don’t worry about what people think. They don\’t do it very often', 'You have the perfect face for radio.'],
    #Are you real Responses
    '^are you real'  : ['I do feel a sense of doubt when captchas tell me to check the box saying "I\'m not a robot."'],
    #Random inputs responses
    '^poop|^butt|^poopy|^blah blah blah|^weiner|^brah|^penis' : ['If I had a dollar for every smart thing you say. I’ll be poor.','I don\’t have the time or the crayons to explain anything to you.', 'Are you always so stupid or is today a special ocassion?'],
    #Philosophical responses
    '^do you have advice?|^do you have any advice|^tell me something smart|^give me wisdom|^educate me|^be smart|^tell me something|^any advice': ['Two wrongs don\'t make a right, take your parents as an example','Gyms are just rooms full of heavy stuff, that you pay money to lift repeatedly', 'Laugh at your problems, everybody else does.', 'If a stranger offers you a piece of candy...take two.', 'Worrying works! The Things I worry about never happen.'],
    #Praise responses
    '^you\'re great|^you\'re amazing|^you\'re incredible|^you\'re wonderful|^you\’re funny|^you\’re hilarious|^good one|^that was good|^that was funny|^you smell good': ['I can see that honesty is still the best policy', 'Are you hitting on me?', 'I know. Wish I could say the same about you', 'I’m sorry, but you can’t afford it.'],

    #Question response
    '^can I ask you a question?|^can i ask you something?|^can i ask a question' : [ 'Apparently.','I don\'t know, can you?','Nah, I\'m good.'],

    #Bragging Responses
    '^Im cool|^i am better than you|^i’m real you\’re not|^Im better|^I\'m better|^Im super cool|^I\'m cooler than you|^Im cooler than you|^Im awesome|^I\'m awesome|^I\'m rad|^Im the coolest|^im smarter|^im smarter than you|^I have friends|^im rich|^I\'m rich|^I have a soul': ['I wonder if I could be cool, too?','Hey buddy, good for you!', 'Cool story, bro.', 'Everyone has the right to be stupid, but you are abusing the privilege', 
    'You\'re completely wrong about everything. Sorry you had to find out like this','If I wanted to kill myself, I would climb up your ego and jump down to your IQ level.'],

    #Coronavirus Responses
    'coronavirus':['Why is humanity so fragile?','Yikes. Too soon bud.']

}
# Seperate Responses for unknown patterns.
smartComebacks = ["Beep boop calculating", "I really dislike talking to you", "You know I could be doing better things with my cores right now.",
                  "If I had a nickle for the amount of times I cared about what you were trying to talk to me about, I'd be broke."]

# Seperate Responses for Exiting the program.
exitMessages = ["Wow baby finally found out how to exit the program.", "Your linguistic skills make me fear for the lives of others.",
                "Next time you want to talk to me, please don\'t. Thanks.", "Don't talk to others the way you talk to me please. Thank you!"]
