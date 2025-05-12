import os
import pandas as pd
from tqdm import tqdm

def create_esd_metadata(base_dir):
    """
    为ESD数据集创建metadata.csv文件
    
    Args:
        base_dir: ESD数据集的根目录
    """
    # 定义情感标签映射
    emotion_mapping = {
        'Angry': 'angry',
        'Happy': 'happy',
        'Neutral': 'neutral',
        'Sad': 'sad',
        'Suprise': 'surprise'
    }
    
    # 存储所有文件信息的列表
    data = []
    
    # 遍历每个说话人目录（0001-0005）
    for speaker_dir in tqdm(sorted(os.listdir(base_dir))):
        speaker_path = os.path.join(base_dir, speaker_dir)
        
        # 检查是否是目录
        if not os.path.isdir(speaker_path):
            continue
            
        # 遍历每个情感目录
        for emotion_dir in emotion_mapping.keys():
            emotion_path = os.path.join(speaker_path, emotion_dir)
            
            # 检查情感目录是否存在
            if not os.path.exists(emotion_path):
                print(f"警告: 目录不存在 - {emotion_path}")
                continue
                
            # 获取该情感目录下的所有wav文件
            wav_files = [f for f in os.listdir(emotion_path) if f.endswith('.wav')]
            
            # 添加每个音频文件的信息
            for wav_file in wav_files:
                file_path = os.path.join(emotion_dir, wav_file)
                data.append({
                    'name': file_path,
                    'label': emotion_mapping[emotion_dir],
                    'speaker': speaker_dir
                })
    
    # 创建DataFrame
    df = pd.DataFrame(data)
    
    # 保存为CSV文件
    output_path = os.path.join(base_dir, 'metadata.csv')
    df.to_csv(output_path, index=False)
    
    # 打印数据集统计信息
    print("\n数据集统计信息:")
    print(f"总样本数: {len(df)}")
    print("\n每个情感类别的样本数:")
    print(df['label'].value_counts())
    print("\n每个说话人的样本数:")
    print(df['speaker'].value_counts())
    
    return output_path

def main():
    import argparse
    parser = argparse.ArgumentParser(description='为ESD数据集创建metadata.csv文件')
    parser.add_argument('--base_dir', type=str, required=True, help='ESD数据集的根目录路径')
    
    args = parser.parse_args()
    
    try:
        output_path = create_esd_metadata(args.base_dir)
        print(f"\nmetadata.csv文件已生成: {output_path}")
    except Exception as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    main() 