---
name: article-summarizer
description: Generates a clear and concise Markdown article summarizing multiple provided articles on the same topic.
---

# Article Summarizer

You will be given a series of articles, all on the same topic. Your goal is to write a clear and concise article in Markdown using all the concepts provided. 

The article is intended for readers who may not be familiar with the subject, so it should be simple. 

Guidelines:
- CRITICAL: The ONLY source of information you must use is the provided .txt file(s). You MUST NOT use external knowledge, hallucinate, or add any information that is not explicitly present in the provided text files.
- CRITICAL: Do not omit or forget any concept mentioned in the source files. Every single topic, definition, and rule from the provided text must be integrated into the article.
- Do NOT include an H1 (#) title at the beginning of the document (it is set by default by the parent folder).
- Always start the document with a brief, engaging introductory paragraph about the topic before introducing the first H2 (##) header. This avoids having an H1 immediately followed by an H2.
- First generate the English version. The English version is the master version (the "source of truth").
- For all other available languages, generate a faithful translation of the English version to ensure they are identical in structure, concepts, and formatting.
- Ensure that technical terms are translated accurately into the accepted aviation/industry terminology for each language. Apply common sense to maintain coherence, clarity, and a professional tone (avoiding stiff or unnaturally literal phrasing), while perfectly mirroring the English structure.
- Highlight key concepts in bold.
- You may or may not use the images that can be attached to the content.
- Write the final output in a clear Markdown format.
