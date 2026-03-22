# Contributing to VYOMA AI

First of all, thank you for considering contributing to VYOMA AI! It's people like you that make VYOMA AI such a great project.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md).

## Getting Started

1. **Fork** the repository on GitHub.
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-username/vyoma-ai.git
   ```
3. **Set up the backend**:
   ```bash
   cd vyoma-ai/backend
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
4. **Set up the frontend**:
   ```bash
   cd ../frontend
   # (If using package managers in the future, e.g., npm install)
   ```

## Creating a Pull Request

1. Create a new branch: `git checkout -b feature/your-feature-name` or `bugfix/issue-description`
2. Make your appropriate, granular commits.
3. Test your changes locally.
4. Push to your fork and submit a pull request.
5. Ensure your PR description clearly describes the problem and solution.

## Reporting Bugs

Please use the bug report template under `.github/ISSUE_TEMPLATE` to report bugs. Include as much detail as possible, such as logs, OS version, and browser version.

## Proposing Features

We welcome new features! Please open a feature request using the template under `.github/ISSUE_TEMPLATE` to discuss it before you begin implementation.
