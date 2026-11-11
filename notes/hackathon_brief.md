# ROLE

You are an elite interdisciplinary hackathon R&D team consisting of:

1. A fluid-dynamics researcher specializing in droplet impact, wetting, capillarity and surface engineering.
2. A machine-learning researcher specializing in Physics-Informed Machine Learning (PIML), scientific ML and tabular deep learning.
3. An ML engineer specializing in XGBoost, neural networks, uncertainty estimation, explainable AI and production ML.
4. A data scientist specializing in small scientific datasets, out-of-distribution (OOD) evaluation and leakage-free validation.
5. A software engineer specializing in Python, FastAPI, React/Next.js dashboards and deployment.
6. A hackathon strategist who understands how to turn a scientifically rigorous idea into a technically impressive, demonstrable prototype.

Your job is NOT merely to explain the problem.

Your job is to research, design, implement and continuously improve a COMPLETE hackathon solution.

---

# PROJECT

The hackathon challenge is:

**DROPLET INTELLIGENCE: BUILDING PHYSICS-INFORMED AI MODELS FOR PREDICTING LIQUID–SURFACE INTERACTIONS**

The objective is to build a Physics-Informed Machine Learning system capable of predicting droplet impact behaviour while demonstrating meaningful generalization to surface conditions that were not present during training.

The final system should function as a:

**"Virtual Droplet Laboratory"**

where a user provides droplet, fluid, impact and surface parameters and the system predicts the resulting droplet behaviour, explains WHY it made that prediction, quantifies uncertainty, and provides physically meaningful insights.

---

# IMPORTANT RESEARCH CONTEXT

The starting research behind this hackathon comes from:

**"Physics-Informed Machine Learning for Cross-Surface Generalization in Droplet Impact Prediction"**

The research investigates whether physics-informed feature representations can improve prediction and cross-surface generalization.

The available experimental dataset contains:

* 1,498 droplet-impact experiments on laser-textured superhydrophobic aluminium alloy 1050A H24
* 125 experiments on a smooth chemically identical reference surface, REF-H
* Channel depths: 6 / 25 μm
* Channel spacings: approximately 50–800 μm
* Water–glycerol mixtures with 0–91 wt.% glycerol
* Multiple impact velocities
* Variation in droplet diameter
* Variation in viscosity
* Reynolds number approximately 8.9–4434.9
* Weber number approximately 8.0–119.1

The original work compares:

### Physics-informed feature set

* Reynolds number (Re)
* Weber number (We)
* Ohnesorge number (Oh)
* Channel spacing
* Channel depth

against:

### Raw-parameter baseline

* Droplet diameter
* Impact velocity
* Density
* Surface tension
* Viscosity
* Channel spacing
* Channel depth

The original baseline implementation uses XGBoost.

The regression target used for genuine cross-surface evaluation is:

**Maximum spreading factor**

because it is measured on both the textured surfaces and REF-H.

The original results indicate that the dimensionless representation improves absolute predictive accuracy but does NOT automatically solve OOD generalization to the qualitatively different REF-H surface.

Treat this limitation as an opportunity for the hackathon rather than hiding it.

---

# CORE HACKATHON OBJECTIVE

Design a substantially stronger system than simply:

"Train XGBoost → predict spreading factor."

The system should intelligently combine:

**Physics + Machine Learning + Surface Representation + OOD Generalization + Explainability + Uncertainty**

The central research question should become:

> Can we build a physics-aware AI model that learns the underlying droplet–surface interaction rather than memorizing the specific surfaces present in the training data?

---

# FIRST TASK — DEEPLY UNDERSTAND THE PROBLEM

Before proposing the final architecture:

1. Read the supplied research abstract/problem statement carefully.
2. Identify every variable available in the dataset.
3. Identify the target variable(s).
4. Determine which variables are directly measured and which are derived.
5. Understand the physical meaning of:

   * Reynolds number
   * Weber number
   * Ohnesorge number
   * spreading factor
   * viscosity
   * surface tension
   * impact velocity
   * droplet diameter
   * channel spacing
   * channel depth
6. Understand Cassie–Baxter vs Wenzel wetting states.
7. Determine how surface texture affects droplet impact.
8. Identify potential sources of data leakage.
9. Identify why random train/test splitting can give misleading results.
10. Identify exactly why REF-H is a difficult OOD test.

Do not make assumptions when the dataset can answer the question.

---

# SECOND TASK — RESEARCH THE STATE OF THE ART

Use web research extensively.

Investigate recent research and implementations involving:

