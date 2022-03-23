"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:創作理念- 模仿hello kitty，但因為沒有足夠的時間研究多邊形與圓弧，變成一隻可怕的貓
    """
    window = GWindow(width=800, height=400)

    background = GRect(800, 400)
    background.filled = True
    background.fill_color = 'blue'

    face = GOval(200, 100, x=50, y=150)
    face.filled = True
    face.fill_color = 'white'

    left_ear = GPolygon()
    left_ear.add_vertex((50, 180))
    left_ear.add_vertex((60, 130))
    left_ear.add_vertex((100, 160))
    left_ear.filled = True
    left_ear.fill_color = 'white'

    right_ear = GPolygon()
    right_ear.add_vertex((250, 180))
    right_ear.add_vertex((240, 130))
    right_ear.add_vertex((200, 160))
    right_ear.filled = True
    right_ear.fill_color = 'white'

    left_eye = GOval(10, 20)
    left_eye.filled = True
    left_eye.fill_color = 'black'
    
    right_eye = GOval(10, 20)
    right_eye.filled = True
    right_eye.fill_color = 'black'

    whisker_l1 = GArc(30,3,0,10)
    whisker_l1.color = 'black'

    nose = GOval(20, 10)
    nose.color = 'black'
    nose.filled = True
    nose.fill_color = 'yellow'

    window.add(background)
    window.add(face)
    window.add(left_ear)
    window.add(right_ear)
    window.add(left_eye, x=100, y=180)
    window.add(right_eye, x=200, y=180)
    window.add(nose, x=140, y=195)
    window.add(whisker_l1, x= 80, y=180)



if __name__ == '__main__':
    main()
