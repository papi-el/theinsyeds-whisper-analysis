#!/bin/bash
echo "🔍 Verifying theinsyeds-whisper-analysis project completion..."
echo "=" * 60

# Check main directories
for dir in analysis assets data documentation research results; do
    if [ -d "$dir" ]; then
        echo "✅ $dir/ directory exists"
    else
        echo "❌ $dir/ directory missing"
    fi
done

# Check key files
key_files=(
    "requirements.txt"
    "README.md" 
    "RESEARCH_LOG.md"
    "analysis/notebooks/whisper-pipeline-deep-dive.ipynb"
    "documentation/technical/README.md"
    "documentation/technical/METHODOLOGY.md"
    "documentation/beginner/whisper-explained-simply.md"
    "documentation/beginner/getting-started-guide.md"
)

for file in "${key_files[@]}"; do
    if [ -f "$file" ]; then
        echo "✅ $file exists"
    else
        echo "❌ $file missing"
    fi
done

echo ""
echo "📊 Project Statistics:"
echo "Total files: $(find . -type f | wc -l)"
echo "Total directories: $(find . -type d | wc -l)"
echo "Documentation files: $(find documentation -name "*.md" | wc -l)"
echo "Analysis files: $(find analysis -type f | wc -l)"

echo ""
echo "🎉 Project completion verification done!"
