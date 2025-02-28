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

# Create aly_poems.txt file with all 50 poems
poems_text = """The CAD Whisperer
Aly’s got hands that sketch with grace,
SolidWorks bends at his pace.
Blueprints turn from thought to steel,
Precision’s touch, a mastered feel.

The Tesla Effect
In Fremont’s walls, he left his mark,
A jig, a rack, a storage spark.
Saved some cash, improved a line,
Made a bumper fit just fine.

FMEA Dreams
A failure’s chance he seeks to tame,
Risk assessment’s not a game.
Designs refined, defects are few,
Six Sigma green, he’ll see it through.

3D Print King
From polymers to metal beams,
His printer hums in vibrant schemes.
If you need a prototype,
Aly’s got you—built just right!

Arduino Nights
Circuits hum, the code runs tight,
Sensors blink into the night.
A walking aid, a gas alarm,
Aly’s tech keeps folks from harm.

McMaster Grind
Four long years, plus one more,
Equations, stress, and coffee galore.
But soon a title, crisp and clean:
“Aly Pirbay, Eng Machine.”

Dancing Engineer
Sparks may fly in factories grand,
But have you seen this man first-hand?
On the dance floor, watch him go—
A rhythm-filled kinetic show!

The Chess Gambit
A knight, a pawn, a queen so fierce,
Strategic mind that cuts and pierces.
An engineer by day, no less,
But also quite the game of chess.

Lean Six Sigma Date
Aly planned the perfect date,
Minimized delays—wasn’t late.
Optimized each step with care,
But forgot to bring a chair…

Built to Last
Some build bridges, some build dreams,
Aly does both, or so it seems.
His hands create, his mind refines,
A world designed with sharper lines.

Chasing the Stars
From Tesla’s halls to nuclear sites,
He learns, he grows, he soars in flight.
His work speaks loud, his dreams run high,
The future shines in Aly’s eye.

Blueprints & Purpose
Machines may rust, designs may fade,
But impact stays in those he’s made.
Each bolt, each plan, each coded line,
A world improved, one step at a time.

From Sketch to Reality
A drawing first, then comes the steel,
Aly’s hands shape what we feel.
From simple gears to grand design,
Tomorrow’s world is partly mine.

The Racing Baja Beat
Drivetrain roars, the tires spin,
Aly grins—it’s time to win.
Gears engage, acceleration bright,
This car was made to fly tonight.

The Internship Saga
Tesla called, he took the flight,
California’s sun shone bright.
Made a jig, improved a line,
Saved them cash—a job divine!

The Toastmaster
Aly steps up, the crowd leans in,
Confidence bold, a wry little grin.
A speech well-crafted, no wasted space,
Words engineered with perfect grace.

The Chessboard Blueprint
Plan ahead, think in three,
Moves designed geometrically.
Every piece a perfect part,
Strategy’s an engineer’s art.

The Mechanical Dancer
Fluid moves, the timing clean,
A waltz of bolts, a twist machine.
Each step refined, a fine design,
Dance and physics intertwine.

The Engineer of My Heart
You sketch designs with perfect grace,
But darling, none can match your face.
No blueprint made, no CAD design,
Could shape a love as true as mine.

Algorithm of Love
If love’s a code, then I have found,
That every loop brings you around.
Each function calls your name so true,
A program built for me and you.

A Love Designed to Last
No finite state, no brittle steel,
Just something strong, a love that’s real.
Through tensile strain and stress we go,
Yet here we stand, unbreakable.

MISA’s Guiding Light
At MISA’s heart, he leads the way,
Helping students find their say.
With wisdom, care, and time so free,
Aly builds community.

The Big-Lil Sib Champion
Frosh and seniors, paired as one,
Aly makes sure they have fun.
With every challenge, bond, and test,
He proves that MISA’s got the best.

The Resume Wizard
Aly scans each resume tight,
Fixing wording, making it right.
Mock interviews with tips so true,
He helps them land what they pursue.

The Interview Ace
Confidence high, a firm handshake,
Aly preps them, no mistake.
With all his help, they stand so tall,
Ready to ace their career call.

The MISA Legacy
One day he’ll leave, but not in vain,
His impact here will long remain.
Big-Lil bonds and careers set right,
Aly’s legacy burns bright.
"""

with open("aly_poems.txt", "w", encoding="utf-8") as f:
    f.write(poems_text)