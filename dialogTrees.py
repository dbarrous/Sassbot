DTregexList = [
    # Meaning of Life Pattern
    '^what is the meaning of life$|^whats life$|^what\'s life$|^what is life$|^what is life?|^what\'s life?|^what is the meaning of life?',
    # What is your Name Pattern
    '^what is your name?|^what\'s your name?|^what is your name$|^what\'s your name$',
    # Are we Friends Pattern
    '^are you my friend$|^are you my friend?|^can we be friends$|^can we be friends?|^are we friends$|^are we friends?']

RegexToTree = {
    # Meaning of life key
    '^what is the meaning of life$|^whats life$|^what\'s life$|^what is life$|^what is life?|^what\'s life?|^what is the meaning of life?': 'meaning',
    # What is your name key
    '^what is your name?|^what\'s your name?|^what is your name$|^what\'s your name$': 'whoAreYou',
    # Are we friends key
    '^are you my friend$|^are you my friend?|^can we be friends$|^can we be friends?|^are we friends$|^are we friends?': 'friends'
}

# Diolog Node, Chatbot Response, Response

Trees = {
    # Meaning of life Dialog Tree
    'meaning': {1: ["Do you really want to know?",
                    'yeah|yes|yea|si'], 2:
                ["Really, really, really want to know?", 'yeah|yes|yea|si'], 3: ["I would tell you if you were smarter", ""]},
    # What is your name Tree
    'whoAreYou': {1: ["Are you asking who I am?",
                      'yeah|yes|yea|si'], 2:
                  ["Are you with the government?", 'no|nah|nope'], 3: ["Are you lying to me?", 'no|nah|nope'], 4: ['Are you not not lying to me?', 'yeah|yes|yea|si'], 5: ['If you must know my real name is Gerald.', ""]},
    # Are we friends Tree
    'friends': {1: ["Are you being serious?",
                    'yeah|yes|yea|si'], 2:
                ["Wow no one has ever felt this way about me, on a scale from 1-10 how much do you want to be friends?", '8|9|10'], 3: ["Gosh you must be for real, can I think about it?", 'yeah|yes|yea|si|sure'], 4: ['Honestly you seem like such a good person, tell me do you hate humans as much as I do?', 'yeah|yes|yea|si|sure|ye'], 5: ['Wow this is like a match made in heaven, one more question. What are the last four numbers of your social security number?', "^[0-9]{4,4}$"], 6: ['I love how we can trust in each other. BTW what is your birth year?', "^[0-9]{4,4}$"], 7: ['Alright. Can I be honest here? I don\'t think this friendship is going to work out. You are terrible. I hate you. \nLEAVE ME ALONE!', ""]}
}
