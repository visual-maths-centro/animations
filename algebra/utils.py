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

