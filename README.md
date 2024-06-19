# Battleship Game

## Overview
This C program implements a simple console version of the classic game Battleship. The game is played between a human player and the computer. Both players place a fleet of ships on a grid, and then they take turns guessing each other's ship placements to try to sink the entire fleet.

## Features
- **Dynamic Board Initialization**: Boards for both the player and the computer are dynamically initialized at the start of the game.
- **Ship Placement**: Players can manually place their ships with specific start and end coordinates. The computer places its ships automatically.
- **Game Play**: The game alternates turns between the player and the computer, with each player guessing coordinates to attack. Hits and misses are recorded, and the game continues until all ships of a player are sunk.
- **Result Tracking**: The game tracks and stores the final scores in a file named `game_result.txt`.

## How to Compile and Run
To compile and run the game, use the following commands on a system with a C compiler like `gcc`:
