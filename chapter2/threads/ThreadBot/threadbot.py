import threading
from attr import attrs, attrib
from queue import Queue

class ThreadBot(threading.Thread):
  def __init__(self):
    super().__init__(target=self.manage_table)
    self.cutlery = Cutlery(knives=0, forks=0)
    self.tasks = Queue()

  def manage_table(self):
    while True:
      task = self.tasks.get()
      if task == 'prepare table':
        kitchen.give(to=self.cutlery, knives=4, forks=4)
      elif task == 'clear table':
        self.cutlery.give(to=kitchen, knives=4, forks=4)
      elif task == 'shutdown':
        return

@attrs
class Cutlery:
    knives = attrib(default=0)
    forks = attrib(default=0)
    # User-defined classes can be used as type hints as a string representing their classname.
    # This synax doesn't require loading the type immediately, (ex. Cutlery as is raises undefined error)
    def give(self, to: 'Cutlery', knives=0, forks=0):
        self.change(-knives, -forks)
        to.change(knives, forks)

    def change(self, knives, forks):
        self.knives += knives
        self.forks += forks


kitchen = Cutlery(knives=100, forks=100)
bots = [ThreadBot() for i in range(10)]
