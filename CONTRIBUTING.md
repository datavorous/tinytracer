# Contributing to TinyTracer

Welcome to Winter of Open Source! 🎉    
We're excited to have you contribute to this path tracing project.

## Getting Started

### Prerequisites
1. Python 3.8 or higher
2. Git installed on your system
3. A GitHub account

### Setting Up Local Environment

1. **Fork the repository**  
   Click the "Fork" button at the top right of this repository.

2. **Clone your fork**
```bash
git clone https://github.com/YOUR_USERNAME/tinytracer.git
cd tinytracer
````

3. **Create a virtual environment** (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. **Install dependencies**

```bash
pip install uv
```

5. **Test the setup**

```bash
uv run tinytracer/main.py
```

This should generate `output/image.ppm`.

## How to Contribute

### Step 1: Choose an Issue

* Browse [open issues](../../issues)
* Look for labels:

  * `good first issue` – beginner-friendly
  * `easy`, `medium`, `hard` – based on difficulty
  * `documentation`, `bug`, `feature`, `enhancement`

### Step 2: Assign Yourself

* Comment `/assign` on the issue
* Wait for maintainer approval
* Complete issue within **48 hours**
* Work on **only 1 issue at a time**

### Step 3: Create a Branch

```bash
git checkout -b fix/issue-number-short-description
```

Example branch names:

* `fix/23-add-docstrings`
* `feature/45-png-export`
* `docs/12-improve-readme`

### Step 4: Make Changes

* Follow existing code style (`black` in this case)
* Add meaningful comments
* Test your changes thoroughly
* Keep commits atomic

### Step 5: Commit Changes

```bash
git add .
git commit -m "Clear commit message

- Description of changes
- Link to issue: Fixes #23"
```

### Step 6: Push & Create PR

```bash
git push origin fix/issue-number-short-description
```

* Go to your fork on GitHub --> “Compare & pull request”
* Fill out the PR template:
    - Link the issue using `Fixes #<issue-number>`
    - Describe what changes you made
    - Include screenshots/test results if applicable
    - Check all checklist items (if present)

## PR Acceptance Criteria

* Code is clean, commented, and follows PEP 8
* Code formatted with `black`
* Docstrings added for new functions/classes
* PR linked to an issue
* Screenshots/tests included if applicable
* No plagiarism

## Points System

| Contribution Type | Points |
| ----------------- | ------ |
| Easy Issue        | 10     |
| Medium Issue      | 20     |
| Hard Issue        | 40     |
| Documentation Fix | 5      |
| Bug Fix           | 20     |
| Feature Addition  | 30     |

### Bonuses

* First 10 PRs : +10 points
* First PR of the week : +10 points
* Most impactful PR : +50 points

## Reporting Bugs

* Provide description, steps to reproduce, expected vs actual behavior
* Include Python version and OS
* Include error messages/screenshots if any

## Suggesting Features

* Describe the feature
* Explain why it's useful
* Optional: share implementation ideas

> [!NOTE]
> Follow the default templates while creating an Issue.

## Code Style

- Follow [PEP 8](https://pep8.org/)
- Use 4-space indentation
- Maximum line length: 88 characters
- Use descriptive variable names
- Explain **why**, not just what in comments
- **All code must be formatted using [`black`](https://github.com/psf/black)**
  - Install: `pip install black`
  - Format your code before committing: `black .`

### Example:

```python
# Good: Explains WHY
# Use half_b optimization to reduce floating point errors
half_b = oc.dot(ray.direction)

# Bad: Explains WHAT (obvious)
half_b = oc.dot(ray.direction)
```

## Getting Help

* Discord: [Server link]()
* GitHub Discussions
* Comment on issues to reach maintainers

## Important Rules

* Work on **one issue at a time**
* Complete assigned issues in 48 hours (can be extended based on difficulty)
* Respect code of conduct
* Always link your PR to an issue
* Avoid plagiarism or AI generated slop
<p>
<center>
<b>Happy Contributing! <3</b>
</center>
</p>