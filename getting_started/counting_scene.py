from manim import *

class Count(Animation):

  def __init__(self, number: DecimalNumber, start: float, end: float, **kwargs) -> None:
    super().__init__(number,  **kwargs)

    # Set start and end
    self.start = start
    self.end = end

  def interpolate_mobject(self, alpha: float) -> None:
    value = self.start + (alpha * (self.end - self.start))
    self.mobject.set_value(value)

class CountingScene(Scene):

  def construct(self):

    # Create Decimal Number and add it to scene
    number = DecimalNumber().set_color(WHITE).scale(5)
    number.add_updater(lambda number: number.move_to(ORIGIN))

    self.add(number)

    self.play(Count(number, 250, 1000), run_time=3.5, rate_func=linear)

    self.wait(1)
