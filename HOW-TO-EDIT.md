# How to edit the Climate Health website

**Alex Davies** is currently the best person to contact for help:

[alexander.davies@bristol.ac.uk](mailto:alexander.davies@bristol.ac.uk)

Slack, Teams etc also work.

---

You don't need to install anything or know how to code. Everything can be done in your web browser on GitHub, and every change can be undone.

**The website:** https://alexodavies.github.io/bristol-climate-health-page/
**The files:** https://github.com/alexodavies/bristol-climate-health-page

**Jump to:** [Before you start](#before-you-start) · [Update your profile](#1-update-your-profile) · [Add your photo](#2-add-your-photo) · [Get your publications showing](#3-get-your-publications-showing) · [Write a blog post](#4-write-a-blog-post) · [Format your text (Markdown)](#5-format-your-text-markdown) · [Change other text](#6-change-other-text-on-the-site) · [Add a new person](#7-add-a-new-person-or-remove-one) · [If something goes wrong](#if-something-goes-wrong)


---

## Before you start

1. You need a free **GitHub account** (github.com → Sign up).
2. Ask a group lead to **add you as a collaborator** on the repository, so you can edit files directly. (If you don't have access yet, you can still suggest changes. See "Want a second pair of eyes?" below.)
3. After you save a change, the site rebuilds by itself. **Wait 1–3 minutes, then refresh the website** (hold Shift while you click refresh, in case your browser kept the old version).

### The basic edit, which is the same every time
1. Open the file on GitHub (the steps below tell you which).
2. Click the **pencil icon** (✏️) at the top right of the file to edit it.
3. Make your change.
4. Click the green **Commit changes…** button, then **Commit changes** again. Saving it is that simple.

### Want a second pair of eyes?
When you press **Commit changes…**, choose **"Create a new branch for this commit and start a pull request"** instead of committing directly. A group lead can then check your change and press **Merge**. Nothing goes live until then.

**Message/email Alex if you're not sure about something.**


[alexander.davies@bristol.ac.uk](mailto:alexander.davies@bristol.ac.uk)

---

## 1. Update your profile

Your profile lives in a file named after you in the **`_members`** folder, for example `_members/ruby-lieber.md`.

1. On the repository page, click **`_members`**, then click your file.
2. Click the pencil icon to edit.

The file has two parts. The part between the two `---` lines is your details. Everything below the second `---` is your **bio**, which is ordinary text.

```
---
name: Ruby Lieber
initials: RL
role: Research Staff
title: Senior Research Associate (BREATHE)
group: postdocs
order: 7
orcid: 0000-0003-3196-3080
links:
  profile: https://www.climatebristol.org/people/ruby-lieber/
  github:
  scholar:
---
Write your bio here as normal text. Leave a blank line between paragraphs.
```

| Line | What it does |
|---|---|
| `name` | How your name appears everywhere |
| `initials` | Shown if you don't have a photo yet |
| `role` | Your short role, for example Research Staff or PhD Student |
| `title` | Your full job title, shown under your name on the Team page |
| `group` | Which section of the Team page you appear in: `leads`, `postdocs` or `phds` |
| `stage` | Optional. The colour of the ring round your photo: `phd`, `postdoc` or `later` (later career). If you leave it out, it follows your `group` |
| `order` | A number, only used for ordering on the home page. Leave it as it is |
| `orcid` | Your ORCID iD, which fills in your publications (see section 3) |
| `links` | Your profile links (`profile`, `github`, `scholar` and `email`). Leave a link blank if you don't have one, or delete the line. Write any email address as `first dot last at bristol.ac.uk` (see below) |

**About email addresses:** spam programs ("crawlers") scan web pages for anything that looks like an email address. To avoid that, **please don't type your address in the normal way**. Write it in words instead:

```
email: first dot last at bristol.ac.uk
```

For example, `alexander dot davies at bristol.ac.uk`. Visitors still get a normal "Email" link that opens their mail program, because the site converts it in their browser. Leave the line blank if you would rather not list an email at all.

**Rules that keep the file working:**
- Keep the two `---` lines exactly as they are.
- Keep the spaces. Each line is `name:` followed by **one space**, then your text. The lines under `links:` are indented by two spaces.
- If your text contains a colon followed by a space (like `title: Research: climate`), put it in quotes: `title: "Research: climate"`.

---

## 2. Add your photo

The photo is found automatically from its **file name**. It has to match the name of your profile file.

- Profile file `_members/ruby-lieber.md` → photo `ruby-lieber.jpg`
- It can be `.jpg`, `.jpeg`, `.png` or `.webp`

**Steps:**
1. On the repository page, open the folder **`assets`** → **`images`** → **`people`**.
2. Click **Add file → Upload files**, and drag your photo in.
3. Click **Commit changes**.

**Tips for a good photo:**
- A head-and-shoulders photo, with your face in the **middle** of the picture (it is cropped into a hexagon).
- Roughly **800 pixels wide** is plenty. A huge file makes the site slow. Under 500 KB is ideal.
- If you replace a photo, upload the new one with the **same name**.

---

## 3. Get your publications showing

Publications are collected automatically from your **ORCID** record.

1. Make sure your ORCID iD is in your profile file (the `orcid:` line), written like `0000-0003-3196-3080` with no web address.
2. In your own ORCID account, check that your works are set to **visible to "Everyone"**. The site can only see public works.
3. The site updates every **Monday morning**. To update now, go to the repository's **Actions** tab → **Update citations** → **Run workflow**. Give it a couple of minutes.

**Good to know:**
- Only **journal articles** are shown.
- A small photo of each group member appears next to their papers. If a paper is missing your photo, your name is probably written differently on it. Tell a group lead, who can add it to your profile as an `aliases:` line.
- **Please don't edit `_data/citations.yaml` by hand.** It is rewritten automatically, so your edits would be lost.

---

## 4. Write a blog post

Posts are short and informal. Think "what I found, in a few paragraphs".

1. On the repository page, open the **`_posts`** folder.
2. Click **Add file → Create new file**.
3. In the name box, type the file name **with today's date first**, like `2026-05-14-my-short-title.md`. Use dashes, no spaces.
4. Paste in this template and fill it in:

```
---
title: A short, plain-English title
author: ruby-lieber
tag: Heat
excerpt: One or two sentences on what you found and why it matters.
paper: 10.xxxx/xxxxx
---
Write your post here. A few short paragraphs is plenty: what question you
asked, what you did, what you found, and what surprised you.
```

5. Click **Commit changes…**

| Line | What to put |
|---|---|
| `title` | The headline |
| `author` | **The name of your profile file without `.md`**, for example `ruby-lieber`. This puts your photo on the post and makes it appear on your profile page |
| `tag` | Optional. A one-word label such as Heat |
| `excerpt` | The one or two sentences shown in the blog list |
| `paper` | Optional. The DOI of the paper this post is about, which adds a "Read the paper" link. Delete the line if you don't have one |

Once you have a post, your profile page lists your posts and has a link that readers can use to subscribe to them.

To make text bold, add links or lists, see [section 5](#5-format-your-text-markdown).

**To fix a typo in a post:** open it from `_posts`, click the pencil, edit and commit.

---

## 5. Format your text (Markdown)


*This is the same syntax/language as any github `README.md`s you've written before.*

Your bio and your blog posts are written in **Markdown**: ordinary text with a few simple symbols for **bold**, links, lists and so on. It is much simpler than it sounds, and you can already write plain paragraphs without knowing any of it.


**Where it applies:** the text *below* the second `---` line in a profile or a post. The top part (name, title, and so on) is plain text, with no formatting.

**Tip:** when you edit a file on GitHub there is a **Preview** tab above the text box. Click it to see how your formatting will look before you commit.

### The basics

| You type | You get |
|---|---|
| A blank line between blocks of text | A new paragraph. **Always leave a blank line between paragraphs**, otherwise they run together |
| `**bold**` | **bold** |
| `*italic*` | *italic* |
| `[link text](https://www.bristol.ac.uk)` | a clickable link reading "link text". The web address goes in the round brackets and must start with `https://` |
| `## A heading` | a section heading. Use `##`, not `#`. A post's title is already the main heading |
| `### A smaller heading` | a smaller heading |
| `> A quotation` | an indented quotation |

### Lists

Start each line with a dash and a space for bullets, or a number and a full stop for a numbered list. Put a blank line before the list.

```
- First point
- Second point
- Third point

1. First step
2. Second step
3. Third step
```

### Pictures

1. Upload your picture to the **`assets/images`** folder (the same way as a profile photo in section 2). Small files are best, under 500 KB.
2. Add it to your text like this. Start with an exclamation mark and put a short description in the square brackets:

```
![Map of UK heat deaths in 2022](/bristol-climate-health-page/assets/images/my-map.png)
```

Notice that the address starts with `/bristol-climate-health-page/`. Leave that part exactly as it is and only change the file name at the end.

### Things that trip people up

- **A symbol suddenly does something unexpected.** Characters like `*`, `_` and `#` have special meanings. To show one as it is, put a backslash in front of it, for example `\*`.
- **A line starting with a number and a full stop becomes a list.** "2022. Was a hot year" turns into a list item. Rewrite it as "In 2022 it was a hot year", or put a backslash before the full stop: `2022\.`
- **Copying from Word or Google Docs.** The words come across fine, but bold, links and lists do not. Redo those using the symbols above.
- **Everything looks squashed together.** You probably need a blank line between paragraphs or before a list.
- **Not sure?** Write plain paragraphs. It is always fine, and a group lead can add the formatting later.

Want to see every trick? The official summary is at https://www.markdownguide.org/cheat-sheet/

---

## 6. Change other text on the site


**Please double check with the authors or Alex before removing or editing other peoples' files.**

| To change… | Open this file |
|---|---|
| The big title and intro on the home page | `index.md` |
| The three research cards (home and Research page) | `_data/research.yaml` |
| The project cards | `_data/projects.yaml` |
| The Research, Projects, Team, Blog or Contact page intro | `research.md`, `projects.md`, `team.md`, `blog.md`, `contact.md` (the text after `lede:` at the top) |
| The contact email address | `_config.yml` (the `email:` line) |

Click the file, then the pencil, and change the words, being careful not to delete the punctuation around them (quotes, dashes or colons).

---

## 7. Add a new person (or remove one)

**Please double check with Dann, Eunice or Alex before removing files or people.**

**Add someone:**
1. Open `_members`, then open any existing person's file.
2. Click the **copy icon** at the top right of the file contents (or select all the text and copy it).
3. Go back to `_members`, click **Add file → Create new file**, name it after the person like `first-last.md`, paste in the text and change the details. Set `group:` to `leads`, `postdocs` or `phds`.
4. Upload their photo with the matching name (see section 2).

**Remove someone:** open their file in `_members`, click the **⋯ menu → Delete file**, then commit. (They disappear from the Team page and the site, but their old photo file stays harmlessly in the images folder.)

---

## If something goes wrong

**It's very hard to break the site, and every change can be undone.**

- **My change isn't showing.** Wait 3 minutes and refresh with Shift held down. If it still isn't there, open the repository's **Actions** tab. A **red ✗** next to your change means the site couldn't be built. Most of the time that's a small typo in the top part of a file (a missing colon, a missing `---`, or indentation in the wrong place). Open your file again and compare it with the example above.
- **I made a mistake.** Open the file and click **History** (top right). Find the version you want and click **⋯ → Revert**. Or just ask a group lead.
- **My photo isn't showing.** Check that the photo's file name matches your profile file name **exactly**, including capital letters, and that it is in `assets/images/people`.
- **My publications are missing.** Check that your ORCID iD is correct and that your works are public. See section 3.

**Never edit these:** the `_site` folder, `_data/citations.yaml`, and anything in `_plugins`, `scripts` or `.github`.

**Stuck?** Ask a group lead. If you can, send them a link to the file you were editing.
