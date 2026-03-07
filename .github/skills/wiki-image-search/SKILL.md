---
name: wiki-image-search
description: 'Search for images on Wikimedia Commons using the workspace script. Use this skill when you need to find relevant images or diagrams for a topic or when asked to search for images.'
---

# Wiki Image Search

## When to Use
- You need to find images, photos, or diagrams on Wikimedia Commons for a specific topic, concept, or theory.
- The user requests to add visualizations or pictures to a document.
- You need direct URLs to images about a specific subject.

## Procedure
1. Identify the search keyword or query based on the user's request.
2. Run the search script located in the workspace root:
   ```bash
   python wiki_image_search.py "<query>"
   ```
   *Optional: Append `--limit <N>` to specify the maximum number of results (default is 5).*
3. Wait for the script execution and capture its output, which will be a JSON array containing objects with `title` and `url`.
4. Use the returned direct URLs to embed the images in markdown format (`![<title>](<url>)`) or provide them directly to the user as appropriate to fulfill their request.

## Quality Criteria
- Make sure the query is specific enough to find relevant images.
- Ensure you wrap the search query in quotes to avoid syntax errors if it contains spaces.
- If no images are found, try simplifying or modifying the search terms.