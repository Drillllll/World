# World
Simple world simulator using object-oriented programming.

This project is a basic simulation of a world represented by a 2D board. Each organism occupies exactly one field on the board, and collisions between organisms are handled accordingly, resulting in one of the organisms dying or being moved if they collide.

The user can add new organisms from a list displayed after clicking on an empty field with the left mouse button. Additionally, the user can save and load game states from a file.

Organisms have different strengths, initiatives, and abilities. Here are some examples:

Animals

Human: After pressing the space bar, the human (player) becomes immortal for 5 turns.
Antelope: Has a 50% chance of escaping from a fight.
Fox: Will not move to a field occupied by a stronger organism.
Sheep: None.
Turtle: Defends against animal attacks.
Wolf: None.
Cyber Sheep: Tries to move to the closest Sosnowsky's Hogweed plant and eat it.

Plants

Grass: None.
Belladonna: Toxic plant that kills an animal that eats it.
Guarna: If an animal eats this plant, its strength increases.
Sonchus: Spreads more quickly.
Sosnowsky's Hogweed: Kills every animal in the vicinity (except Cyber Sheep).

