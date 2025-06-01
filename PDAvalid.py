# Mohammed Murtuza
# MMM263, 31586302
# Section Number 002
# Spring 2025
# Professor Arashdeep Kaur

def PDA263(string): # This will be the function that handles the PDA nature of the program
    stack = [] # empty stack as per PDA standards
    str = "" # string to hold the reasoning on why it failed
    transition_count = 1  # incrementing transition for printing transitions neatly
    failstate = ""

    print("="*50)
    print(f"\n{string} is being processed\n")
    flag = False # flag for checking if the PDA fails or not
    state = 'q0' # initialize current state

    for i in string:
        if state == 'q0' and i == 'a': # From here on out, the program will progress through each state and check i which is the current letter in the string as well as the current state and the stack top in some cases
            push = stack.append('z0')
            state = 'q1'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q0")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: z0")
            print(f"- Next State: {state}\n")
            transition_count += 1
                
        elif state == 'q1' and i == 'a':
            stack.append(i)
            state = 'q2'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q1")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: {i}")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q1' and i == 'b':
            stack.append(i)
            state = 'q1'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q1")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: {i}")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q2' and i.isnumeric():
            state = 'q4'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q2")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1
                
        elif state == 'q2' and i == ')':
            failstate = state
            state = 'q9' # in this program, I utilize q9 as a "trap state" so that it is easier to trace when mismatches occur in the code and for it to print the proper reason behind the PDA failing 
            # i labeled didnt draw next to all the if statements that go to q9 as they are not necessary for the diagram but better to implement in the code for proper PDA handling
            print(f"Transition {transition_count}:")
            print(f"- Present State: q2")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q2' and i == '.':
            state = 'q3'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q2")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q2' and i == '(':
            state = 'q2'
            stack.append(i)
            print(f"Transition {transition_count}:")
            print(f"- Present State: q2")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: {i}")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q2' and i.isalpha(): # didnt draw 
            failstate = state
            state = 'q9'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q2")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q2' and i == '+':
            failstate = state
            state = 'q9'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q2")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q2' and i == '*':
            failstate = state
            state = 'q9'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q2")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q3' and i.isnumeric():
            state = 'q5'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q3")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q3' and i.isalpha(): # didnt draw
            failstate = state
            state = 'q9'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q3")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q3' and i == '+': # didnt draw
            failstate = state
            state = 'q9'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q3")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q3' and i == '*': #didnt draw
            failstate = state
            state = 'q9'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q3")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q4' and i == '.':
            state = 'q5'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q4")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q4' and i.isnumeric():
            state = 'q4'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q4")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q4' and i == ')': #didnt draw
            failstate = state
            state = 'q9'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q4")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q5' and i.isnumeric():
            state = 'q5'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q5")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q5' and i == ')' and stack[-1] == '(':
            stack.pop()
            state = 'q6'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q5")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: (")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q5' and i in '+-*/':
            state = 'q2'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q5")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q5' and i == 'a' and stack[-1] == 'a':
            stack.pop()
            state = 'q7'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q5")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: a")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q5' and i == 'a':
            state = 'q7'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q5")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q5' and i == '.':  #didnt draw 
            failstate = state 
            state = 'q9'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q5")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q6' and i in '+-*/':
            state = 'q2'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q6")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q6' and i == ')' and stack[-1] == '(':
            stack.pop()
            state = 'q6'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q6")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: (")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q6' and i == 'a' and stack[-1] == 'a':
            stack.pop()
            state = 'q7'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q6")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: a")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q6' and i == 'a':
            state = 'q7'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q6")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q6' and i == ')':
            state = 'q6'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q6")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q6' and i.isnumeric(): #didnt draw
            failstate = state
            print(f"Transition {transition_count}:")
            print(f"- Present State: q6")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: q9\n")
            state = 'q9'
            transition_count += 1

        elif state == 'q6' and i == '.': #didnt draw
            failstate = state 
            print(f"Transition {transition_count}:")
            print(f"- Present State: q6")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: q9\n")
            state = 'q9'
            transition_count += 1

        elif state == 'q7' and i == 'b' and stack[-1] == 'b':
            stack.pop()
            state = 'q7'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q7")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: b")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q7' and i == 'b':
            state = 'q8'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q7")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: epsilon")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q7' and i == 'a' and stack[-1] == 'z0':
            stack.pop()
            state = 'q8'
            print(f"Transition {transition_count}:")
            print(f"- Present State: q7")
            print(f"- Current input symbol: {i}")
            print(f"- Stack Top: {'epsilon' if not stack else stack[-1]}")
            print(f"- Popped: z0")
            print(f"- Pushed: epsilon")
            print(f"- Next State: {state}\n")
            transition_count += 1

        elif state == 'q8' and not stack:
            print("Accepted\n\n")
            break
        else:
            flag = True
            break

    if flag: # if the PDA fails, it will go here where the reasoning for failing will be printed
        if state == 'q8':
            str = "the stack is not empty."
        elif stack and state == 'q8':
            str = "the stack is not empty."
        elif not string and state != 'q8':
            str = "the string did not reach the final state."
        elif not string and stack and state != 'q8':
            str = "the stack is not empty."
        elif i == ')' and stack[-1] != '(':
            str = f"the stack top ({stack[-1]}) is mismatched with the input symbol: {i}"
        elif i == 'b' and stack[-1] != 'b':
            str = f"the stack top: ({stack[-1]}) is mismatched with the input symbol: {i}"
        elif i == 'a' and stack[-1] == 'b':
            str = f"the stack top: ({stack[-1]}) is mismatched with the input symbol: {i}"
        elif not string and stack:
            str = "the stack is not empty"
        elif state == 'q2' and not string:
            str = "the string ended before reaching the final state q8."
        elif state == 'q9':  # Entering the trap state due to invalid transition
            str = f"Invalid transition at state {failstate} with input '{i}'"
            print(f"The string is in a trap state because {str}")

        print("The PDA has failed.")
        return f"The string {string} is not acceptable by the given PDA because {str} \n"
    elif not stack:
        return f"\nThe string is accepted.\n"

print("Project 2 for CS 341")
print("Section number: 002")
print("Semester: Spring 2025")
print("Written by: Mohammed Murtuza, mmm263")
print("Instructor: Arashdeep Kaur, ak3257@njit.edu")

index = int(input("Enter the number of strings you want to test: "))
for i in range(index):
    print("="*50)
    inp = input(f"Enter string {i+1} of total strings {index}: ")
    result = PDA263(inp)
    print(result)
