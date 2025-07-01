#!/usr/bin/env python3
"""
Whisper Speech Recognition Test Script
Part of: theinsyeds-whisper-analysis
Author: @theinsyeds
Purpose: Basic functionality test and performance measurement
"""

import whisper
import time
import torch
from pathlib import Path

def test_whisper_setup():
    """Test Whisper installation and system capabilities"""
    print("🔬 Whisper Setup Analysis")
    print("=" * 50)
    
    # System info
    print(f"📱 Device: {'Apple Silicon (MPS)' if torch.backends.mps.is_available() else 'CPU'}")
    print(f"🐍 Python: {torch.version.__version__}")
    print(f"🤖 Available models: {whisper.available_models()}")
    
    return True

def transcribe_with_timing(audio_path, model_size="base"):
    """Transcribe audio and measure performance"""
    print(f"\n🎵 Testing: {audio_path}")
    print(f"🤖 Model: {model_size}")
    
    # Load model and time it
    start_time = time.time()
    model = whisper.load_model(model_size)
    load_time = time.time() - start_time
    
    # Transcribe and time it
    start_time = time.time()
    result = model.transcribe(str(audio_path))
    transcribe_time = time.time() - start_time
    
    # Results
    print(f"⏱️  Load time: {load_time:.2f}s")
    print(f"⏱️  Transcribe time: {transcribe_time:.2f}s")
    print(f"🌍 Language: {result['language']}")
    print(f"📝 Text: {result['text']}")
    
    return {
        'model': model_size,
        'load_time': load_time,
        'transcribe_time': transcribe_time,
        'language': result['language'],
        'text': result['text']
    }

def main():
    """Main research function"""
    print("🔬 theinsyeds Whisper Analysis - Initial Test")
    print("=" * 60)
    
    # Test setup
    test_whisper_setup()
    
    # Test transcription
    audio_file = Path("data/samples/test.wav")
    if audio_file.exists():
        result = transcribe_with_timing(audio_file)
        print(f"\n✅ Test completed successfully!")
        print(f"📊 Performance: {result['transcribe_time']:.2f}s for {result['model']} model")
    else:
        print("❌ Test audio file not found!")

if __name__ == "__main__":
    main()
