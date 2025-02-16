import tkinter as tk
import random

# Load poems from the text file
def load_poems(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read().strip().split("\n\n")

# Display a random poem
def show_random_poem():
    poem.set(random.choice(poems))

# Load poems
poems = load_poems("aly_poems.txt")

# GUI setup
root = tk.Tk()
root.title("Random Poem Generator")
root.geometry("600x400")

poem = tk.StringVar()
poem.set("Click the button to get a poem!")

poem_label = tk.Label(root, textvariable=poem, wraplength=550, justify="left")
poem_label.pack(pady=20)

button = tk.Button(root, text="Generate Poem", command=show_random_poem)
button.pack()

root.mainloop()

# Create aly_poems.txt file with all 60 poems
poems_text = """1. The CAD Whisperer
Aly’s got hands that sketch with grace,
SolidWorks bends at his pace.
Blueprints turn from thought to steel,
Precision’s touch, a mastered feel.

...

50. Legacy in Motion
Things may change, designs may grow,
But Aly’s mark will always show.

51. The Engineer of My Heart
You sketch designs with perfect grace,
But darling, none can match your face.
No blueprint made, no CAD design,
Could shape a love as true as mine.

52. Love in Motion
Like gears that turn in perfect sync,
Our hearts align, no missing link.
A system strong, designed to last,
My love for you is unsurpassed.

53. Voltage of My Soul
Your touch, a current through my veins,
A spark of love I can’t contain.
Resistors fail, I’m drawn so near,
Oh Aly, darling, you're my dear.

54. The Gravity of You
Like physics bound by Newton’s law,
I fall for you without a flaw.
No force can pull me back again,
For you, my love, my heart ascends.

55. My Constant Variable
In a world of change, equations bend,
But you're my constant, my dearest friend.
No need to solve for X or Y,
For love like ours will never die.

56. Heat Transfer of Love
Like metal glowing, burning bright,
You radiate your warmth and light.
No insulation stops the way,
Your love just melts my heart away.

57. Kinetic Devotion
You move, I follow, step in time,
Like forces drawn in pure design.
No friction here, just smooth embrace,
Forever locked in love’s own race.

58. The Torque of My Heart
You spin my world, my heart’s delight,
With just one glance, you turn it right.
The force you bring, the love you show,
My axis shifts—I’m yours to hold.

59. Algorithm of Love
If love’s a code, then I have found,
That every loop brings you around.
Each function calls your name so true,
A program built for me and you.

60. A Love Designed to Last
No finite state, no brittle steel,
Just something strong, a love that’s real.
Through tensile strain and stress we go,
Yet here we stand, unbreakable.
"""

with open("aly_poems.txt", "w", encoding="utf-8") as f:
    f.write(poems_text)
