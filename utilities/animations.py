import animation

wheel = ('-', '/', '|', '\\')


@animation.wait(wheel)
def long_running_function():
    return


long_running_function()
