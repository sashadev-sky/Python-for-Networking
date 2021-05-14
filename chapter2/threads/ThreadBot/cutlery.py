from threadbot import bots, kitchen


import sys
for bot in bots:
    # We get the number of tables as a command-line parameter, and then
    # give each bot that number of tasks for preparing and clearing tables in the restaurant.
    # for i in range(int(sys.argv[1])):
    for i in range(10):
        bot.tasks.put('prepare table')
        bot.tasks.put('clear table')
    # The shutdown task will make the bots stop(so that bot.join()
    # a bit further down will return).
    bot.tasks.put('shutdown')

print('Kitchen inventory before service:', kitchen)
for bot in bots:
    bot.start()

for bot in bots:
    bot.join()
print('Kitchen inventory after service:', kitchen)


"""
attrs, which is an open source Python library, is a really wonderful library
for making class creation easy.
  * @attrs decorator will ensure that this Cutlery class will get
    all the usual boilerplate code (like __init__()) automatically set up.
  * attrib() provides easy way to create attributes, including defaults, which you
    might normally have handled as keyword arguments in the __init__() method.

This script is showing why threading is considered unsafe.

Testing this script:
  * If you run a bunch of ThreadBots over a bunch of tables a specific number of times,
    you expect that after all the work is done, all of the knives and forks should be back
    in the kitchen and accounted for.

  * Test that with one hundred tables to be prepared and cleared by each ThreadBot and all
    of them operating at the same time:

    $ p3 cutlery.py 100
    Kitchen inventory before service: Cutlery(knives=100, forks=100)
    Kitchen inventory after service: Cutlery(knives=100, forks=100)

    100 works great. Update it to 10000 and it's off every time, and by different values:

    $ p3 cutlery.py 10000
    Kitchen inventory before service: Cutlery(knives=100, forks=100)
    Kitchen inventory after service: Cutlery(knives=112, forks=96)

    $ p3 cutlery.py 10000
    Kitchen inventory before service: Cutlery(knives=100, forks=100)
    Kitchen inventory after service: Cutlery(knives=100, forks=104)

  * Let’s summarize the situation:
    - Your ThreadBot code is very simple and easy to read. The logic is fine.
    - You have a working test (with 100 tables) that reproducibly passes.
    - You have a longer test (with 10,000 tables) that reproducibly fails.
    - The longer test fails in *different, nonreproducible ways*.

    * These are a few typical signs of a race condition bug. The reason: the `change` method
      in the other file:

      def change(self, knives, forks):
        self.knives += knives
        self.forks += forks

      The problem with preemptive multitasking is that any thread busy with these steps can
      be interrupted at any time, and a different thread can be given the opportunity
      to work through the same steps.

"""
