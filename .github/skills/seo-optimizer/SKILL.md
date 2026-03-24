---
name: seo-optimizer
description: 'Analyze a markdown article, extract key concepts, and inject or optimize SEO keywords in the YAML frontmatter. Use this skill when the user wants to improve the SEO or tagging of a page.'
---

# SEO Optimizer

## When to Use
- The user requests to improve SEO, add keywords, or optimize the tags for a specific document or lesson.
- You need to generate relevant metadata so search engines or site searches index the article correctly.

## Procedure
1. **Manual File-by-File Analysis**: This procedure CANNOT be automated via bulk scripts. You must process articles one by one.
2. **Read the Document & Theory Context**: Open and analyze the target markdown file (`.md`). You MUST ALSO locate and read the corresponding `.txt` theory file for that specific topic. Any theoretical information you add must be strictly based on this `.txt` file to ensure the info is correct.
3. **Analyze Real GSC Data (Low-Hanging Fruits)**:
   - **CRITICAL**: Do NOT just guess keywords. You MUST use the **Google Search Console MCP server tools** (such as `get_search_analytics` or `get_advanced_search_analytics`) to find real, high-performance SEO queries related to the document's topic.
   - Look specifically for queries ranking in positions 11-20 (page 2 of Google) with high impressions to push them to the first page.
   - Match the queries to the actual content intent.
4. **Optimize Titles and `translations.json`**:
   - Create an SEO-optimized title that clearly explains the lesson scope and captures the search intent (e.g. including target audience like "ATPL", "EASA").
   - For syllabus-style content, prioritize descriptive academic wording over question-style headlines.
   - If the existing title is too generic (e.g. "General"), expand it with the section context (e.g. "Generalidades del Despegue").
   - **CRITICAL:** Update the global `translations.json` file in the root directory to replace the old title with your new SEO-optimized title for that specific topic ID (e.g., "050-01-01") and language.
5. **Generate & Optimize Frontmatter (CTR Improvement)**:
   - **Keywords**: Select 5 to 10 highly relevant SEO keywords/keyphrases from the real GSC data, matching the language of the file.
   - **Title**: Update the `title` in the YAML frontmatter to exactly match the new title you just set in `translations.json`. (Do NOT add an explicit `# H1` overwriting the title in the markdown body, it is no longer needed).
   - **Description**: Add or update the YAML `description` to act as a compelling hook that summarizes the content and includes primary keywords.
   - Inject or update the YAML block (enclosed in `---`) at the very top of the file.
6. **Optimize Content for Position Zero & Engagement**:
   - **Clean Opening Structure**: If the first section heading is a generic opener (e.g., `## Introducción`, `## Introduction`, `## Resumen`, `## Summary`, `## Definición`, `## Definition`, `## Contexto`) and it only repeats a generic opening after the title/frontmatter, remove that heading and keep a clean start like the best-formatted lessons.
   - **Opening Paragraph Completeness**: If the lesson is missing the first introductory paragraph after the title/frontmatter, add a concise opening paragraph (2-4 lines) based strictly on the corresponding section `.txt` theory file.
   - **Featured Snippets**: Add `## Q&A style` headings (e.g., `## What is [Topic]?` / `## ¿Qué es [Tema]?`) followed by a direct 2-3 line answer. **The information in this answer MUST be extracted solely from the lesson's `.txt` theory file.**
   - **Image Alt Texts**: Ensure all `![alt text]` for images contain descriptive keywords.
   - **Internal Linking**: Insert relevant internal links to other lessons in the syllabus using relative paths.
7. **Multilingual consistency**: ALWAYS check if the document has multiple language versions (e.g., in `es/`, `en/`). Repeat this process manually for every language version.
8. **Report**: Inform the user about the changes made to both the markdown files and `translations.json`.

## Quality Criteria
- Keywords must be data-driven via GSC, not blindly assumed.
- The tone should match the aviation/meteorology/technical domain context of the project.
- For syllabus pages, titles must be explicit and contextual, avoiding overly question-like phrasing.
- The article opening must be clean: avoid redundant generic first headings (e.g., Introducción, Resumen, Definición, Contexto) when they add no structural value.
- The article opening must be complete: include a clear first paragraph when missing, sourced only from the lesson `.txt` theory.
- Do not remove existing frontmatter data; safely update or append elements like `title`, `description`, and `keywords`.