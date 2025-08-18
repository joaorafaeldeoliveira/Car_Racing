# Car Racing Game

## Overview

This is a 2D car racing game built with Python and Pygame. The game features a menu system with multiple game modes including single player, 2-player cooperative, and 2-player competitive modes. Players control cars that can move in all directions while navigating through scrolling background levels. The game implements an entity-based architecture with abstract base classes for game objects and uses a factory pattern for entity creation.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Game Engine Architecture
The game follows an object-oriented design with clear separation of concerns:

- **Entity System**: Uses an abstract `Entity` base class that all game objects inherit from, ensuring consistent behavior across different game elements
- **Factory Pattern**: `EntityFactory` centralizes entity creation, making it easy to spawn different types of game objects
- **Game Loop Structure**: Traditional game loop with event handling, update logic, and rendering phases

### Core Components

**Main Game Controller**
- `Game` class manages the overall application flow
- Handles transitions between menu and gameplay states
- Manages the main game window and Pygame initialization

**Menu System**
- `Menu` class provides navigation interface with keyboard controls
- Supports multiple game modes and configuration options
- Uses event-driven input handling for menu navigation

**Level Management**
- `Level` class orchestrates gameplay mechanics
- Manages entity collections and game state
- Implements timer-based events for enemy spawning and level progression
- Handles collision detection and game over conditions

**Entity Framework**
- Abstract `Entity` base class enforces consistent interface
- Automatic sprite loading based on entity names
- Built-in positioning and movement capabilities
- Specialized classes for `Player` and `Background` entities

### Input System
The game implements a flexible key mapping system:
- Separate key configurations for Player1 and Player2
- Support for movement in all four directions
- Dedicated shooting controls (though shooting mechanics appear incomplete)
- Menu navigation through keyboard events

### Asset Management
- Convention-based asset loading (entities load sprites based on their names)
- Assets stored in `./asset/` directory
- Support for PNG images with alpha transparency

### Game State Management
- State transitions between menu and gameplay
- Level progression system with timeout mechanics
- Player lifecycle management and game over detection

## External Dependencies

### Core Framework
- **Pygame**: Primary game development framework for graphics, input handling, sound, and window management

### Asset Requirements
- PNG image assets for sprites and backgrounds stored in `./asset/` directory
- Background music files (MP3 format, currently commented out)

### Python Standard Library
- **sys**: System-specific functions for application termination
- **abc**: Abstract base class support for the entity system

The architecture is designed for extensibility, with clear patterns for adding new entity types, levels, and game modes. The factory pattern and abstract entity system make it straightforward to introduce new game elements without modifying existing code.