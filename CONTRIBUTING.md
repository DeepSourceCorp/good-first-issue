# Contributing to Good First Issue

Thanks for your interest in contributing! This guide will help you get started.

## Prerequisites

Before you begin, make sure you have the following installed:

- **Node.js** (v18 or later) - [Download](https://nodejs.org/)
- **Python 3** - [Download](https://www.python.org/downloads/)
- **Bun** - A fast JavaScript runtime and package manager. Install it with:
  ```bash
  curl -fsSL https://bun.sh/install | bash
  ```
  Or see [bun.sh](https://bun.sh/) for other installation methods.

## Project Structure

Good First Issue has two main components:

- **Front-end app** - Built with Nuxt.js, displays the curated list of repositories
- **Data population script** - Written in Python, fetches repository data from GitHub

## Setting Up Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/DeepSourceCorp/good-first-issue.git
   cd good-first-issue
   ```

2. **Set up sample data files**

   The front-end app needs data files to display repositories. Copy the sample files to get started:

   ```bash
   cp data/generated.sample.json data/generated.json
   cp data/tags.sample.json data/tags.json
   ```

   These files contain:
   - `generated.json` - Repository metadata (stars, issues, languages, etc.)
   - `tags.json` - Language tags for filtering

3. **Install dependencies**

   ```bash
   bun install
   ```

4. **Start the development server**

   ```bash
   bun dev
   ```

   The app will open at [http://localhost:3000](http://localhost:3000).

## Running Tests

To run the data sanity tests:

```bash
python -m pytest gfi/test_data.py
```

Or using unittest directly:

```bash
python gfi/test_data.py
```

## Making Changes

1. Create a new branch for your changes
2. Make your changes and test them locally
3. Submit a pull request with a clear description of what you changed and why
