@echo off
echo 🚀 Setting up Good First Issue development environment...

:: Check if required tools are installed
echo 📋 Checking required tools...

:: Check Node.js/Bun
where bun >nul 2>&1 || where node >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Neither Bun nor Node.js is installed
    echo Please install Bun (recommended): https://bun.sh/docs/installation
    echo Or Node.js: https://nodejs.org/
    exit /b 1
)

:: Check Python
where python >nul 2>&1 || where python3 >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python is not installed
    echo Please install Python 3.9+: https://www.python.org/downloads/
    exit /b 1
)

:: Check Poetry
where poetry >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Poetry is not installed
    echo Please install Poetry: https://python-poetry.org/docs/#installation
    exit /b 1
)

echo ✅ All required tools are available

:: Install Python dependencies
echo 🐍 Installing Python dependencies...
poetry install --no-root

:: Install Node.js dependencies
echo 📦 Installing Node.js dependencies...
where bun >nul 2>&1
if not errorlevel 1 (
    bun install
) else (
    npm install
)

:: Copy sample data files
echo 📋 Setting up data files...
copy data\generated.sample.json data\generated.json
copy data\tags.sample.json data\tags.json

:: Create environment file if it doesn't exist
if not exist .env (
    echo ⚙️  Creating environment file...
    copy .env.example .env
    echo 📝 Please edit .env and add your GitHub token
) else (
    echo ✅ Environment file already exists
)

echo.
echo 🎉 Setup complete!
echo.
echo Next steps:
echo 1. Edit .env and add your GitHub token from https://github.com/settings/tokens
echo 2. Run 'bun dev' or 'npm run dev' to start the development server
echo 3. Run 'bun populate' or 'npm run populate' to fetch real data
echo.
echo For more information, see README.md