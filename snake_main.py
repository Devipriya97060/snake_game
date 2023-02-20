class Box:
    """
    Box of the snake.
    A simple structure for a Snake-block.

    Attributes:
    -----------------
        head : tuple(int, int)
            x,y coordinates of the head of the snake.

        size : tuple(int, int)
            size of the snake.

        colour : tuple(int, int, int)
            r,g,b(colour) of the snake block.

    Methods:
    -----------------
        get_coordinates():
            To get the coordinates of the snake head.

        get_size():
            To returns the size of snake block.

        get_colour():
            Returns the colour of snake block.
    """
    def __init__(self, head, size, colour):
        """Initializing the snake.
        Parameters:
        ------------------------------------------
        head : (int,int)
            The coordinates for top left corner of snake block.

        size : (int, int)
            Size of the block

        colour : (int, int, int)
            RGB (colour code) for colour of snake block.

        """
        self.head = head
        self.size = size
        self.colour = colour

    def get_coordinates(self):
        """Coordinates of block.
         Return: tuple(int, int)
            x-coordinate and y-coordinate of the snake head.
        """
        return self.head

    def get_size(self):
        """Size of block.
         Return: tuple(int, int)
            The dimensions of the block.
        """
        return self.size

    def get_colour(self):
        """Colour of block
         Return: tuple(int, int)
            The colour code of the snake block.
        """
        return self.colour



