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

    pointer = Triangle(
      fill_color=YELLOW,
      fill_opacity=1.0,
      stroke_width=0.0
    ).scale(0.2)
    labelX = MathTex("x = ").add_updater(lambda m: m.next_to(pointer, DOWN))

    number = DecimalNumber().set_color(WHITE)

    vec = Vector(x_axis.n2p(4) - x_axis.n2p(0))
    vec.align_to(x_axis.n2p(-1.5), LEFT)
    vec.shift(UP * 0.5)
    vec.set_stroke(color=ORANGE, width=8)
    vec.set_fill(color=ORANGE)
    labelVec = MathTex("+ 4").move_to(vec, UP).shift(UP * 0.5).set_color(color=ORANGE)

    pointer.add_updater(
      lambda m: m.next_to(x_axis.n2p(tracker.get_value()), DOWN)
    )

    number.add_updater(
      lambda m: m.next_to(labelX, RIGHT)
    )

    number.add_updater(
      lambda m: m.set_value(tracker.get_value())
    )

    self.add(x_axis, pointer, labelX, number, vec, labelVec)

    self.wait(1)
    self.play(tracker.animate.increment_value(4.0))
    self.wait(1)

class AddRange(Scene):
  def construct(self):
    return super().construct()