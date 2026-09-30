# Module 1 — Git & GitHub

**Student:** Navarro, Josell Marion C.
**Date:** October 1, 2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

Well technically, Git is a "save-game" machine that running locally in our computer.
It solves a lot of lost work by tracking every samll modification that makes to our codebaes.
Instead of saving a lot of files, Git takes a snapshot of our project. So basicaly, if there
a new feature that breaks our code, we can efforlessly back in time to that specific snapshot.

Github is like a hostplatform like to our Git repositories, think about like Google Docs, Cloud
storage. It stores, back it up, showcase, and collaborate with other team members seamlessly across different devices.

---

## Key vocabulary (in your own words)

- repository: This is the main project folder managed by Git that stores all project files, assets, and the complete history of every snapshot.
- commit: It is a saved snapshot of our staged code changes in Git, accompanied by a unique hash and a descriptive message explaining what was updated.
- branch:This is an independent, parallel copy of the codebase where we can safely build features or test bug fixes without breaking the stable main project
- push / pull: push uploads our local commit, while pull downloads and combines the latest changes.
- pull request: A request submitted on GitHub proposing that changes made in a feature branch be reviewed and merged into the main codebase.
- merge conflict: An error that occurs when two branches modify the exact same line of code in different ways, forcing to manually choose which version to keep before merging.

---

## Walking through what I did


```
git clone https://github.com/josellmarion62-sys/devnet-navarro-josell
cd devnet-navarro-josell
cd ..
git branch
git switch -c lesson4-functions
ni lesson4-functions.py
ctrl + s
git add lesson4-function.py
git commit -m "finishing lesson 4 - functions"
git push -u origin lesson4-functions

git add lesson-1-variables-datatypes
git commit -m "finishing lesson 1 - variables datatypes"
git push -u origin lesson-1-variables-datatypes

git add lesson-2-control-flow
git commit -m "finishing lesson 2 - control flow"
git push -u origin lesson-2-control-flow

git add lesson-3-loops-and-list
git commit -m "finishing lesson 3 - loops and list"
git push -u origin lesson-3-loops-and-list
```

---

## A mistake I made (or one I want to avoid)

Since I'm new to this Git and Github and didn't know this because I'm not on ICT strand before,
a mistake I made is that at first I dont know how to create different branches and Im confused about the compare & pull request before. I dont know how to git add, commit, and push but thankfully I may able to grasp the situation.

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
