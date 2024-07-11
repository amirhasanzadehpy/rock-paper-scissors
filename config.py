GAME_CHOICES = ('r', 'p', 's')

RULES = {
    ('p', 'r'): 'p',
    ('p', 's'): 's',
    ('r', 's'): 'r',
}

MATCH_ELEMENT = {
    'r': 'rock 🪨',
    'p': 'paper 📃',
    's': 'scissors ✂️',
}

SCOREBOARD = {
    'user': 0,
    'system': 0
}
