"""
Module 2 — Lesson 1: Variables & Data Types
Student: Navarro, Josell Marion C.
Date: September 27, 2026

============================================
WHAT IS THIS TOPIC? 
============================================
Think of variable is like placing your shoe on a shoebox.
The shoebox outside is the variable name
and whatever brand of shoe you place inside the container is the value stored in.

============================================
KEY VOCABULARY
============================================
- variable: This is a container where we used to store and hold data values.
- data type: A category that tells Python what kind of value that a variable holds.
- int: These are whole numbers without decimal points 
- float: These are numbers that contain decimal points
- string: A sequence of text characters the enclosed with single ('..') or double ("..").
- boolean: A logical data type that can only hold one or two values: True or False.

============================================
MY OWN EXAMPLE(S)
============================================
restaurant_name = "Mang Inasal"  
pm1_orders = 3                   
price_per_meal = 149.50                       

subtotal = pm1_orders * price_per_meal
discount = 0.10                 
final_total = subtotal * (1 - discount)

print("================================")
print(f"Restaurant: {restaurant_name}")
print(f"Orders: {pm1_orders}x PM1")
print(f"Total Bill (after discount): ₱{round(final_total, 2)}")
print("================================")

============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
For me and the most annoying mistake I did everytime I code python
is the added strings and integers together.
Take it for this example 'age = 20; print("I am " + age)` will result in error.
But if we convert the number into string first (`str(age)`) or use an f-string: `f"I am {age}"`.
it'll work out just fine.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
I think I can still connect this lesson to Pokemon! hehehe
Think about this:

- Character Name: 'string' = "Venusaur"
- Current Level: 'integer' = 25
- Attack Multiplier: 'float' = 1.5
- Is Fainted Status: 'boolean' = False

"""