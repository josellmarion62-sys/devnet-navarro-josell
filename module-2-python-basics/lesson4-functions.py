"""
Module 2 — Lesson 4: Functions
Student: Navarro, Josell Marion C.
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? 
============================================
Think a function is like a recipe for cooking Sinigang.
Instead of writing out every single step, all you need is to write down the master recipe once
and give it a name such as 'make_sinigang()'.

Let's break it down for further clarification:
-Take the parameters as ingredients where you pass it to the cooking pot 'protein="pork"'
-Take function call when the head chef starts the cooking using that master recipe
'make_sinignang("pork", extra_sour=True)'.
-Take return statement as finished, that's when the hot bowl of Sinigang handed over to 
the customers.

============================================
KEY VOCABULARY
============================================
- function: This is a reusable block of code that can be used to perform a single task.
- parameter: This is where like the place-holder of the value when defining a function.
- return: This is the keyword where it sends a result back to the function to where it was 
called and it will immediately exiting the function.
- argument: This is the actual value that passed into function when we call it.
- function call: This is the command that execute the function by following its name 
and next to the parenthesis.

============================================
MY OWN EXAMPLE(S)
============================================
def make_sinigang(protein, sourness_level="Medium"):
    if protein.lower() == "shrimp":
        cook_time = "10 mins"
    else:
        cook_time = "45 mins"
        
    finished_dish = f"Mangkok of {protein} Sinigang (Cook time: {cook_time})"
    return finished_dish

order1 = make_sinigang("Pork")
order2 = make_sinigang("Shrimp", sourness_level="Extra Sour")

print(order1) 
print(order2)

============================================
A MISTAKE I MADE 
============================================
At first, I'm confused about the purpose of the return value. Then when I research
about it, that's when I found out about its function and what does it do to the code.

Looking at my own example in the line 41: 'return finished_dish'
where it returns/hands the dish over to variable named 'order1' or the other part of the code.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Well, you can connect function to a Pokemon battle!

Instead of a long code when calculating the damage and health deduction. Developers can
wrote a single function and calls it whenever a attack happens.

"""