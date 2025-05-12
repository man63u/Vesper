import os
import shutil
from tqdm import tqdm

def move_esd_files(source_dir, target_dir):
    """
    将ESD文件从CASIA目录移动到新的目录
    
    Args:
        source_dir: 源目录（CASIA目录）
        target_dir: 目标目录（新的ESD目录）
    """
    # 定义情感标签目录
    emotion_dirs = ['Angry', 'Happy', 'Neutral', 'Sad', 'Suprise']
    
    print("正在移动文件...")
    
    # 遍历每个说话人目录（0001-0005）
    for speaker_dir in tqdm(sorted(os.listdir(source_dir))):
        speaker_path = os.path.join(source_dir, speaker_dir)
        
        # 检查是否是目录
        if not os.path.isdir(speaker_path):
            continue
            
        # 遍历每个情感目录
        for emotion_dir in emotion_dirs:
            emotion_path = os.path.join(speaker_path, emotion_dir)
            
            # 检查情感目录是否存在
            if not os.path.exists(emotion_path):
                print(f"警告: 目录不存在 - {emotion_path}")
                continue
                
            # 创建目标目录
            target_speaker_path = os.path.join(target_dir, speaker_dir)
            target_emotion_path = os.path.join(target_speaker_path, emotion_dir)
            os.makedirs(target_emotion_path, exist_ok=True)
            
            # 获取该情感目录下的所有wav文件
            wav_files = [f for f in os.listdir(emotion_path) if f.endswith('.wav')]
            
            # 移动每个音频文件
            for wav_file in wav_files:
                src_file = os.path.join(emotion_path, wav_file)
                dst_file = os.path.join(target_emotion_path, wav_file)
                shutil.move(src_file, dst_file)
            
            # 如果源目录为空，删除它
            if not os.listdir(emotion_path):
                os.rmdir(emotion_path)
        
        # 如果说话人目录为空，删除它
        if not os.listdir(speaker_path):
            os.rmdir(speaker_path)
    
    print("\n文件移动完成!")
    print(f"源目录: {source_dir}")
    print(f"目标目录: {target_dir}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='将ESD文件从CASIA目录移动到新的目录')
    parser.add_argument('--source_dir', type=str, required=True, help='源目录路径（CASIA目录）')
    parser.add_argument('--target_dir', type=str, required=True, help='目标目录路径（新的ESD目录）')
    
    args = parser.parse_args()
    
    try:
        # 创建目标根目录
        os.makedirs(args.target_dir, exist_ok=True)
        
        # 移动文件
        move_esd_files(args.source_dir, args.target_dir)
    except Exception as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    main() 