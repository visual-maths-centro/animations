from manim import *

def createRange(a, b, axis, text_a="a", text_b="b"):
  rect = Rectangle(
    width=(axis.n2p(b) - axis.n2p(a))[0],
    height=0.5,
    stroke_width=0
  ).set_fill(color=YELLOW, opacity=0.75)\
  .align_to(axis, UP)\
  .shift(UP * 0.15)\
  .align_to(axis.n2p(a), LEFT)

  pointer_min = Triangle(
    fill_color=WHITE,
    fill_opacity=1.0,
    stroke_width=0.0
  ).scale(0.2)\
  .next_to(axis.n2p(a), DOWN * 3.0)

  label_min = MathTex(text_a).add_updater(lambda m: m.next_to(pointer_min, DOWN))

  pointer_max = Triangle(
    fill_color=WHITE,
    fill_opacity=1.0,
    stroke_width=0.0
  ).scale(0.2)\
  .next_to(axis.n2p(b), DOWN * 3.0)

  label_max = MathTex(text_b).add_updater(lambda m: m.next_to(pointer_max, DOWN))

  return (rect, pointer_min, pointer_max, label_min, label_max)

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

    label_x = MathTex("x = ").add_updater(lambda m: m.next_to(pointer, DOWN))
    number = DecimalNumber().set_color(WHITE)\
    .add_updater(
      lambda m: m.next_to(label_x, RIGHT)
    )\
    .add_updater(
      lambda m: m.set_value(tracker.get_value())
    )

    vec = Vector(x_axis.n2p(4) - x_axis.n2p(0))
    vec.align_to(x_axis.n2p(-1.5), LEFT)
    vec.shift(UP * 0.5)
    vec.set_stroke(color=ORANGE, width=8)
    vec.set_fill(color=ORANGE)
    label_vec = MathTex("+ 4").move_to(vec, UP).shift(UP * 0.5).set_color(color=ORANGE)

    self.add(x_axis, pointer, label_x, number, vec, label_vec)

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

    (rect, pointer_min, pointer_max, label_min, label_max) = createRange(
      7,
      11,
      x_axis,
      "a +",
      "b +"
    )

    tracker = ValueTracker(7)

    len = (x_axis.n2p(11) - x_axis.n2p(7))[0]
    rect.add_updater(
      lambda m: m.align_to(x_axis.n2p(tracker.get_value()), LEFT)
    )

    pointer_min.add_updater(
      lambda m: m.next_to(x_axis.n2p(tracker.get_value()), DOWN * 3.0)
    )

    pointer_max.add_updater(
      lambda m: m.next_to(
        x_axis.n2p(tracker.get_value()) + [len, 0, 0],
        DOWN * 3.0
      )
    )

    min_number = DecimalNumber().set_color(WHITE)\
    .add_updater(
      lambda m: m.next_to(label_min, RIGHT * 0.5).set_value(tracker.get_value() - 7.0)
    )
    max_number = DecimalNumber().set_color(WHITE)\
    .add_updater(
      lambda m: m.next_to(label_max, RIGHT * 0.5).set_value(tracker.get_value() - 7.0)
    )

    self.add(
      x_axis,
      rect,
      pointer_min,
      label_min,
      min_number,
      pointer_max,
      label_max,
      max_number
    )

    self.wait(1)
    self.play(tracker.animate.increment_value(4.0))
    self.wait(1)

class LenRange(Scene):

  def construct(self):
    x_axis = NumberLine(
      x_range=[0, 8, 1],
      stroke_width=4.0,
      length=12,
      include_numbers=True,
      label_direction=np.array([ 0., -1.5, 0.])
    )

    rect_a = Rectangle(
      width=(x_axis.n2p(2.5) - x_axis.n2p(0))[0],
      height=0.5,
      stroke_width=0
    ).set_fill(color=YELLOW, opacity=0.5)\
    .move_to(x_axis.n2p(0), LEFT)
    rect_b = Rectangle(
      width=(x_axis.n2p(7) - x_axis.n2p(0))[0],
      height=0.5,
      stroke_width=0
    ).set_fill(color=BLUE, opacity=0.5)\
    .move_to(x_axis.n2p(0), LEFT)

    pointer_min = Triangle(
      fill_color=WHITE,
      fill_opacity=1.0,
      stroke_width=0.0
    ).scale(0.2)\
    .next_to(x_axis.n2p(2.5), DOWN * 3.0)
    label_min = MathTex("a").next_to(pointer_min, DOWN)

    pointer_max = Triangle(
      fill_color=WHITE,
      fill_opacity=1.0,
      stroke_width=0.0
    ).scale(0.2)\
    .next_to(x_axis.n2p(7), DOWN * 3.0)
    label_max = MathTex("b").next_to(pointer_max, DOWN)

    self.add(
      x_axis,
      rect_a,
      rect_b,
      pointer_min,
      label_min,
      pointer_max,
      label_max
    )

class MultiplyRange(Scene):
  def construct(self):
    x_axis_a = NumberLine(
      x_range=[-8, 8, 1],
      stroke_width=4.0,
      length=12,
      include_numbers=True,
      label_direction=np.array([ 0., -1.5, 0.])
    )\
    .move_to(UP * 1.25)

    (
      rect_a,
      pointer_min_a,
      pointer_max_a,
      label_min_a,
      label_max_a
    ) = createRange(-2, 3, x_axis_a)
    rect_a_s = createRange(-4, 6, x_axis_a)[0]

    pointer_min_a.add_updater(
      lambda m: m.next_to(rect_a.get_left(), DOWN).shift(DOWN * 0.5)
    )
    pointer_max_a.add_updater(
      lambda m: m.next_to(rect_a.get_right(), DOWN).shift(DOWN * 0.5)
    )

    label_2x = MathTex("[2a, 2b]").next_to(x_axis_a, UP * 1.75)

    x_axis_b = NumberLine(
      x_range=[-3, 3, 0.5],
      stroke_width=4.0,
      length=12,
      include_numbers=True,
      label_direction=np.array([ 0., -1.5, 0.])
    )\
    .move_to(DOWN * 2.0)

    (
      rect_b,
      pointer_min_b,
      pointer_max_b,
      label_min_b,
      label_max_b
    ) = createRange(-2.0, 3.0, x_axis_b)
    rect_b.set_fill(color=ORANGE)

    rect_b_s = createRange(-0.5, 0.75, x_axis_b)[0]
    rect_b_s.set_fill(color=ORANGE)

    pointer_min_b.add_updater(
      lambda m: m.next_to(rect_b.get_left(), DOWN).shift(DOWN * 0.5)
    )
    pointer_max_b.add_updater(
      lambda m: m.next_to(rect_b.get_right(), DOWN).shift(DOWN * 0.5)
    )

    label_75x = MathTex("[0.25a, 0.25b]").next_to(x_axis_b, UP * 1.75)

    self.add(
      x_axis_a,
      rect_a,
      pointer_min_a,
      pointer_max_a,
      label_min_a,
      label_max_a,
      label_2x,

      x_axis_b,
      rect_b,
      pointer_min_b,
      pointer_max_b,
      label_min_b,
      label_max_b,
      label_75x
    )

    self.wait(1)

    self.play(
      ReplacementTransform(rect_a, rect_a_s),
      ReplacementTransform(rect_b, rect_b_s)
    )

    self.wait(1)
