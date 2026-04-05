# Urban Chaos – Open World Gameplay Prototype

Author: Raunak Singh  
Project Type: Gameplay Prototype  
Technology: Python, Pygame  
Year: 2026  

---

# 1. Project Overview

Urban Chaos is a small open-world gameplay prototype developed to simulate core mechanics commonly found in open-world action games. The purpose of the project was to implement basic gameplay systems and practice gameplay testing and debugging workflows similar to those used in professional game QA environments.

The prototype focuses on player movement, environment interaction, collision detection, and camera behavior within a simple game environment.

---

# 2. Project Objectives

The main objectives of this prototype were:

- Implement basic open-world gameplay mechanics
- Build a simple environment with interactive objects
- Test player movement and collision systems
- Identify and document gameplay bugs
- Practice QA documentation including test plans and bug reports

---

# 3. Gameplay Systems Implemented

## Player Movement

The player can:

- Move forward, backward, left, and right
- Jump
- Navigate the game environment

Movement mechanics were designed to simulate typical third-person gameplay movement.

---

## Collision Detection

Collision systems were implemented to prevent the player from passing through environmental objects.

Objects included:

- Walls
- Crates
- Environment boundaries

Collision behavior was tested to ensure that the player properly interacts with environmental obstacles.

---

## Environment Interaction

The environment contains simple objects such as crates and walls to simulate gameplay navigation.

These objects were used to test:

- Player navigation
- Movement restrictions
- Collision edge cases

---

# 4. Testing Process

The prototype was tested using multiple QA testing approaches:

### Functional Testing

Testing focused on verifying that gameplay mechanics function correctly.

Example checks:

- Player movement responsiveness
- Jump functionality
- Environment collision behavior

---

### Gameplay Testing

Gameplay sessions were used to identify gameplay issues and system inconsistencies.

Focus areas included:

- Player navigation
- Camera stability
- Interaction with environment objects

---

### Edge Case Testing

Edge cases were tested by performing unusual gameplay actions.

Examples:

- Jumping into object corners
- Moving diagonally into collision edges
- Rapid movement input combinations

These tests helped identify several gameplay bugs.

---

# 5. Bugs Identified

During testing, multiple issues were discovered including:

- Player getting stuck between objects
- Minor camera jitter near obstacles
- Movement delay after key release
- Collision boundary inconsistencies

All bugs were documented using structured QA bug reports.

---

# 6. QA Documentation

The following QA documents were created as part of this project:

- Test Plan
- Gameplay Bug Reports
- Gameplay System Analysis

These documents simulate real QA workflows used during game development.

---

# 7. Skills Demonstrated

This prototype demonstrates the following skills:

- Gameplay system analysis
- Bug identification and documentation
- Functional testing
- Edge-case testing
- Debugging gameplay systems

---

# 8. Conclusion

Urban Chaos was developed as a learning project to understand how gameplay systems operate and how QA testing contributes to game quality.

The project helped demonstrate practical testing workflows, gameplay analysis skills, and structured bug documentation commonly used in game development environments.
