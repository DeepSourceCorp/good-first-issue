# Contributing to Good First Issue

Thanks for your interest in contributing to Good First Issue! 👋

This guide will help you set up the project, understand its structure, and make your first contribution.

## Prerequisites

Before getting started, make sure you have the following tools installed:

- **Node.js (v18 or later):** [Download Node.js](https://nodejs.org/)
- **Bun:** A fast JavaScript runtime and package manager. Install it using:

  ```bash
  curl -fsSL https://bun.sh/install | bash
  ```

  For other installation methods, visit the [official Bun website](https://bun.sh/).

- **uv:** A fast Python package manager. Install it using:

  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

  Alternatively, install it using Homebrew:

  ```bash
  brew install uv
  ```

  For more information, see the [uv documentation](https://docs.astral.sh/uv/).

## Project Structure

Good First Issue consists of two main components:

- **Front-end application:** Built with Nuxt.js, it displays a curated list of repositories.
- **Data population script:** Written in Python, it fetches repository information from GitHub.

## Setting Up Locally

Follow these steps to run the project on your computer.

### 1. Clone the repository

Clone the repository and navigate to its directory:

```bash
git clone https://github.com/DeepSourceCorp/good-first-issue.git
cd good-first-issue
```

### 2. Set up the Python environment

Install the Python dependencies and configure the development environment:

```bash
uv sync --all-extras
```

This command creates a virtual environment and installs the project's dependencies.

### 3. Set up sample data files

The front-end application requires data files to display repository information. Create them by copying the provided sample files:

```bash
cp data/generated.sample.json data/generated.json
cp data/tags.sample.json data/tags.json
```

The files serve the following purposes:

- `generated.json`: Contains repository metadata, including stars, issues, and programming languages.
- `tags.json`: Contains language tags used for filtering repositories.

### 4. Install front-end dependencies

Install the JavaScript dependencies using Bun:

```bash
bun install
```

### 5. Start the development server

Run the following command:

```bash
bun dev
```

Once the development server starts, open [http://localhost:3000](http://localhost:3000) in your browser.

## Running Tests

Run the data sanity tests with:

```bash
uv run python gfi/test_data.py
```

To check Python code for type errors, run:

```bash
uv run mypy gfi/*.py
```

You can also run both checks using:

```bash
make test
```

## Formatting Code

To format the code according to the project's configured formatting tools, run:

```bash
make format
```

Run the formatter before submitting changes when your contribution modifies code.

## Making Changes

Follow these steps when contributing:

1. Create a new branch for your changes.
2. Make your changes and test them locally.
3. Review your changes to ensure they follow the project's contribution guidelines.
4. Submit a pull request with a clear description of what you changed and why.
5. Respond to feedback from maintainers and make any requested updates.

Keep contributions focused, useful, and easy to review.

## AI Usage Guidelines

If you use AI tools such as ChatGPT, Claude, or GitHub Copilot while contributing, please follow these guidelines:

- **Disclose AI usage:** Mention AI assistance in your pull request description.
- **Review and test:** Check all AI-generated changes and test them where applicable.
- **Ensure accuracy:** Do not submit code or documentation changes that you have not reviewed and verified.

Low-quality AI-generated pull requests or issues may be closed without review.

*Inspired by [Ghostty's AI Policy](https://github.com/ghostty-org/ghostty/blob/main/AI_POLICY.md).*
