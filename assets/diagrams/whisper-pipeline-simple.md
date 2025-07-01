# Whisper Pipeline Architecture (Text Version)

Raw Audio File
↓
[Preprocessing: Resample to 16kHz]
↓
[Mel Spectrogram Generation: 80 channels]
↓
[Neural Network: Transformer Model]
↓
[Language Detection + Text Generation]
↓
Final Transcription Text

## Model Size Comparison

| Model | Size | Speed | Accuracy | Use Case |
|-------|------|-------|----------|----------|
| Tiny  | 39MB | Fastest (0.37s) | 99.2% | Real-time |
| Base  | 74MB | Balanced (0.54s) | 100% | General |
| Small | 244MB | Slower (1.44s) | 100% | Quality |

## Mac M4 Performance Benefits

- MPS Acceleration: ✅ Enabled
- Processing Speed: 17-27x real-time
- Memory Efficiency: Optimized for Apple Silicon
- No Internet Required: Complete local processing
