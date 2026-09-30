"""
Module 2 — Lesson 3: Loops & Lists
Student: Navarro, Josell Marion C.
Date: September 30, 2026

============================================
WHAT IS THIS TOPIC? 
============================================
Think of it like listing a grocery paper bag that holds ordered collection of items.
But keep in mind that each item inside the bag has a specific slot number starting from 0.

Loops are like having an automated worker inside the grocery bag:
- A `for` loop is like saying: "Go through every item in this bag, one by one,
 until the bag is empty."
- A `while` loop is like saying: "Keep taking out items and checking them until
 a specific condition changes."

============================================
KEY VOCABULARY
============================================
- list: It is an ordered, mutable collections of items enclosed in square brackets.
- for loop: A loop used to iterate over a sequence under a predetermined number of times.
- while loop: A loop that repeatedly execute a block of code as long as specified conditions
    are met.
- index: It is the the numerical position of an item inside a list, 
    starting at `0` for the first element
- iteration: It is the one single pass or repetition through a loop's block of code.
- break: A keyword that immediately stops and exits the loop entirely.

============================================
MY OWN EXAMPLE(S)
============================================
student_names = ["Josell", "Marion", "Camilo", "Navarro"]
exam_scores = [82, 71, 95, 68]

passing_count = 0

for i in range(len(student_names)):
    name = student_names[i]
    score = exam_scores[i]
    
    if score >= 75:
        status = "PASSED"
        passing_count += 1
    else:
        status = "FAILED"
        
    print(f"Student: {name:<8} | Score: {score} | Status: {status}")

print(f"\nPassing Rate: {(passing_count / len(student_names)) * 100:.1f}%")

============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
I get bit of confuse to modifying a list while iterating it over.
By removing items from a list inside a 'for' loop that is actively iterating over the same list
which causes the items to be skipped.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
I can connect this to Pokemon world!

Let's say your inventory backpack is stored as a list:
 `inventory = ["Potion", "Pokeball", "Antidote", "Revive"]`.
When you open your item menu, the game runs a `for` loop to draw 
    every item button on your screen:

for index, item in enumerate(inventory):
    display_button(x_pos=100, y_pos=index * 50, label=item)

When you use a consumable item (like a Potion), a loop searches the list, 
    applies the healing logic, and uses `.remove("Potion")` or pops it by index!
"""
