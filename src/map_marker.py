import turtle as t


def map_marker(x, y):
    marker = t.Turtle()
    marker.shape('circle')
    marker.color('red')
    marker.penup()
    marker.goto(x, y)

    return marker