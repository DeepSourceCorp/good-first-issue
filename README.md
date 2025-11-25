<p align="center">
  <a href="https://goodfirstissue.dev" target="_blank">
    <img src="public/readme-logo.svg">
  </a>
</p>
<hr>

Welcome! 👋🏼

**Good First Issue** is an initiative to curate easy pickings from popular projects, so developers who've never contributed to open-source can get started quickly.

Open-source maintainers are always looking to get more people involved, but new developers generally think it's challenging to become a contributor. We believe getting developers to fix super-easy issues removes the barrier for future contributions. This is why Good First Issue exists.

## Adding a new project

## Adding a new project

You are welcome to add a new project to **Good First Issue**, and we encourage all projects—old or new, large or small—to participate. This section provides a clear guide to help you prepare and submit your project correctly.

### 1. Verify project eligibility

Before adding your project, ensure that it meets the minimum quality standards. These checks help maintain consistency and make it easier for beginners to contribute.

#### Requirements:

- **At least three issues labeled `good first issue`**  
  The label `good first issue` helps identify beginner-friendly issues.  
  To create one:
  1. Navigate to your repository on GitHub and select the **Issues** tab.  
  2. Click **New issue**.  
  3. Write a clear title and description for a simple, well-defined task.  
  4. Click the **Labels** option and select `good first issue`.  
  5. Save the issue.  
  If this label does not already exist, you can create it manually or refer to [GitHub’s label documentation](https://help.github.com/en/github/managing-your-work-on-github/applying-labels-to-issues-and-pull-requests).

- **At least ten contributors**  
  You can check your contributors by navigating to **Insights → Contributors** in your repository.

- **Required documentation**  
  Your project should include both:
  - `README.md`: Explains the purpose, setup process, and basic usage of the project.  
  - `CONTRIBUTING.md`: Outlines contribution rules, coding standards, and best practices for new contributors.

- **Active maintenance**  
  Projects should show signs of recent activity—new commits, issue responses, or pull request reviews—to ensure that contributors receive timely support.

---

### 2. Add your repository entry

Once your project meets the above requirements, add it to the project list by editing the file [`data/repositories.toml`](data/repositories.toml).  
Insert your project details in **alphabetical order**.

Example entry:
```toml
["github.com/abhiramch018/AquaBotanica"]
issues = "https://github.com/abhiramch018/AquaBotanica/issues"


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

The app should open in your browser.
