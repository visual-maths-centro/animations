from manim import *

class SquareToCircle(Scene):

  def construct(self):
    circle = Circle()
    square = Square()

    square.set_fill(BLUE, opacity=0.5)
    square.next_to(circle, RIGHT, buff=2.5)

    self.play(Create(square))
    self.play(square.animate.rotate(PI / 4.0))
    self.play(ReplacementTransform(square, circle))
    self.play(circle.animate.set_fill(PINK, opacity=0.5))

class DifferentRotations(Scene):
  def construct(self):
    left_square = Square(color=BLUE, fill_opacity=0.7).shift(3 * LEFT)
    right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
    self.play(
      left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
    )
    self.wait()

class MobjectDotsExample(Scene):
  def construct(self):
    p1 = [-1,-1,0]
    p2 = [1,-1,0]
    p3 = [1,1,0]
    p4 = [-1,1,0]
    a = Line(p1, p2).append_points(Line(p2, p3).points).append_points(Line(p3, p4).points)

    point_start = a.get_start()
    point_end = a.get_end()
    point_center = a.get_center()

    self.add(Text(f"a.get_start() = {np.round(point_start, 2).tolist()}", font_size=24).to_edge(UR).set_color(YELLOW))
    self.add(Text(f"a.get_end() = {np.round(point_end, 2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(RED))
    self.add(Text(f"a.get_center() = {np.round(point_center, 2).tolist()}", font_size=24).next_to(self.mobjects[-1],DOWN).set_color(BLUE))

    self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
    self.add(Dot(a.get_end()).set_color(RED).scale(2))
    self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
    self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
    self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
    self.add(Dot(a.point_from_proportion(0.15)).set_color(ORANGE).scale(2))

    self.add(*[Dot(x) for x in a.points])

    self.add(a)

class ExampleRotation(Scene):
  def construct(self):
    # self.camera.background_color = WHITE

    m1a = Square().set_color(RED).shift(LEFT)
    m1b = Circle().set_color(RED).shift(LEFT * 2.0)

    m2a = Square().set_color(BLUE).shift(RIGHT)
    m2b = Circle().set_color(BLUE).shift(RIGHT * 2.0)

    m2a.points = np.roll(m2a.points, int(len(m2a.points) / 4), axis=0)

    self.play(
      Transform(m1a, m1b),
      Transform(m2a, m2b),
      lag_ratio=2,
      run_time=1
    )

class LagRatios(Scene):
  def construct(self):
    ratios = [0, 0.1, 0.5, 1, 2]  # demonstrated lag_ratios

    # Create dot groups
    group = VGroup(*[Dot() for _ in range(4)]).arrange_submobjects()
    groups = VGroup(*[group.copy() for _ in ratios]).arrange_submobjects(buff=1)
    self.add(groups)

    # Label groups
    self.add(Text("lag_ratio = ", font_size=36).next_to(groups, UP, buff=1.5))
    for group, ratio in zip(groups, ratios):
      self.add(Text(str(ratio), font_size=36).next_to(group, UP))

    #Animate groups with different lag_ratios
    self.play(AnimationGroup(*[
      group.animate(lag_ratio=ratio, run_time=1.5).shift(DOWN * 2)
      for group, ratio in zip(groups, ratios)
    ]))

    # lag_ratio also works recursively on nested submobjects:
    self.play(groups.animate(run_time=1, lag_ratio=0.1).shift(UP * 2))
