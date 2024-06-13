import os
import subprocess

def crop_videos():
    # 获取当前文件夹下的所有视频文件
    videos = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(('.mp4', '.avi', '.mkv'))]

    for video in videos:
        # 构建FFmpeg命令
        command = ['ffmpeg', '-i', video, '-vf', 'crop=752:752', 'resize_'+video, '-y']
        # 执行FFmpeg命令
        subprocess.call(command)
        os.remove(video)
        os.rename('resize_'+video, video)

    print('视频裁剪完成！')

crop_videos()