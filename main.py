from random import randint

monster_list = []

player = {
    "name":"Lucas",
    "level": 1,
    "exp":0,
    "expMax":50,
    "dmg":25,
    "hp":100,
    "hp_max":100,

}

prompt = input("Prompt:")


def create_monster(level):
    new_npc = {
        
        "name": f"Monster #{level}",
        "level": level,
        "dmg": 5 * level,
        "hp": 100 * level,
        "hp_max": 100 * level,
        "exp_give": 25 * level,
    }


    monster_list.append(new_npc)
    



def gen_monster(n_monster):
    for x in range(n_monster):
        create_monster(x + 1)


def show_npcs():
    for npcs in monster_list:
        print(npcs)

#attack_npc() hp:npc - plr:dmg
#attack_plr() plr:dmg - hp:npc


def show_fight_info():
    print(f'player HP:{player["hp"]} // {selected_npc["name"]} HP:{selected_npc["hp"]}')
    print(f'Attacked NPC: {selected_npc["name"]}')

def attack_npc(npc):
    npc["hp"] = npc["hp"] - player["dmg"]



def attack_plr(npc):
    player["hp"] = player["hp"] - npc["dmg"]


def startbattle():
    attack_npc(selected_npc)
    attack_plr(selected_npc)
    show_fight_info()




gen_monster(5)
selected_npc = monster_list[0]

if prompt == "start":
    startbattle()