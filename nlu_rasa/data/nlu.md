## intent:greet
- hello
- good morning
- hi

## intent:affirm
- let's do it
- i love that
- it's perfect
- that looks great
- yes
- yes of course

## intent:deny
- no thank you
- do you have something else
- no this does not work for me
- no i don't like that
- no
- no thanks

## intent:get_lore
- Where are [Yennefer](lore) from
- Who is [Vesemir](lore)
- Who is [Geralt](lore)
- Can you tell me more about [Ciri](lore)
- How [Ciri](lore) is related to you
- Who are [The Nifgaardian](lore)
- Who are [The Witcher](lore)
- Where is [Kaer Morhen](lore)
- What is [Kaer Morhen](lore)
- What happened at [White Orchard](lore)
- Can you tell me more about [Kaer Morhen](lore)
- What is [Temeria](lore)
- What happened in [White Orchard](lore)

## lookup:lore
data/lore.txt

## intent:ask_quest_confirmation
- Should we [follow the tracks](action)
- Do I need to [follow the tracks](action)
- Do we need to [talk to villager](action)
- Should I [talk to Tomira](action)
- Do we need to [kill the griffon](action)
- Should I [kill the wild dogs](action)

## lookup:action
data/action.txt

## intent:ask_help_quest
- I'm not sure what we need to do now
- What do we need to do
- What do I need to do
- Where should I go
- Where should we need to go
- What is the point of the quest
- What do I need to do to complete the quest
- Where should we go now

## intent:location
- Where I am
- Where are we
- What is this place
- Do you know where we are
- I'm lost

## intent:inventory
- What do I have in the inventory
- What do I have in my bag
- Can you tell me what we have in our bag
- Do we have a lot of item
- Is our bag full

## intent:craft_helper
- How can I craft the [Petri's Philter](ingredient)
- Where do I find [Arenaria](ingredient)
- What can I do with a [Griffin mutagen](ingredient)
- Can we craft [White Honey](ingredient)
- Can i craft an [Axeman's trousers](ingredient)
- How can i get [Dark iron ingots](ingredient)
- How should we craft a [Thunderbolt](ingredient)
- Where can I pick [Crow's Eye](ingredient)
- Where can I get [Hop Umbels](ingredient)
- Where should I gather [Ribleaf](ingredient)

## lookup:ingredient
data/ingredient.txt

## intent:combat_helper
- How do we defeat a [griffin](monster)
- How can I kill a [ghoul](monster)
- Can I kill a [wolf](monster)
- What is a [griffin](monster)
- What is [this](monster) monster
- What do I use to defeat [The Griffin](monster)
- What are the weaknesses of a [Griffin](monster)
- Where may i find the monster [Devil by the Well](monster)
- Should i prepare before attempting to kill the [Devil by the well](monster)
- Where can I fight a [Griffin](monster) 

## lookup:monster
data/monster.txt

## intent:thanking
- thanks
- thank you
