import pprint

#Read all Spells
with open('input/spells.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
spells = dict()
lineno = 0
currentName = "asd"
for line in content:
    if (line.find('[level') != -1):
        lineno = 0
        name = line.split('[level')[0].rstrip()
        lvl = line.split('[level')[1].replace("]", "").lstrip()
        spells[name] = {'lvl': lvl}
        currentName = name
    else:
        lineno = lineno+1
        if lineno == 1:
            spells[currentName]["name"] = currentName
            spells[currentName]["casters"] = "NONE"
            spells[currentName]['school'] = line
        if lineno == 2:
            spells[currentName]['castingtime'] = line.replace(
                "Casting Time:", "")
        if lineno == 3:
            spells[currentName]['range'] = line.replace("Range:", "")
        if lineno == 4:
            #TODO Material: Components: V, S, M (empty egg shell)
            spells[currentName]['components'] = line.replace("Components:", "")
        if lineno == 5:
            spells[currentName]['duration'] = line.replace("]", "")
        if lineno == 6:
            spells[currentName]['desc'] = line
        if lineno > 6:
            description = spells[currentName]['desc'] + \
                "\n" + line.replace("]", "")
            spells[currentName]['desc'] = description
pp = pprint.PrettyPrinter(indent=2, width=1000)
#Read all Casters
with open('input/casternames.txt') as f:
    casternamesFile = f.readlines()
casternamesFile = [x.strip() for x in casternamesFile]

casters = dict()
casterNames = []
for line in casternamesFile:
    casterNames.append(line)
    
casterNames.append("MAX")
pp.pprint(casterNames)

#TODO: Store which spells can be accessed
with open('input/spellist.txt') as f:
    spelllistFile = f.readlines()
spelllistFile = [x.strip() for x in spelllistFile]

currentCasterIndex = 0
for line in spelllistFile:
    #check if the next caster section begins
    if casterNames[currentCasterIndex+1] in line:
        currentCasterIndex = currentCasterIndex+1
    #add caster to spell
    for spellname in spells.keys():

        if spellname in line:
            if spells[spellname]["casters"] == "NONE":
                spells[spellname]["casters"] = casterNames[currentCasterIndex]
            else:
                if casterNames[currentCasterIndex] not in spells[spellname]["casters"]:
                    spells[spellname]["casters"] = spells[spellname]["casters"] + ", " + casterNames[currentCasterIndex]

for spellname in spells.keys():
    print(spells[spellname]["name"] + ": " + spells[spellname]["casters"])


 
#pp.pprint(spells)










#TODO: Edit main Spell XMLs

# mask for class Names
# \(([A-Z]{3}?)\)
'''
spellExample = {
    'Slumber': {
        'classes' : 'Druid, Shaman',
        'castingtime': ' 1 action',
        'components': ' V, S',
        'description': 'This spell sends a willing creature that can sleep into magical sleep. The caster may designate up to three conditions to cause the sleeper to wake up (such as after 24 hours, when a horn is blown, etc.), but only conditions the sleeping target would be able to perceive should they be awake. If resting as part of this slumber, any hit dice the sleeper spends to heal themselves can be rolled again, taking the higher result.\nWhile resting this way, the sleeper does not age, and all poisons, curses, and diseases are suspended (they continue acting once the sleeper awakens).\nHeightened. When you cast this spell using a higher level spell, the maximum duration increases, according to the below.\n24 hours - 10 days - 30 days - 1 year and a day - 20 years - 200 years.\nSpecial. This spell can be cast while in a druidâ€™s wild shape.\n',
        'duration': 'Duration: Up to 24 hours.',
        'lvl': '3',
        'range': ' Touch',
        'school': 'Enchantment'},
}

classExample = {
    "Alchemist": {
        {
            "hd": 8,
            "proficiency": "Intelligence, Stamina",  # 44
            "spellAbility": "Intelligence",  # 94
            "spellLvl": [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9, 9],
            "slots": {
                "1": "0,0,0,0,0,0",
                "2": "0,0,0,0,0,0",
                "3": "0,2,0,0,0,0",
            },
            "progression": {
                "1": {
                    "Starting Proficiencies": "text",
                    "Starting Equipment": "You start with the following equipment, in addition to the equipment granted by your background:\n•	(a) chain mail or (b) leather, longbow, and 20 arrows\n•	(a) a martial weapon and a shield or (b) two martial weapons\n•	(a) a light crossbow and 20 bolts or (b) two handaxes\n•	(a) a dungeoneer’s pack or (b) an explorer’s pack",
                    "SPECIAL FEATURES": "special feature asdasd",
                    "optional": {
                        "1": "1",
                        "2": "2",
                    }
                }
            }
        }
    }
}

raceExample = {
    "Draenei": {
        "size": "M",
        "speed": "30",
        "ability": "Your Spirit or Intelligence increases by 1.",
        "traits": {
            "Fel Resistance": "You have resistance to fel damage",
            "Heroic Presence": "You can spend 10 minutes inspiring your companions, shoring up their resolve to fight. When you do so, choose up to six friendly creatures (which can include yourself) within 30 feet of you who can see or hear you and who can understand you. Each creature can gain temporary hit points equal to your level + your Charisma or Spirit modifier. A creature can’t gain temporary hit points from this feat again until it has finished a short or long rest. If you spend Inspiration when using Heroic Presence, creatures can benefit multiple times from the temporary hit points (so long as there is Inspiration to spend), but it does not stack. Alternatively, you may declare use of this ability upon landing a critical hit. The range remains the same. ",
            "Languages": "You can speak, read, and write Common and Eredun. The Eredun Draenei speak is an altered dialect that is less corrupt, and thus does not impose penalties when speaking, but is perfectly understandable by fiends.",
        }
    }
}
'''
