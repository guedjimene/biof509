"""
Do a mouseclick somewhere, move the mouse to some destination, release
the button.  This class gives click- and release-events and also draws
a line or a box from the click-point to the actual mouseposition
(within the same axes) until the button is released.  Within the
method 'self.ignore()' it is checked wether the button from eventpress
and eventrelease are the same.

"""
from matplotlib.widgets import RectangleSelector
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook


def line_select_callback(eclick, erelease):
    'eclick and erelease are the press and release events'
    x1, y1 = eclick.xdata, eclick.ydata
    x2, y2 = erelease.xdata, erelease.ydata
    print ("(%3.2f, %3.2f) --> (%3.2f, %3.2f)" % (x1, y1, x2, y2))
    print (" The button you used were: %s %s" % (eclick.button, erelease.button))

    
def toggle_selector(event):
    print (' Key pressed.')
    if event.key in ['Q', 'q'] and toggle_selector.RS.active:
        print (' RectangleSelector deactivated.')
        toggle_selector.RS.set_active(False)
    if event.key in ['A', 'a'] and not toggle_selector.RS.active:
        print (' RectangleSelector activated.')
        toggle_selector.RS.set_active(True)


        
image_file = cbook.get_sample_data('grace_hopper.png')
image = plt.imread(image_file)
fig, current_ax = plt.subplots()
plt.imshow(image)
toggle_selector.RS = RectangleSelector(current_ax, 
        line_select_callback,
        drawtype='box', useblit=True,
        button=[1,3], # don't use middle button
        minspanx=5, minspany=5,
        spancoords='pixels')
plt.connect('key_press_event', toggle_selector)
plt.show()
