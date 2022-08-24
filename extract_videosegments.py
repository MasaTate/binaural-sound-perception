"""
Author: Arun Balajee Vasudevan
Licensed under the CC BY-NC 4.0 license (https://creativecommons.org/licenses/by-nc/4.0/)
"""

import glob,os
import numpy as np
import argparse
from tqdm import tqdm
import ffmpeg

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip

import cv2

parser = argparse.ArgumentParser()
parser.add_argument("--root",default=".",help="dataset root directory")
args = parser.parse_args()

############################### Extract video segments ############################

for sc in tqdm(range(1,2)):
    subdir="/dataset_public/scene%04d/"%sc
    fdir = args.root + subdir
    videonum = int(glob.glob(fdir+"/*cropped.mp4")[0].split('/')[-1].split('_')[1]);
    videofile="VIDEO_"+"%04d"%videonum+"_cropped.mp4"
    save_dir = fdir +"split_videos_test/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    clip = VideoFileClip(fdir+videofile);
    print(ffmpeg.probe(fdir+videofile))
    """
    for t in np.arange(1,clip.duration,2):
        start=t;end = t+2;
        save_clip = clip.subclip(start, end)
        ffmpeg_extract_subclip(fdir+videofile, start, end, targetname=save_dir+videofile[:-4]+"_%06d"%t+".mp4")
        cap = cv2.VideoCapture(save_dir+videofile[:-4]+"_%06d"%t+".mp4")
        fps = cap.get(cv2.CAP_PROP_FPS)
        fcount = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        count = 0
        duration = fcount / fps
        print(fps, fcount, duration)
    """


############################### Extract video frames ###############################

"""
for sc in tqdm(range(1,2)): #TODO change here
    subdir="/dataset_public/scene%04d/"%sc
    fdir = args.root + subdir
    print(fdir)
    videonum = int(glob.glob(fdir+"/*cropped.mp4")[0].split('/')[-1].split('_')[1]);
    videofile="VIDEO_"+"%04d"%videonum+"_cropped.mp4"
    save_dir = fdir +"split_videoframes_test/"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
"""
"""use moviepy
    video = VideoFileClip(fdir+videofile)
    print(fdir+videofile)
    #clip = VideoFileClip(fdir+videofile);
    for it in np.arange(2,video.duration,2):
        clip = video.subclip(it, it+1)
        print("it:", it)
        #np_frame = video.get_frame(it) # get the frame at t=2 seconds
        #np_frame = video.get_frame(frame_number * video_fps) # get frame by index
        #video.save_frame(save_dir+videofile[:-4]+"_%06d"%(it-1)+".png", t=it) # save frame at t=2 as PNG
        clip.save_frame(save_dir+videofile[:-4]+"_%06d"%(it-1)+".png", t=0)
"""
"""
    for video_split in sorted(glob.glob(fdir+"split_videos/*.mp4")):
        start_time_str = video_split.split('_')[-1].split('.')[0]
        print(start_time_str)
        start_time = int(start_time_str)
        
        #if start_time % 2 == 0:
        #    continue
        cap = cv2.VideoCapture(video_split)
        fps = cap.get(cv2.CAP_PROP_FPS)
        fcount = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        count = 0
        duration = fcount / fps
        print(duration)
        cap.set(cv2.CAP_PROP_POS_FRAMES, fcount // 2)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(save_dir+videofile[:-4]+"_"+start_time_str+".png", frame)

        else:
            print("Can't read frame from video")

"""
"""        
    frames = np.arange(2, duration, 2)
    for it in tqdm(frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, fps * (it-2))
        ret, frame = cap.read()

        if ret:
            cv2.imwrite(save_dir+videofile[:-4]+"_%06d"%(it-1)+".png", frame)
        else:
            print("Can't read frame from video")
"""