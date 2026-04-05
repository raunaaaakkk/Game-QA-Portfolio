# Game QA Test Plan
## Urban Chaos – Open World Gameplay Prototype

### Author
Raunak Singh

### Version
1.0

### Date
2026

---

# 1. Objective

The objective of this test plan is to verify the functionality, stability, and gameplay mechanics of the Urban Chaos gameplay prototype. The testing process focuses on identifying gameplay bugs, collision issues, system inconsistencies, and edge-case scenarios that could affect player experience.

---

# 2. Scope

### Features to be Tested

- Player movement system
- Jump mechanics
- Collision detection
- Environment interaction
- Camera behavior
- Boundary handling
- Object interaction

### Features Not in Scope

- Multiplayer systems
- Online connectivity
- Advanced AI behavior
- Console platform testing

---

# 3. Test Environment

### Hardware

PC / Laptop  
8GB RAM minimum  

### Software

Operating System: Windows 10 / Windows 11  
Game Engine: Python + Pygame  
Input Devices: Keyboard / Mouse  

---

# 4. Test Strategy

Testing will be performed using the following methods:

### Functional Testing
Verify that all gameplay systems work as expected.

### Gameplay Testing
Evaluate whether gameplay mechanics behave correctly during player interaction.

### Regression Testing
Ensure that previously fixed bugs do not reappear after updates.

### Edge Case Testing
Test unusual player actions or unexpected gameplay sequences.

---

# 5. Test Scenarios

| Test ID | Test Scenario | Expected Result |
|-------|---------------|----------------|
| TC-01 | Player moves forward | Player moves smoothly |
| TC-02 | Player jumps | Player jumps and lands correctly |
| TC-03 | Player collides with object | Player stops at object boundary |
| TC-04 | Player moves into wall corner | Player should not get stuck |
| TC-05 | Player reaches map boundary | Player cannot move outside map |

---

# 6. Bug Reporting Process

Each bug will be documented using the following structure:

### Bug Report Format

Bug ID  
Title  
Environment  
Steps to Reproduce  
Expected Result  
Actual Result  
Severity  
Frequency  

---

# 7. Sample Bug Report

### Bug ID
BUG-01

### Title
Player gets stuck between wall and crate collision

### Environment
Windows 11  
Keyboard / Mouse  

### Steps to Reproduce

1. Start game
2. Move player toward crate near spawn
3. Jump diagonally into the corner between wall and crate

### Expected Result

Player should slide away from the collision or land normally.

### Actual Result

Player becomes stuck and cannot move without restarting position.

### Severity

Medium

### Frequency

Occurs 3 out of 5 attempts.

---

# 8. Exit Criteria

Testing will be considered complete when:

- All major gameplay systems have been tested
- Critical and high-severity bugs are resolved
- Core gameplay loop functions without major issues

---

# 9. Risks

- Prototype gameplay mechanics may change frequently
- Limited testing environment
- Small team testing limitations

---

# 10. Deliverables

- Test Plan Document
- Test Case List
- Bug Reports
- Gameplay Testing Notes
