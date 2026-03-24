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
1. **Iterative Process (Topic by Topic)**: When asked to add images to multiple topics or a whole module, you MUST work iteratively. Focus on **one specific topic at a time**.
2. For the current topic, identify the search keyword or query based on its content. **Important: Always translate the search term to English first** before searching (even if the user asks in Spanish), as Wikimedia Commons has much broader image coverage for English terms.
3. Run the search script located in the workspace root:
   ```bash
   python wiki_image_search.py "<query>"
   ```
   *Optional: Append `--limit <N>` to specify the maximum number of results (default is 5).*
4. Wait for the script execution and capture its output.
5. **Fallback mechanism**: If no images are found using the initial English term, try alternative English synonyms, or as a last resort, try the original Spanish term.
6. **Insertion**: Once you have the results, immediately embed the returned direct URLs as images in the markdown format (`![<title>](<url>)`) in the most coherent place within the current topic's file.
7. **Multilingual consistency**: ALWAYS check if the document has multiple language versions (e.g., in `es/`, `en/`, etc. subdirectories). You must inject the imágenes into **every language version** of the file so that no language is left out. Make sure the context where it is inserted is exactly the same across languages.
8. **Advance**: Only after successfully inserting the images for the current topic across all its language versions, proceed to step 1 for the **next topic** in the list.

## Quality Criteria
- Make sure the query is specific enough to find relevant images.
- Ensure you wrap the search query in quotes to avoid syntax errors if it contains spaces.
- If no images are found, try simplifying or modifying the search terms.