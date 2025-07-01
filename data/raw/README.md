# Raw Data Directory

## Original Audio Files
- `original-test-audio.aiff` - Source audio created with macOS `say` command
- `original-test-audio.wav` - Converted version for compatibility

## Data Collection Method
Audio generated using:
say "Hello, this is a test of Whisper speech recognition on Mac M4. I am building a technical analysis for the Insyeds brand." -o test.aiff
ffmpeg -i test.aiff test.wav

## Specifications
- **Content:** Technical phrase including brand name for quality testing
- **Duration:** ~10 seconds
- **Quality:** Clean synthetic speech for consistent benchmarking
- **Purpose:** Standardized input for model comparison analysis
