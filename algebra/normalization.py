from re import M
from manim import *

def create_range(a, b, axis):
  rect = Rectangle(
    width=(axis.n2p(b) - axis.n2p(a))[0],
    height=0.3,
    stroke_width=0
  ).set_fill(color=YELLOW_D, opacity=0.75)\
  .next_to(axis, DOWN, buff=-axis.height * 1.1)\
  .align_to(axis.n2p(a), LEFT)

  return rect

def create_bezier(start, end, color):
  len = np.linalg.norm(start - end)
  bezier = DashedVMobject(CubicBezier(
    start_anchor=start,
    start_handle=start + np.array([0, -len * 0.25, 0]),
    end_handle=end + np.array([0, len * 0.25, 0]),
    end_anchor=end,
    stroke_opacity=0.75,
    stroke_color=color
  ))

  return bezier

def create_curves(start_a, end_a, start_b, end_b, axis_a, axis_b, color=ORANGE):
  left_curve = create_bezier(
    axis_a.n2p(start_a),
    axis_b.n2p(start_b),
    color
  )
  right_curve = create_bezier(
    axis_a.n2p(end_a),
    axis_b.n2p(end_b),
    color
  )

  return (left_curve, right_curve)

class NormalizationA(Scene):
  def construct(self):

    # Axis
    axis_a = NumberLine(
      x_range=[0, 6, 1],
      stroke_width=4.0,
      length=9,
      include_numbers=True
    ).shift(UP * 2.0)\
    .shift(LEFT * 1.25)

    axis_b = NumberLine(
      x_range=[0, 6, 1],
      stroke_width=4.0,
      length=9,
      include_numbers=True
    ).shift(DOWN * 1.5)\
    .shift(LEFT * 1.25)

    # Tracker
    tracker = ValueTracker(2.0)

    # Range A
    range_a = create_range(0, 4, axis_a)

    # Curves
    curves = create_curves(0, 4, 0, 1, axis_a, axis_b)

    # Pointer A
    pointer_a = Triangle(
      fill_color=WHITE,
      fill_opacity=1.0,
      stroke_width=0.0
    ).scale([0.15, -0.15, 0.15])\
    .add_updater(
      lambda m: m.next_to(axis_a.n2p(tracker.get_value()), UP * 1.5)
    )

    # Label and number A
    label_a = MathTex("x = ").add_updater(lambda m: m.next_to(pointer_a, UP))
    number_a = DecimalNumber().set_color(WHITE).add_updater(
      lambda m: m.next_to(label_a, RIGHT).set_value(tracker.get_value())
    )

    # Range B
    range_b = create_range(0, 1, axis_b)
    range_b.set_fill(color=BLUE_D)

    # Pointer
    pointer_b = Triangle(
      fill_color=WHITE,
      fill_opacity=1.0,
      stroke_width=0.0
    ).scale([0.15, -0.15, 0.15])\
    .add_updater(
      lambda m: m.next_to(axis_b.n2p(tracker.get_value() / 4.0), UP * 1.5)
    )

    # Label and number B
    label_b = MathTex("\\alpha = ").add_updater(lambda m: m.next_to(pointer_b, UP))
    number_b = DecimalNumber().set_color(WHITE).add_updater(
      lambda m: m.next_to(label_b, RIGHT).set_value(tracker.get_value() / 4.0)
    )

    # Label norm
    label_norm = MathTex("\\alpha = \\frac{x}{b}").scale(1.5)\
      .align_to(axis_a, RIGHT).shift(RIGHT * 2.5)

    self.add(axis_a, range_a, axis_b, range_b)

    self.wait(0.5)
    self.play(Create(curves[0]), Create(curves[1]))
    self.wait(0.5)

    self.play(
      FadeIn(pointer_a),
      FadeIn(label_a),
      FadeIn(number_a),

      FadeIn(pointer_b),
      FadeIn(label_b),
      FadeIn(number_b),

      FadeIn(label_norm)
    )

    self.wait(0.5)
    self.play(tracker.animate.increment_value(2.0), run_time=2, rate_func=linear)
    self.wait(0.75)
    self.play(tracker.animate.increment_value(-4.0), run_time=2, rate_func=linear)
    self.wait(0.75)
    self.play(tracker.animate.increment_value(2.0), run_time=2, rate_func=linear)
    self.wait(0.5)