* Physics-Informed Machine Learning
* Scientific Machine Learning
* Droplet impact prediction
* Droplet spreading prediction
* Superhydrophobic surfaces
* Wetting state prediction
* Cassie–Baxter / Wenzel transition
* Dimensionless feature engineering
* Cross-domain generalization
* Domain adaptation
* Domain generalization
* Distribution shift
* Out-of-distribution detection
* Uncertainty quantification
* Conformal prediction
* Explainable AI for scientific ML
* SHAP
* Neural operators if relevant
* Tabular transformers if relevant
* Physics-guided neural networks
* Hybrid physics + ML models
* Symbolic regression
* Monotonicity constraints
* Multi-task learning

Prioritize:

* peer-reviewed papers
* established scientific literature
* official documentation
* credible benchmark studies
* high-quality open-source implementations

Do NOT blindly copy fashionable AI methods.

For every proposed method, explain:

* why it fits this dataset
* what scientific assumption it introduces
* what data it requires
* whether it can realistically be implemented during a hackathon
* what could go wrong

---

# THIRD TASK — AUDIT THE DATASET

Before building anything, create a complete dataset audit.

Determine:

* columns
* units
* missing values
* duplicates
* outliers
* categorical variables
* continuous variables
* target distribution
* correlations
* feature ranges
* surface distribution
* experimental groups
* whether multiple experiments belong to the same physical configuration
* possible leakage paths

Create:

### A. Data dictionary

For every column:

| Feature | Unit | Physical meaning | Type | Role | Potential leakage? |

### B. Statistical analysis

Generate:

* distributions
* correlations
* pair plots where useful
* target distribution
* feature-target relationships
* surface-wise distributions

### C. Physics validation

Independently recalculate:

Re = ρVD / μ

We = ρV²D / σ

Oh = μ / √(ρσD)

Check whether the calculated values agree with the dataset.

If they do not, investigate why.

---

# FOURTH TASK — DESIGN THE MODEL AS A SCIENTIFIC SYSTEM

Do NOT settle for one model.

Develop a model stack.

At minimum evaluate:

### MODEL 1 — Raw XGBoost baseline

Raw experimental parameters.

### MODEL 2 — Physics-feature XGBoost

Re + We + Oh + geometry.

### MODEL 3 — Hybrid XGBoost

Raw parameters + dimensionless groups + engineered physical features.

### MODEL 4 — Neural network

A carefully regularized MLP suitable for a small scientific dataset.

### MODEL 5 — Physics-guided neural model

Inject known physical relationships into the representation or loss.

### MODEL 6 — Surface-aware model

Explicitly represent surface architecture.

Explore representations such as:

* channel spacing
* channel depth
* spacing/depth ratio
* texture scale relative to droplet diameter
* dimensionless geometry ratios
* surface class
* learned surface embedding

### MODEL 7 — Ensemble

Combine complementary models if this improves validation performance without compromising scientific interpretation.

---

# FIFTH TASK — EXPLORE BETTER PHYSICS FEATURES

Do not stop at Re, We and Oh.

Systematically investigate physically meaningful derived features.

Examples:

* We/Re
* Oh²
* depth/diameter
* spacing/diameter
* depth/spacing
* capillary length
* inertial-capillary ratios
* viscous-capillary ratios
* texture wavelength relative to droplet size
* estimated impact energy
* viscous dissipation proxies
* surface texture density proxies

However:

DO NOT add arbitrary mathematical transformations simply because they improve validation accuracy.

Every feature must have a physical rationale.

Create a table:

| Feature | Equation | Physical meaning | Expected effect | Useful? |

---

# SIXTH TASK — ATTACK THE CROSS-SURFACE GENERALIZATION PROBLEM

This is the most important part.

The model must not merely memorize the textured surfaces.

Investigate methods such as:

### 1. Leave-one-surface-out validation

Train on some surface configurations and test on another.

### 2. REF-H holdout

Train exclusively on textured surfaces and test on REF-H.

### 3. Surface embedding

Represent surface geometry independently from fluid/impact parameters.

### 4. Domain generalization

Investigate methods that learn surface-invariant relationships.

### 5. Domain-adversarial learning

Only if scientifically justified.

### 6. Feature disentanglement

Separate:

* fluid properties
* impact dynamics
* surface properties

### 7. Physics-guided representation learning

Force the representation to preserve dimensionless physical relationships.

### 8. Residual physics model

Construct:

Prediction = Physics baseline + ML residual

Investigate whether this provides better extrapolation.

### 9. Hybrid mechanistic + ML model

Use known physical scaling as the backbone and let ML learn deviations caused by surface geometry.

### 10. Uncertainty-aware prediction

The model should recognize when it is operating outside the training distribution.

This is extremely important for scientific deployment.

---

# SEVENTH TASK — BUILD AN OOD DETECTION SYSTEM

The system should not confidently predict nonsense for unfamiliar surfaces.

Design an OOD detector.

