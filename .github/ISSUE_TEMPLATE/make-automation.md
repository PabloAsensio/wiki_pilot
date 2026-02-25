---
name: Make Automation
about: Ask Copilot to review content, add images, or fix errors
title: ''
labels: ''
assignees: ''

---

**Request Type:**
- [ ] Image Request 🖼️
- [ ] Error Report ⚠️
- [ ] Content Suggestion ✏️

**Topic URL:**
<!-- Paste the URL here -->

**Topic Code:**
<!-- e.g. [050-02-06] -->

**Description:**
<!-- Description of what needs to be done -->

---
### 🤖 Instructions for Copilot

**If this is an Image Request:**
Please use the script located at `wiki_image_search.py` to search for relevant images.
1. Run the script: `python wiki_image_search.py "search query"`
2. If suitable images are found, add them to the content markdown file.
3. Ensure the images are properly credited if required.

**If this is an Error Report or Content Suggestion:**
1. Analyze the reported error or suggestion.
2. If you are confident it is a factual error, propose a fix.
3. **CRITICAL:** If there is any doubt about the technical accuracy of the content, or if it requires subject matter expertise, pleaes mention @PabloAsensio for review.

**General:**
- Check the directory for the relevant markdown file based on the Topic Code.
- Make changes directly to the `.md` file.
- Make sure all languages are modified properly as well.
