# Escape

By Mohammadparsa Tabasi

## Game idea

Escape is a text adventure game where the player is trapped inside an abandoned house.
The player must explore different rooms, collect items and find the ESCAPE KEY.
The player must then use the key to escape through the front yard.

## Objective

The objective of the game is to find the ESCAPE KEY and escape the house.

## How to play

The player starts in the living room.

The player can:
- Start the game
- Explore rooms
- Move between rooms
- Collect items
- Check their inventory
- Read the instructions
- Save the game and load the game
- End the game

The front yard is locked until the player finds the ESCAPE KEY.

## Game features

- Player name and age
- Multiple rooms
- Items that can be collected
- Inventory system
- Locked escape route
- Save game functionality
- Instructions loaded from a text file
- Introduction loaded from a text file


## Project structure

- game.py - Main game and menu
- player.py - Player class and player actions
- room.py - Room class
- item.py - Item class
- intro.txt - Introduction text
- instructions.txt - Game instructions
- save.txt - Saved game information

## Classes

### Player
Stores the player's name, location and inventory.

### Room
Stores the room name and the item located in the room.

### Item
Stores the item's name and weight.