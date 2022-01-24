"""
Name(s): Anjali Ravichandra
Name of Project: Pokemon Battle
"""

#Write the main part of your program here. Use of the other pages is optional.

import random 
user_name = input(str("What do you want to call yourself: "))

user_pokemon = input("Choose what pokemon in your party, Metagross, Arcanine, Greninja ")




Metagross = [247,175,238,166,130,270]
Greninja = [175,189,125,132,224,254]
Arcanine = [202,184,148,148,175,290]
#stats{attack, spattack, defense, special defense, speed, hp
def extreme_speed():
  extreme_speed_damage = int(((((2 * 100)/5) + 2) * 80 * (user_pokemon[0]/comp_pokemon[2])/50) + 5) 
  return(extreme_speed_damage) 

def flare_biltz():
  flare_biltz_damage = int(((((2 * 100)/5) + 2) * 120 * (user_pokemon[0]/comp_pokemon[2])/50) + 5) 
  return(flare_biltz_damage)

def wild_charge():
  wild_charge_damage = int(((((2 * 100)/5) + 2) * 90 * (user_pokemon[0]/comp_pokemon[2])/50) + 5) 
  return(wild_charge_damage)

def crunch():
  crunch_damage = int(((((2 * 100)/5) + 2) * 90 * (user_pokemon[0]/comp_pokemon[2])/50) + 5) 
  return(crunch_damage)

def hydro_pump():
  Hydro_pump_damage = int(((((2 * 110)/5) + 2) * 90 * (user_pokemon[0]/comp_pokemon[2])/50) + 5) 
  return(Hydro_pump_damage)

def dark_pulse():
  dark_pulse_damage = int(((((2 * 80)/5) + 2) * 90 * (user_pokemon[0]/comp_pokemon[2])/50) + 5) 
  return(dark_pulse_damage)

def ice_beam():
  ice_beam_damage = int(((((2 * 80)/5) + 2) * 90 * (user_pokemon[0]/comp_pokemon[2])/50) + 5) 
  return(ice_beam_damage)

def extrasensory():
  extra_sensory_damage = int(((((2 * 90)/5) + 2) * 90 * (user_pokemon[0]/comp_pokemon[2])/50) + 5) 
  return(extra_sensory_damage)

def meteor_mash():
  meteor_mash_damage = int(((((2 * 90)/5) + 2) * 90 * (user_pokemon[0]/comp_pokemon[2])/50) + 5) 
  return(meteor_mash_damage)

def earthquake():
  earthquake_damage = int(((((2 * 100)/5) + 2) * 90 * (user_pokemon[0]/comp_pokemon[2])/50) + 5) 
  return(earthquake_damage)

def zen_headbutt():
  zen_headbutt_damage = int(((((2 * 80)/5) + 2) * 90 * (user_pokemon[0]/comp_pokemon[2])/50) + 5) 
  return(zen_headbutt_damage)

def ice_punch():
  ice_punch_damage = int(((((2 * 75)/5) + 2) * 90 * (user_pokemon[0]/comp_pokemon[2])/50) + 5) 
  return(ice_punch_damage)

Metagrossmoves = ["ice punch", "zen headbutt", "earthquake", "meteor mash"]
Greninjamoves = ["extrasensory", "ice beam", "hydro pump", "dark pulse"]
Arcaninemoves = ["extreme speed", "flare biltz", "wild charge", "crunch"]

if user_pokemon in ("Metagross", "metagross"):
  print("You sent out Metagross")
  user_pokemon = Metagross
  user_pokemon_name = "Metagross"
  userhp = Metagross[5]
  comp_pokemon = Arcanine
  comphp = Arcanine[5]
  comp_pokemon_name = "Arcanine"
  print("Metagross's hp is ", userhp)
if user_pokemon in ("Arcanine", "arcanine"):
  print("You sent out Arcanine")
  user_pokemon = Arcanine
  user_pokemon_name = "Arcanine"
  userhp = Arcanine[5]
  comp_pokemon = Greninja
  comphp = Greninja[5]
  comp_pokemon_name = "Greninja"
  print("Arcanine's hp is ", userhp)
if user_pokemon in ("Greninja", " greninja"):
  print("You sent out Greninja")
  user_pokemon = Greninja
  user_pokemon_name = "Greninja"
  userhp = Greninja[5]
  comp_pokemon = Metagross
  comphp = Metagross[5]
  comp_pokemon_name = "Metagross"
  print("Greninja's hp is ", userhp)

