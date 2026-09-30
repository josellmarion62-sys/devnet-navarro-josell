"""
Module 2 — Lesson 2: Control Flow (if / elif / else)
Student: Navarro, Josell Marion C.  
Date: September 30, 2026

============================================
WHAT IS THIS TOPIC? 
============================================
Think of this topic as a decision-making wether how to get home safe
based on the weather outside of the school. 

-IF its raining heavily outside, take a Grab car or tricyle.
-ELIF its just drizzling, you can take out your umbrella or jeepney.
-ELSE if its not raining at all, you can just walk home.

============================================
KEY VOCABULARY
============================================
- condition: It is an expression where it evaluates either 'True' or 'False'
and to determine which code block to run. 
- if / elif / else: These are keywords to build a conditional logic paths. 
'if' starts the decison, 'elif' checks the additional condition, and 
'else' catches everything else.
- comparison operator: These are symbols used to compare values.
('==', '>', '<', '<=', '>=').
- boolean expression: Any code statement that simplifies down to single boolean value 
('True' or 'False').
- indentation: Well, this is very important that requires 4 tabs or single tabs in
Python to determine which lines of code belong inside a specific: 'if', 'elif', and 'else'.


============================================
MY OWN EXAMPLE(S)
============================================
load_balance = 45.0
data_mb = 150
is_roaming = False

if is_roaming:
    print("Roaming active: Standard local promos are currently unavailable.")
elif load_balance >= 50 and data_mb < 500:
    print("Recommendation: Register for GoSURF50 (1GB data for 3 days).")
elif load_balance >= 20 and data_mb < 200:
    print("Recommendation: Register for DATA20 (400MB data for 1 day).")
elif data_mb >= 500:
    print("You still have sufficient mobile data left!")
else:
    print("Insufficient balance for data add-ons. Please top up your account.")

============================================
A MISTAKE I MADE (or one I want to avoid)
============================================
For me, the confusing part is the incorrect order of 'if' / 'elif' conditions.
Since placing broad conditions before specific one breaks the logic.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
This connects to the type of game where you choose decision and it 
tailored by how we play it, every decision we made along the way; it shapes
based on the decision and gameplay we had. This leads to using if/elif/else statement,
where every decision create branching timeline and different outcome/output.
"""
