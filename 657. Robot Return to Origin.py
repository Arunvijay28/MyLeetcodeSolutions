def judgeCircle(self, moves: str) -> bool:
        count_x=0
        count_y=0
        for i in moves.lower():
            if i=="u":
                count_x+=1
            elif i=="d":
                count_x-=1
            elif i=="r":
                count_y+=1
            else:
                count_y-=1
        
        return (count_x==0 and count_y==0)


# Example 1:

# Input: moves = "UD"
# Output: true
# Explanation: The robot moves up once, and then down once. All moves have the same magnitude, so it ended up at the origin where it started. Therefore, we return true.

# Example 2:

# Input: moves = "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. We return false because it is not at the origin at the end of its moves.