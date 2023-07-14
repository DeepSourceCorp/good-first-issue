<p align="center">
  <a href="https://goodfirstissue.dev" target="_blank">
    <img src="static/readme-logo.svg">
  </a>
</p>
<hr>

Welcome! 👋🏼

**Good First Issue** is an initiative that curates easy tasks from popular open-source projects, allowing developers who've never contributed to open-source before to get started quickly.

Open-source maintainers are always looking to involve more people, but new developers often perceive contributing as challenging. We believe that by providing developers with super-easy tasks, we can remove the barriers to entry and encourage future contributions. This is why Good First Issue exists.

## Adding a New Project

You are welcome to add a new project to Good First Issue. We encourage projects of all types and sizes to participate.

Follow these simple steps:

- Our goal is to curate projects suitable for new open-source contributors. To ensure the quality of projects in Good First Issue, please ensure that your GitHub repository meets the following criteria:

  - It should have at least three issues labeled as `good first issue`. This label is already present on all repositories by default. If not, you can follow the steps [here](https://help.github.com/en/github/managing-your-work-on-github/applying-labels-to-issues-and-pull-requests).

  - It should have at least 10 contributors.

  - It should contain a README.md file with detailed setup instructions for the project and a CONTRIBUTING.md file with guidelines for new contributors.

  - It should be actively maintained.

- Add your repository's path (in lexicographic order) in [data/repositories.toml](data/repositories.toml).

- Create a new pull request. Please include the link to the issues page of the repository in the PR description. Once the pull request is merged, the changes will be live on [goodfirstissue.dev](https://goodfirstissue.dev/).

## Setting Up the Project Locally

Good First Issue consists of two components: the front-end app built with Nuxt.js and a data population script written in Python.

To contribute new features and changes to the website, you will want to run the app locally. Please follow these steps:

1. Clone the project locally. Ensure that you have Python 3 and a recent version of Node.js installed on your computer.

2. Make a copy of the sample data files for your local app to use and rename them to the filenames that the app expects. **This step is important, as the front-end app won't work without these data files.**

```bash
$ cp data/generated.sample.json data/generated.json
$ cp data/tags.sample.json data/tags.json

Build the front-end app and start the development server.

$ yarn # install the dependencies
$ yarn dev -o # start the development server

