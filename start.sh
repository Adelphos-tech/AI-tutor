#!/bin/bash

# Simple launcher script for AI Science Teacher
# This script will try different methods to start a local server

echo "🌟 Amlak AI Science Teacher - Launcher"
echo "======================================"
echo ""

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 found - Starting server..."
    python3 start_server.py
    exit 0
fi

# Check if Python is available (might be Python 3)
if command -v python &> /dev/null; then
    PYTHON_VERSION=$(python --version 2>&1 | grep -oP '\d+\.\d+')
    MAJOR_VERSION=$(echo $PYTHON_VERSION | cut -d. -f1)
    
    if [ "$MAJOR_VERSION" -eq "3" ]; then
        echo "✅ Python 3 found - Starting server..."
        python start_server.py
        exit 0
    fi
fi

# Check if Node.js is available
if command -v node &> /dev/null; then
    echo "✅ Node.js found - Starting server with npx serve..."
    npx serve . -l 8000
    exit 0
fi

# If nothing is available
echo "❌ Error: No suitable server found!"
echo ""
echo "Please install one of the following:"
echo "  • Python 3: https://www.python.org/downloads/"
echo "  • Node.js: https://nodejs.org/"
echo ""
echo "Or simply open 'voice_white_theme.html' directly in your browser"
exit 1
