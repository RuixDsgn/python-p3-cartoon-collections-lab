def roll_call_dwarves(names):
    for i, name in enumerate(names, start=1):
        print(f"{i}. {name}")

def summon_captain_planet(lists):
    planateer_calls = [f"{list.title()}!" for list in lists]
    
    return planateer_calls

def long_planeteer_calls(string_list):
    for list in string_list:
        if len(list) > 4:
            return True
    else:
        return False

def find_the_cheese(foods):
    for food in foods:
        if "cheddar" in foods:
            return "cheddar"
        elif "gouda" in foods:
            return "gouda"
        elif "camembert" in foods:
            return "camembert"
        else:
            return None
