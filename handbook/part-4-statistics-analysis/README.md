---
description: Guidance on data analysis, uncertainties, and fitting
---

# Part 4 · Statistics & Data Analysis

Sound data analysis underpins credible conclusions. Plan your workflow before collecting data and document every processing step.

## Core Principles
- **Separate uncertainties:** Distinguish clearly between **statistical** (random) and **systematic** (bias) contributions. Report them individually and, if combined, show the method used.
- **Traceability:** Every plotted point must be traceable back to raw data and an analysis script or calculation in your notebook.
- **Transparency:** Describe all corrections (background subtraction, efficiency factors, dead-time corrections, etc.) and justify assumptions.
- **Significant figures:** Quote results with significant digits consistent with their total uncertainty.

## Standard Tools & Methods
- **Descriptive statistics:** Mean, median, variance, standard error of the mean, confidence intervals.
- **Uncertainty propagation:** Apply differential error propagation or Monte Carlo sampling to transmit uncertainties through calculations.
- **Curve fitting:** Use linear regression, weighted least squares, or non-linear χ² minimization depending on the model. Provide fit parameters with covariance matrices or confidence intervals.
- **Goodness-of-fit metrics:** Report χ²/ndf, p-values, or adjusted R² and comment on their implications.
- **Graphical analysis:** Plot data with error bars, include units on axes, and add residual plots to inspect systematic deviations.
- **Outlier treatment:** Apply justified criteria (e.g., Chauvenet’s) and document decisions; never delete points without explanation.

## Recommended Workflow
1. **Organize data** in structured folders (raw, processed, plots, scripts). Keep a README describing file contents.
2. **Calibrate first:** Convert instrument readings using calibration curves or reference measurements before main analysis.
3. **Perform preliminary checks** (quick plots, sanity checks) to identify issues while still in the lab.
4. **Automate analysis** with scripts (Python, MATLAB, ROOT, etc.). Version-control your code and comment intermediate steps.
5. **Quantify uncertainties** for each derived quantity; tabulate both statistical and systematic components.
6. **Interpret results** by comparing to theory or literature values within uncertainty bounds. Discuss discrepancies realistically.

## Documentation in Reports
- Include a dedicated subsection that explains your analysis pipeline, software used, and uncertainty evaluation.
- Present representative plots with readable legends and captions that describe what the reader should notice.
- Attach tables of raw data or long results in appendices; reference them in the main text when relevant.
- When using external code or libraries, cite them (e.g., NumPy, SciPy) and state the versions.

## Common Pitfalls to Avoid
- Estimating systematic uncertainty solely from the deviation between your result and a literature value.
- Reporting fit parameters without uncertainties or without specifying units.
- Rounding intermediate results too early, which propagates significant rounding errors.
- Ignoring correlations between measured quantities; consider covariance where applicable.

If you are unsure about a statistical method, consult your tutor early or use the statistics help desks offered by the Faculty of Physics.

## Interactive Tutorial (Pilot)
Launch the in-browser notebook via our splash page (acknowledgment required):
[Launch the Linear Regression Pilot](../../binder_splash/index.md)

> **Note on Binder**
> - The **first launch may take 2–5 minutes**, as Binder builds the environment.  
> - Subsequent launches will be faster.  
> - If the environment fails to load, refresh or try again later (Binder servers are free and can be busy).
