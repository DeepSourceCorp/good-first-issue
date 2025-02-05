<p align="center">
  <a href="https://goodfirstissue.dev" target="_blank">
    <img src="public/readme-logo.svg" alt="Good First Issue Logo">
  </a>
</p>

---

# 🚀 Welcome to **Good First Issue** 👋

> A platform to curate easy pickings from popular projects, making open-source contributions beginner-friendly.

## 🌟 Why Good First Issue?

- Open-source maintainers want more contributors 🤝
- New developers often find contributing challenging ❓
- We make it **easier** by listing beginner-friendly issues ✅

## 🔥 How to Add a New Project?

Follow these simple steps:

- Ensure your GitHub repository meets the following criteria:
  - ✅ At least **three** issues labeled `good first issue`.
  - 👥 At least **10 contributors**.
  - 📜 Contains a **detailed README.md** & **CONTRIBUTING.md**.
  - 🛠️ **Actively maintained**.
- Add your repository’s path (in lexicographic order) in [`data/repositories.toml`](data/repositories.toml).
- Create a **pull request (PR)** with a link to your issues page.
- Once merged, your project goes live on [goodfirstissue.dev](https://goodfirstissue.dev/) 🎉.

---

## 🛠 Setting Up Locally

### ⚡ Prerequisites
Ensure you have the following installed:

- [Python 3](https://www.python.org/downloads/)
- [Node.js (latest)](https://nodejs.org/)

### 🔧 Steps to Run Locally

1️⃣ **Clone the repository:**

```bash
$ git clone https://github.com/your-repo-url.git
$ cd your-repo
```

2️⃣ **Prepare the data files:**

```bash
$ cp data/generated.sample.json data/generated.json
$ cp data/tags.sample.json data/tags.json
```

3️⃣ **Install dependencies & start development server:**

```bash
$ bun install  # Install dependencies
$ bun dev      # Start development server
```

🚀 The app should now be running in your browser!

---

💡 **Happy Contributing!** 🎯
