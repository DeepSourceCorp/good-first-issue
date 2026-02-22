<p align="center">
  <a href="https://goodfirstissue.dev" target="_blank">
    <img src="public/readme-logo.svg" width="600" alt="Good First Issue Logo">
  </a>
</p>

<p align="center">
  <strong>Democratizing Open Source contribution by lowering the barrier to entry for everyone.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/github/stars/DeepSourceCorp/good-first-issue?style=for-the-badge&logo=github&color=FFD700" alt="3.2k stars">
  <img src="https://img.shields.io/github/forks/DeepSourceCorp/good-first-issue?style=for-the-badge&logo=github&color=white" alt="1.2k forks">
  <img src="https://img.shields.io/github/contributors/DeepSourceCorp/good-first-issue?style=for-the-badge&logo=github&color=32c955" alt="220 contributors">
  <img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="MIT License">
</p>

---

## 💡 The Philosophy: Why This Matters

The "Empty Editor" problem is real. Many brilliant developers want to contribute to open source but feel like imposters when looking at massive, complex codebases. 

**Good First Issue** exists because we believe:
* **The first PR is the hardest:** Once a developer clears the psychological hurdle of their first contribution, they are 10x more likely to continue.
* **Maintainers need fresh energy:** Every large project started with one small commit. We help maintainers find their future long-term contributors.
* **Community > Code:** We aren't just a list of bugs; we are a gateway to the global developer community.

---

## 🏗️ Technical Deep Dive & Setup

This project is a hybrid of a **Python-powered data engine** and a **Vue/Nuxt-based frontend**. Here is how to get the engine purring on your local machine.

### 🔌 Prerequisites
* **Python 3.8+** (for processing the GitHub data)
* **Node.js 16+** (for the Nuxt.js web interface)

### 🚀 Getting Started
```bash
# 1. Clone the project
git clone [https://github.com/DeepSourceCorp/good-first-issue.git](https://github.com/DeepSourceCorp/good-first-issue.git)
cd good-first-issue

# 2. Setup Python environment (The Brain)
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Setup Vue/Nuxt environment (The Beauty)
npm install
