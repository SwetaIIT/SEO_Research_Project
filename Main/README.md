## Overview
This project is a structured SEO research system that collects, organizes, and analyzes content from leading SEO practitioners across YouTube, blogs, and LinkedIn

## Research Sources
All selected experts are documented in `expert.md`, which includes 10 SEO practitioners from YouTube, Linkedin, and industry platforms. Each expert was chosen based on real-world SEO practice, case studies, and active content creation.

## Project Structure

## Architecture Diagram
flowchart

flowchart TD

A[Main Repository]

A --> B[README.md]
A --> C[experts.md]

R[Research Repository]

R --> C1[code/]
C1 --> C2[youtube.py]
C1 --> C3[blog.py]
C1 --> C4[linkedin.py]

R --> T[youtube-transcripts (3 files)]
R --> L[linkedin-posts (3 files)]
R --> O[other (4 files)]


## Data Collection Methods

### 1. YouTube Transcripts
- Extracted using Supadata API
- Focus: SEO tutorials, case studies, and strategy breakdowns
- Output: Structured transcript files for analysis

### 2. Other Content
- Collected using RSS feeds and HTML parsing
- Tools: Python (requests + BeautifulSoup + feedparser)
- Focus: Long-form SEO insights and experiments

### 3. LinkedIn Content
- Collected manually due to API limitations
- Attempts were made using Python tools and Bardeen automation, but extraction was limited due to platform restrictions
- Final dataset includes curated posts from selected SEO practitioners

## Tech Stack
- Python
- Supadata API (YouTube transcript extraction)
- RSS Feed Parsing (blog ingestion)
- BeautifulSoup (HTML parsing)
- Claude Code (AI-assisted coding)
- OpenAI Codex (AI coding assistant for workflow automation)
- GitHub (project hosting)



