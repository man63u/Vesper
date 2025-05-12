import os
import pandas as pd
from tqdm import tqdm

def create_metadata(base_dir):
    """
    从CASIA数据集目录结构创建metadata.csv文件
    
    Args:
        base_dir: CASIA数据集根目录，包含angry, fear, happy等子目录
    """
    # 定义情感标签映射
    emotion_dirs = {
        'angry': 'angry',
        'fear': 'fear',
        'happy': 'happy',
        'neutral': 'neutral',
        'sad': 'sad',
        'surprise': 'surprise'
    }
    
    # 存储所有文件信息
    data = []
    
    print("正在处理音频文件...")
    # 遍历每个情感目录
    for emotion_dir, emotion_label in emotion_dirs.items():
        emotion_path = os.path.join(base_dir, emotion_dir)
        
        # 检查目录是否存在
        if not os.path.exists(emotion_path):
            print(f"警告: 目录不存在 - {emotion_path}")
            continue
            
        # 获取该情感目录下的所有音频文件
        audio_files = [f for f in os.listdir(emotion_path) if f.endswith('.wav')]
        
        print(f"\n处理 {emotion_label} 目录:")
        # 处理每个音频文件
        for audio_file in tqdm(audio_files):
            # 构建完整的文件路径
            file_path = os.path.join(emotion_dir, audio_file)
            
            # 添加到数据列表
            data.append({
                'name': file_path,
                'label': emotion_label
            })
    
    # 创建DataFrame
    df = pd.DataFrame(data)
    
    # 保存为CSV文件
    output_file = os.path.join(base_dir, 'metadata.csv')
    df.to_csv(output_file, index=False)
    
    # 打印统计信息
    print("\n数据集统计信息:")
    print(f"总样本数: {len(df)}")
    print("\n每个情感的样本数量:")
    print(df['label'].value_counts())
    print(f"\n元数据文件已保存到: {output_file}")

def main():
    import argparse
    parser = argparse.ArgumentParser(description='从CASIA数据集目录结构创建metadata.csv文件')
    parser.add_argument('--base_dir', type=str, required=True, help='CASIA数据集根目录路径')
    
    args = parser.parse_args()
    
    try:
        create_metadata(args.base_dir)
    except Exception as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    main() 