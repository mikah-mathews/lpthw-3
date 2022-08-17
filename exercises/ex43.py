class Scene(object):
  def enter(self):
    Pass
  
class Engine(object):
  def __init__(self, scene_map):
    Pass
  
  def play(self):
    Pass
  
class Death(Scene):
  def enter(self):
    Pass

class CentralCorridor(Scene):
  def enter(self):
    Pass

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