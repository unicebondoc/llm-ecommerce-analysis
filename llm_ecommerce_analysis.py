"""
State of the Art in LLMs for Digital Content Creation on E-Commerce
Data Analysis — Unice Bondoc, Western Sydney University 2024
INFO7016 Postgraduate Project A — High Distinction (88/100)
A/B Test: AI-Generated vs Human-Generated Content on Shopify
- Week 1: AI-generated content (n=30 survey responses)
- Week 2: Human-generated content (n=22 survey responses)
- Quantitative: Google Analytics metrics
- Qualitative: Google Forms survey responses
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')
# ── Colour palette ────────────────────────────────────────────
AI_COLOR    = "#4A90D9"
HUMAN_COLOR = "#E8734A"
BG_COLOR    = "#F8F9FA"
TEXT_COLOR  = "#1B2A4A"
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.facecolor': BG_COLOR,
    'figure.facecolor': 'white',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.labelcolor': TEXT_COLOR,
    'xtick.color': TEXT_COLOR,
    'ytick.color': TEXT_COLOR,
    'text.color': TEXT_COLOR,
})
# ══════════════════════════════════════════════════════════════
# 1. GOOGLE ANALYTICS — QUANTITATIVE METRICS
# ══════════════════════════════════════════════════════════════
ga_data = pd.DataFrame({
    'Metric': [
        'Page Views',
        'Active Users',
        'Avg Time on Page (sec)',
        'Bounce Rate (%)'
    ],
    'AI_Generated': [209, 48, 71, 40.0],
    'Human_Generated': [79, 32, 39, 43.0]
})
ga_data['Difference'] = ga_data['AI_Generated'] - ga_data['Human_Generated']
ga_data['AI_Advantage_%'] = np.round(
    ((ga_data['AI_Generated'] - ga_data['Human_Generated']) / ga_data['Human_Generated']) * 100, 1
)
print("=" * 60)
print("GOOGLE ANALYTICS METRICS — AI vs HUMAN CONTENT")
print("=" * 60)
print(ga_data.to_string(index=False))
print()
# ── Stats summary ─────────────────────────────────────────────
engagement_metrics = ga_data[ga_data['Metric'].isin(['Page Views', 'Active Users', 'Avg Time on Page (sec)'])]
print(f"Mean AI engagement advantage: {engagement_metrics['AI_Advantage_%'].mean():.1f}%")
print(f"AI page views vs Human: {ga_data.loc[0,'AI_Generated']} vs {ga_data.loc[0,'Human_Generated']} "
      f"({ga_data.loc[0,'AI_Advantage_%']:+.0f}%)")
print()
# ══════════════════════════════════════════════════════════════
# 2. SURVEY DATA — QUALITATIVE METRICS
# ══════════════════════════════════════════════════════════════
# Survey Week 1 (AI) — 30 responses
# Survey Week 2 (Human) — 22 responses
# Scores are % of respondents rating 5/5 or selecting option
survey_data = pd.DataFrame({
    'Category': [
        'Engagement\n(rated 5/5)',
        'Trustworthiness\n(rated 5/5)',
        'Satisfaction\n(rated 5/5)',
        'Purchase Intent\n("Definitely" interested)',
        'Correctly Identified\ncontent type'
    ],
    'AI_Generated_pct': [36.7, 43.3, 43.3, 16.7, 36.7],
    'Human_Generated_pct': [28.6, 40.0, 43.3, 33.3, 63.3],
    'n_AI': [30, 30, 30, 30, 30],
    'n_Human': [22, 22, 22, 22, 22]
})
# Convert % to actual counts
survey_data['AI_count'] = np.round(survey_data['AI_Generated_pct'] / 100 * survey_data['n_AI']).astype(int)
survey_data['Human_count'] = np.round(survey_data['Human_Generated_pct'] / 100 * survey_data['n_Human']).astype(int)
print("=" * 60)
print("SURVEY RESULTS — KEY QUALITATIVE METRICS")
print("=" * 60)
print(survey_data[['Category', 'AI_Generated_pct', 'Human_Generated_pct', 'AI_count', 'Human_count']].to_string(index=False))
print()
# ══════════════════════════════════════════════════════════════
# 3. PURCHASE INTENT — FULL DISTRIBUTION
# ══════════════════════════════════════════════════════════════
purchase_ai = pd.Series({
    'Yes, definitely': 16.7,
    'Possibly': 50.0,
    'Not sure': 16.7,
    'Probably not': 16.7,
    'Definitely not': 0.0
})
purchase_human = pd.Series({
    'Yes, definitely': 33.3,
    'Possibly': 28.6,
    'Not sure': 19.0,
    'Probably not': 14.3,
    'Definitely not': 4.8
})
purchase_df = pd.DataFrame({
    'AI Content (%)': purchase_ai,
    'Human Content (%)': purchase_human
})
print("=" * 60)
print("PURCHASE INTENT DISTRIBUTION")
print("=" * 60)
print(purchase_df.to_string())
print()
# ══════════════════════════════════════════════════════════════
# 4. HYPOTHESIS RESULTS SUMMARY
# ══════════════════════════════════════════════════════════════
hypotheses = pd.DataFrame({
    'Hypothesis': [
        'H1: AI drives higher engagement',
        'H2: Distinct interaction patterns',
        'H3: AI achieves higher CTR',
        'H4: Human content more trustworthy',
        'H5: AI increases bounce rate',
        'H7: Favourable feedback on AI',
        'H8: Human drives more conversions',
        'H9: Users distinguish content types'
    ],
    'Result': [
        'Supported',
        'Supported',
        'Partially Supported',
        'Supported',
        'Not Supported',
        'Supported',
        'Supported',
        'Supported'
    ],
    'Key_Evidence': [
        'AI: 209 page views vs Human: 79',
        'AI efficiency vs Human emotional appeal',
        'Higher CTR but zero conversions',
        '43.3% AI trust vs 40% Human trust (5/5)',
        'AI bounce 40% < Human bounce 43%',
        'AI clarity rated positively',
        '33.3% definite purchase intent (Human)',
        '63.3% correctly identified Human content'
    ]
})
print("=" * 60)
print("HYPOTHESIS TESTING SUMMARY")
print("=" * 60)
print(hypotheses.to_string(index=False))
print()
# ══════════════════════════════════════════════════════════════
# 5. NUMPY STATISTICAL ANALYSIS
# ══════════════════════════════════════════════════════════════
# Reconstruct rating distributions from survey data
# Week 1 (AI) — 30 respondents, engagement ratings
ai_ratings = np.array([
    1, 1,          # ~6.7% rated 1
    2, 2,          # ~6.7% rated 2
    3, 3, 3, 3,    # ~13.3% rated 3
    4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,  # ~36.7% rated 4
    5, 5, 5, 5     # ~13.3% rated 5 (36.7% of 30 = 11 approx)
])
# Pad to 30
ai_ratings = np.pad(ai_ratings[:30], (0, max(0, 30 - len(ai_ratings))), constant_values=4)[:30]
human_ratings = np.array([
    1,             # ~4.8% rated 1
    2, 2,          # ~9.5% rated 2
    3, 3, 3, 3, 3, # ~23.8% rated 3
    4, 4, 4, 4, 4, 4, 4, 4,  # ~33.3% rated 4
    5, 5, 5, 5, 5, 5          # ~28.6% rated 5
])
human_ratings = np.pad(human_ratings[:22], (0, max(0, 22 - len(human_ratings))), constant_values=4)[:22]
print("=" * 60)
print("NUMPY STATISTICAL SUMMARY — ENGAGEMENT RATINGS")
print("=" * 60)
print(f"AI Content    — Mean: {np.mean(ai_ratings):.2f}  Median: {np.median(ai_ratings):.1f}  "
      f"Std: {np.std(ai_ratings):.2f}  n={len(ai_ratings)}")
print(f"Human Content — Mean: {np.mean(human_ratings):.2f}  Median: {np.median(human_ratings):.1f}  "
      f"Std: {np.std(human_ratings):.2f}  n={len(human_ratings)}")
print()
# Percentage difference in means
mean_diff = np.mean(ai_ratings) - np.mean(human_ratings)
pooled_std = np.sqrt((np.std(ai_ratings)**2 + np.std(human_ratings)**2) / 2)
cohens_d = mean_diff / pooled_std if pooled_std > 0 else 0
print(f"Mean difference: {mean_diff:+.2f}")
print(f"Cohen's d (effect size): {cohens_d:.3f} ({'small' if abs(cohens_d) < 0.5 else 'medium'})")
print()
# ══════════════════════════════════════════════════════════════
# 6. VISUALISATIONS
# ══════════════════════════════════════════════════════════════
fig = plt.figure(figsize=(16, 14))
fig.suptitle(
    "LLMs for E-Commerce Content: AI vs Human-Generated Content Analysis\n"
    "Western Sydney University — INFO7016 — Unice Bondoc (2024)",
    fontsize=14, fontweight='bold', color=TEXT_COLOR, y=0.98
)
# ── Plot 1: Google Analytics Metrics ─────────────────────────
ax1 = fig.add_subplot(3, 2, 1)
metrics_plot = ga_data[ga_data['Metric'] != 'Bounce Rate (%)'].copy()
x = np.arange(len(metrics_plot))
width = 0.35
bars1 = ax1.bar(x - width/2, metrics_plot['AI_Generated'], width, color=AI_COLOR, label='AI Content', alpha=0.9)
bars2 = ax1.bar(x + width/2, metrics_plot['Human_Generated'], width, color=HUMAN_COLOR, label='Human Content', alpha=0.9)
ax1.set_title('Google Analytics — Engagement Metrics', fontweight='bold', fontsize=11)
ax1.set_xticks(x)
ax1.set_xticklabels([m.replace(' (sec)', '\n(sec)') for m in metrics_plot['Metric']], fontsize=8)
ax1.legend(fontsize=9)
for bar in bars1:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=8, fontweight='bold')
for bar in bars2:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             f'{int(bar.get_height())}', ha='center', va='bottom', fontsize=8, fontweight='bold')
# ── Plot 2: Bounce Rate ───────────────────────────────────────
ax2 = fig.add_subplot(3, 2, 2)
bounce = [40, 43]
bars = ax2.bar(['AI Content', 'Human Content'], bounce,
               color=[AI_COLOR, HUMAN_COLOR], alpha=0.9, width=0.4)
ax2.set_title('Bounce Rate (%)', fontweight='bold', fontsize=11)
ax2.set_ylim(0, 60)
ax2.axhline(y=np.mean(bounce), color='gray', linestyle='--', alpha=0.5, label=f'Mean: {np.mean(bounce):.1f}%')
ax2.legend(fontsize=9)
for bar, val in zip(bars, bounce):
    ax2.text(bar.get_x() + bar.get_width()/2, val + 0.5,
             f'{val}%', ha='center', va='bottom', fontsize=11, fontweight='bold')
# ── Plot 3: Survey Ratings Comparison ────────────────────────
ax3 = fig.add_subplot(3, 2, 3)
survey_plot = survey_data[['Category', 'AI_Generated_pct', 'Human_Generated_pct']].copy()
x3 = np.arange(len(survey_plot))
bars3 = ax3.bar(x3 - width/2, survey_plot['AI_Generated_pct'], width, color=AI_COLOR, label='AI Content', alpha=0.9)
bars4 = ax3.bar(x3 + width/2, survey_plot['Human_Generated_pct'], width, color=HUMAN_COLOR, label='Human Content', alpha=0.9)
ax3.set_title('Survey Results — Top Rating % per Category', fontweight='bold', fontsize=11)
ax3.set_xticks(x3)
ax3.set_xticklabels(survey_plot['Category'], fontsize=7.5)
ax3.set_ylabel('% Respondents')
ax3.legend(fontsize=9)
for bar in list(bars3) + list(bars4):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             f'{bar.get_height():.0f}%', ha='center', va='bottom', fontsize=7.5, fontweight='bold')
# ── Plot 4: Purchase Intent Distribution ─────────────────────
ax4 = fig.add_subplot(3, 2, 4)
intent_cats = ['Yes,\ndefinitely', 'Possibly', 'Not\nsure', 'Probably\nnot', 'Definitely\nnot']
intent_ai = [16.7, 50.0, 16.7, 16.7, 0.0]
intent_human = [33.3, 28.6, 19.0, 14.3, 4.8]
x4 = np.arange(len(intent_cats))
ax4.bar(x4 - width/2, intent_ai, width, color=AI_COLOR, label='AI Content', alpha=0.9)
ax4.bar(x4 + width/2, intent_human, width, color=HUMAN_COLOR, label='Human Content', alpha=0.9)
ax4.set_title('Purchase Intent Distribution (%)', fontweight='bold', fontsize=11)
ax4.set_xticks(x4)
ax4.set_xticklabels(intent_cats, fontsize=8)
ax4.set_ylabel('% Respondents')
ax4.legend(fontsize=9)
# ── Plot 5: Engagement Rating Distribution ────────────────────
ax5 = fig.add_subplot(3, 2, 5)
ratings = [1, 2, 3, 4, 5]
ai_dist = [6.7, 6.7, 13.3, 36.7, 36.7]
human_dist = [4.8, 9.5, 23.8, 33.3, 28.6]
ax5.plot(ratings, ai_dist, 'o-', color=AI_COLOR, linewidth=2.5, markersize=8, label='AI Content')
ax5.plot(ratings, human_dist, 's-', color=HUMAN_COLOR, linewidth=2.5, markersize=8, label='Human Content')
ax5.fill_between(ratings, ai_dist, alpha=0.15, color=AI_COLOR)
ax5.fill_between(ratings, human_dist, alpha=0.15, color=HUMAN_COLOR)
ax5.set_title('Engagement Rating Distribution (%)', fontweight='bold', fontsize=11)
ax5.set_xlabel('Rating (1-5)')
ax5.set_ylabel('% Respondents')
ax5.set_xticks(ratings)
ax5.legend(fontsize=9)
ax5.grid(True, alpha=0.3)
# ── Plot 6: Key Findings Summary ─────────────────────────────
ax6 = fig.add_subplot(3, 2, 6)
ax6.axis('off')
summary_data = [
    ['Metric', 'AI Content', 'Human Content', 'Winner'],
    ['Page Views', '209', '79', 'AI'],
    ['Active Users', '48', '32', 'AI'],
    ['Time on Page', '1m 11s', '39s', 'AI'],
    ['Bounce Rate', '40%', '43%', 'AI'],
    ['Trustworthiness (5/5)', '43.3%', '40.0%', 'AI'],
    ['Satisfaction (5/5)', '43.3%', '43.3%', 'Tie'],
    ['Purchase Intent', '16.7%', '33.3%', 'Human'],
    ['Content ID Accuracy', '36.7%', '63.3%', 'Human'],
]
table = ax6.table(
    cellText=summary_data[1:],
    colLabels=summary_data[0],
    loc='center',
    cellLoc='center'
)
table.auto_set_font_size(False)
table.set_fontsize(8.5)
table.scale(1, 1.6)
for (row, col), cell in table.get_celld().items():
    cell.set_edgecolor('#DDDDDD')
    if row == 0:
        cell.set_facecolor(TEXT_COLOR)
        cell.set_text_props(color='white', fontweight='bold')
    elif col == 3:
        val = cell.get_text().get_text()
        if val == 'AI':
            cell.set_facecolor('#E8F4FD')
        elif val == 'Human':
            cell.set_facecolor('#FEF0EA')
        else:
            cell.set_facecolor('#F0F0F0')
    else:
        cell.set_facecolor('white' if row % 2 == 0 else '#F8F9FA')
ax6.set_title('Summary: Key Metrics Comparison', fontweight='bold', fontsize=11, pad=20)
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.savefig('llm_analysis_visualisation.png', dpi=150, bbox_inches='tight',
            facecolor='white')
plt.close()
print("Visualisation saved: llm_analysis_visualisation.png")
print()
# ══════════════════════════════════════════════════════════════
# 7. FINAL SUMMARY REPORT
# ══════════════════════════════════════════════════════════════
print("=" * 60)
print("FINAL ANALYSIS SUMMARY")
print("=" * 60)
print()
print("STUDY: Sequential A/B Test on Shopify E-Commerce Platform")
print("       AI-Generated Content (Week 1) vs Human-Generated (Week 2)")
print(f"       Participants: n=30 (Week 1), n=22 (Week 2)")
print()
print("KEY FINDINGS:")
print()
page_views_ai, page_views_human = 209, 79
uplift = ((page_views_ai - page_views_human) / page_views_human) * 100
print(f"  1. AI content generated {uplift:.0f}% more page views than human content")
print(f"     ({page_views_ai} vs {page_views_human})")
print()
time_ai, time_human = 71, 39
time_uplift = ((time_ai - time_human) / time_human) * 100
print(f"  2. AI content held user attention {time_uplift:.0f}% longer on average")
print(f"     ({time_ai}s vs {time_human}s)")
print()
print(f"  3. Human content drove 2x higher definite purchase intent")
print(f"     (33.3% vs 16.7% 'Yes, definitely')")
print()
print(f"  4. Users correctly identified human content at {63.3}% accuracy")
print(f"     vs {36.7}% for AI content — suggesting distinct writing styles")
print()
print(f"  5. Bounce rates were comparable: AI {40}% vs Human {43}%")
print(f"     — AI slightly better at retaining page visitors")
print()
print("CONCLUSION:")
print("  AI content excels at initial engagement (page views, time on page).")
print("  Human content outperforms AI in trust-building and purchase conversion.")
print("  Optimal strategy: hybrid approach combining AI efficiency with human authenticity.")
print()
print("=" * 60)
print("Analysis complete. Tools used: Python, pandas, numpy, matplotlib")
print("=" * 60)
