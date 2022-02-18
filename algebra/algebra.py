from ctypes import pointer
from manim import *

class AddNumber(Scene):

  def construct(self):
    x_axis = NumberLine(
      x_range=[-2, 6, 1],
      stroke_width=4.0,
      length=12,
      include_numbers=True
    )

    tracker = ValueTracker(-1.5)

    # Pointer
    pointer = Triangle(
      fill_color=YELLOW,
      fill_opacity=1.0,
      stroke_width=0.0
    ).scale(0.2)\
    .add_updater(
      lambda m: m.next_to(x_axis.n2p(tracker.get_value()), DOWN)
    )

    labelX = MathTex("x = ").add_updater(lambda m: m.next_to(pointer, DOWN))
    number = DecimalNumber().set_color(WHITE)\
    .add_updater(
      lambda m: m.next_to(labelX, RIGHT)
    )\
    .add_updater(
      lambda m: m.set_value(tracker.get_value())
    )

    vec = Vector(x_axis.n2p(4) - x_axis.n2p(0))
    vec.align_to(x_axis.n2p(-1.5), LEFT)
    vec.shift(UP * 0.5)
    vec.set_stroke(color=ORANGE, width=8)
    vec.set_fill(color=ORANGE)
    labelVec = MathTex("+ 4").move_to(vec, UP).shift(UP * 0.5).set_color(color=ORANGE)

    self.add(x_axis, pointer, labelX, number, vec, labelVec)

    self.wait(1)
    self.play(tracker.animate.increment_value(4.0))
    self.wait(1)

class AddRange(Scene):
  def construct(self):
    x_axis = NumberLine(
      x_range=[6, 18, 1],
      stroke_width=4.0,
      length=12,
      include_numbers=True,
      label_direction=np.array([ 0., -1.5, 0.])
    )

    tracker = ValueTracker(7)

    len = (x_axis.n2p(11) - x_axis.n2p(7))[0]
    rect = Rectangle(
      width=len,
      height=0.5,
      stroke_width=0
    ).set_fill(color=YELLOW, opacity=0.75)\
    .add_updater(
      lambda m: m.align_to(x_axis.n2p(tracker.get_value()), LEFT)
    )

    pointerMin = Triangle(
      fill_color=WHITE,
      fill_opacity=1.0,
      stroke_width=0.0
    ).scale(0.2)\
    .add_updater(
      lambda m: m.next_to(x_axis.n2p(tracker.get_value()), DOWN * 3.0)
    )
    pointerMax = Triangle(
      fill_color=WHITE,
      fill_opacity=1.0,
      stroke_width=0.0
    ).scale(0.2)\
    .add_updater(
      lambda m: m.next_to(
        x_axis.n2p(tracker.get_value()) + [len, 0, 0],
        DOWN * 3.0
      )
    )

    labelMin = MathTex("a +").add_updater(lambda m: m.next_to(pointerMin, DOWN))
    minNumber = DecimalNumber().set_color(WHITE)\
    .add_updater(
      lambda m: m.next_to(labelMin, RIGHT * 0.5).set_value(tracker.get_value() - 7.0)
    )

    labelMax = MathTex("b + ").add_updater(lambda m: m.next_to(pointerMax, DOWN))
    maxNumber = DecimalNumber().set_color(WHITE)\
    .add_updater(
      lambda m: m.next_to(labelMax, RIGHT * 0.5).set_value(tracker.get_value() - 7.0)
    )

    self.add(
      x_axis,
      rect,
      pointerMin,
      labelMin,
      minNumber,
      pointerMax,
      labelMax,
      maxNumber
    )

    self.wait(1)
    self.play(tracker.animate.increment_value(4.0))
    self.wait(2)
