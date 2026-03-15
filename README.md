# LLMs for E-Commerce Content Generation

**WSU Masters Research Project** | School of Computer Science, Western Sydney University

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![Research](https://img.shields.io/badge/Grade-HD%2088%2F100-brightgreen)](.)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

---

## Overview

This repository contains the data analysis and research artefacts for a Masters-level study examining the effectiveness of **Large Language Model (LLM)-generated content versus human-authored content** in e-commerce product listings, conducted on the Shopify platform.

The study employed a controlled A/B testing methodology, measuring how AI- and human-generated content influences key consumer engagement and purchase behaviour metrics.

---

## Research Summary

| Attribute | Detail |
|---|---|
| **Study Type** | Controlled A/B Experiment |
| **Platform** | Shopify |
| **Participants** | 30 |
| **Content Conditions** | AI-generated (LLM) vs. Human-authored |
| **Grade Achieved** | High Distinction — 88 / 100 |

---

## Key Findings

| Metric | AI-Generated | Human-Authored | Outcome |
|---|---|---|---|
| **Page Views** | +165% higher | Baseline | AI content drove significantly more traffic |
| **Purchase Intent** | Baseline | 2× higher | Human content drove stronger purchase intent |

### Interpretation

The findings reveal a nuanced trade-off between AI and human content in e-commerce contexts:

- **AI-generated content** excels at discoverability — likely due to SEO-optimised language, keyword density, and structured formatting — producing substantially more page views.
- **Human-authored content** builds greater purchase intent, suggesting that authentic, emotionally resonant writing is more persuasive at the conversion stage of the customer journey.

These results imply that a **hybrid content strategy** — using LLMs for top-of-funnel discoverability and human writers for conversion-focused copy — may yield optimal outcomes for e-commerce merchants.

---

## Repository Structure

```
llm-ecommerce-analysis/
├── README.md              # Project overview and findings
├── .gitignore             # Python gitignore
└── analysis.py            # Data analysis script
```

---

## Methods

1. **Participant Recruitment** — 30 participants recruited for the study.
2. **A/B Content Creation** — Product listings written by both a human copywriter and an LLM (e.g., GPT-4 / Claude), matched for product category and length.
3. **Platform Deployment** — Listings deployed on Shopify with randomised variant assignment.
4. **Metric Collection** — Page view analytics and purchase intent measured via post-exposure survey and platform analytics.
5. **Statistical Analysis** — Python-based analysis (see `analysis.py`) used to compare conditions.

---

## Getting Started

### Prerequisites

```bash
python >= 3.10
pip install -r requirements.txt  # if applicable
```

### Running the Analysis

```bash
python analysis.py
```

---

## Citation

If you reference this work, please cite:

```
Bondoc, U. (2025). LLMs for E-Commerce Content Generation: An A/B Testing Study
of AI vs. Human Content on Shopify. Masters Research Project, Western Sydney University.
```

---

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

*Western Sydney University · Masters of Computer Science · 2025*
