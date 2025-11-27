# Development Guide

This document provides detailed instructions for setting up and contributing to the Good First Issue project.

## Quick Start

For the fastest setup, run one of the setup scripts:

**Unix/macOS/Linux:**
```bash
chmod +x setup.sh
./setup.sh
```

**Windows:**
```cmd
setup.bat
```

## Manual Setup

If you prefer to set up manually or the scripts don't work:

### Prerequisites

- **Node.js** (v18+) or **Bun** (recommended)
- **Python** (3.9+)
- **Poetry** (for Python dependency management)
- **Git**

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/BugHunterX2101/goodfirst.git
   cd goodfirst
   ```

2. **Install Python dependencies:**
   ```bash
   poetry install --no-root
   ```

3. **Install Node.js dependencies:**
   ```bash
   # Using Bun (recommended)
   bun install
   
   # Or using npm
   npm install
   ```

4. **Set up data files:**
   ```bash
   # Copy sample data files
   cp data/generated.sample.json data/generated.json
   cp data/tags.sample.json data/tags.json
   ```

5. **Configure environment:**
   ```bash
   # Create environment file
   cp .env.example .env
   
   # Edit .env and add your GitHub token
   # Get a token from: https://github.com/settings/tokens
   ```

## Development Commands

### Frontend Development

```bash
# Start development server
bun dev        # or npm run dev

# Build for production
bun build      # or npm run build

# Generate static site
bun generate   # or npm run generate

# Preview production build
bun preview    # or npm run preview
```

### Data Management

```bash
# Populate with real data (requires GitHub token)
bun populate   # or npm run populate

# Sync data to/from Vercel Blob (requires BLOB_READ_WRITE_TOKEN)
bun sync up    # Upload local data
bun sync down  # Download remote data
```

### Code Quality

```bash
# Format code
bun format     # or npm run format

# Lint code
bun lint       # or npm run lint

# Run tests
bun test       # or npm run test
```

## Project Structure

```
goodfirst/
├── assets/           # CSS and other assets
├── components/       # Vue.js components
├── composables/      # Vue.js composables
├── data/            # Repository and tag data
├── gfi/             # Python scripts for data population
├── layouts/         # Nuxt.js layouts
├── pages/           # Nuxt.js pages
├── public/          # Static files
├── .env.example     # Environment variables template
├── nuxt.config.ts   # Nuxt.js configuration
├── package.json     # Node.js dependencies and scripts
├── pyproject.toml   # Python dependencies
└── tailwind.config.js # Tailwind CSS configuration
```

## Environment Variables

Create a `.env` file based on `.env.example`:

- `GH_ACCESS_TOKEN`: GitHub personal access token for fetching repository data
- `BLOB_READ_WRITE_TOKEN`: Vercel Blob storage token (for deployment)

## Common Issues and Solutions

### Missing Data Files

**Error:** Application fails to load with missing data files.

**Solution:** Run the setup script or manually copy sample files:
```bash
cp data/generated.sample.json data/generated.json
cp data/tags.sample.json data/tags.json
```

### GitHub API Rate Limiting

**Error:** "API rate limit exceeded" when populating data.

**Solution:** 
1. Ensure you have a valid GitHub token in `.env`
2. Use a personal access token with appropriate permissions
3. Wait for rate limit to reset (usually 1 hour)

### Python Dependencies

**Error:** Poetry or Python packages not found.

**Solution:**
1. Install Poetry: https://python-poetry.org/docs/#installation
2. Run `poetry install --no-root`

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Run tests and linting: `bun test && bun lint`
5. Commit your changes: `git commit -am 'Add feature'`
6. Push to the branch: `git push origin feature-name`
7. Create a Pull Request

## Deployment

The site is deployed on Vercel. Key points:

- Static generation is used (`bun generate`)
- Data is synced using Vercel Blob storage
- Environment variables must be set in Vercel dashboard

For more information, see the main README.md file.