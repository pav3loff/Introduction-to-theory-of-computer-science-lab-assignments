import sys


# Prints given automata definition
def printAutomataDefinition(raw_input_strings, states, \
                            symbols, acceptables, \
                            start_state, raw_transitions):
    print("AUTOMATA DEFINITION:")
    print("+---------------------------+")
    print("Input strings:")
    for input_string in raw_input_strings:
        print("\t", input_string)
    print("States:")
    for state in states:
        print("\t", state)
    print("Symbols:")
    for symbol in symbols:
        print("\t", symbol)
    print("Acceptable states:")
    for acceptable in acceptables:
        print("\t", acceptable)
    print("Starting state:", start_state)
    print("Transitions:")
    for transition in raw_transitions:
        print("\t", transition)
    print("+---------------------------+")

    
# Returns list of lists of input symbols
def inputStringCreator(raw_input_strings):
    input_strings = list()
    for input_string in raw_input_strings:
        input_strings.append(list(input_string.split(",")))

    return input_strings


# Returns list of triplets (current_state, transition, next_state)
def transitionCreator(raw_transitions):
    transitions = list()
    for transition in raw_transitions:
        (state_symbol, next_state) = transition.split("->")
        (state, symbol) = state_symbol.split(",")
        transitions.append((state, symbol, next_state))

    return transitions
    

# Returns set of states and their epsilon transition states
def getEpsilonTransitions(current_states, transitions):
    new_states = set()
    current_states = set(current_states)

    while True:
        new_states.clear()
        for state in current_states:
            for transition in transitions:
                if(state == transition[0] and str(transition[1]) == "$"):
                    next_states = list(transition[2].split(","))
                    for next_state in next_states:
                        if(str(next_state) != "#"):
                            new_states.add(next_state)

        if(len(new_states) == 0 or new_states.issubset(current_states)):
            break
        current_states = current_states.union(new_states)

    return current_states
    

# Returns set of next states (epsilon transition states included)
def getNextStates(current_states, symbol, transitions):
    new_states = set()
    old_current_states = set()
    old_current_states = old_current_states.union(current_states)
    current_states = list(current_states)

    for state in current_states:
        for transition in transitions:
            if(state == transition[0] and symbol == transition[1]):
                next_states = list(transition[2].split(","))
                for next_state in next_states:
                    if(str(next_state) != "#"):
                        new_states.add(next_state)
    
    for state in new_states:
        current_states.append(state)

    for state in old_current_states:
        current_states.remove(state)
        
    current_states = getEpsilonTransitions(current_states, transitions)

    return current_states


automata_definition = list()

# Reads automata definition from standard input
for line in sys.stdin:
    if(len(line.strip()) != 0):
        automata_definition.append(line.strip())

raw_input_strings = list(automata_definition[0].split("|"))
states = list(automata_definition[1].split(","))
symbols = list(automata_definition[2].split(","))
acceptables = list(automata_definition[3].split(","))
start_state = automata_definition[4]
raw_transitions = list()

for i in range(5, len(automata_definition)):
    raw_transitions.append(automata_definition[i])

printAutomataDefinition(raw_input_strings, states, \
                        symbols, acceptables, \
                        start_state, raw_transitions)


# Automata simulation
transitions = transitionCreator(raw_transitions)

input_strings = inputStringCreator(raw_input_strings)
row_count = 0

print("SIMULATION:")
print("+---------------------------+")
for input_string in input_strings:
    row_count += 1
    result = "0" + str(row_count) + " "
    start_states = set()
    start_states.add(start_state)

    start_states = getEpsilonTransitions(start_states, transitions)

    start_states = sorted(list(start_states))
    for i in range(0, len(start_states)):
        if(i == 0):
            result += str(start_states[i])
        else:
            result += "," + start_states[i]
    result += "|"

    current_states = set(start_states)
    count = 0

    for symbol in input_string:
        count += 1
        next_states = getNextStates(current_states, symbol, transitions)
        next_states = sorted(list(next_states))

        if(len(next_states) == 0):
            result += "#"
        else:
            for i in range(0, len(next_states)):
                if(i == 0):
                    result += str(next_states[i])
                else:
                    result += "," + next_states[i]

        current_states = set(next_states)
        if(count < len(input_string)):
           result += "|"

    print(result)
