from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
  def enter(self):
    print("This scene is not yet configured. Subclass it and impement enter().")
      exit(1)

class Engine(object):
  def __init__(self, scene_map):
    self.scene_map = scene_map
  
  def play(self):
    current_scene = self.scene_map.opening_scene()
    last_scene = self.scene_map.next_scene('finished')

    while current_scene != last_scene:
      next_scene_name = current_scene.enter()
      current_scene = self.scene_map.next_scene(next_scene_name)
    
    current_scene.enter()

class Death(Scene):
  quips = ["You could have done a better job there mate.",
    "Man, you really could use some practice on the range",
    "Does the unrelenting coldness of death ever weigh on your soul?",
    "Your mother is a hamster and your father smells of elderberries.",
    "You could go up against a mouse and you would still die.",
    "Disappointment fills you up once again.",
    "Do your best next time!",
    "lol ur a loser",
    "Keep trying and you may make it to the end eventually"]
  def enter(self):
    print(Death.quips[randint(0, len(self.quips)-1)])
    exit(1)

class CentralCorridor(Scene):
  def enter(self):
    print(dedent('''
    The Gothons of Planet Percival #25 have invaded your ship and murdered the rest of your 
    fellow crewmates. You are the last surviving member and your last mission is to get the
    neutron desctruction bomb from the Weapons Armory, put it in the bridge, and blow the ship 
    up after getting into an escape pod.\n
    You're running down the corridor towards the Weapons Armory when a Gothon steps into the hallway.
    Their sharp teeth are exposed as they gleefully grin at the sight of you. The Gothon aims it's gun
    towards you. \n
    Actions\n
    --------
    r - Run back down the corridor and try to escape into an adjacent hallway\n
    f - Pull out your own lazer gun and try to shoot the Gothon\n
    j - Tell a dirty joke that your Gothon friend taught you in college'''))
    
    action = input("> ")

    if action.lower() == "r":
      print(dedent('''
       '''))
    elif action.lower() == "f":

    elif action.lower() == "j":

    else:

class LazerWeaponArmory(Scene):
  def enter(self):
    Pass

class Map(object):
  scenes = {
    'central_corridor' : CentralCorridor(),
    'lazer_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished()
  }
  def __init__(self, start_scene):
    self.start_scene = start_scene

  def next_scene(self, scene_name):
    val = Map.scenes.get(scene_name)
    return val

  def opening_scene(self):
    return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
