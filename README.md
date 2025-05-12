# Vesper: Emotion Recognition System

A deep learning-based emotion recognition system that combines CASIA and ESD datasets for improved emotion classification.

## Features

- Multi-dataset support (CASIA and ESD)
- Emotion classification for 6 categories (angry, fear, happy, neutral, sad, surprise)
- Pre-trained and fine-tuned models
- Feature extraction using WavLM
- Comprehensive training pipeline

## Setup

1. Install dependencies:
```bash
pip install torch torchaudio yacs tqdm einops librosa soundfile
```

2. Prepare datasets:
- Place CASIA dataset in `CASIA/` directory
- Place ESD dataset in `ESD/ESV/` directory

3. Generate metadata:
```bash
python combine_metadata.py
```

4. Extract features:
```bash
python extract_feature/WavLM/extract_wavlm.py
```

5. Training:
```bash
# Pre-training
python pretrain.py -M Vesper-12 -b 32 -g 0 -l 0.0005

# Fine-tuning
python finetune.py -M Vesper-12 -d combined -g 0 -b 32 -l 0.0007
```

## Project Structure

```
Vesper/
├── configs/                 # Configuration files
├── extract_feature/        # Feature extraction modules
├── models/                 # Model definitions
├── utils/                  # Utility functions
├── combine_metadata.py     # Dataset merging script
├── pretrain.py            # Pre-training script
└── finetune.py            # Fine-tuning script
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
