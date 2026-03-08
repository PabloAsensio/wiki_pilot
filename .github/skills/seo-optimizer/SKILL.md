---
name: seo-optimizer
description: 'Analyze a markdown article, extract key concepts, and inject or optimize SEO keywords in the YAML frontmatter. Use this skill when the user wants to improve the SEO or tagging of a page.'
---

# SEO Optimizer

## When to Use
- The user requests to improve SEO, add keywords, or optimize the tags for a specific document or lesson.
- You need to generate relevant metadata so search engines or site searches index the article correctly.

## Procedure
1. **Manual File-by-File Analysis**: This procedure CANNOT be automated via bulk scripts. You must process articles one by one. Check the exact title of the lesson in `translations.json` to ensure consistency.
2. **Read the Document**: Open and analyze the target markdown file (`.md`) provided by the user to understand its main subject and concepts.
3. **Analyze Real GSC Data (Low-Hanging Fruits)**:
   - **CRITICAL**: Do NOT just guess keywords. You MUST use the **Google Search Console MCP server tools** (such as `get_search_analytics` or `get_advanced_search_analytics`) to find real, high-performance SEO queries related to the document's topic.
   - Look specifically for queries ranking in positions 11-20 (page 2 of Google) with high impressions to push them to the first page.
   - Match the queries to the actual content intent.
4. **Generate & Optimize Frontmatter (CTR Improvement)**:
   - **Keywords**: Select 5 to 10 highly relevant SEO keywords/keyphrases from the real GSC data, matching the language of the file.
   - **Title**: Update the `title` in the YAML frontmatter. It should be exact to `translations.json` but can be subtly enhanced if needed, addressing the user's search intent (e.g. including target audience like "ATPL", "EASA").
   - **Description**: Add or update the YAML `description` to act as a compelling hook that summarizes the content and includes primary keywords.
   - Inject or update the YAML block (enclosed in `---`) at the very top of the file.
5. **Override Default H1 Title**:
   - The platform ignores default markdown H1 titles unless explicitly defined. Immediately after the YAML frontmatter, add an explicit `# [Title from translations.json]` that matches the exact title.
6. **Optimize Content for Position Zero & Engagement**:
   - **Featured Snippets**: Add or modify `## Q&A style` headings (e.g., `## What is [Topic]?` / `## ¿Qué es [Tema]?`) followed by a direct 2-3 line direct answer that you write by comprehending the text.
   - **Image Alt Texts**: Ensure all `![alt text]` for images contain descriptive keywords.
   - **Internal Linking**: Insert relevant internal links to other lessons in the syllabus using relative paths.
7. **Multilingual consistency**: ALWAYS check if the document has multiple language versions (e.g., in `es/`, `en/`). Repeat this process manually for every language version.
8. **Report**: Inform the user about the changes made.

## Quality Criteria
- Keywords must be data-driven via GSC, not blindly assumed.
- The tone should match the aviation/meteorology/technical domain context of the project.
- Do not remove existing frontmatter data; safely update or append elements like `title`, `description`, and `keywords`.