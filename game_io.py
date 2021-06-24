import globals
import json
from os import path

def load_Q():
    if (path.exists("npc_data.json")):
        with open("npc_data.json", "r") as infile: 
            globals.Q = json.loads(infile.read())
        print("Loaded Q: ", globals.Q)
    else:
        globals.Q = {}
        
def save_Q():
    with open("npc_data.json", "w") as outfile: 
        json.dump(globals.Q, outfile)
