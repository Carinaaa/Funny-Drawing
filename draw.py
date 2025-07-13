import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider

from turtle import Turtle, Screen, clearscreen, colormode

threshold1 = 100
threshold2 = 200

img = cv.imread("_NKL5841.jpg")
assert img is not None, "File could not be read, check with os.path.exists()"
edges = cv.Canny(img, threshold1, threshold2)

fig, (ax1, ax2) = plt.subplots(1,2)
ax1.axis('off')
ax2.axis('off')
plt.subplots_adjust(bottom=0.4)
org_pic = ax1.imshow(img, cmap='gray')
edge_pic = ax2.imshow(edges, cmap='gray')


slider_ax = plt.axes([0.2, 0.15, 0.6, 0.03])
slider_ay = plt.axes([0.2, 0.05, 0.6, 0.03])

x_slider = Slider(
    ax=slider_ax,
    label='Threshold 1',
    valmin=0,
    valmax=300,
    valinit=0,
    valstep=10
)

y_slider = Slider(
    ax=slider_ay,
    label='Threshold 2',
    valmin=0,
    valmax=300,
    valinit=0,
    valstep=10
)
# Update function
def update(frame_idx):
    t1 = x_slider.val
    t2 = y_slider.val
    new_edges = cv.Canny(img, t1, t2)
    edge_pic.set_data(new_edges)
    fig.canvas.draw_idle()

# Connect slider to update function
x_slider.on_changed(update)
y_slider.on_changed(update)

image_data = edge_pic.get_array()
print(np.min(image_data), np.max(image_data))  # Should be 0-255 (or 0-1)
cv.imwrite("output.png", image_data)
np.savetxt('basic_array.csv', image_data, delimiter=',')

plt.show()

tim = Turtle()
tim.penup()
tim.goto(-(image_data.shape[1]/2-20),image_data.shape[0]/2-20)
screen = Screen()
screen.setup(height=image_data.shape[0]*1.5,width=image_data.shape[1]*2)

tim.speed("fastest")

for (i, j), pixel in np.ndenumerate(image_data):
    print((i,j))
    print(pixel)
    tim.penup()
    if pixel == 255:
        if i % 10 == 0:
            tim.pendown()
            #tim.pencolor("pink")
            tim.dot(5, "black")
            tim.penup()
            tim.goto(j-image_data.shape[0]/2-200,-i+(image_data.shape[1]/2)+100)

screen.exitonclick()


