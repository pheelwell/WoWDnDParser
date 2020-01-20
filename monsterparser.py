import docx
import pprint

#this script is still broken, since it doesn't store in which order monsters are.
#since this is mid developement I need to think more about it.

currentMonster= "ERROR" #store the current monster name
currentAttribute= "ERROR" #store the current Attribute name
wasM1=False #store if last item as a monster name
wasS=False #store if last item as a monster name
monsters=dict() #monster dict

doc = docx.Document('input/monsters_marked.docx')
for para in doc.paragraphs:
    for run in para.runs:
        if run.style.name == "M1 Zchn" or run.style.name == "M2 Zchn": #does the run have the monster formatting?
            if not wasM1: #assume it is a new monster
                currentMonster = run.text
                currentAttribute = "SiTyAl" # after a monster name there are infos about size alignment and type
                wasM1 = True
                monsters[currentMonster]= {'name': run.text,'SiTyAl': ""}
            else:#assume it is the same monster
                monsters[currentMonster+run.text] = monsters.pop(currentMonster) #update data
                currentMonster = currentMonster+run.text #update key
                monsters[currentMonster]["name"]= monsters[currentMonster]["name"] + run.text 
            wasM1 = True
        else: #if not M1 style, its not a monster name
            wasM1 = False
        
        if run.style.name == "S Zchn": #are we in a attribute?
            if not wasS: #assume it is a new Attribute
                currentAttribute = run.text
                wasS = True
                monsters[currentMonster][currentAttribute]= ""
            else:
                monsters[currentMonster][currentAttribute+run.text] = monsters[currentMonster].pop(currentAttribute) #map data
                currentAttribute = currentAttribute+run.text #update key
                monsters[currentMonster][currentAttribute]= ""
        else: #if not S style, its not a Attribute name
            wasS = False
        if run.style.name == "Default Paragraph Font": #are we in a attribute?
            monsters[currentMonster][currentAttribute]=monsters[currentMonster][currentAttribute]+ run.text #append text of current Attribute



pp = pprint.PrettyPrinter(indent=2, width=1000)

pp.pprint(monsters)
#TODO
#last paragraph is description
#ACTIONS /Traits/Spellcasting/LEGENDARY ACTIONS 
#build Json for Export



#spell:
#get https://www.worldanvil.com/heroes/sheet/choose?templateId=19&is_character=false
#Creature:
#get https://www.worldanvil.com/heroes/sheet/choose?templateId=21&is_character=false
#Race:
#get https://www.worldanvil.com/heroes/sheet/choose?templateId=23&is_character=false
#Class Feature:
#get https://www.worldanvil.com/heroes/sheet/choose?templateId=25&is_character=false

#in response: "location: /heroes/sheet/290806/edit
#after that: edit: https://www.worldanvil.com/heroes/sheet/XXXXXX/edit

'''
name: Testname
cr: TestCR
types: Testtypes
size: Tiny
languages: TestLanguage
alignment: Any Chaotic
description: TestDescription
suggestedenvironment: TestSuggestedEnvironments
ac: Test Armor Class 12
hitpoints: Test HP 14hp (2d8+4) [roll:2d8+4]
strength: 4
dexterity: -3
constitution: 5
intelligence: 4
wisdom: -1
charisma: 10
movement: 123
fly: 124
hover: 22
burrow: 123
swim: 51
climb: 108
senses: TestSenses
skills: TestSkills
savingthrows: TestSavingThrows
damagevulnerabilities: TestDamageVulnerabilities
damageresistances: TestDamageResistances
damageimmunities: TestDamage Immunities
conditionimmunities: TestCondition Immunities
spellcasting: TestSpellcasting
atwill: Test Cast at will
onceperday: Test Cast one per day
twiceperday: test Cast twice per day
thriceperday: Test Cast thrice per day
specialabilities: Test Special Abilities
actions: test Actions
reactions: test Reactions
legendaryactions: Test [b]Reactions[/b]
lairdescription: Test Lair Description
lairactions: test Lair Actions
regionaleffects: test Regional Effects
image: 123
tabledata: Test Table Data
tags: 
isShared: 1
templateId: 21
blockId: 290813
tags: Test Tag, Tag 2, Tag 3
'''