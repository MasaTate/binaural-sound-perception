from pickletools import uint8
import cv2
import numpy as np
import argparse
from tqdm import tqdm
import glob
import os

parser = argparse.ArgumentParser()

parser = argparse.ArgumentParser()

parser.add_argument("--root", type=str, default=".", help="dataset root directory")

args = parser.parse_args()

for sc in tqdm(range(1, 166)):
    subdir = "/dataset_public/scene%04d/"%sc
    fdir = args.root + subdir
    videonum = int(glob.glob(fdir+"/*_cropped.mp4")[0].split('/')[-1].split('_')[1])
    video_file = "VIDEO_"+"%04d"%videonum+"_cropped.mp4"
    img_files = glob.glob(fdir+"split_videoframes/*.png")
    
    savedir = fdir+"masked_videoframes"
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    for img_path in img_files:
        img = cv2.imread(img_path)
        height, width, channel = img.shape[:3]
        out = np.zeros_like(img)
        out[:,width//4:width//4*3,:] = img[:,width//4:width//4*3,:]
        
        cv2.imwrite(savedir+img_path[-30:], out)