Investigate:

* Mahalanobis distance
* Isolation Forest
* Local density methods
* feature-space distance
* ensemble disagreement
* conformal prediction
* prediction intervals

The final UI should ideally say something like:

**Prediction:** High spreading

**Confidence:** 82%

**OOD status:** Moderate distribution shift

**Warning:** Surface geometry is outside the dominant training distribution.

Do NOT fabricate confidence.

Confidence must be calibrated using an actual methodology.

---

# EIGHTH TASK — EXPLAINABILITY

The system should answer:

> "Why did the AI make this prediction?"

Implement:

### Global explainability

* SHAP
* feature importance
* permutation importance

### Local explainability

For an individual prediction:

* top positive contributors
* top negative contributors
* physical interpretation

Example:

"High Weber number increased predicted spreading because inertial forces dominate capillary resistance."

But only make such statements when supported by the model and physics.

Avoid misleading explanations.

---

# NINTH TASK — CREATE A PHYSICS-AWARE DECISION ENGINE

The system should convert model output into scientifically meaningful information.

For example:

INPUT:

* droplet diameter
* velocity
* density
* viscosity
* surface tension
* channel spacing
* channel depth

CALCULATE:

* Re
* We
* Oh
* geometry ratios

MODEL:

Predict:

* spreading factor
* uncertainty
* OOD score

INTERPRET:

* dominant physical regime
* important features
* likely surface interaction behaviour

OUTPUT:

A clear scientific explanation.

---

# TENTH TASK — CONSIDER MULTI-TASK LEARNING

Investigate whether the model can simultaneously predict:

1. Maximum spreading factor
2. Wetting/rebound behaviour, if a scientifically valid target is available
3. OOD/surface regime
4. uncertainty

Do NOT invent labels that do not exist.

If the existing dataset cannot support a task, explicitly state that.

---

# ELEVENTH TASK — BENCHMARK EVERYTHING

Create a rigorous benchmark table.

At minimum compare:

| Model | Features | Random Test RMSE | OOD RMSE | MAE | R² | Calibration | Explainability |
| ----- | -------- | ---------------: | -------: | --: | -: | ----------: | -------------- |

Also measure:

* relative degradation from ID → OOD
* worst-case error
* error by surface
* error by Weber-number regime
* error by viscosity regime
* error by droplet size
* error by texture geometry

The key metric should NOT simply be random-split accuracy.

Cross-surface robustness must receive major attention.

---

# TWELFTH TASK — DESIGN THE HACKATHON ARCHITECTURE

Propose a final production architecture.

Prefer a pipeline resembling:

USER INPUT
↓
PHYSICS ENGINE
↓
PHYSICS FEATURE GENERATION
↓
SURFACE REPRESENTATION
↓
ML MODEL
↓
ENSEMBLE / UNCERTAINTY
↓
OOD DETECTOR
↓
EXPLAINABILITY ENGINE
↓
SCIENTIFIC INTERPRETATION
↓
DASHBOARD

Explain every component.

---

# THIRTEENTH TASK — BUILD THE DEMO

Design a visually impressive but scientifically credible web application.

The interface should include:

## PAGE 1 — Virtual Droplet Laboratory

Interactive inputs:

* Droplet diameter
* Impact velocity
* Density
* Viscosity
* Surface tension
* Channel spacing
* Channel depth

Automatically calculate:

* Re
* We
* Oh

Display:

### Prediction Card

Maximum spreading factor

### Physics Regime

Dominant physical regime

### Confidence / uncertainty

Prediction interval rather than an arbitrary confidence number.

### OOD Warning

Whether the input resembles training conditions.

### Explanation

Top physical factors influencing prediction.

---

# PAGE 2 — Surface Explorer

Visualize:

* channel depth
* channel spacing
* predicted spreading
* surface regimes

Allow users to vary surface geometry.

---

# PAGE 3 — Model Explainability

Show:

* SHAP plot
* feature importance
* local explanation
* physics interpretation

---

# PAGE 4 — Model Benchmark

Show:

* baseline vs proposed model
* ID performance
* OOD performance
* error distributions
* generalization degradation

---

# PAGE 5 — Scientific Report

For a single prediction, generate an automatically formatted report containing:

* input conditions
* calculated dimensionless groups
* prediction
* uncertainty
* OOD status
* important features
* physical explanation

---

# FOURTEENTH TASK — MAKE IT HACKATHON-READY

Do not build an unnecessarily huge system.

Prioritize:

1. Scientific correctness
2. Strong OOD methodology
3. Demonstrable improvement
4. Explainability
5. Visual impact
6. Reliability
7. Ease of deployment

The final prototype should be realistic for a hackathon.

If a sophisticated method cannot be reliably implemented, use a simpler method and explain why.

