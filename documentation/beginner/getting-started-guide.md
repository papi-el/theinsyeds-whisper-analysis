# Getting Started with Whisper on Mac M4: Complete Beginner's Guide

## What You'll Need
- Mac with Apple Silicon (M1, M2, M3, or M4)
- About 30 minutes of setup time
- Basic comfort with Terminal (we'll guide you!)

## Step 1: Prepare Your Mac

### Install Homebrew (if you don't have it)
Open Terminal and paste this command:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

### Install Python and FFmpeg
brew install python@3.11 ffmpeg

## Step 2: Set Up Your Environment

### Create a Clean Python Environment
Install miniconda if you don't have it

curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh
bash Miniconda3-latest-MacOSX-arm64.sh
Create environment for Whisper

conda create -n whisper-setup python=3.11
conda activate whisper-setup

### Install Whisper
pip install openai-whisper

## Step 3: Test Your Installation

### Create a Test Audio File
Create a folder for your audio files

mkdir whisper-test
cd whisper-test
Create a test audio file using your Mac's built-in speech

say "Hello, this is a test of Whisper speech recognition" -o test.aiff
ffmpeg -i test.aiff test.wav

### Run Your First Transcription
python -c "import whisper; model = whisper.load_model('base'); result = model.transcribe('test.wav'); print('Transcription:', result['text'])"

## Step 4: Understanding the Results

You should see output like:
Transcription: Hello, this is a test of Whisper speech recognition

**What just happened?**
1. Whisper loaded the "base" model (good balance of speed and accuracy)
2. It processed your audio file
3. It returned the transcribed text

## Step 5: Try Different Models

### Fastest (for real-time use)
python -c "import whisper; model = whisper.load_model('tiny'); result = model.transcribe('test.wav'); print('Tiny model:', result['text'])"

### Most Accurate (for important transcriptions)
python -c "import whisper; model = whisper.load_model('small'); result = model.transcribe('test.wav'); print('Small model:', result['text'])"

## Common Issues and Solutions

### "Command not found" errors
- Make sure you activated your conda environment: `conda activate whisper-setup`
- Restart Terminal after installing Homebrew

### Slow processing
- First run downloads the model (takes time)
- Subsequent runs are much faster
- Larger models take longer but are more accurate

### Audio file errors
- Make sure your audio file exists: `ls -la test.wav`
- Try different audio formats: MP3, M4A, WAV all work

## Next Steps

Once you have basic transcription working:
1. **Try your own audio files**: Replace `test.wav` with your recordings
2. **Experiment with different models**: tiny, base, small, medium, large
3. **Explore the full analysis**: Check out our technical notebook for advanced features

## Getting Help

If you run into issues:
1. Check that all commands ran without errors
2. Make sure you're in the right directory
3. Verify your conda environment is activated
4. Try restarting Terminal and starting over

**Congratulations!** You now have Whisper running locally on your Mac M4! 🎉

