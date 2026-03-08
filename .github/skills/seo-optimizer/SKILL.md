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
   - Create a catchy SEO-optimized title capturing the search intent (e.g. including target audience like "ATPL", "EASA").
   - **CRITICAL:** Update the global `translations.json` file in the root directory to replace the old title with your new SEO-optimized title for that specific topic ID (e.g., "050-01-01") and language.
5. **Generate & Optimize Frontmatter (CTR Improvement)**:
   - **Keywords**: Select 5 to 10 highly relevant SEO keywords/keyphrases from the real GSC data, matching the language of the file.
   - **Title**: Update the `title` in the YAML frontmatter to exactly match the new title you just set in `translations.json`. (Do NOT add an explicit `# H1` overwriting the title in the markdown body, it is no longer needed).
   - **Description**: Add or update the YAML `description` to act as a compelling hook that summarizes the content and includes primary keywords.
   - Inject or update the YAML block (enclosed in `---`) at the very top of the file.
6. **Optimize Content for Position Zero & Engagement**:
   - **Featured Snippets**: Add `## Q&A style` headings (e.g., `## What is [Topic]?` / `## ¿Qué es [Tema]?`) followed by a direct 2-3 line answer. **The information in this answer MUST be extracted solely from the lesson's `.txt` theory file.**
   - **Image Alt Texts**: Ensure all `![alt text]` for images contain descriptive keywords.
   - **Internal Linking**: Insert relevant internal links to other lessons in the syllabus using relative paths.
7. **Multilingual consistency**: ALWAYS check if the document has multiple language versions (e.g., in `es/`, `en/`). Repeat this process manually for every language version.
8. **Report**: Inform the user about the changes made to both the markdown files and `translations.json`.

## Quality Criteria
- Keywords must be data-driven via GSC, not blindly assumed.
- The tone should match the aviation/meteorology/technical domain context of the project.
- Do not remove existing frontmatter data; safely update or append elements like `title`, `description`, and `keywords`.