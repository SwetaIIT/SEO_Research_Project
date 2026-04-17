## Overview
This project is a structured SEO research system that collects, organizes, and analyzes content from leading SEO practitioners across YouTube, blogs, and LinkedIn

## Research Sources
All selected experts are documented in `expert.md`, which includes 10 SEO practitioners from YouTube, Linkedin, and industry platforms. Each expert was chosen based on real-world SEO practice, case studies, and active content creation.

## Project Structure
Main/
│
├── research/
│   │
│   ├── code/
│   │     ├── youtube.py
│   │     ├── blog.py
│   │     ├── linkedin.py
│   │
│   ├── youtube-transcripts/
│   │     ├── video1.txt
│   │     ├── video2.txt
│   │
│   ├── blogs/
│   │     ├── blog1.txt
│   │     ├── blog2.txt
│   │
│   ├── linkedin-posts/
│   │     ├── expert1.txt
│   │     ├── expert2.txt
│   │
│   ├── other/
│   │
│   ├── expert.md
│
├── README.md

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



