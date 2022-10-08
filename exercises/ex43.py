from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
  def enter(self):
    Pass
  
class Engine(object):
  def __init__(self, scene_map):
    Pass
  
  def play(self):
    Pass
  
class Death(Scene):

  lines = [
    "You could have done a better job there mate.",
    "Man, you really could use some practice on the range",
    "Does the unrelenting coldness of death ever weigh on your soul?",
    "Your mother is a hamster and your father smells of elderberries.",
    "You could go up against a mouse and you would still die.",
    "Disappointment fills you up once again.",
    "Do your best next time!",
    "lol ur a loser",
    "Keep trying and you may make it to the end eventually"
  ]
  def enter(self):
    print(lines[random.randint(0, 8)])
    exit(1)

class CentralCorridor(Scene):
  def enter(self):
    enter_scene = """
    It's a lonely existance out in space. It is so rare
    for you to meet another ship, let alone another species. All was 
    running smoothly until over 3/4 of the oxygen generators gave out. Your
    crew mates went on a space walk to repair them. You stayed inside to monitor the
    systems and give directions from repair manuals. Everything seems to be 
    going well until you hear one of your crew mates give a startled shout. Suddenly
    all of their life monitors start shrieking. They have died. You turn,
    startled by the air lock's hissing. Something is coming inside."""

class LaserWeaponArmory(Scene):
  def enter(self):
    Pass

class TheBridge(Scene):
  def enter(self):
    Pass

class EscapePod(Scene):
  def enter(self):
    Pass

class Map(object):
  def __init__(self, start_scene):
    Pass
  
  def next_scene(self, scene_name):
    Pass
  
  def opening_scene(self):
    Pass

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()