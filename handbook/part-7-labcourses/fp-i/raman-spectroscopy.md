---
description: Applications of Spectroscopy
---

# Raman Spectroscopy

## Learning Goals

* Understand the **principle of Raman scattering** versus fluorescence and Rayleigh scattering.
* Align a basic Raman setup (excitation laser, cuvette holder, collection optics, spectrometer).
* Record and analyze Raman spectra of liquids and solids.
* Apply statistics to background subtraction and peak fitting.
* Identify **systematic errors** (e.g., background fluorescence, power drift, misalignment).

***

## Pre-lab Reading & Safety

* Light–matter interaction and molecular vibrations (selection rules for Raman).
* **Laser safety**: verify laser class; wear certified goggles; avoid direct/indirect viewing of beams and fiber outputs; handle cuvettes carefully.

**Helpful primers**

* Raman spectroscopy (overview): https://en.wikipedia.org/wiki/Raman\_spectroscopy
* Selection rules (molecular vibrations): https://en.wikipedia.org/wiki/Raman\_scattering#Selection\_rules

***

## Experimental Setup (example)

* **Laser** (e.g., 532 nm, fiber-coupled).
* **Cuvette holder** with multiple ports (excitation, transmission, side-scatter).
* **Collection optics** → **spectrometer** (e.g., Ocean Insight / similar).

**Alignment checklist**

1. Dark/detector background with laser off.
2. Align excitation through the cuvette; verify transmission.
3. Optimize side-scatter coupling into the spectrometer fiber.
4. Check for fluorescence; plan background measurement.

***

## Measurement Plan

1. Record **dark/background** spectra (laser off; closed shutter).
2. Water sample: transmitted and side-scatter spectra.
3. Ethanol (and optional samples): acquire spectra under identical conditions.
4. Vary **integration time** and **laser power** to study SNR scaling.
5. Demonstrate the effect of **neglecting background** on peak parameters.

***

## Data & Analysis Checkpoints

* Plot raw spectra with uncertainties (repeat scans → standard errors).
* Perform **background subtraction** (dark + sample background).
* Fit Raman lines (Gaussian/Lorentzian); report **peak position (cm⁻¹)** and width.
* Compare measured Raman shifts with **literature values** (cite source).
* Inspect **residuals**; diagnose model mismatch (e.g., unmodeled background slope).
* Discuss **systematic vs. statistical** uncertainties; do not infer systematics from literature deviation alone.

***

## Typical Pitfalls

* Weak signal from fiber misalignment.
* Fluorescence misinterpreted as Raman features.
* Single-shot “nice looking” spectra without error estimation.
* Missing dark/background baselines.

***

## Figures / Tables to Include

* Optical schematic (laser, cuvette, collection, spectrometer).
* Example spectrum (raw vs. background-subtracted).
* Table: **Raman shift** (measured vs. literature).
* Fit with residuals (showing background-induced bias if unmodeled).

***

## Reflection Questions

* Why is **background modeling** critical for unbiased peak parameters?
* How do peak **intensity** and **width** respond to laser power and integration time?
* Which safety aspects are specific to Raman compared to other optics labs?

***

## References & Useful Links

* **Course materials** (ILIAS; internal):
* **Textbooks**
  * Long, D. A., _The Raman Effect: A Unified Treatment of the Theory of Raman Scattering by Molecules_ (Wiley).
  * Demtröder, W., _Experimentalphysik 3: Atome, Moleküle und Festkörper_ (Springer).
* **Instrumentation & application notes**
  * Ocean Insight Raman basics (application note): https://www.oceaninsight.com/applications/measurement-techniques/raman/
  * HORIBA Raman Academy (tutorials): https://www.horiba.com/int/scientific/learning-center/raman-academy/
* **Data handling**
  * Background modeling & bias (handbook tutorial): see **Part 4 → Interactive Tutorials → Background Modeling**.
