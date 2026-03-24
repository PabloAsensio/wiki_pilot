---
name: article-summarizer
description: Generates bilingual Markdown summaries (en/page.md and es/page.md) from provided source text files.
---

# Article Summarizer Skill

This skill is designed to process source text files (typically `.txt` containing question banks or notes) and generate structured Markdown summaries in English and Spanish.

## Workflow
When a source file (e.g., `topic.txt`) is provided or read:
1.  **Analyze** the content to identify key concepts, definitions, and rules.
2.  **Generate** two separate files for the topic:
    *   `[path]/en/page.md` (English)
    *   `[path]/es/page.md` (Spanish)

## Content Guidelines
*   **Completeness**: Do not omit any concept mentioned in the source file. Every topic, definition, and rule must be integrated.
*   **Format**: Use clear Markdown.
    *   Start with a YAML frontmatter block.
    *   Do not follow with an H1 (`# Title`) header, starting directly with the content.
    *   Use H2 (`##`) and H3 (`###`) for subsections.
    *   Highlight key concepts in **bold**.
*   **Tone**: Educational, clear, and concise. Intended for aviation students (ATPL level).

## YAML Frontmatter
Every generated file must start with the following frontmatter:
```yaml
---
title: "Short Title"
description: "Brief summary of the content (1-2 sentences)."
keywords: ["keyword1", "keyword2", "keyword3"]
---
```

## Structure Example
```markdown
---
title: "Basic Principles"
description: "Overview of gyroscopic principles."
keywords: ["gyroscopic", "principles", "aviation"]
---

Brief introductory paragraph.

## Section 1
Details...

### Subsection
More details...

## Section 2
More details...
```

## Translation
*   Ensure the Spanish version (`es/page.md`) is a high-quality technical translation of the English version, using appropriate aviation terminology.
