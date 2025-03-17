def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
   # move_and_put()
    #come_back_karel()
    #check_above_line()
    put_all()

def put_all():
    while left_is_clear():
        move_and_put()
        come_back_karel()
        check_above_line()
    move_and_put()



def trun_right():
    turn_left()
    turn_left()
    turn_left()


def move_and_put():
    while front_is_clear():
        put_beeper()
        #if front_is_clear():
        move()
    put_beeper()

def come_back_karel():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
    turn_left()


def check_above_line():
    if left_is_clear():
        turn_left()
        move()
        turn_left()
        turn_left()
        turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()