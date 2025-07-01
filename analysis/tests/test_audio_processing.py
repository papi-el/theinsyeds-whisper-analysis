#!/usr/bin/env python3
"""
Audio processing tests for Whisper analysis
"""

import unittest
import numpy as np
import librosa
import soundfile as sf
from pathlib import Path

class TestAudioProcessing(unittest.TestCase):
    
    def setUp(self):
        """Set up test audio files"""
        self.test_dir = Path("../../data/samples")
        self.sample_rate = 16000
        
    def test_audio_loading(self):
        """Test audio file loading"""
        test_file = self.test_dir / "test.wav"
        if test_file.exists():
            audio, sr = librosa.load(str(test_file), sr=None)
            self.assertIsInstance(audio, np.ndarray)
            self.assertGreater(len(audio), 0)
    
    def test_mel_spectrogram_generation(self):
        """Test mel spectrogram creation"""
        # Create test audio
        duration = 1.0
        t = np.linspace(0, duration, int(self.sample_rate * duration))
        test_audio = 0.3 * np.sin(2 * np.pi * 440 * t)
        
        # Generate mel spectrogram
        mel_spec = librosa.feature.melspectrogram(
            y=test_audio, 
            sr=self.sample_rate, 
            n_mels=80
        )
        
        self.assertEqual(mel_spec.shape[0], 80)  # 80 mel channels
        self.assertGreater(mel_spec.shape[1], 0)  # Time frames
    
    def test_audio_resampling(self):
        """Test audio resampling to 16kHz"""
        # Create test audio at different sample rate
        original_sr = 44100
        duration = 1.0
        t = np.linspace(0, duration, int(original_sr * duration))
        test_audio = 0.3 * np.sin(2 * np.pi * 440 * t)
        
        # Resample to 16kHz
        resampled = librosa.resample(test_audio, orig_sr=original_sr, target_sr=16000)
        
        expected_length = int(len(test_audio) * 16000 / original_sr)
        self.assertAlmostEqual(len(resampled), expected_length, delta=10)

if __name__ == '__main__':
    unittest.main()
