#create a class called State which will hold the states(posititons) for the three cannibals, three missionaries, and the boat
class State():
    def __init__(self, cannibalLeft, missionaryLeft, ship, cannibalRight, missionaryRight):
        self.cannibalLeft = cannibalLeft
        self.cannibalRight = cannibalRight
        self.missionaryLeft = missionaryLeft
        self.missionaryRight = missionaryRight
        self.ship = ship
        self.parent = None

    # checking to see if the all the cannibals and missionaries have been moved to the right side of the river
    def isCompleted(self):
        if (self.missionaryLeft == 0 and self.cannibalLeft == 0):
            return True
        else:
            return False

    # checking if the movement done is valid and does not break the rules of the problem
    def isValid(self):
        if(self.missionaryRight + self.missionaryLeft != 3 or self.cannibalRight + self.cannibalLeft != 3) or \
            (self.missionaryLeft < 0 or self.missionaryRight < 0 or self.cannibalRight < 0 or self.cannibalLeft < 0) or \
                (self.cannibalLeft > self.missionaryLeft and self.missionaryLeft > 0) or (self.cannibalRight > self.missionaryRight and self.missionaryRight > 0):
            return False
        else:
            return True

# with this function we will evaluate every single possible move, and determine if its a valid move or not. if the move is valid we append it to an array which we will be using our BFS algorithm on
def moves(self):
    options = []
    # if the ship is on the left, we explore all the options for moves that can occur
    if self.ship == "L":
        # 2 missionaries moving to the right side of the river
        newPositions = State(self.cannibalLeft, self.missionaryLeft - 2, "R", self.cannibalRight, self.missionaryRight +2)
        if newPositions.isValid():
            newPositions.parent = self
            options.append(newPositions)
        
        # 2 cannibals moving to the right side of the river
        newPositions = State(self.cannibalLeft - 2, self.missionaryLeft, "R", self.cannibalRight + 2, self.missionaryRight)
        if newPositions.isValid():
            newPositions.parent = self
            options.append(newPositions)

        # 1 missionsary 1 cannibal moving to the right side of the river
        newPositions = State(self.cannibalLeft - 1, self.missionaryLeft - 1, "R", self.cannibalRight + 1, self.missionaryRight +1)
        if newPositions.isValid():
            newPositions.parent = self
            options.append(newPositions)

        # 1 missionary moving to the right side of the river
        newPositions = State(self.cannibalLeft, self.missionaryLeft - 1, "R", self.cannibalRight, self.missionaryRight +1)
        if newPositions.isValid():
            newPositions.parent = self
            options.append(newPositions)

        # 1 cannibal moving to the right side of the river
        newPositions = State(self.cannibalLeft - 1, self.missionaryLeft, "R", self.cannibalRight + 1, self.missionaryRight)
        if newPositions.isValid():
            newPositions.parent = self
            options.append(newPositions)

        # if the ship is on the right, we explore all the options for moves that can occur
    else:
        # 2 missionaries moving to the left side of the river
        newPositions = State(self.cannibalLeft, self.missionaryLeft + 2, "L", self.cannibalRight, self.missionaryRight - 2)
        if newPositions.isValid():
            newPositions.parent = self
            options.append(newPositions)
        
        # 2 cannibals moving to the left side of the river
        newPositions = State(self.cannibalLeft + 2, self.missionaryLeft, "L", self.cannibalRight - 2, self.missionaryRight)
        if newPositions.isValid():
            newPositions.parent = self
            options.append(newPositions)

        # 1 missionsary 1 cannibal moving to the left side of the river
        newPositions = State(self.cannibalLeft + 1, self.missionaryLeft + 1, "L", self.cannibalRight - 1, self.missionaryRight - 1)
        if newPositions.isValid():
            newPositions.parent = self
            options.append(newPositions)

        # 1 missionary moving to the left side of the river
        newPositions = State(self.cannibalLeft, self.missionaryLeft + 1, "L", self.cannibalRight, self.missionaryRight - 1)
        if newPositions.isValid():
            newPositions.parent = self
            options.append(newPositions)

        # 1 cannibal moving to the left side of the river
        newPositions = State(self.cannibalLeft + 1, self.missionaryLeft, "L", self.cannibalRight - 1, self.missionaryRight)
        if newPositions.isValid():
            newPositions.parent = self
            options.append(newPositions)
        
    return options


# this is our bfs algorithm. We set the initial state with all 6 members and the boat on the left side of the river. Just to make sure we check all edge cases, we check to see if the initial state we have 
# is the completed state we need. The rest is a basic bfs implimentation.
def breadthFirstSearch():
	startState = State(3,3,'L',0,0)

	if startState.isCompleted(): 
		return startState

	queue = []
	explored = []
	queue.append(startState)

	while queue:
		state = queue.pop(0)
		if state.isCompleted():
			return state
		explored.append(state)
		positions = moves(state)
		for position in positions:
			if (position not in explored) or (position not in queue):
				queue.append(position)
                
	return None

# this function just prints the solution to the screen so that you can see it displayed

def displaySolution(solution):
    path = []
    path.append(solution)
    parent = solution.parent
    while parent:
        path.append(parent)
        parent = parent.parent
    
    steps = len(path)
    for i in range(len(path)):
        state = path[len(path)-i -1]
        print(state.cannibalLeft,state.missionaryLeft, state.ship, state.cannibalRight, state.missionaryRight)


#this is where our code is executed
print("Solution to the Cannibals and Missionaries problem")
print("Can-Mis/r/Can-Mis")
solution = breadthFirstSearch()
displaySolution(solution)