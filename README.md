# My Game
Inspiration: 
## 🎮 Game Overview

## Game Flow
* Creates Base Character with some default stats
* Based on the Superhero use selects it updates the stats of the character to match that of the super Hero (Making each superhero have different advantages and total stats)
* Each superhero also has a unique skill that can only be used by that superhero (i.e for hulk rage; by default rage is 0, but when damage_inflicted increases,it increases rage which inturn when it hits 10 hulk can then make use of his special skill (super smash))
* The default way of using special character is by maxing all character attributes, by using items type character buff and type weapon. This is not yet completed

So here for now sticking with just only a base game 

We are going to have:
### Items
So for now it's simple we have a list []: Character inventory
#### Items Attribute
Name, type 

##### Methods
get_name, get_type

#### Sub Class of Items (Type: Character buff)
This sub class of items only affects and updates the character stats

In Theory, since it is a game, the potion should be dynamic same with other sub class, they should have a unique increment which is determined by the game it self 
Also user can have many items in their inventory but when use them with the use method

##### 1. Healing potion
- Attribute: increase_health_by: int
- method: getter - get_increased_health_by, setter - use_healing_potion affect stats

##### speed boost
##### hacker eyes
##### strenght med 
##### posion

With Identical methods, 

#### Sub Class of Items (Type: Weapons)
This sub class increase inflicted damage by the character
##### Sniper
- Attribute: damage
- Method: get_damage, use_sniper (update_character_damage_stats)

##### Bow and arrow

For now I will just go with this 



So Although this is just a rough idea, The summary is pretty simple, make a character which has special abilities and inventory of items they can use, the inventory is created by the play and the game does not really have the layout where players can pick up items yet so the main.py just allows players to add to inventory and make use of items which all affects stats and gives notification is special ability is available
