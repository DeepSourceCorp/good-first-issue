<p align="center">
  <a href="https://goodfirstissue.dev" target="_blank">
    <img src="public/readme-logo.svg" alt="Good First Issue Logo" width="300">
  </a>
</p>

---

# Welcome to Good First Issue! 👋🏼

**Good First Issue** is an initiative to curate easy pickings from popular projects, so developers who've never contributed to open-source can get started quickly.

Open-source maintainers are always looking to get more people involved, but new developers often think it's challenging to become contributors. We believe fixing super-easy issues removes the barrier for future contributions. This is why **Good First Issue** exists.

---

## **Table of Contents**
1. [Adding a New Project](#adding-a-new-project)
2. [Setting Up Locally](#setting-up-the-project-locally)
3. [Guide to Python Scripts](#guide-to-python-scripts)
4. [Contributing Guidelines](#contributing-guidelines)
5. [License](#license)

---

## **Adding a New Project**

We welcome and encourage you to add new projects — old and new, big and small. Here's how you can do it:

1. **Ensure Your Repository Meets These Criteria**:
   - Contains at least three issues labeled as `good first issue`. If the label is missing, you can add it by following [these steps](https://help.github.com/en/github/managing-your-work-on-github/applying-labels-to-issues-and-pull-requests).
   - Has at least 10 contributors.
   - Includes a `README.md` with detailed setup instructions and a `CONTRIBUTING.md` with guidelines for new contributors.
   - Is actively maintained.

2. **Add Your Repository**:
   - Add your repository's path (in lexicographic order) in the file [data/repositories.toml](data/repositories.toml).

3. **Submit a Pull Request**:
   - Create a new pull request with a link to the issues page of your repository in the description.
   - Once approved and merged, the changes will be live on [goodfirstissue.dev](https://goodfirstissue.dev/).

---

## **Setting Up the Project Locally**

Good First Issue has two components:
1. **Front-end App**: Built with Nuxt.js.
2. **Data Population Script**: Written in Python.

Follow these steps to run the app locally:

### Prerequisites
Make sure you have the following installed:
- Python 3.
- A recent version of Node.js.

### Steps to Set Up
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/DeepSourceCorp/good-first-issue.git
   cd good-first-issue
   ```

2. **Prepare Sample Data**:
   Copy the sample data files and rename them to the expected filenames:
   ```bash
   cp data/generated.sample.json data/generated.json
   cp data/tags.sample.json data/tags.json
   ```

3. **Install Dependencies and Start the Server**:
   ```bash
   bun install # Install dependencies
   bun dev # Start the development server
   ```

4. Open your browser and navigate to `http://localhost:3000` to view the app.

---

## **Guide to Python Scripts**

This section explains the purpose and usage of the Python scripts included in this repository. It covers:

- **Data Population**: Scripts to populate the latest data required for the project.
- **Testing**: Scripts to ensure data consistency and integrity.

Refer to the [python-scripts-guide.md](python-scripts-guide.md) file for detailed instructions.

---

## **Contributing Guidelines**

We welcome contributions of all kinds! Here's how you can help:

1. **Explore Open Issues**:
   Check for open issues in this repository and start with those labeled `good first issue`.

2. **Submit Enhancements**:
   Propose new features or improvements by opening a pull request.

3. **Report Bugs**:
   If you find any issues, create a new issue with detailed steps to reproduce.

---

## **License**

Good First Issue is licensed under the [MIT License](LICENSE).