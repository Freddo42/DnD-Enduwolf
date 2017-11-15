#!/usr/bin/python
Session = 20

server = 'https://roll20.net/'
channel = '##Endu\'s game'
date = 20171114

def playerCount(world,server):
  ppl = server.players.userid
  count = 0
  for c in world:
    if ppl == c:
      count += 1
  return count

players = playerCount(channel,server)

sitrep = 'Lizard Cave west south west of Abernathy\'s pont'
Session += 1

def DnD(ppl,world,session,location):

  print('Welcome to week ' + session + ' of DnD with ' + world + '!\n Today you are with ' + ppl + ' other players.')
  print('Your last location was ' + location + '.')
  return

DnD(players, channel, Session, sitrep)

print('''Historical events:
  We ventured further into the cave and was surprised by lizard folk.
  Morgran then surprised them by catching the first javlen and throwing it back at them.

  We then captured one alive. We learned that there was 8 in total and called themselves scales
  We learned to fear the bridge and his name is Ur'ash-kth.
  Korm killed the hostage.

  We found a fork in the cave one side was baracaded and the other appears to be a trap.
  As we attempted to cross the bridge found further down a Gnome sized rock flys across the bridge almost killing Veryba and Morgran
  Veryba dashes across the bridge to find a cannon like weapon.

  The party proceeded to cross the bridge however another cannon ball was shot and knocked out Morgran and almost killed Gemmel and Korm.

  Veryba discovered that the weapon was being fired by large stones. Veryba proceeded to cast Sacred Flame on the crate housing the stones.
  The create and stones scattered as two of the six exploded.
  ''')

print('''Historical events (continued):
  The creatures within the room was concused and blinded.
  Veryba ran into the room and proceeded to enact a plan to push one of the Lizards over the edge and into the large pit.
  Gemmel turned the large cannon weapon towards the large lizards ass and attempted to fire the device. However it wasn't loaded.

  Korm contemplated leaving Morgran to die when Gemmel ran forth towards the enemy.
  The fight continued.
  Korm delivered a mortal blow against the large lizard with his dagger.

  The battle appeared to have taken longer than expected (The fight was an epic one that somewhat ended with a toaster thrown at someones head we believe).
  Gemmel and Veryba were unable to shove the Lizard folk into the pit. However Veryba eventually brought down a fierce blow with a two handed shield strike onto the lizards head which in turn the lizard collapsed and fell into the pit.

  Morgran and Veryba argued about having the thunderstones in their pockets and if they would explode. Morgran was able to determine that it would require a significate force to make them explode.
  Veryba however was quickly picking up the thunderstones.
''')
