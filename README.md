# LLMs for E-Commerce Content Generation — Data Analysis

**Western Sydney University | Master of ICT | INFO7016 Postgraduate Project A | 2024**
**Result: High Distinction (88/100)**

---

## Overview

This repository contains the Python data analysis for my Masters research project investigating the impact of Large Language Models (LLMs) on digital content creation in e-commerce. The study conducted a sequential A/B test on a live Shopify platform, comparing AI-generated content (ChatGPT/GPT-4) against human-generated content across a two-week period.

**Research Question:** Does AI-generated content outperform human-generated content on key e-commerce engagement and conversion metrics?

---

## Study Design

| Parameter | Detail |
|---|---|
| Platform | Shopify E-Commerce Store |
| Method | Sequential A/B Testing |
| Week 1 | AI-generated content (ChatGPT/GPT-4) |
| Week 2 | Human-generated content |
| Participants | n=30 (Week 1), n=22 (Week 2) |
| Data Sources | Google Analytics (quantitative) + Google Forms surveys (qualitative) |
| Chatbot | GPT-4 powered chatbot integrated for real-time feedback |

---

## Key Findings

### Quantitative — Google Analytics

| Metric | AI Content | Human Content | Difference |
|---|---|---|---|
| Page Views | 209 | 79 | AI +165% |
| Active Users | 48 | 32 | AI +50% |
| Avg Time on Page | 1m 11s | 39s | AI +82% |
| Bounce Rate | 40% | 43% | AI lower |
| CTR | Higher | Lower | AI better |

### Qualitative — Survey Results (n=30 / n=22)

| Category | AI Content | Human Content |
|---|---|---|
| Trustworthiness (rated 5/5) | 43.3% | 40.0% |
| Satisfaction (rated 5/5) | 43.3% | 43.3% |
| Definite Purchase Intent | 16.7% | 33.3% |
| Correctly identified content type | 36.7% | 63.3% |

### Statistical Summary

```
AI Content    — Engagement Mean: 3.67  Median: 4.0  Std: 1.01  n=30
Human Content — Engagement Mean: 3.73  Median: 4.0  Std: 1.09  n=22
Cohen's d: -0.058 (small effect — comparable satisfaction between content types)
```

---

## Conclusion

- **AI content excels at initial engagement** — 165% more page views, 82% longer time on page
- **Human content wins on trust and conversion** — 2x higher definite purchase intent
- **Optimal strategy:** Hybrid approach combining AI efficiency with human authenticity
- 63.3% of users correctly identified human-written content, suggesting distinct stylistic differences

---

## Hypothesis Testing Summary

| Hypothesis | Result |
|---|---|
| H1: AI drives higher engagement metrics | ✅ Supported |
| H2: Distinct interaction patterns for each content type | ✅ Supported |
| H3: AI achieves higher CTR | ⚠️ Partially Supported (higher CTR, zero conversions) |
| H4: Human content perceived as more trustworthy | ✅ Supported |
| H5: AI content increases bounce rate | ❌ Not Supported (AI bounce lower) |
| H7: Favourable feedback on AI content | ✅ Supported |
| H8: Human content drives more conversions | ✅ Supported |
| H9: Users can distinguish AI vs human content | ✅ Supported |

---

## Repository Contents

```
llm-ecommerce-analysis/
├── llm_ecommerce_analysis.py      # Full Python analysis (pandas, numpy, matplotlib)
├── llm_analysis_visualisation.png # 6-panel data visualisation
└── README.md                      # This file
```

---

## Tech Stack

```
Python 3.x
├── pandas      — Data manipulation and A/B test metric analysis
├── numpy       — Statistical calculations (mean, std, Cohen's d)
└── matplotlib  — 6-panel data visualisation
```

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/unicebondoc/llm-ecommerce-analysis.git
cd llm-ecommerce-analysis

# Install dependencies
pip install pandas numpy matplotlib

# Run the analysis
python llm_ecommerce_analysis.py
```

---

## Research Context

This project was completed as part of the Master of ICT (Web and Mobile Computing) at Western Sydney University, supervised by Dr. Jason Lee (School of Computer, Data and Mathematical Sciences).

The full study included:

- Literature review covering AI-generated content in e-commerce (EcomGPT, LLaMA-E, ChatGPT)
- Ethical framework addressing transparency, bias, and data privacy
- Mixed-methods analysis combining Google Analytics quantitative data with thematic analysis of qualitative survey responses
- Practical recommendations for SME businesses integrating AI into content strategies

---

## Author

**Unice Bondoc**
AI Engineer | Master of ICT Graduate | Western Sydney University

[unicebondoc.com](https://unicebondoc.com) · [LinkedIn](https://linkedin.com/in/unicebondoc) · [GitHub](https://github.com/unicebondoc)
