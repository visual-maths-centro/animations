from manim import *
from sympy import Le, trailing

class CreateMobjects(Scene):

  def construct(self):
    circle = Circle()

    self.add(circle)
    self.wait(1)
    self.remove(circle)
    self.wait(1)

class Shapes(Scene):
  def construct(self):
    circle = Circle()
    square = Square()
    triangle = Triangle()

    circle.shift(LEFT)
    square.shift(UP)
    triangle.shift(RIGHT)

    self.add(circle, square, triangle)

class MobjectPlacement(Scene):

  def construct(self):
    circle = Circle()
    square = Square()
    triangle = Triangle()

    circle.move_to(LEFT * 2.0)
    circle.move_to(UP)

    square.next_to(circle, LEFT)
    triangle.align_to(square, DOWN)
    triangle.align_to(square, LEFT)

    self.add(circle, square, triangle)

class MobjectStyling(Scene):

  def construct(self):
    circle = Circle().shift(LEFT)
    square = Square().shift(UP)
    triangle = Triangle().shift(RIGHT)

    circle.set_stroke(color=GREEN, width=20)
    square.set_fill(YELLOW, opacity=1.0)
    triangle.set_fill(PINK, opacity=0.5)

    self.play(Create(circle), Create(square), Create(triangle))
    self.wait(1)

class AnimateExample(Scene):

  def construct(self):
    square = Square().set_fill(RED, opacity=1.0)

    self.add(square)

    self.play(square.animate.set_fill(WHITE, opacity=0.5), run_time=3.0)
    self.play(square.animate.shift(UP).rotate(PI / 3.0), run_time=0.25)

    self.wait(1)
