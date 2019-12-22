# Imports
import random
# Generate Character


class character:
    def __init__(self):
        self.background = None
        self.year = 0
        self.house = None
        self.finesse = 0
        self.intelligence = 0
        self.power = 0
        self.spirit = 0
        self.masteries = None
        self.flaw = None
        self.wand = None
        self.perks = None

# Name randomized Online


# Houses
houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']


def selectHouse(houses):
    return random.choice(houses)


# years
year = random.randint(1, 7)

# Attributes
attribute_points = 3
finesse = 1
intelligence = 1
spirit = 1
power = 1
# Increase attribute points by the year of the student
if(year > 1):
    attribute_points += (year - 1)

background = random.choice(
    ['Wizard-Raised Halfblood', 'Muggle-Raised halfblood', 'Muggleborn', 'Pureblood'])
school_credits = 0
perks = 0
if(background == 'Wizard-Raised Halfblood'):
    school_credits = 2
elif(background == 'Muggle-Raised halfblood'):
    school_credits = 2
elif(background == 'Muggleborn'):
    houses.remove('Slytherin')
    perks = 1
else:
    school_credits = 3

house = selectHouse(houses)

# Distribute attribute points
attributes = ['Finesse', 'Intelligence', 'Spirit', 'Power']
while(attribute_points > 0):
    temp_attribute = random.choice(attributes)
    if(temp_attribute == 'Finesse'):
        finesse += 1
    elif(temp_attribute == 'Intelligence'):
        intelligence += 1
    elif(temp_attribute == 'Spirit'):
        spirit += 1
    else:
        power += 1
    attribute_points -= 1

# Masteries
# General Masteries
masteries = []
flaw = ''
general_masteries = ['Charms', 'Transfiguration', 'Potions',
                     'Defense', 'Dark Arts', 'Metamorph',
                     'The Gift', 'Flawed', 'Curse-Breaking']

special_masteries = ['Creature', 'Herbology', 'Spell-Making',
                     'Flying', 'History', 'Perception',
                     'Research', 'Enchanting', 'Healing',
                     'Ward', 'Mischief']

choice_mastery = random.choice(['General', 'Special'])
if(choice_mastery == 'General'):
    temp_choice = random.choice(general_masteries)
    # If the first choice is flawed, the character should then have
    # a general master and a special mastery, and one general mastery as their flawed mastery
    if(temp_choice == 'Flawed'):
        masteries.append(temp_choice)
        # Remove Flawed, the Gift, and Metamorph
        general_masteries.remove(temp_choice)
        general_masteries.remove('The Gift')
        general_masteries.remove('Metamorph')
        temp_choice = random.choice(special_masteries)
        masteries.append(temp_choice)
        temp_choice = random.choice(general_masteries)
        masteries.append(temp_choice)
        flaw = random.choice(general_masteries)
else:
    # if their choice master is special, they should have two special masteries then
    # It is possible to choose the same special mastery twice, so no need to remove
    for i in range(1, 3):
        temp_choice = random.choice(special_masteries)
        masteries.append(temp_choice)


# Choosing perks
# For every point they have in spirit, they should select one perk
perks += spirit
perk_list = ['A Pretty Face', 'A Way With Wands', 'Can I Borrow Your Notes?',
             'Dont Sweat the Small Stuff', 'Finders Keepers', 'Free Tutoring',
             'Hack Job', 'Home Study', 'Ive Been Everywhere', 'I Know A Guy', 'I Owe You One',
             'Its Okay My Friends a Goblin', 'Practiced Procrastinator', 'Rich in the Ways that Mattered',
             'Summer Chores', 'Teachers Pet', 'Tussle Hardened', 'Up Close and Personal',
             'Well Connected', 'You Wouldnt Hit A Face Like Mine']
chosen_perks = []

# Because a large portion of these perks can be selected more than once,
# I'm only going to confirm the logic as only each perk being selectable once
# might make sense to contain perks as an object?
for i in range(perks):
    temp_perk = random.choice(perk_list)
    chosen_perks.append(temp_perk)
    perk_list.remove(temp_perk)


# Wands
# There are three factors to wands: The Wood, Core, and Length
wood_types = ['Beech', 'Apple', 'Ash', 'Alder', 'Willow',
              'Hawthorn', 'Oak', 'Holly', 'Hazel', 'Vine']
core_types = ['Unicorn Hair', 'Dragon Heartstring', 'Phoenix Feather',
              'Augurey Fether', 'Veela Hair', 'Clabbert Horn',
              'Jarvey Tendon', 'Erumpent Hair', 'Fwooper Feather',
              'Kelpie Hair']
lengths = ['8 1/2"', '9"', '9 1/2"',
           '10"', '10 1/2"', '11"',
           '11 1/2"', '12"', '12 1/2"',
           '13"']

wand = {
    "wood_type": random.choice(wood_types),
    "core_type": random.choice(core_types),
    "Length": random.choice(lengths)
}
# Since this is for NPCs, I'm not sure if I need to keep track of modifiers,
# As I can reference the rule book when needed
# modifiers = {}
# for i in range(len(masteries)):
#     if(masteries[i] == 'Charms'):
#         modifiers.charms = 1
#     elif(masteries[i] == 'Transfiguration'):
#     elif(masteries[i] == 'Potions'):
#     elif(masteries[i] == 'Defense'):
#     elif(masteries[i] == 'Dark Arts'):
#     elif(masteries[i] == 'The Gift'):

npc = character()
npc.year = year
npc.background = background
npc.house = house
npc.finesse = finesse
npc.intelligence = intelligence
npc.spirit = spirit
npc.power = power
npc.masteries = masteries
if(flaw != ''):
    npc.flaw = flaw
npc.perks = chosen_perks
npc.wand = wand
print(npc.__dict__)
