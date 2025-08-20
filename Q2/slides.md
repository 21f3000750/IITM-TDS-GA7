---
marp: true
theme: custom
paginate: true
header: 'NexusCorp - Product Documentation'
footer: 'Contact: 21f3000750@ds.study.iitm.ac.in'
--
<!--
This is a theme directive block. It allows you to define a custom theme using CSS.
We are creating a theme named 'custom-theme' as specified in the front matter.
This is where you can define the base styling for all your slides.
-->

<!-- theme: custom-theme -->

<style>
/* This is a special @theme import that imports the default Marp theme styles. */
@import 'default';

/* This section defines the base style for all slides. */
section {
background-color: #f0f4f8;
color: #1a202c;
font-family: 'Helvetica', 'Arial', sans-serif;
padding: 60px;
}

/* Styling for the main heading (h1) on the slides. */
h1 {
color: #2c5282;
text-align: center;
}

/* Styling for the secondary heading (h2) on the slides. */
h2 {
color: #2a69ac;
border-bottom: 2px solid #718096;
padding-bottom: 10px;
}

/* Custom style class 'lead' for creating impactful text. */
.lead {
text-align: center;
font-size: 1.5em;
color: #2d3748;
}

/* Custom style class 'highlight' for a slide with a different background. */
.highlight {
background-color: #e2e8f0;
}
</style>

<!-- This is the title slide. -->

Project Phoenix
Next-Generation Data Analytics Platform
<br>
Technical Documentation

<!-- This slide has a background image. -->

<!-- The backgroundImage directive sets the image URL. -->

<!-- 'blur(5px)' is a CSS filter applied to the image. -->

<!-- backgroundSize: cover ensures the image covers the whole slide. -->

<!-- backgroundColor is a fallback color if the image fails to load. -->

<h1 style="color: #fff; text-shadow: 2px 2px 4px #000;">System Architecture</h1>

<!-- This slide uses a custom class defined in our theme. -->

<!-- The _class directive applies the 'highlight' class to this specific slide. -->

<!-- This is an example of a local directive. -->

<!-- _class: highlight -->

Core Features
Real-time Data Processing: Ingest and analyze data streams with sub-second latency.

Scalable Infrastructure: Built on a microservices architecture for horizontal scaling.

Advanced Analytics: Leverage machine learning models for predictive insights.

Secure & Compliant: End-to-end encryption and GDPR-ready.

Algorithmic Complexity
Understanding the performance of our core algorithms is crucial for optimization. The primary sorting algorithm we use has a time complexity of:

O(n \log n) $$This ensures efficient processing even with large datasets. The search functionality utilizes a hash map, providing an average time complexity of: $$O(1)
<!-- This slide uses another custom class for a different layout/style. -->

<!-- _class: lead -->

Questions?
Feel free to reach out for more details.
