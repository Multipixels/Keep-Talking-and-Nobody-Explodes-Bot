from module import Module

descriptionWords = ["maze"]
isPersistent = False

class MazeModule(Module):
    def __init__(self, widgets):
        self.numbers = {
            'one': 1,
            'two': 2,
            'to': 2,
            'too': 2,
            'three': 3,
            'for' : 4,
            'four': 4,
            'five': 5,
            'six': 6
        }

        self.mazes = ( 
            ( 
                (1, 2), 
                (6, 3), 
                (
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"),
                    ("X", " ", " ", " ", " ", " ", "X", " ", " ", " ", " ", " ", "X"),
                    ("X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X", "X", "X"),
                    ("X", " ", "X", " ", " ", " ", "X", " ", " ", " ", " ", " ", "X"),
                    ("X", " ", "X", " ", "X", "X", "X", "X", "X", "X", "X", " ", "X"),
                    ("X", " ", "X", " ", " ", " ", "X", " ", " ", " ", " ", " ", "X"),
                    ("X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X", " ", "X"),
                    ("X", " ", "X", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X"),
                    ("X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", " ", "X"),
                    ("X", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X", " ", "X"),
                    ("X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X"),
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X")
                )
            ),
            ( 
                (5, 2), 
                (2, 3), 
                (
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"),
                    ("X", " ", " ", " ", " ", " ", "X", " ", " ", " ", " ", " ", "X"),
                    ("X", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X", "X", "X"),
                    ("X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X"),
                    ("X", " ", "X", "X", "X", " ", "X", "X", "X", "X", "X", " ", "X"),
                    ("X", " ", "X", " ", " ", " ", "X", " ", " ", " ", " ", " ", "X"),
                    ("X", " ", "X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X"),
                    ("X", " ", " ", " ", "X", " ", " ", " ", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", "X", "X", " ", "X", "X", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", " ", "X", "X", "X", " ", "X"),
                    ("X", " ", "X", " ", " ", " ", "X", " ", " ", " ", " ", " ", "X"),
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X")
                )
            ),
            ( 
                (4, 4), 
                (6, 4), 
                (
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"),
                    ("X", " ", " ", " ", " ", " ", "X", " ", "X", " ", " ", " ", "X"),
                    ("X", " ", "X", "X", "X", " ", "X", " ", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", " ", " ", " ", "X", " ", "X"),
                    ("X", "X", "X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X"),
                    ("X", " ", " ", " ", "X", " ", "X", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", " ", " ", "X", " ", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X", " ", "X"),
                    ("X", " ", " ", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X"),
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X")
                )
            ),
            ( 
                (1, 1), 
                (1, 4), 
                (
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"),
                    ("X", " ", " ", " ", "X", " ", " ", " ", " ", " ", " ", " ", "X"),
                    ("X", " ", "X", " ", "X", "X", "X", "X", "X", "X", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", " ", " ", " ", " ", " ", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X"),
                    ("X", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", "X", "X", "X", "X", " ", "X", "X", "X", " ", "X"),
                    ("X", " ", "X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"),
                    ("X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", " ", "X"),
                    ("X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", "X", "X", "X", "X", "X", "X", " ", "X", " ", "X"),
                    ("X", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X", " ", "X"),
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X")
                )
            ),
            ( 
                (5, 3), 
                (4, 6), 
                (
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"),
                    ("X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"),
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", " ", "X", " ", "X"),
                    ("X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", "X", "X", "X", "X", " ", "X", "X", "X", "X", "X"),
                    ("X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X"),
                    ("X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", " ", " ", " ", " ", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", "X", "X", "X", "X", " ", "X", "X", "X", " ", "X"),
                    ("X", " ", "X", " ", " ", " ", " ", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", "X", "X", "X", "X", "X", "X", " ", "X"),
                    ("X", " ", "X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"),
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X")
                )
            ),
            ( 
                (5, 1), 
                (3, 5), 
                (
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"),
                    ("X", " ", "X", " ", " ", " ", "X", " ", " ", " ", " ", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", "X", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", " ", "X", "X", "X", " ", "X"),
                    ("X", " ", " ", " ", "X", " ", "X", " ", "X", " ", " ", " ", "X"),
                    ("X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X", "X", "X"),
                    ("X", " ", " ", " ", "X", " ", " ", " ", "X", " ", "X", " ", "X"),
                    ("X", "X", "X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X"),
                    ("X", " ", " ", " ", "X", " ", "X", " ", "X", " ", " ", " ", "X"),
                    ("X", " ", "X", "X", "X", "X", "X", " ", "X", "X", "X", " ", "X"),
                    ("X", " ", " ", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X"),
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X")
                )
            ),
            ( 
                (2, 1), 
                (2, 6), 
                (
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"),
                    ("X", " ", " ", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X"),
                    ("X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", "X", "X", "X", "X", "X", "X", " ", "X"),
                    ("X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X"),
                    ("X", "X", "X", "X", "X", " ", "X", "X", "X", " ", "X", "X", "X"),
                    ("X", " ", " ", " ", "X", " ", " ", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", " ", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", "X", "X", "X", "X", "X", "X", " ", "X", " ", "X"),
                    ("X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"),
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X")
                )
            ),
            ( 
                (4, 1), 
                (3, 4), 
                (
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"),
                    ("X", " ", "X", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X"),
                    ("X", " ", "X", " ", "X", "X", "X", " ", "X", " ", "X", " ", "X"),
                    ("X", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X", " ", "X"),
                    ("X", " ", "X", " ", " ", " ", " ", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", " ", " ", "X", " ", " ", " ", " ", " ", "X"),
                    ("X", " ", "X", "X", "X", " ", "X", "X", "X", "X", "X", "X", "X"),
                    ("X", " ", "X", " ", "X", " ", " ", " ", " ", " ", " ", " ", "X"),
                    ("X", " ", "X", " ", "X", "X", "X", "X", "X", "X", "X", "X", "X"),
                    ("X", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"),
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X")
                )
            ),
            ( 
                (3, 2), 
                (1, 5), 
                (
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"),
                    ("X", " ", "X", " ", " ", " ", " ", " ", " ", " ", " ", " ", "X"),
                    ("X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", " ", " ", "X", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", "X", "X", " ", "X", " ", "X"),
                    ("X", " ", " ", " ", " ", " ", "X", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", "X", "X", "X", "X", " ", "X", "X", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", "X", "X", "X", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", " ", " ", " ", "X", " ", "X"),
                    ("X", " ", "X", " ", "X", " ", "X", " ", "X", " ", "X", "X", "X"),
                    ("X", " ", " ", " ", "X", " ", " ", " ", "X", " ", " ", " ", "X"),
                    ("X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X")
                )
            ),
        )

        self.positions = []

    def logic(self):
        speechOutput = ""

        #Input will be Xmarker, Ymarker, *Xmarker2*, *YMarker2*, XTarget, YTarget, XPlayer, YPlayer
        if len(self.positions) != 6 and len(self.positions) != 8:
            speechOutput = "I didn't hear that correctly, try again."
            return [-1, speechOutput]

        markerPosition = (self.positions[0], self.positions[1])
        targetPosition = (self.positions[-2], self.positions[-1])
        playerPosition = (self.positions[-4], self.positions[-3])

        self.currentMaze = -1

        for maze in self.mazes:
            if maze[0] == markerPosition or maze[1] == markerPosition:
                self.currentMaze = maze[2]
                break
        
        if self.currentMaze == -1:
            speechOutput = f"I couldn't find maze with marker position {markerPosition[0]}, {markerPosition[1]}."
            return [-1, speechOutput]

        realPlayerPosition = (playerPosition[1] * 2 - 1, playerPosition[0] * 2 - 1)
        self.realTargetPosition = (targetPosition[1] * 2 - 1, targetPosition[0] * 2 - 1)

        self.labels = []

        self.__recurseMaze([], realPlayerPosition)
        
        for letter in self.labels:
            speechOutput += letter

        return [0, speechOutput]

    def __recurseMaze(self, visited, position):
        if position in visited:
            return -1

        visited.append(position)

        if position == self.realTargetPosition:
            return visited

        if self.currentMaze[position[0] + 1][position[1]] == " ":
            self.labels.append("down, ")
            if self.__recurseMaze(visited, (position[0] + 2, position[1])) != -1:
                return visited
            del self.labels[-1]

        if self.currentMaze[position[0] - 1][position[1]] == " ":
            self.labels.append("up, ")
            if self.__recurseMaze(visited, (position[0] - 2, position[1])) != -1:
                return visited
            del self.labels[-1]

        if self.currentMaze[position[0]][position[1] + 1] == " ":
            self.labels.append("right, ")
            if self.__recurseMaze(visited, (position[0], position[1] + 2)) != -1:
                return visited
            del self.labels[-1]

        if self.currentMaze[position[0]][position[1] - 1] == " ":
            self.labels.append("left, ")
            if self.__recurseMaze(visited, (position[0], position[1] - 2)) != -1:
                return visited
            del self.labels[-1]

        del visited[-1]
        return -1

    def solve(self, rawInput):
        for word in rawInput.split():
            if word in self.numbers:
                self.positions.append(self.numbers[word])

        output = self.logic()
        return output