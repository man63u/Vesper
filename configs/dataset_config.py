from yacs.config import CfgNode as CN

def get_default_dataset_config():
    cfg = CN()
    
    # 数据集通用配置
    cfg.num_classes = 6  # 情感类别数（angry, fear, happy, neutral, sad, surprise）
    cfg.batch_length = 80000  # 音频长度（5秒，16kHz）
    cfg.evaluate = ['accuracy', 'recall']  # 评估指标
    cfg.folds = [1]  # 交叉验证折数
    cfg.f1 = 'weighted'  # F1分数类型
    cfg.have_test_set = True  # 是否有测试集
    
    # CASIA数据集配置
    cfg.casia = CN()
    cfg.casia.meta_csv_file = 'CASIA/metadata.csv'
    cfg.casia.wavdir = 'CASIA'
    
    # ESD数据集配置
    cfg.esd = CN()
    cfg.esd.meta_csv_file = 'ESD/ESV/metadata.csv'
    cfg.esd.wavdir = 'ESD/ESV'
    
    # 数据集组合配置
    cfg.combined = CN()
    cfg.combined.meta_csv_file = 'combined_metadata.csv'  # 合并后的元数据文件
    cfg.combined.use_full_path = True  # 使用完整路径
    cfg.combined.wavdir = ''  # 不使用wavdir，因为使用full_path
    
    return cfg

def get_dataset_config(dataset_name):
    cfg = get_default_dataset_config()
    
    if dataset_name == 'casia':
        cfg.meta_csv_file = cfg.casia.meta_csv_file
        cfg.wavdir = cfg.casia.wavdir
        cfg.use_full_path = False
    elif dataset_name == 'esd':
        cfg.meta_csv_file = cfg.esd.meta_csv_file
        cfg.wavdir = cfg.esd.wavdir
        cfg.use_full_path = False
    elif dataset_name == 'combined':
        cfg.meta_csv_file = cfg.combined.meta_csv_file
        cfg.wavdir = cfg.combined.wavdir
        cfg.use_full_path = cfg.combined.use_full_path
    else:
        raise ValueError(f"Unknown dataset: {dataset_name}")
    
    return cfg

###########
# CASIA #
###########
_C.casia = CN(new_allowed=True)
_C.casia.num_classes = 6  # CASIA有6种情感：angry, fear, happy, neutral, sad, surprise
_C.casia.meta_csv_file = 'CASIA/metadata.csv'  # 元数据文件路径
_C.casia.wavdir = 'CASIA'  # 音频文件目录
_C.casia.batch_length = 80000  # 16000 * 5.0，可以根据你的音频长度调整
_C.casia.evaluate = ['accuracy', 'recall']
_C.casia.folds = [1]
_C.casia.f1 = 'weighted'
_C.casia.have_test_set = True

###########
# IEMOCAP #
###########
_C.iemocap = CN(new_allowed=True)
_C.iemocap.num_classes = 4
_C.iemocap.meta_csv_file = '/148Dataset/data-chen.weidong/iemocap/feature/name_label_text.csv'
_C.iemocap.wavdir = '/148Dataset/data-chen.weidong/iemocap/wav_all_sentences'
_C.iemocap.batch_length = 104000 # 16000 * 6.5
_C.iemocap.evaluate = ['accuracy', 'recall']
_C.iemocap.folds = [1, 2, 3, 4, 5]
_C.iemocap.f1 = 'weighted'
_C.iemocap.have_test_set = False

########
# MELD #
########
_C.meld = CN(new_allowed=True)
_C.meld.num_classes = 7
_C.meld.meta_csv_file = '/148Dataset/data-chen.weidong/meld/label/official'
_C.meld.wavdir = '/148Dataset/data-chen.weidong/meld/audio_16k'
_C.meld.batch_length = 72000 # 16000 * 4.5
_C.meld.evaluate = ['f1']
_C.meld.folds = [1]
_C.meld.f1 = 'weighted'
_C.meld.have_test_set = True

###########
# CREMA-D #
###########
_C.crema = CN(new_allowed=True)
_C.crema.num_classes = 6
_C.crema.meta_csv_file = '/148Dataset/data-chen.weidong/CREMA-D/CREMA-D.csv'
_C.crema.wavdir = '/148Dataset/data-chen.weidong/CREMA-D/AudioWAV'
_C.crema.batch_length = 48000 # 16000 * 3.0
_C.crema.evaluate = ['accuracy', 'recall']
_C.crema.folds = [1]
_C.crema.f1 = 'weighted'
_C.crema.have_test_set = False

#########
# LSSED #
#########
_C.lssed = CN(new_allowed=True)
_C.lssed.num_classes = 4
_C.lssed.meta_csv_file = '/148Dataset/data-chen.weidong/lssed_all/metadata_english_all.csv'
_C.lssed.wavdir = '/148Dataset/data-chen.weidong/lssed_all/wav_all'
_C.lssed.batch_length = 80000 # 16000*5
_C.lssed.evaluate = ['accuracy', 'recall']
_C.lssed.folds = [1]
_C.lssed.f1 = 'weighted'
_C.lssed.have_test_set = True

_C.lssed.target_length = 249
_C.lssed.l_target_dir = '/148Dataset/data-chen.weidong/lssed_all/feature/wavlm_large_L12_mat'
_C.lssed.h_target_dir = '/148Dataset/data-chen.weidong/lssed_all/feature/wavlm_large_L24_mat'

###########
# Chinese #
###########
_C.chinese = CN(new_allowed=True)
_C.chinese.num_classes = 6  # 可以根据你的情感类别数量调整
_C.chinese.meta_csv_file = 'data/chinese/metadata.csv'  # 你的中文数据集元数据文件路径
_C.chinese.wavdir = 'data/chinese/wav'  # 你的中文音频文件目录
_C.chinese.batch_length = 80000  # 16000 * 5.0，可以根据你的音频长度调整
_C.chinese.evaluate = ['accuracy', 'recall']
_C.chinese.folds = [1]
_C.chinese.f1 = 'weighted'
_C.chinese.have_test_set = True