class Snake:
    """
    Class for whole snake body.
     Attributes:
    -----------------
        size : tuple(int, int)
            The size of the snake.

        colour : tuple(int, int, int)
            Colour of the snake block.

        snake_length : int
            Length of the snake in integers.

        blocks : list(SnakeBlock)
            List of parts of the snake blocks in order.

    Methods:
    -----------------
        move_left():
            The head of the snake moved one block to its left.

        move_right():
            The head of the snake moved one block to its right.

        move_up():
            The head of the snake moved one block up.

        move_down():
            The head of the snake moved one block down.
        
        check_collision(left_top, right_down):
            Check the collision with the given coordinates of object.
        
        check_collision_with_fruit(left_top, right_down):
            Check the collision of snake head with the fruit coordinates.
        
        inside_bounds(left_top, right_down):
            Check if the snake blocks are inside the given points as boundaries.
        
        check_collision_with_self():
            Returns True if snake head collides with its other blocks of the body.
        
        grow(self):
            Other blocks of the snake follow each other in the direction of snake head.

    """
    def __init__(self, head, size, colour):
        """Initialize the snake.
         Parameters:
        ------------------------------------------
        colour : (int, int, int)
            A triple of values between 0 and 255 indicating the r, g, b value of the snake block.

        head : (int, int)
            x-coordinate and y-coordinate values for top left corner of the snake head.

        size : (int, int)
            The width and height of the snake block.
        """

        self.size = size
        self.colour = colour
        self.dict_part = {}
        self.length = 1
        self.dict_part[self.length] = Box(head, self.size, self.colour)

    def move_left(self):
        """Move the head to the left.
        """
        tup = (self.dict_part[1].head[0], self.dict_part[1].head[1])
        xcoor = tup[0]
        ycoor = tup[1]
        for i in range(len(self.dict_part.values()), 1, -1):
            self.dict_part[i].head = self.dict_part[i-1].head
        self.dict_part[1].head = (xcoor - self.size[0], ycoor)


    def move_right(self):
        """Move the head to the right.
        """
        tup = (self.dict_part[1].head[0], self.dict_part[1].head[1])
        xcoor = tup[0]
        ycoor = tup[1]
        for i in range(len(self.dict_part.values()), 1, -1):
            self.dict_part[i].head = self.dict_part[i-1].head
        self.dict_part[1].head = (xcoor + self.size[0], ycoor)


    def move_up(self):
        """Move the head of the snake up.
        """
        tup = (self.dict_part[1].head[0], self.dict_part[1].head[1])
        xcoor = tup[0]
        ycoor = tup[1]
        for i in range(len(self.dict_part.values()), 1, -1):
            self.dict_part[i].head = self.dict_part[i-1].head
        self.dict_part[1].head = (xcoor, ycoor - self.size[1])


    def move_down(self):
        """Move the head of the snake down.
        """
        tup = (self.dict_part[1].head[0], self.dict_part[1].head[1])
        xcoor = tup[0]
        ycoor = tup[1]
        for i in range(len(self.dict_part.values()), 1, -1):
            self.dict_part[i].head = self.dict_part[i-1].head
        self.dict_part[1].head = (xcoor, ycoor + self.size[1])

    def check_collision(self, left_top, right_down):
        """Check if there is a collision.
        Parameters:
            left_top : tuple(int,int)
            right_down : tuple(int,int)

        Return: bool
            True: if Collision happens
            False: if Collision not happens.
        """
        collision = False
        if left_top == self.dict_part[1].head:
            collision = True
        for i in range(1, len(self.dict_part) + 1):
            if (left_top[0] < self.dict_part[i].head[0] < right_down[0] and left_top[1] < self.dict_part[i].head[1] + self.size[1] < right_down[1]) or (left_top[0] < self.dict_part[i].head[0] + self.size[0] < right_down[0] and left_top[1] < self.dict_part[i].head[1] + self.size[1] < right_down[1]):
                collision = True
            if (left_top[0] < self.dict_part[i].head[0] < right_down[0] and left_top[1] < self.dict_part[i].head[1] < right_down[1]) or (left_top[0] < self.dict_part[i].head[0] + self.size[0] < right_down[0] and left_top[1] < self.dict_part[i].head[1] < right_down[1]):
                collision = True
        return collision

    def check_collision_with_fruit(self, left_top, right_down):
        """Check collision with fruit.
        Parameters:
            left_top : tuple(int,int)
            right_down : tuple(int,int)

        Return: bool
            True: if Collide with fruit.
            False: if Not Collide with fruit.
        """
        if self.dict_part[1].head[0] == left_top[0] and self.dict_part[1].head[1] == left_top[1]:
            return True
        return False

    def inside_bounds(self, left_top, right_down):
        """Inside bounds function.
        Parameters:
            left_top : tuple(int,int)
            right_down : tuple(int,int)

        Return: bool
            True: if Inside bounds
            False: if Not inside bounds
        """
        if left_top[0] <= self.dict_part[1].head[0] <= right_down[0] and left_top[1] <= self.dict_part[1].head[1] <= right_down[1] and left_top[0] <= self.dict_part[1].head[0] + self.size[0] <= right_down[0] and left_top[1] <= self.dict_part[1].head[1] <= right_down[1]:
                if left_top[0] <= self.dict_part[1].head[0] <= right_down[0] and left_top[1] <= self.dict_part[1].head[1] + self.size[1] <= right_down[1] and left_top[0] <= self.dict_part[1].head[0] + self.size[0] <= right_down[0] and left_top[1] <= self.blocks[0].head[1] + self.size[1] <= right_down[1]:
        if left_top[0] = self.dict_part[1]:    
            return True
        return False


    def check_collision_with_self(self):
        """Check collision with self.
        Return: bool
            True: if Collide with self
            False: if Not Collide with self
        """
        for i in range(2, len(list(self.dict_part.values()))):
            if self.dict_part[1].head == list(self.dict_part.values())[i].head:
                return True
        return False

    def grow(self):
        """Growth function.

        """
        self.dict_part[self.length+1] = Box(list(self.dict_part.values())[-1].head, self.size, self.colour)
        self.length += 1

    def start_iterator(self):
        '''Iterator class.
        Tol set iterator count -loop to 0.'''
        self.iter = 0

    def __iter__(self):
        """Iterator
        To return the respective Block.

        Return: Class(SnakeBox)
        """
        self.start_iterator()
        return self

    def __next__(self):
        """__next__
        Return: Function(return_block).
        """
        if self.iter < self.length:
            self.iter += 1
            return self.dict_part[self.iter]
        raise StopIteration
