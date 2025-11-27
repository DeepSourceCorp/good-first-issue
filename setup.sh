#!/usr/bin/env bash

# Development setup script for Good First Issue
set -e

echo "🚀 Setting up Good First Issue development environment..."

# Check if required tools are installed
echo "📋 Checking required tools..."

# Check Node.js/Bun
if ! command -v bun &> /dev/null && ! command -v node &> /dev/null; then
    echo "❌ Error: Neither Bun nor Node.js is installed"
    echo "Please install Bun (recommended): https://bun.sh/docs/installation"
    echo "Or Node.js: https://nodejs.org/"
    exit 1
fi

# Check Python
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ Error: Python is not installed"
    echo "Please install Python 3.9+: https://www.python.org/downloads/"
    exit 1
fi

# Check Poetry
if ! command -v poetry &> /dev/null; then
    echo "❌ Error: Poetry is not installed"
    echo "Please install Poetry: https://python-poetry.org/docs/#installation"
    exit 1
fi

echo "✅ All required tools are available"

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
poetry install --no-root

# Install Node.js dependencies
echo "📦 Installing Node.js dependencies..."
if command -v bun &> /dev/null; then
    bun install
else
    npm install
fi

# Copy sample data files
echo "📋 Setting up data files..."
cp data/generated.sample.json data/generated.json
cp data/tags.sample.json data/tags.json

# Create environment file if it doesn't exist
if [ ! -f .env ]; then
    echo "⚙️  Creating environment file..."
    cp .env.example .env
    echo "📝 Please edit .env and add your GitHub token"
else
    echo "✅ Environment file already exists"
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env and add your GitHub token from https://github.com/settings/tokens"
echo "2. Run 'bun dev' or 'npm run dev' to start the development server"
echo "3. Run 'bun populate' or 'npm run populate' to fetch real data"
echo ""
echo "For more information, see README.md"