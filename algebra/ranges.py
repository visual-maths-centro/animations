from cProfile import label
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

    # Curve A
    curve_a_start = axis_a.n2p(0)
    curve_a_end = axis_b.n2p(0)
    curve_a_mid = (curve_a_start + curve_a_end) * 0.5

    curve_a = DashedVMobject(CubicBezier(
      start_anchor=curve_a_start,
      start_handle=curve_a_mid,
      end_handle=curve_a_mid,
      end_anchor=curve_a_end,
      stroke_color=ORANGE
    ))

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

    # Curve b
    curve_b_start = axis_a.n2p(4)
    curve_b_end = axis_b.n2p(1)

    len = np.linalg.norm(curve_b_start - curve_b_end)

    curve_b = DashedVMobject(CubicBezier(
      start_anchor=curve_b_start,
      start_handle=curve_b_start + np.array([0, -len * 0.25, 0]),
      end_handle=curve_b_end + np.array([0, len * 0.25, 0]),
      end_anchor=curve_b_end,
      stroke_opacity=0.75,
      stroke_color=ORANGE
    ))

    # Label norm
    label_norm = MathTex("\\alpha = \\frac{x}{b}").scale(1.5)\
      .align_to(axis_a, RIGHT).shift(RIGHT * 2.5)

    self.add(axis_a, range_a, pointer_a, label_a, number_a)
    self.add(axis_b, range_b, pointer_b, label_b, number_b)
    self.add(label_norm)

    self.wait(0.5)

    self.play(Create(curve_a), Create(curve_b))
    self.play(tracker.animate.increment_value(2.0), run_time=2, rate_func=linear)

    self.wait(0.75)

    self.play(tracker.animate.increment_value(-4.0), run_time=2, rate_func=linear)

    self.wait(0.75)

    self.play(tracker.animate.increment_value(2.0), run_time=2, rate_func=linear)

    self.wait(0.5)