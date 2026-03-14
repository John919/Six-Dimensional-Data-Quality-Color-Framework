#!/bin/bash
# Six-Dimensional Data Quality Framework Setup Script

echo "🔧 Creating virtual environment..."
python -m venv venv

echo "📦 Activating virtual environment..."
source venv/Scripts/activate  # Git Bash 用这个，Windows CMD 用 venv\Scripts\activate

echo "📚 Installing dependencies..."
pip install -r requirements.txt

echo "✅ Setup completed! Now run: python code/visual_demo.py"
