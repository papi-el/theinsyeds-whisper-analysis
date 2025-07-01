#!/usr/bin/env python3
"""
Unit tests for Whisper analysis functions
Part of: theinsyeds-whisper-analysis
"""

import unittest
import whisper
import numpy as np
from pathlib import Path

class TestWhisperFunctions(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_audio_path = "../../data/samples/test.wav"
        self.model = whisper.load_model("tiny")  # Use smallest model for testing
    
    def test_model_loading(self):
        """Test that Whisper models load correctly"""
        self.assertIsNotNone(self.model)
        self.assertTrue(hasattr(self.model, 'transcribe'))
    
    def test_transcription_basic(self):
        """Test basic transcription functionality"""
        if Path(self.test_audio_path).exists():
            result = self.model.transcribe(self.test_audio_path)
            self.assertIn('text', result)
            self.assertIn('language', result)
            self.assertIsInstance(result['text'], str)
    
    def test_empty_audio_handling(self):
        """Test handling of silent audio"""
        # Create silent audio for testing
        silent_audio = np.zeros(16000)  # 1 second of silence
        # This test would require creating a temporary file
        # Implementation depends on your specific needs
        pass
    
    def test_model_sizes_available(self):
        """Test that expected model sizes are available"""
        available_models = whisper.available_models()
        expected_models = ['tiny', 'base', 'small']
        for model in expected_models:
            self.assertIn(model, available_models)

if __name__ == '__main__':
    unittest.main()
