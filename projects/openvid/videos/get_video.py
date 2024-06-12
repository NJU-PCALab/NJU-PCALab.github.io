import os
import shutil

dir_list = ['Gen2', 'OpenSoraPlan-V1.1', 'Pika', 'VideoCrafter2']
s = set()

# 扫描文件�?
for dir in dir_list:
    for videos in os.listdir(dir):
        if videos.endswith('.mp4'):
            s.add(videos)

source = r'E:\Wechat File\WeChat Files\wxid_lw4c5uos3d4k21\FileStorage\File\2024-05\ours_ft1024_16K\ft1024_epoch4-global_step16000_eval'
# 从source中复制s的视频到Ours下
for video in s:
    shutil.copy(os.path.join(source, video), 'Ours')
