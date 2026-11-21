import pytest
import math
from render import stereo_reprojection as mod

CASES = [
    ("reproj", 'm.reproject((0.5, 0.5), (0.1, 0.2)) == approx((0.6, 0.7))'),
    ("depth", 'm.depth_aligned(0.5, 0.55, 0.1) is True'),
    ("fallback", 'm.fallback(False, 9) == 9'),
    ("eye", 'm.eye_center(0.064, -1) == approx(-0.032)'),
    ("trans", 'm.transparent_vec((0.1, 0.2), (0.3, 0.4)) == approx((0.4, 0.6))'),
    ("edge", 'm.is_edge(0.8, 0.5) is True'),
    ("latest", 'm.latest([1, 2, 3]) == 3'),
    ("split", 'm.warp_split(1, 2) == 3'),
    ("eyekey", 'm.eye_key("base", 1) == "base:1"'),
    ("predict", 'm.predict(8, 4) == 12'),
    ("vdepth", 'm.valid_depth(1) is True'),
    ("clamp", 'm.clamp_uv((1.2, -0.2)) == (1.0, 0.0)'),
    ("lerp", 'm.lerp_pose(0, 10, 0.5) == approx(5.0)'),
    ("len", 'm.motion_len(3, 4) == approx(5.0)'),
    ("id", 'm.stereo_id(3, 2) == "3:2"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
