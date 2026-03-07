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
2. **Analyze Real GSC Data**:
   - **CRITICAL**: Do NOT just guess keywords. You MUST use the **Google Search Console MCP server tools** (such as `get_search_analytics`) to find real, high-performance SEO queries related to the document's topic.
   - Look for queries with high impressions or clicks that match the document's content.
3. **Generate Keywords**:
   - Select 5 to 10 highly relevant SEO keywords/keyphrases from the real GSC data.
   - Ensure the keywords match the language in which the document is written (e.g., Spanish keywords for an `es/page.md` file). If the GSC data doesn't have exact language matches, translate the best performing ones natively.
4. **Inject Frontmatter**:
   - Check if the document already has a YAML frontmatter block at the very top (enclosed in `---`).
   - If it exists, add or update the `keywords` array. 
   - If it does not exist, create a new YAML frontmatter block at the start of the file.
   - Example format:
     ```yaml
     ---
     keywords: [keyword1, keyword2, keyword3]
     ---
     ```
5. **Multilingual consistency**: ALWAYS check if the document has multiple language versions (e.g., in `es/`, `en/`, etc. subdirectories). You must repeat this process for **every language version** of the file, pulling appropriate GSC data for that language and saving them correctly.
6. **Report**: Inform the user about the keywords added for each language version based on the GSC metrics.

## Quality Criteria
- Keywords should accurately reflect the aviation/meteorology/technical domain context of the project.
- Do not remove existing frontmatter data (like `title` or `date`); safely append the keywords.