---
description: Set up a new project folder for Dr. Mona Instagram work
argument-hint: "[target folder — defaults to the current directory]"
---

Set up a working folder for Dr. Mona Instagram content, using the `dr-mona-posts` skill.

**The user's request:**

$ARGUMENTS

**Do this**

1. Load the `dr-mona-posts` skill so you know where its files live.
2. In the target folder (default: the current directory), create:
   ```
   assets/          <- copy the skill's assets/ folder here
   ready-posts/     <- static posts and carousels, dated
   reels/           <- reel covers, dated
   ```
   Copy the skill's `assets/` directory in, so slide files can use the `../../../assets/…`
   paths the templates already carry. Never move or modify the skill's own copy.
3. Write a short `README.md` in the target folder covering: the folder rule
   (`ready-posts/YYYY-MM-DD/post-NN-topic/`), the three slash commands
   (`/dr-mona:post`, `/dr-mona:carousel`, `/dr-mona:reel-cover`), and the fact that the
   background colour is the one input the user supplies per post.
4. Do **not** create a `CLAUDE.md` unless the user asks — the skill already carries the
   rules, and duplicating them is how the two drift apart.
5. Confirm what you created, then tell the user they can start with
   `/dr-mona:carousel <topic> ground: sage`.
