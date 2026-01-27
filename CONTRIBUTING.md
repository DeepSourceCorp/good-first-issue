# Contributing to Good First Issue

Thanks for your interest in contributing! This guide will help you get started.

## Prerequisites

Before you begin, make sure you have the following installed:

- **Node.js** (v18 or later) - [Download](https://nodejs.org/)
- **Bun** - A fast JavaScript runtime and package manager. Install it with:
  ```bash
  curl -fsSL https://bun.sh/install | bash
  ```
  Or see [bun.sh](https://bun.sh/) for other installation methods.
- **uv** - A fast Python package manager. Install it with:
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
  Or via Homebrew: `brew install uv`. See [docs.astral.sh/uv](https://docs.astral.sh/uv/) for details.

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

2. **Set up Python environment**

   ```bash
   uv sync --all-extras
   ```

   This creates a virtual environment and installs all dependencies.

3. **Set up sample data files**

   The front-end app needs data files to display repositories. Copy the sample files to get started:

   ```bash
   cp data/generated.sample.json data/generated.json
   cp data/tags.sample.json data/tags.json
   ```

   These files contain:
   - `generated.json` - Repository metadata (stars, issues, languages, etc.)
   - `tags.json` - Language tags for filtering

4. **Install frontend dependencies**

   ```bash
   bun install
   ```

5. **Start the development server**

   ```bash
   bun dev
   ```

   The app will open at [http://localhost:3000](http://localhost:3000).

## Running Tests

To run the data sanity tests:

```bash
uv run python gfi/test_data.py
```

To run type checking:

```bash
uv run mypy gfi/*.py
```

Or run both with:

```bash
make test
```

## Formatting Code

```bash
make format
```

## Making Changes

1. Create a new branch for your changes
2. Make your changes and test them locally
3. Submit a pull request with a clear description of what you changed and why

## AI Usage Guidelines

If you use AI tools (Claude, Copilot, ChatGPT, etc.) when contributing:

- **Disclose AI usage** in your pull request description
- **Review and test** all AI-generated code before submitting
- **Ensure accuracy** - don't submit code you haven't verified works

Low-quality AI-generated PRs or issues will be closed without review.

_Inspired by [Ghostty's AI Policy](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md)._