class Normalization(Scene):
  def construct(self):

    # Axis
    axis_a = NumberLine(
      x_range=[0, 8, 1],
      stroke_width=4.0,
      length=9,
      include_numbers=True
    ).shift(UP * 2.5).shift(LEFT * 1.25)

    axis_b = NumberLine(
      x_range=[0, 8, 1],
      stroke_width=4.0,
      length=9,
      include_numbers=True
    ).shift(UP * 0.25).shift(LEFT * 1.25)

    axis_c = NumberLine(
      x_range=[0, 8, 1],
      stroke_width=4.0,
      length=9,
      include_numbers=True
    ).shift(DOWN * 2.0).shift(LEFT * 1.25)

    # Ranges
    range_a = create_range(2, 7, axis_a)
    range_b = create_range(0, 5, axis_b).set_fill(color=BLUE_D)
    range_c = create_range(0, 1, axis_c).set_fill(color=GREEN_D)

    # Curves
    curves_a_b = create_curves(2, 7, 0, 5, axis_a, axis_b)
    curves_b_c = create_curves(0, 5, 0, 1, axis_b, axis_c)

    # Tracker
    tracker = ValueTracker(4.5)

    # Pointers
    pointer_a = Triangle(
      fill_color=WHITE,
      fill_opacity=1.0,
      stroke_width=0.0
    ).scale([0.15, -0.15, 0.15]).add_updater(
      lambda m: m.next_to(axis_a.n2p(tracker.get_value()), UP * 1.5)
    )

    pointer_b = Triangle(
      fill_color=WHITE,
      fill_opacity=1.0,
      stroke_width=0.0
    ).scale([0.15, -0.15, 0.15]).add_updater(
      lambda m: m.next_to(axis_b.n2p(tracker.get_value() - 2.0), UP * 1.5)
    )

    pointer_c = Triangle(
      fill_color=WHITE,
      fill_opacity=1.0,
      stroke_width=0.0
    ).scale([0.15, -0.15, 0.15]).add_updater(
      lambda m: m.next_to(axis_c.n2p((tracker.get_value() - 2.0) / 5.0), UP * 1.5)
    )

    # Numbers and labels
    label_a = MathTex("x = ").add_updater(lambda m: m.next_to(pointer_a, UP))
    number_a = DecimalNumber().set_color(WHITE).add_updater(
      lambda m: m.next_to(label_a, RIGHT).set_value(tracker.get_value())
    )

    label_b = MathTex("x' = ").add_updater(lambda m: m.next_to(pointer_b, UP))
    number_b = DecimalNumber().set_color(WHITE).add_updater(
      lambda m: m.next_to(label_b, RIGHT).set_value(tracker.get_value() - 2.0)
    )

    label_c = MathTex("\\alpha = ").add_updater(lambda m: m.next_to(pointer_c, UP))
    number_c = DecimalNumber().set_color(WHITE).add_updater(
      lambda m: m.next_to(label_c, RIGHT).set_value((tracker.get_value() - 2.0) / 5.0)
    )

    # Label norms
    label_norm_a = MathTex("x'= x - a").scale(1)\
      .next_to(axis_b, RIGHT * 2.5 + UP * 2.5)

    label_norm_b = MathTex("\\alpha = \\frac{x - a}{b - a}").scale(1)\
      .next_to(axis_c, RIGHT * 2.5 + UP)

    self.add(axis_a, axis_b, axis_c)
    self.add(range_a, range_b, range_c)

    self.wait(0.5)
    self.play(Create(curves_a_b[0]), Create(curves_a_b[1]))
    self.play(Create(curves_b_c[0]), Create(curves_b_c[1]))
    self.wait(0.5)

    self.play(
      FadeIn(pointer_a),
      FadeIn(label_a),
      FadeIn(number_a),

      FadeIn(pointer_b),
      FadeIn(label_b),
      FadeIn(number_b),

      FadeIn(pointer_c),
      FadeIn(label_c),
      FadeIn(number_c),

      FadeIn(label_norm_a),
      FadeIn(label_norm_b)
    )

    self.wait(1)

    self.play(tracker.animate.increment_value(2.5), run_time=1.5, rate_func=linear)
    self.wait(0.75)
    self.play(tracker.animate.increment_value(-5.0), run_time=2, rate_func=linear)
    self.wait(0.75)
    self.play(tracker.animate.increment_value(2.5), run_time=1.5, rate_func=linear)
    self.wait(0.75)
