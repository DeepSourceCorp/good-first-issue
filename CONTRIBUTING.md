# Contributing to Good First Issue

Thank you for your interest in contributing to Good First Issue! We welcome contributions from developers of all skill levels.

## How to Contribute

### Adding a New Project

You're welcome to add a new project to Good First Issue. Please ensure your GitHub repository meets the following criteria:

- It has at least three issues with the `good first issue` label
- It has at least 10 contributors
- It contains a `README.md` with detailed setup instructions
- It contains a `CONTRIBUTING.md` with guidelines for new contributors
- It is actively maintained

**Steps to add a project:**

1. Fork this repository
2. Add your repository's path in **lexicographic order** in [`data/repositories.toml`](data/repositories.toml)
3. Create a pull request with the link to the issues page of your repository in the PR description

### Contributing Code or Documentation

1. **Fork the repository** - Click the "Fork" button at the top right of this repository
2. **Clone your fork locally**
   ```bash
   git clone https://github.com/YOUR_USERNAME/good-first-issue.git
   cd good-first-issue
   ```
3. **Create a new branch**
   ```bash
   git checkout -b your-branch-name
   ```
4. **Make your changes** - Edit the relevant files
5. **Test your changes** (see Testing section below)
6. **Commit your changes**
   ```bash
   git add .
   git commit -m "Brief description of your changes"
   ```
7. **Push to your fork**
   ```bash
   git push origin your-branch-name
   ```
8. **Create a Pull Request** - Go to the original repository and click "New Pull Request"

## Setting Up the Development Environment

Good First Issue has two components:
- **Front-end app** built with Nuxt.js
- **Data population script** written in Python

### Prerequisites

- Python 3.9 or higher
- Node.js (recent version)
- [Bun](https://bun.sh/docs/installation) - JavaScript runtime and package manager
- Poetry (Python package manager)

### Setup Steps

1. **Clone the repository** (if you haven't already)
   ```bash
   git clone https://github.com/YOUR_USERNAME/good-first-issue.git
   cd good-first-issue
   ```

2. **Set up sample data files**
   ```bash
   cp data/generated.sample.json data/generated.json
   cp data/tags.sample.json data/tags.json
   ```

3. **Install dependencies**
   
   For Python:
   ```bash
   pip install --upgrade poetry
   poetry install --no-root
   ```
   
   For JavaScript:
   ```bash
   bun install
   ```

4. **Start the development server**
   ```bash
   bun dev
   ```

The app should now be running on `http://localhost:3000`.

## Running Tests Locally

### Running Python Tests

The project includes data validation tests and type checking:

```bash
# Run all tests
make test

# Or run individually:
poetry run python gfi/test_data.py    # Run data sanity tests
poetry run mypy gfi/*.py               # Run type checking
```

### Test Coverage

The tests verify:
- Data file existence and validity
- No duplicate repository entries
- Proper TOML and JSON formatting
- Type safety across Python modules

## Code Formatting

We use automated code formatters to maintain consistent code style:

```bash
# Format all code (Python and JavaScript)
make format

# Or run individually:
poetry run ruff format .               # Format Python code
bunx prettier --write .                # Format JavaScript/TypeScript/Markdown
```

Please ensure your code is properly formatted before submitting a pull request.

## Building the Project

```bash
# Full build
make build

# Generate data from repositories
make generate

# Production build with remote data sync
make generate-prod
```

## Pull Request Guidelines

- Keep pull requests focused on a single issue or feature
- Write clear, descriptive commit messages
- Reference the issue number in your PR description (e.g., "Fixes #123")
- Ensure all tests pass before submitting
- Update documentation if you're changing functionality
- Follow the existing code style and conventions

## Need Help?

- Check existing [issues](https://github.com/DeepSourceCorp/good-first-issue/issues) for similar problems or questions
- Look for issues labeled `good first issue` if you're new to the project
- Feel free to ask questions in the issue comments

## Code of Conduct

Please be respectful and considerate in all interactions. We aim to foster an inclusive and welcoming community for everyone.

---

Thank you for contributing to Good First Issue! 🎉
