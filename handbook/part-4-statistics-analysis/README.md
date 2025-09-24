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

### Error propagation
When combining measured quantities, propagate their uncertainties explicitly—either via first-order Taylor expansions (Gaussian approximation) or by sampling (Monte Carlo) when relationships are highly non-linear. Track correlations introduced by shared calibration constants so combined uncertainties remain credible.

> 📚 **See also:** Propagation rules (U. Washington PDF) and Columbia’s *Introduction to Error and Uncertainty* in **Further Reading** below.

### Fitting with `curve_fit`
SciPy’s `curve_fit` automates non-linear least squares and supports weighting via the `sigma` argument. Supply realistic initial guesses, scale your data to avoid ill-conditioned matrices, and always inspect the returned covariance matrix (or its failure to converge) before quoting results.

> 🎥 **See also:** StatQuest’s *Linear Regression, Clearly Explained* and the SciPy `curve_fit` docs in **Further Reading**.

### Residuals & χ²
Residual plots reveal model misspecification and heteroscedasticity; combine them with reduced χ² and p-values to judge fit quality. Structured trends or χ² ≫ 1 signal unaccounted-for systematics or underestimated errors—document your diagnosis and next steps.

> 🎥 **See also:** Khan Academy’s *Residuals & least squares regression* for visual intuition.

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

## Interactive Tutorials
- [Linear Regression with Uncertainty (Pilot)](../../binder_splash/index.md)
- [Gaussian Fit with Uncertainty (Pilot)](../../binder_splash/gaussian.md)

### How to use the interactive tutorials
1. Open the tutorial via the **splash page** (acknowledgment required).
2. First Binder launch may take **2–5 minutes** while the environment builds; later runs are faster.
3. Save your work by **File → Download as .ipynb** (Binder sessions are ephemeral).
4. If Binder is busy, try again in a few minutes or switch to local Jupyter (see repo README for setup).

## Further Reading & References

For those who wish to dive deeper into uncertainty propagation, fitting techniques, or statistical foundations, the following resources are recommended:

- **A Brief Introduction to Error Analysis and Propagation** (Fantner, EPFL) — concise, student-level PDF on random vs. systematic errors and propagation rules.  
  [Download PDF](https://www.epfl.ch/labs/lben/wp-content/uploads/2018/07/Error-Propagation_2013.pdf)

- **Introduction to Error and Uncertainty** (Columbia Physics Lab Guide) — practical introduction for lab students; explains uncertainty propagation with real examples.  
  [Download PDF](https://www.physics.columbia.edu/sites/default/files/content/Lab%20Resources/Lab%20Guide%201_%20Introduction%20to%20Error%20and%20Uncertainty.pdf)

- **Propagation of Errors — Basic Rules** (University of Washington) — concise formulas for sums, products, and general functions.  
  [Download PDF](https://courses.washington.edu/phys431/propagation_errors_UCh.pdf)

- **Introduction to Statistics and Data Analysis for Physicists** (University of Siegen / DESY) — comprehensive notes covering significance tests, goodness-of-fit, and systematic uncertainties.  
  [Download PDF](https://www-library.desy.de/preparch/books/vstatmp_engl.pdf)

- **Open Textbook: Introduction to Statistics** (Open Textbook Library) — free online book for a broad statistics foundation beyond physics labs.
  [Access Online](https://open.umn.edu/opentextbooks/textbooks/introduction-to-statistics)

## Further Reading & Video Tutorials

**Core APIs / Docs**
- SciPy `curve_fit` documentation — reference for weighted and non-linear least squares.  
  https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html

**University handouts (open)**
- Columbia Physics: *Introduction to Error and Uncertainty* — lab-focused primer with examples (PDF).  
  https://www.physics.columbia.edu/sites/default/files/content/Lab%20Resources/Lab%20Guide%201_%20Introduction%20to%20Error%20and%20Uncertainty.pdf
- Univ. of Washington: *Propagation of Errors — Basic Rules* — compact formula sheet (PDF).  
  https://courses.washington.edu/phys431/propagation_errors_UCh.pdf
- Illinois (Grainger): *Basic Error Analysis* — summary of random vs. systematic, common pitfalls (PDF).  
  https://courses.grainger.illinois.edu/phys401/fa2017/lectures/Basic%20Error%20Analysis_Fall%202017.pdf

**Open courses**
- MIT OCW: *What’s Significant in Laboratory Measurement? (Error Analysis Lecture)* — measurement strategy & error thinking.  
  https://ocw.mit.edu/courses/5-310-laboratory-chemistry-fall-2019/resources/lecture-4-whats-significant-in-laboratory-measurement-error-analysis-lecture/

**Videos (clear & student-friendly)**
- StatQuest: *Linear Regression, Clearly Explained* — least squares intuition & R².  
  https://www.youtube.com/watch?v=7ArmBVF2dCs
- StatQuest: *Using Linear Models for t-tests/ANOVA* — extending regression logic.  
  https://www.youtube.com/watch?v=R7xd624pR1A
- Khan Academy: *Residuals & least squares regression* — residual meaning and diagnostics.  
  https://www.youtube.com/watch?v=yMgFHbjbAW8

