---
# marp: true enables Marp features.
marp: true
# theme: custom specifies the custom theme defined below.
theme: custom
# paginate: true automatically adds page numbers to each slide.
paginate: true
# A global footer is a better practice than adding one to each slide manually.
footer: 'Contact: 21f3000750@ds.study.iitm.ac.in'
---

<!--
This block defines a custom theme for the presentation.
The styles here will apply to all slides unless overridden by local directives.
-->
<style>
/* @import 'default'; is used to build upon Marp's default theme. */
@import 'default';

/* Base styling for every slide (section). */
section {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  color: #333;
  background-color: #f9f9f9;
  padding: 60px;
}

/* Styling for headings. */
h1, h2, h3 {
  color: #1a237e; /* A deep blue for strong headings. */
}

/* This custom class adds a dark overlay to a slide. 
  It's useful for making text readable over a background image.
*/
section.dark-overlay {
  position: relative;
  color: white;
  text-shadow: 0 0 10px rgba(0,0,0,0.7);
}

/* The ::before pseudo-element creates the actual dark layer. */
section.dark-overlay::before {
  content: "";
  position: absolute;
  inset: 0; /* Covers the entire slide. */
  background: rgba(0,0,0,0.5);
  z-index: 0;
}

/* Ensures the slide's content appears above the dark overlay. */
section.dark-overlay > * {
  position: relative;
  z-index: 1;
}

/* A custom style for creating an 'info' blockquote. */
blockquote.info {
  background: #e8f0fe;
  border-left: 6px solid #1a237e;
  padding: 1em 1.5em;
  color: #1a237e;
  border-radius: 4px;
}
</style>

<!-- Slide 1: Title Slide -->
# **QuantumLeap API**
### Product Documentation

**Technical Writer:** Gemini  
**Version:** 1.0

---

<!-- Slide 2: Features Slide with Background Image -->
<!-- 
  Local directives starting with an underscore apply styles to a specific slide.
  Here we set a background image, make it cover the slide, and apply our dark overlay.
-->
<!--
_backgroundImage: "url('https://placehold.co/1600x900/000000/FFFFFF?text=API+Features')"
_backgroundSize: cover
_backgroundPosition: center
_class: dark-overlay
-->

# Core Capabilities

- **Maintainable:** Write docs in plain Markdown.
- **Version Controlled:** Track changes easily with Git.
- **Multi-Format Export:** Generate PDF, PPTX, and HTML effortlessly.
- **Highly Customizable:** Full control over styling with CSS.

---

<!-- Slide 3: Technical Details Slide -->
# Algorithmic Performance

Our data caching mechanism uses a Least Recently Used (LRU) eviction policy. The time complexity for the primary operations is:

- **Get (Retrieval):** $$O(1)$$
- **Set (Insertion/Update):** $$O(1)$$

This ensures high-speed access to frequently used data.

---

<!-- Slide 4: Custom Styling Example Slide -->
# Custom Styling in Action

<blockquote class="info">
  This is an example of an **info block**. It's perfect for highlighting important notes, warnings, or tips within your documentation.
</blockquote>

---

<!-- Slide 5: Closing Slide -->
# Thank You

For questions or support, please reach o
