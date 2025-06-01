# 341-PDA
PDA simulator in Python for validating string patterns involving arithmetic and stack-based matching.

## Pushdown Automaton (PDA) Expression Validator
A Python-based PDA that simulates transitions through a complex grammar of input strings, including alphanumeric characters, parentheses, and arithmetic symbols. Handles multi-state logic and provides a step-by-step trace of transitions. Designed to accept or reject strings based on final state and stack conditions.

## Tech: 
Python, Stack Simulation
## Features:
Manual state transitions through q0–q9,
Stack push/pop logic with custom rules,
Trap state handling and detailed failure reasoning,
Accepts expressions like aab(3.14)+aab and rejects invalid ones
