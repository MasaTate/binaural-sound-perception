import cv2
import numpy as np
import argparse
import glob
from tqdm import tqdm
import os

parser = argparse.ArgumentParser()

parser.add_argument("--root", type=str, default=".", help="dataset root directory")

args = parser.parse_args()


for sc in tqdm(range(1, 166)):
    subdir = "/dataset_public/scene%04d/"%sc
    fdir = args.root + subdir
    videonum = int(glob.glob(fdir+"/*_bg.png")[0].split('/')[-1].split('_')[1])
    bg_file = "VIDEO_"+"%04d"%videonum+"_bg_seman.png"
    savedir = fdir+"pred_sound_making"
    bg = cv2.imread(fdir+bg_file)
    mask_bg = np.sum(bg, axis=2)
    mask_bg[mask_bg==142] = 255
    mask_bg[mask_bg==180] = 255
    mask_bg[mask_bg==230] = 255
    mask_bg[mask_bg!=255] = 0
    if not os.path.exists(savedir):
        os.makedirs(savedir)
    pred_path = glob.glob(fdir+"pred_frames/*.png")
    for img_path in pred_path:
        img = cv2.imread(img_path)
        height, width, channels = img.shape[:3]
        
        original = np.copy(img)
        #tmp = tmp.transpose(2,0,1)
        car = np.array([[[0, 0, 142]]])
        """
        car = np.broadcast_to(car, (height, width, channels))
        tmp_car = original - car
        tmp_car = np.sum(tmp_car, axis=2)
        tmp_car[tmp_car!=0] = 1
        mask_car = np.ones_like(tmp_car)
        mask_car = mask_car - tmp_car
        """
        mask = np.sum(original, axis=2)
        mask[mask==142] = 255
        mask[mask==180] = 255
        mask[mask==230] = 255
        
        mask = mask - mask_bg
        
        mask[mask!=255] = 0
        mask = mask.astype(np.uint8)
        #print(mask)
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        #print(mask)
        cv2.imwrite(savedir+img_path[-30:], mask)        
        