# Model Comparison Experiments

## Experiment 1: Performance Benchmarking
**Date**: July 1, 2025
**Objective**: Compare processing speed across model sizes

### Results
| Model | Load Time | Transcribe Time | Total Time |
|-------|-----------|-----------------|------------|
| tiny  | 0.24s     | 0.37s          | 0.62s      |
| base  | 0.43s     | 0.54s          | 0.96s      |
| small | 1.04s     | 1.44s          | 2.48s      |

### Observations
- Clear linear relationship between model size and processing time
- Mac M4 MPS acceleration provides significant speedup
- All models process faster than real-time

## Experiment 2: Quality Assessment
**Objective**: Analyze transcription accuracy and error patterns

### Results
- **Tiny**: 99.2% accuracy, 3 formatting issues
- **Base**: 100% accuracy, 1 brand name issue
- **Small**: 100% accuracy, 1 capitalization issue

### Key Findings
- Brand name recognition challenge across all models
- Base model best for capitalization consistency
- Quality improvements diminish beyond base model for simple audio
