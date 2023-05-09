import os
import imageio
import cv2
import numpy as np
from tqdm import tqdm

MAX_H, MAX_W = 600, 400
exp_name = "360_v2"
keys = ["color", "distance_mean"]

root = os.path.join("exp", exp_name)
scenes = sorted(os.listdir(root))

video_files = [[os.path.join(root, scene, "render",
                             f"{scene}_360_v2_path_renders_step_25000_{k}.mp4")
                for k in keys] for scene in scenes]
video_files = [f for f in video_files if os.path.exists(f[0])]

with imageio.get_writer(os.path.join("assets", exp_name+'.mp4'), fps=60) as writer:
    for scene_videos in tqdm(video_files):
        readers = [imageio.get_reader(f) for f in scene_videos]
        for data in zip(*readers):
            data = np.concatenate([cv2.resize(img, (MAX_H, MAX_W)) for img in data], axis=1)
            writer.append_data(data)
