<p align="center">
  <a href="https://goodfirstissue.dev" target="_blank">
    <img src="public/readme-logo.svg">
  </a>
</p>
<hr>

# Welcome to Good First Issue! 👋🏼

**Good First Issue** is an initiative to curate beginner-friendly issues from popular projects, enabling developers new to open-source to contribute effortlessly.

Maintainers are always looking for new contributors, but for many developers, starting out in open-source can feel daunting. We aim to bridge this gap by highlighting "good first issues" — easy fixes that lower the entry barrier for future contributions.

---

## 🚀 Adding a New Project

You're encouraged to add new projects to **Good First Issue**, regardless of their size or age. Here's how you can contribute:  

### Requirements for Projects
To ensure quality, please ensure your project meets these criteria before adding it:  
1. **Good First Issue Label**: The repository must have at least three issues with the `good first issue` label. (If the label isn’t available, follow [these steps](https://docs.github.com/en/issues/using-labels).)  
2. **Contributors**: The project must have at least 10 contributors.  
3. **Documentation**: The repository should include:
   - A `README.md` with detailed setup instructions.
   - A `CONTRIBUTING.md` file outlining guidelines for new contributors.  
4. **Active Maintenance**: The project must be actively maintained.  

### Steps to Add Your Project
1. Add your repository's path (in lexicographic order) in `data/repositories.toml`.  
2. Create a pull request (PR) with your changes.  
3. Include a link to your repository's issues page in the PR description.  
4. Once your PR is merged, your project will be live on [goodfirstissue.dev](https://goodfirstissue.dev). 🎉  

---

## 🛠️ Setting Up the Project Locally

**Good First Issue** consists of two components:  
- A **front-end app** built with Nuxt.js.  
- A **data population script** written in Python.  

Follow these steps to set up the project locally:  

### Prerequisites  
- Python 3 installed on your computer.  
- A recent version of Node.js.  
- Bun package manager (used for dependency management and running the app).  
Install dependencies and start the development server:

🖋️ Contributing
We welcome contributions from everyone! Whether you're a beginner or an experienced developer, check out the issues labeled good first issue to get started.

For more details on contributing, please refer to the CONTRIBUTING.md file.

Follow these simple steps:

- Our goal is to narrow down projects for new open-source contributors. To maintain the quality of projects in Good First Issue, please make sure your GitHub repository meets the following criteria:

  - It has at least three issues with the `good first issue` label. This label is already present on all repositories by default. If not, you can follow the steps [here](https://help.github.com/en/github/managing-your-work-on-github/applying-labels-to-issues-and-pull-requests).

  - It has at least 10 contributors.

  - It contains a README.md with detailed setup instructions for the project, and a CONTRIBUTING.md with guidelines for new contributors.

  - It is actively maintained.

- Add your repository's path (in lexicographic order) in [data/repositories.toml](data/repositories.toml).

- Create a new pull-request. Please add the link to the issues page of the repository in the PR description. Once the pull request is merged, the changes will be live on [goodfirstissue.dev](https://goodfirstissue.dev/).

## Setting up the project locally

Good First Issue has two components — the front-end app built with Nuxt.js and a data population script written in Python.

To contribute new features and changes to the website, you would want to run the app locally. Please follow these steps:

1. Clone the project locally. Make sure you have Python 3 and a recent version of Node.js installed on your computer.

2. Make a copy of the sample data files for your local app to use and rename them to the filename that the app expects. **This step is important, as the front-end app won't work without these data files.**

```bash
$ cp data/generated.sample.json data/generated.json
$ cp data/tags.sample.json data/tags.json
```

3. Build the front-end app and start the development server.

```bash
$ bun install # install the dependencies
$ bun dev # start the development server
```

Open the app in your browser. It should now be running locally! 🎉
