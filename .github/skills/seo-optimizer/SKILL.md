---
name: seo-optimizer
description: 'Analyze a markdown article, extract key concepts, and inject or optimize SEO keywords in the YAML frontmatter. Use this skill when the user wants to improve the SEO or tagging of a page.'
---

# SEO Optimizer

## When to Use
- The user requests to improve SEO, add keywords, or optimize the tags for a specific document or lesson.
- You need to generate relevant metadata so search engines or site searches index the article correctly.

## Procedure
1. **Read the Document**: Open and analyze the target markdown file (`.md`) provided by the user to understand its main subject and concepts.
2. **Analyze Real GSC Data (Low-Hanging Fruits)**:
   - **CRITICAL**: Do NOT just guess keywords. You MUST use the **Google Search Console MCP server tools** (such as `get_search_analytics` or `get_advanced_search_analytics`) to find real, high-performance SEO queries related to the document's topic.
   - Look specifically for queries ranking in positions 11-20 (page 2 of Google) with high impressions to push them to the first page.
   - Match the queries to the actual content intent.
3. **Generate & Optimize Frontmatter (CTR Improvement)**:
   - **Keywords**: Select 5 to 10 highly relevant SEO keywords/keyphrases from the real GSC data, matching the language of the file.
   - **Title**: Write a catchy SEO-optimized title. Update the `title` in the YAML frontmatter to make it more "clickable", addressing the user's search intent (e.g. including target audience like "ATPL", "EASA").
   - **Description**: Add or update the YAML `description` to act as a compelling hook that summarizes the content and includes primary keywords.
   - Inject or update the YAML block (enclosed in `---`) at the very top of the file.
4. **Override Default H1 Title**:
   - The platform ignores default markdown H1 titles unless explicitly defined. Immediately after the YAML frontmatter, add an explicit `# [SEO Optimized Title]` that matches or closely relates to the frontmatter title.
5. **Optimize Content for Position Zero & Engagement**:
   - **Featured Snippets**: Add or modify `## Q&A style` headings (e.g., `## What is...?` / `## ¿Qué es...?`) followed by a direct 2-3 line direct answer. Use Markdown tables where applicable.
   - **Image Alt Texts**: Ensure all `![alt text]` for images contain descriptive keywords relevant to the query.
   - **Internal Linking**: Insert relevant internal links to other lessons in the syllabus using relative paths.
6. **Multilingual consistency**: ALWAYS check if the document has multiple language versions (e.g., in `es/`, `en/`). You must repeat this process for **every language version**, pulling appropriate GSC data for that language and applying the full optimization.
7. **Report**: Inform the user about the changes made (frontmatter, H1 heading, alt texts) and the GSC metrics that justified them.

## Quality Criteria
- Keywords must be data-driven via GSC, not blindly assumed.
- The tone should match the aviation/meteorology/technical domain context of the project.
- Do not remove existing frontmatter data; safely update or append elements like `title`, `description`, and `keywords`.