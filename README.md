# A basic guide on Git, GitHub & Markdown

This guide introduces some essential tools used in modern software development. If you're just getting started, these concepts will quickly become part of your daily workflow.

---

## 1. What is Git?

Unlike a centralised system where a single server hosts the main repository (Developers must connect to this server to perform any sort of task), Git is a **distributed version control system** used to track changes to files, especially in software projects.

Git helps you:

1.1. **Track changes over time** – Records every modification you make, allowing you to revisit earlier versions if needed. It basically records the history of your project. 
1.2. **Work safely** – If something breaks, you can revert to a stable version without losing your work. You can branch out, revert or edit.  
1.3. **Collaborate efficiently** – Multiple individuals can work on the same project simultaneously without overwriting each other’s changes.

One of Git’s most powerful features is **branching**, which allows you to create separate versions of your project (branches) to experiment with or develop features independently, and later merge them back into the main project.

Git is also supported across a variety of software not related to programming too, such as KiCad, Overleaf etc!

---

## 2. How to Push Code to GitHub

GitHub is where your Git projects live online.

Here’s a simple step-by-step process:

### Step 1: Initialise Git in your project

git init


### Step 2: Add your files

git add .

### Step 3: Save (commit) your changes


git commit -m "First commit"


### Step 4: Connect your project to GitHub


git remote add origin https://github.com/your-username/your-repo-name.git

### Step 5: Push your code

git push -u origin main

That's it!!

---

## 3. What is Markdown?

Markdown is a markup language for formatting plain text. 

Instead of relying on graphical editors (like Word or Google Docs), Markdown uses simple formatting symbols (which makes it easy to learn), and hence it is:

3.1. **Very Readable** – Even without formatting, the text is still clear
3.2. **Widely supported** – Used across platforms like GitHub, documentation sites, and note-taking tools

Markdown is commonly used for:

* README files (like this one)
* Project documentation
* Technical notes and reports

---

## 4. Basic Markdown Syntax

Below are some of the most commonly used Markdown features.

### Headings

Headings are created using the `#` symbol. The number of `#` symbols determines the level of the heading.

```markdown
# Heading 1
## Heading 2
### Heading 3
```

This helps organise content into sections.

---

### Lists

Useful for structuring information.

**Unordered lists** (bulleted):

```markdown
- Item 1
- Item 2
- Item 3
```

**Ordered lists** (numbered):

```markdown
1. First item
2. Second item
3. Third item
```

---

### Code Blocks (for code snippets)

Inline code (within a sentence):

```markdown
Use the `git status` command to check changes.
```

Multiline code blocks:

````markdown
```python
print("Hello, world!")
```
````

You can also specify the programming language (like `python`, `bash`, etc.) for better readability.

---

### Links

Links allow you to reference external resources.

```markdown
[Visit GitHub](https://github.com)
```

This will display as:
[Visit GitHub](https://github.com)

---
