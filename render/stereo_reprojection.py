import math

def reproject(uv, motion):
    """重投影。"""
    raise NotImplementedError("TODO: reproject")

def depth_aligned(prev, cur, threshold):
    """深度对齐。"""
    raise NotImplementedError("TODO: depth_aligned")

def fallback(valid, fallback):
    """去遮挡回退。"""
    raise NotImplementedError("TODO: fallback")

def eye_center(ipd, sign):
    """畸变中心。"""
    raise NotImplementedError("TODO: eye_center")

def transparent_vec(base, extra):
    """透明矢量。"""
    raise NotImplementedError("TODO: transparent_vec")

def is_edge(distance, radius):
    """注视区边缘。"""
    raise NotImplementedError("TODO: is_edge")

def latest(poses):
    """最新姿态。"""
    raise NotImplementedError("TODO: latest")

def warp_split(timewarp, spacewarp):
    """扭曲分工。"""
    raise NotImplementedError("TODO: warp_split")

def eye_key(base, eye):
    """眼缓冲键。"""
    raise NotImplementedError("TODO: eye_key")

def predict(frame_ms, latency):
    """预测提前量。"""
    raise NotImplementedError("TODO: predict")

def valid_depth(depth):
    """深度合法。"""
    raise NotImplementedError("TODO: valid_depth")

def clamp_uv(uv):
    """UV 钳制。"""
    raise NotImplementedError("TODO: clamp_uv")

def lerp_pose(a, b, t):
    """姿态插值。"""
    raise NotImplementedError("TODO: lerp_pose")

def motion_len(x, y):
    """矢量长度。"""
    raise NotImplementedError("TODO: motion_len")

def stereo_id(seed, index):
    """双目 id。"""
    raise NotImplementedError("TODO: stereo_id")
