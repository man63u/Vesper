import pandas as pd
import os

def combine_metadata():
    """
    合并CASIA和ESD数据集的metadata文件
    """
    # 读取CASIA数据集的metadata
    casia_df = pd.read_csv('CASIA/metadata.csv')
    casia_df['dataset'] = 'casia'
    # 添加完整路径
    casia_df['full_path'] = casia_df['name'].apply(lambda x: os.path.join('CASIA', x))
    
    # 读取ESD数据集的metadata
    esd_df = pd.read_csv('ESD/ESV/metadata.csv')
    esd_df['dataset'] = 'esd'
    # 添加完整路径
    esd_df['full_path'] = esd_df['name'].apply(lambda x: os.path.join('ESD/ESV', x))
    
    # 确保标签一致
    label_mapping = {
        'angry': 'angry',
        'happy': 'happy',
        'neutral': 'neutral',
        'sad': 'sad',
        'fear': 'fear',
        'surprise': 'surprise'
    }
    
    # 统一标签
    casia_df['label'] = casia_df['label'].map(label_mapping)
    esd_df['label'] = esd_df['label'].map(label_mapping)
    
    # 合并数据集
    combined_df = pd.concat([casia_df, esd_df], ignore_index=True)
    
    # 保存合并后的metadata
    output_path = 'combined_metadata.csv'
    combined_df.to_csv(output_path, index=False)
    
    # 打印统计信息
    print("\n合并后的数据集统计信息:")
    print(f"总样本数: {len(combined_df)}")
    print("\n每个数据集的样本数:")
    print(combined_df['dataset'].value_counts())
    print("\n每个情感类别的样本数:")
    print(combined_df['label'].value_counts())
    
    return output_path

if __name__ == "__main__":
    try:
        output_path = combine_metadata()
        print(f"\n合并后的metadata文件已生成: {output_path}")
    except Exception as e:
        print(f"错误: {str(e)}") 