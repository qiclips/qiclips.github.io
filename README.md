# [clips.qilove.store](https://clips.qilove.store)

Clips from online sources. Qilove arranged them to store in this website.


## Workflow（Start from branch `main`）
> - branch `main`: New and edit Markdown files content branch.
> - branch `build`: Your Jekyll theme or others generator code branch.
> - branch `pages`: Generated original website results.

```mermaid
---
config:
  maxHeight: 100%
---
flowchart TD
    Main-1(New or Edit Markdown Files in <i>main</i>)-->Main-2[Commit and push]
    Main-2-->|Switch to branch <i>build</i>| Build-1(cherry-pick from <i>main</i>)
    Build-1 -->|Update Markdown Files| Build-2{Is new article?}
    Build-2 -->|Yes| Build-3[Modify markdown files to fit jekyll theme]
    Build-2 -->|Not| Build-4[Update the same markdown file]
    Build-3 --> Build-5
    Build-4 --> Build-5[Test: <br><i>bundle exec jekyll s -l</i> <br>to preview and check the changes]
    Build-5 --> Build-6{Is the preview correct?}
    Build-6 -->|Yes| Build-7[Commit and push]
    Build-6 -->|Not| Build-4
    Build-7 --> Build-8[Build: <br><i>bundle exec jekyll b</i> <br>to build the website]
    Build-8 --> |<i>cd _site</i> <br>go into branch <i>pages</i> in directory <i>_site</i>| Pages-1{check the changes, <br>is it correct ?}
    Pages-1 --> |Yes| Build-4
    Pages-1 --> |Yes| Pages-2[Commit and push]
    Pages-2 --> Pages-3[Check the changes on the <i>worklt.tech</i>]
    Pages-3 --> Pages-4{Is the view correct?}
    Pages-4 -->|Not| Build-4
    Pages-4 -->|Yes| N(Done)
```