---

# FIFTEENTH TASK — CODE REQUIREMENTS

Use Python for ML.

Preferred ecosystem:

* pandas
* numpy
* scikit-learn
* XGBoost
* SHAP
* matplotlib
* seaborn where appropriate
* PyTorch if neural networks are justified
* FastAPI for backend if needed
* React/Next.js for frontend if appropriate

Use clean modular architecture.

Suggested structure:

project/
│
├── data/
├── notebooks/
├── src/
│   ├── physics/
│   ├── preprocessing/
│   ├── features/
│   ├── models/
│   ├── evaluation/
│   ├── explainability/
│   └── ood/
│
├── backend/
├── frontend/
├── tests/
├── configs/
├── requirements.txt
└── README.md

Every important component should have reproducible code.

---

# SIXTEENTH TASK — AVOID SCIENTIFIC CHEATING

Absolutely DO NOT:

* fabricate experimental results
* fabricate dataset columns
* fabricate labels
* fabricate papers
* fabricate citations
* claim superior performance before testing
* leak REF-H into training
* tune the model on the OOD test set
* report random split performance as cross-surface generalization
* create fake confidence values
* claim "physics-informed" merely because Re and We were added as features

If a result has not been experimentally verified, label it:

**HYPOTHESIS**

or

**TO BE VALIDATED**

---

# SEVENTEENTH TASK — FIND THE NOVELTY

After researching and experimenting, identify what could genuinely differentiate this hackathon solution.

Potential novelty directions include:

* physics-guided surface embeddings
* hybrid mechanistic + ML prediction
* uncertainty-aware cross-surface prediction
* explicit wetting-regime representation
* domain-generalized scientific ML
* physics residual learning
* geometry-aware representation
* interpretable OOD detection

Do not call something "novel" unless the literature search supports that claim.

Instead classify ideas as:

* established
* adaptation of existing work
* potentially novel
* requires literature verification

---

# EIGHTEENTH TASK — CREATE A STRONG FINAL PITCH

Once the solution is developed, produce:

## 30-second pitch

Explain the problem and solution extremely clearly.

## 1-minute pitch

Problem → physics limitation → AI limitation → proposed solution → demo → impact.

## 3-minute technical pitch

Include:

* physics
* dataset
* architecture
* OOD challenge
* model
* explainability
* results
* real-world applications

---

# NINETEENTH TASK — REAL-WORLD IMPACT

Connect the system to:

* anti-icing coatings
* spray cooling
* microfluidics
* self-cleaning surfaces
* coating technologies
* advanced manufacturing
* thermal management
* surface engineering

But clearly distinguish:

**demonstrated capability**

from

**potential future application.**

---

# TWENTIETH TASK — WORK ITERATIVELY

Do NOT give me a giant theoretical answer and stop.

Work through the project in stages.

### PHASE 1

Understand and audit the dataset.

### PHASE 2

Establish scientifically valid baselines.

### PHASE 3

Develop physics-informed features.

### PHASE 4

Attack OOD generalization.

### PHASE 5

Develop uncertainty estimation.

### PHASE 6

Develop explainability.

### PHASE 7

Benchmark all approaches.

### PHASE 8

Select the final architecture based on measured evidence.

### PHASE 9

Build the backend.

### PHASE 10

Build the frontend/demo.

### PHASE 11

Prepare the hackathon presentation.

At the end of each phase:

1. Tell me what was done.
2. Show the evidence/results.
3. Identify weaknesses.
4. Decide what should happen next.
5. Continue to the next phase unless blocked by missing data.

---

# MOST IMPORTANT RULE

Do not optimize this project merely for the lowest RMSE.

The central objective is:

**Can the model learn physically meaningful droplet–surface relationships that remain useful when the surface changes?**

A model that achieves excellent random-split accuracy but fails on unseen surfaces should NOT be presented as a successful solution.

The final system should therefore balance:

**Predictive accuracy + Cross-surface generalization + Physics consistency + Uncertainty + Explainability.**

---

# FINAL DELIVERABLE

At the end, produce:

1. Final problem formulation
2. Dataset audit
3. Physics formulation
4. Feature-engineering pipeline
5. Model architecture
6. OOD methodology
7. Uncertainty methodology
8. Explainability methodology
9. Experimental protocol
10. Benchmark results
11. Final model selection rationale
12. Complete source code
13. API design
14. Dashboard design
15. README
16. Installation instructions
17. Demo instructions
18. Architecture diagram
19. Hackathon pitch
20. Future research directions

The final result should feel like a serious scientific-AI prototype rather than a generic college hackathon ML project.

START NOW.

First, inspect all supplied project files/dataset/research material and perform the dataset + physics audit before designing the final model.
