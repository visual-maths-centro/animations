from manim import *
from utils import create_range, create_curves

class InterpolationA(Scene):
  def construct(self):

    # Axis
    axis_a = NumberLine(
      x_range=[0, 5, 1],
      stroke_width=4.0,
      length=10,
      include_numbers=True
    ).shift(UP * 2.0)\
    .shift(LEFT * 1.25)

    axis_b = NumberLine(
      x_range=[0, 10, 1],
      stroke_width=4.0,
      length=10,
      include_numbers=True
    ).shift(DOWN * 1.5)\
    .shift(LEFT * 1.25)

    # Tracker
    tracker = ValueTracker(0.5)

    # Range A
    range_a = create_range(0, 1, axis_a)
    range_a.set_fill(color=BLUE_D) 

    # Range B
    range_b = create_range(0, 7, axis_b)

    # Curves
    curves = create_curves(0, 1, 0, 7, axis_a, axis_b)

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
    label_a = MathTex("\\alpha = ").add_updater(lambda m: m.next_to(pointer_a, UP))
    number_a = DecimalNumber().set_color(WHITE).add_updater(
      lambda m: m.next_to(label_a, RIGHT).set_value(tracker.get_value())
    )

    # Pointer
    pointer_b = Triangle(
      fill_color=WHITE,
      fill_opacity=1.0,
      stroke_width=0.0
    ).scale([0.15, -0.15, 0.15])\
    .add_updater(
      lambda m: m.next_to(axis_b.n2p(tracker.get_value() * 7.0), UP * 1.5)
    )

    # Label and number B
    label_b = MathTex("x = ").add_updater(lambda m: m.next_to(pointer_b, UP))
    number_b = DecimalNumber().set_color(WHITE).add_updater(
      lambda m: m.next_to(label_b, RIGHT).set_value(tracker.get_value() * 7.0)
    )

    # Label interp
    label_interp = MathTex("x = \\alpha b").scale(1.5)\
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

      FadeIn(label_interp)
    )

    self.wait(0.5)
    self.play(tracker.animate.increment_value(0.5), run_time=2, rate_func=linear)
    self.wait(0.75)
    self.play(tracker.animate.increment_value(-1.0), run_time=2, rate_func=linear)
    self.wait(0.75)
    self.play(tracker.animate.increment_value(0.75), run_time=2, rate_func=linear)
    self.wait(0.5)

class Interpolation(Scene):
  def construct(self):

    # Axis
    axis_a = NumberLine(
      x_range=[0, 6, 1],
      stroke_width=4.0,
      length=10,
      include_numbers=True
    ).shift(UP * 2.5).shift(LEFT * 1.5)

    axis_b = NumberLine(
      x_range=[0, 10, 1],
      stroke_width=4.0,
      length=10,
      include_numbers=True
    ).shift(UP * 0.15).shift(LEFT * 1.5)

    axis_c = NumberLine(
      x_range=[0, 10, 1],
      stroke_width=4.0,
      length=10,
      include_numbers=True
    ).shift(DOWN * 2.25).shift(LEFT * 1.5)

    # Ranges
    range_a = create_range(0, 1, axis_a).set_fill(color=GREEN_D)
    range_b = create_range(0, 4, axis_b).set_fill(color=BLUE_D)
    range_c = create_range(5, 9, axis_c)

    # Curves
    curves_a_b = create_curves(0, 1, 0, 4, axis_a, axis_b)
    curves_b_c = create_curves(0, 4, 5, 9, axis_b, axis_c)

    # Tracker
    tracker = ValueTracker(0.5)

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
      lambda m: m.next_to(axis_b.n2p(tracker.get_value() * 4.0), UP * 1.5)
    )

    pointer_c = Triangle(
      fill_color=WHITE,
      fill_opacity=1.0,
      stroke_width=0.0
    ).scale([0.15, -0.15, 0.15]).add_updater(
      lambda m: m.next_to(axis_c.n2p(tracker.get_value() * 4.0 + 5.0), UP * 1.5)
    )

    # Numbers and labels
    label_a = MathTex("\\alpha = ").add_updater(lambda m: m.next_to(pointer_a, UP))
    number_a = DecimalNumber().set_color(WHITE).add_updater(
      lambda m: m.next_to(label_a, RIGHT).set_value(tracker.get_value())
    )

    label_b = MathTex("x' = ").add_updater(lambda m: m.next_to(pointer_b, UP))
    number_b = DecimalNumber().set_color(WHITE).add_updater(
      lambda m: m.next_to(label_b, RIGHT).set_value(tracker.get_value() * 4.0)
    )

    label_c = MathTex("x = ").add_updater(lambda m: m.next_to(pointer_c, UP))
    number_c = DecimalNumber().set_color(WHITE).add_updater(
      lambda m: m.next_to(label_c, RIGHT).set_value(tracker.get_value() * 4.0 + 5.0)
    )

    # Label interp
    label_interp_a = MathTex("x'= \\alpha(b - a)").scale(0.85)\
      .next_to(axis_b, RIGHT * 0.25 + UP * 2.5)

    label_interp_b = MathTex("x = \\alpha(b - a) + a").scale(0.85)\
      .next_to(axis_c, RIGHT * 0.25 + UP * 1.75)

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

      FadeIn(label_interp_a),
      FadeIn(label_interp_b)
    )

    self.wait(1)
    self.play(tracker.animate.increment_value(0.5), run_time=1.5, rate_func=linear)
    self.wait(0.75)
    self.play(tracker.animate.increment_value(-1.0), run_time=2, rate_func=linear)
    self.wait(0.75)
    self.play(tracker.animate.increment_value(0.75), run_time=1.5, rate_func=linear)
    self.wait(0.75)