while userhp > 0 and comphp > 0: 
    if user_pokemon_name in ("Arcanine", "arcanine"):
      usermove = input("What do you want to do: \n Extreme Speed, Flare Biltz, Wild Charge, Crunch ")
      if usermove in ("Extreme Speed", "extreme speed"):
        print(user_pokemon_name, "used", usermove)
        comphp = comphp - extreme_speed()
        print(comp_pokemon_name, "hp is", comphp)
        compmove = random.choice(Greninjamoves)
        if compmove in ("hydro pump") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * hydro_pump())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("ice beam") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_beam()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("extrasensory") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - extrasensory()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("dark pulse") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - dark_pulse()
          print(user_pokemon_name, "hp is", userhp)
      if usermove in ("Flare Biltz", "flare biltz") and user_pokemon[4] > comp_pokemon[4]:
        print(user_pokemon_name, "used", usermove)
        comphp = comphp - (flare_biltz()/2)
        print(comp_pokemon_name, "hp is", comphp) 
        compmove = random.choice(Greninjamoves)
        if compmove in ("hydro pump") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * hydro_pump())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("ice beam") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_beam()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("extrasensory") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - extrasensory()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("dark pulse") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - dark_pulse()
          print(user_pokemon_name, "hp is", userhp)
      elif usermove in ("Flare Biltz", "flare biltz") and user_pokemon[4] < comp_pokemon[4]:
        compmove = random.choice(Greninjamoves)
        if compmove in ("hydro pump"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * hydro_pump())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("ice beam"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_beam()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("extrasensory"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - extrasensory()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("dark pulse"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - dark_pulse()
          print(user_pokemon_name, "hp is", userhp)
        if userhp > 0:
          print(user_pokemon_name, "used", usermove)
          comphp = comphp - (flare_biltz()/2)
          print(comp_pokemon_name, "hp is", comphp) 
      if usermove in ("Wild Charge", "wild charge",) and user_pokemon[4] > comp_pokemon[4]:
        print(user_pokemon_name, "used", usermove)
        comphp = comphp - (2 * wild_charge())
        print(comp_pokemon_name, "hp is", comphp) 
        compmove = random.choice(Greninjamoves)
        if compmove in ("hydro pump") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * hydro_pump())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("ice beam") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_beam()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("extrasensory") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - extrasensory()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("dark pulse") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - dark_pulse()
          print(user_pokemon_name, "hp is", userhp)
      elif usermove in ("Wild Charge", "wild charge",) and user_pokemon[4] < comp_pokemon[4]:
        compmove = random.choice(Greninjamoves)
        if compmove in ("hydro pump"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * hydro_pump())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("ice beam"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_beam()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("extrasensory"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - extrasensory()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("dark pulse"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - dark_pulse()
          print(user_pokemon_name, "hp is", userhp)
        if userhp > 0:
          print(user_pokemon_name, "used", usermove)
          comphp = comphp - (2 * wild_charge())
          print(comp_pokemon_name, "hp is", comphp) 
      if usermove in ("Crunch", "crunch",) and user_pokemon[4] > comp_pokemon[4]:
        print(user_pokemon_name, "used", usermove)
        comphp = comphp - (crunch()/2)
        print(comp_pokemon_name, "hp is", comphp) 
        compmove = random.choice(Greninjamoves)
        if compmove in ("hydro pump") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * hydro_pump())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("ice beam") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_beam()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("extrasensory") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - extrasensory()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("dark pulse") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - dark_pulse()
          print(user_pokemon_name, "hp is", userhp)
      elif usermove in ("Crunch", "crunch",) and user_pokemon[4] < comp_pokemon[4]:
        compmove = random.choice(Greninjamoves)
        if compmove in ("hydro pump"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * hydro_pump())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("ice beam"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_beam()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("extrasensory"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - extrasensory()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("dark pulse"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - dark_pulse()
          print(user_pokemon_name, "hp is", userhp)
        if userhp > 0:
          print(user_pokemon_name, "used", usermove)
          comphp = comphp - (crunch()/2)
          print(comp_pokemon_name, "hp is", comphp)
    if user_pokemon_name in ("Metagross", "metagross"):
      usermove = input("What do you want to do: \n Meteor Mash, Earthquake, Zen Headbutt, Ice Punch ")
      if usermove in ("Meteor Mash", "meteor mash") and user_pokemon[4] > comp_pokemon[4]:
        print(user_pokemon_name, "used", usermove)
        comphp = comphp - (meteor_mash()/2)
        print(comp_pokemon_name, "hp is", comphp)
        compmove = random.choice(Arcaninemoves)
        if compmove in ("extreme speed") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (extreme_speed()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("flare biltz") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * flare_biltz())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("wild charge") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - wild_charge()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("crunch") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * crunch())
          print(user_pokemon_name, "hp is", userhp)
      elif usermove in ("Meteor Mash", "meteor mash") and user_pokemon[4] < comp_pokemon[4]:
        compmove = random.choice(Arcaninemoves)
        if compmove in ("extreme speed"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (extreme_speed()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("flare biltz"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * flare_biltz())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("wild charge"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - wild_charge()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("crunch"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * crunch())
          print(user_pokemon_name, "hp is", userhp)
        if userhp > 0:
          print(user_pokemon_name, "used", usermove)
          comphp = comphp - (meteor_mash()/2)
          print(comp_pokemon_name, "hp is", comphp)
      if usermove in ("Earthquake", "earthquake") and user_pokemon[4] > comp_pokemon[4]:
        print(user_pokemon_name, "used", usermove)
        comphp = comphp - (2 * earthquake())
        print(comp_pokemon_name, "hp is", comphp) 
        compmove = random.choice(Arcaninemoves)
        if compmove in ("extreme speed") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (extreme_speed()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("flare biltz") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * flare_biltz())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("wild charge") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - wild_charge()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("crunch") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * crunch())
          print(user_pokemon_name, "hp is", userhp)
      elif usermove in ("Earthquake", "earthquake") and user_pokemon[4] < comp_pokemon[4]:
        compmove = random.choice(Arcaninemoves)
        if compmove in ("extreme speed"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (extreme_speed()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("flare biltz"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * flare_biltz())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("wild charge"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - wild_charge()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("crunch"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * crunch())
          print(user_pokemon_name, "hp is", userhp)
        if userhp > 0:
          print(user_pokemon_name, "used", usermove)
          comphp = comphp - (2 * earthquake())
          print(comp_pokemon_name, "hp is", comphp) 
      if usermove in ("Zen Headbutt", "zen headbutt",) and user_pokemon[4] > comp_pokemon[4]:
        print(user_pokemon_name, "used", usermove)
        comphp = comphp - zen_headbutt()
        print(comp_pokemon_name, "hp is", comphp) 
        compmove = random.choice(Arcaninemoves)
        if compmove in ("extreme speed") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (extreme_speed()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("flare biltz") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * flare_biltz())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("wild charge") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - wild_charge()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("crunch") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * crunch())
          print(user_pokemon_name, "hp is", userhp)
      elif usermove in ("Zen Headbutt", "zen headbutt",) and user_pokemon[4] < comp_pokemon[4]:
        compmove = random.choice(Arcaninemoves)
        if compmove in ("extreme speed"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (extreme_speed()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("flare biltz"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * flare_biltz())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("wild charge"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - wild_charge()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("crunch"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * crunch())
          print(user_pokemon_name, "hp is", userhp)
        if userhp > 0:
          print(user_pokemon_name, "used", usermove)
          comphp = comphp - zen_headbutt()
          print(comp_pokemon_name, "is", comphp) 
      if usermove in ("Ice Punch", "ice punch",) and user_pokemon[4] > comp_pokemon[4]:
        print(user_pokemon_name, "used", usermove)
        comphp = comphp - (ice_punch()/2)
        print(comp_pokemon_name, "hp is", comphp) 
        compmove = random.choice(Arcaninemoves)
        if compmove in ("extreme speed") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (extreme_speed()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("flare biltz") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * flare_biltz())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("wild charge") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - wild_charge()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("crunch") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * crunch())
          print(user_pokemon_name, "hp is", userhp)
      elif usermove in ("Ice Punch", "ice punch",) and user_pokemon[4] < comp_pokemon[4]:
        compmove = random.choice(Arcaninemoves)
        if compmove in ("extreme speed"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (extreme_speed()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("flare biltz"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * flare_biltz())
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("wild charge"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - wild_charge()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("crunch"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (2 * crunch())
          print(user_pokemon_name, "hp is", userhp)
        if userhp > 0:
          print(user_pokemon_name, "used", usermove)
          comphp = comphp - (ice_punch()/2)
          print(comp_pokemon_name, "hp is", comphp) 
    if user_pokemon_name in ("Greninja", "greninja"):
      usermove = input("What do you want to do: \n Dark Pulse, Extraensory, Ice Beam, Hydro Pump ")
      if usermove in ("Hydro Pump", "hydro pump") and user_pokemon[4] > comp_pokemon[4]:
        print(user_pokemon_name, "used", usermove)
        comphp = comphp - hydro_pump()
        print(comp_pokemon_name, "hp is", comphp)
        compmove = random.choice(Metagrossmoves)
        if compmove in ("ice punch") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_punch()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("earthquake") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - earthquake()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("meteor mash") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (meteor_mash()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("zen headbutt") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (0 * zen_headbutt())
          print(user_pokemon_name, "hp is", userhp)
      elif usermove in ("Hydro Pump", "hydro pump") and user_pokemon[4] < comp_pokemon[4]:
        compmove = random.choice(Metagrossmoves)
        if compmove in ("ice punch"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_punch()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("earthquake"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - earthquake()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("meteor mash"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (meteor_mash()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("zen headbutt"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (0 * zen_headbutt())
          print(user_pokemon_name, "hp is", userhp)
        if userhp > 0:
          print(user_pokemon_name, "used", usermove)
          comphp = comphp - hydro_pump()
          print(comp_pokemon_name, "hp is", comphp)
      if usermove in ("Extrasensory", "extrasensory") and user_pokemon[4] > comp_pokemon[4]:
        print(user_pokemon_name, "used", usermove)
        comphp = comphp - (extrasensory()/4)
        print(comp_pokemon_name, "hp is", comphp) 
        compmove = random.choice(Metagrossmoves)
        if compmove in ("ice punch") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_punch()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("earthquake") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - earthquake()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("meteor mash") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (meteor_mash()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("zen headbutt") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (0 * zen_headbutt())
          print(user_pokemon_name, "hp is", userhp)
      elif usermove in ("Extrasensory", "extrasensory") and user_pokemon[4] < comp_pokemon[4]:
        compmove = random.choice(Metagrossmoves)
        if compmove in ("ice punch"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_punch()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("earthquake"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - earthquake()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("meteor mash"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (meteor_mash()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("zen headbutt"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (0 * zen_headbutt())
          print(user_pokemon_name, "hp is", userhp)  
        if userhp > 0:
          print(user_pokemon_name, "used", usermove)
          comphp = comphp - (extrasensory()/4)
          print(comp_pokemon_name, "hp is", comphp) 
      if usermove in ("Dark Pulse", "dark pulse",) and user_pokemon[4] > comp_pokemon[4]:
        print(user_pokemon_name, "used", usermove)
        comphp = comphp - (2 * dark_pulse())
        print(comp_pokemon_name, "hp is", comphp) 
        compmove = random.choice(Metagrossmoves)
        if compmove in ("ice punch") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_punch()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("earthquake") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - earthquake()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("meteor mash") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (meteor_mash()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("zen headbutt") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (0 * zen_headbutt())
          print(user_pokemon_name, "hp is", userhp)
      elif usermove in ("Dark Pulse", "dark pulse",) and user_pokemon[4] < comp_pokemon[4]: 
        compmove = random.choice(Metagrossmoves)
        if compmove in ("ice punch"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_punch()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("earthquake"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - earthquake()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("meteor mash"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (meteor_mash()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("zen headbutt"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (0 * zen_headbutt())
          print(user_pokemon_name, "hp is", userhp)
        if userhp > 0:
          print(user_pokemon_name, "used", usermove)
          comphp = comphp - (2 * dark_pulse())
          print(comp_pokemon_name, "hp is", comphp)
      if usermove in ("Ice Beam", "ice beam",) and user_pokemon[4] > comp_pokemon[4]:
        print(user_pokemon_name, "used", usermove)
        comphp = comphp - (ice_beam()/2)
        print(comp_pokemon_name, "hp is", comphp) 
        compmove = random.choice(Metagrossmoves)
        if compmove in ("ice punch") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_punch()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("earthquake") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - earthquake()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("meteor mash") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (meteor_mash()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("zen headbutt") and comphp > 0:
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (0 * zen_headbutt())
          print(user_pokemon_name, "hp is", userhp)
      elif usermove in ("Ice Beam", "ice beam",) and user_pokemon[4] < comp_pokemon[4]:
        compmove = random.choice(Metagrossmoves)
        if compmove in ("ice punch"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (ice_punch()/2)
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("earthquake"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - earthquake()
          print(user_pokemon_name, "hp is", userhp)
        if compmove in ("meteor mash"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (meteor_mash()/2)
          print(user_pokemon_name, "is hp", userhp)
        if compmove in ("zen headbutt"):
          print(comp_pokemon_name, "used", compmove)
          userhp = userhp - (0 * zen_headbutt())
          print(user_pokemon_name, "hp is", userhp)
        if userhp > 0:
          print(user_pokemon_name, "used", usermove)
          comphp = comphp - (ice_beam()/2)
          print(comp_pokemon_name, "hp is", comphp) 
    if userhp <= 0:
      print(user_pokemon_name, "has fainted") 
      print("Trainer Blue has won")
    if comphp <= 0:
      print(comp_pokemon_name, "has fainted")
      print("Trainer ", user_name, "has won")

