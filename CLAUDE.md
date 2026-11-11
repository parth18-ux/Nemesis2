# Droplet Intelligence: guide for Claude Code

Parth Sharma's research project: predict the maximum spreading ratio β_max = D_max/D_0 of a droplet impacting a laser-textured aluminium surface **that the model has never seen**. Presented as a poster at the International Conference on Interfacial Phenomena in Droplets, IISc Bengaluru, 5–7 Oct 2026.

This repository was rebuilt on 25 Oct 2026 from what survived of the original cloud workspace. The earlier GitHub account was suspended. See "Not in this repository yet" before assuming a file exists.

## Ground rules

1. **Numbers come only from the result files.** That means `Droplet_Intelligence_v2/results/*.json`, `Droplet_Intelligence_v2/models/release.json` and `Droplet_Intelligence_v2/results/sem/summary.json`. Never type a figure from memory. Earlier drafts contained invented numbers; see `notes/research_summary.md` §7 and Appendix A of `paper/research_paper_v2.md`.
2. **The data are not Parth's experiments.** They are the public dataset of Može et al., *Data in Brief* 61 (2025) 111697 (doi:10.17632/wsh8rxwd38.1). Parth's work is the surface-held-out evaluation, the descriptors, the models and the uncertainty analysis.
3. **REF-H (the smooth plate) is never used to train or choose a model.** Call it a held-out stress test, not a blind test.
4. **Models are chosen on leave-one-surface-out (LOSO) RMSE.** A change is accepted only if its 95% paired bootstrap interval excludes zero. The bootstrap resamples whole surfaces (4,000 draws, seed 23).
5. **Sole author:** Parth Sharma, Thapar Institute of Engineering and Technology, Patiala, Punjab, India. AI assistance is disclosed in the paper.
6. **Poster rules:**
   - A0 portrait.
   - Conference name at the top, conference logo in the top-right corner, presenter name underlined.
   - Plain wording.
   - No hyphens or dashes in visible poster text, except the sample code REF-H and minus signs in maths.
7. Parth prefers direct, concise answers in English.

## Folder map

| Path | What it is |
|---|---|
| `Droplet_Intelligence_v2/` | **Main code package, v2.1.0**, exactly as uploaded on 23 Sept 2026. It contains code (`droplet/`), data (`data/raw` = the 5 original CSVs, `data/experiments.csv`, `data/sem` = SEM thumbnails and CNN training arrays), five trained GP bundles plus the SEM encoder (`models/`), all fold-level results (`results/`), the browser UI (`web/`), tests and docs. Its own README documents the API and retraining. |
| `web/droplet-intelligence-site/` | The hosted "Droplet Intelligence" site, published 1 Oct 2026. See the row below for its contents. |
| `web/droplet-spread-predictor/` | Live browser predictor (24 Sept). It runs the baseline GP, and its `L.txt` is byte-identical to the site's `models/baseline.L.txt`. |
| `web/v1-beta-max-dashboard/` | v1 single-page dashboard (23 Sept), with its own GP factor in `gp_L.b64.txt`. |
| `paper/research_paper_v2.md` | Full paper text (24 Sept), identical to the project doc. `paper/build.js` is an **earlier revision** of the Node `docx` builder. |
| `poster/landscape_A0/` | `build4.py` (landscape poster of 28 Sept) and `build3.py`. |
| `poster/portrait_v1_with_cover/` | First portrait poster: `build_poster.py`, `figs.py`, `render.py`. |
| `poster/assets/` | Source assets: TIET and IISc logo sources, the organisers' conference logo file (`.pptx`) and a screenshot of it, the original cover image, and the layout reference template Parth chose. |
| `notes/` | `research_summary.md` (all key tables), `pitch_scripts.md`, `phase1_audit_and_plan.md` and `phases_2-4_report.md` (exports of the planning doc), `hackathon_brief.md` and the problem statement PDF. |
| `archive/early_pages/` | Build log (23 Sept) and the first presentation and poster drafts (10 Sept). |

The site in `web/droplet-intelligence-site/` contains:
- `index.html`, `engine.mjs` (GP inference), `imagereader.mjs` (SEM image → φ), `video.mjs` (drop-impact video → β_max);
- `models/` (six GP bundles as JSON plus `L.txt` Cholesky factors, including an `image_only` model);
- `results/`, `sem/` thumbnails, `samples/` and `stats.json`.

The planning doc "Droplet Intelligence — Phase 1 Audit & Plan" also lives online as a claude.ai doc (https://claude.ai/code/artifact/5dee729b-fb8b-4743-8c60-a8c0459a2c4c).

## Final model and headline results

- **Model:** Gaussian process, Matérn 3/2 with one length scale per input, plus white noise.
  - Inputs: ln Re, ln We, ln D_0 (mm), φ, V_tex. Target: ln β_max.
  - 90% interval: exp(μ ± 1.645 σ).
  - φ = (max(s − w, 0)/s)² and V_tex = (1 − φ)·h, with track width w = 45 µm (deep) or 30 µm (shallow). REF-H has φ = 1 and V_tex = 0.
- **Unseen textured surfaces (LOSO):** RMSE 0.0400 (MAPE 1.1%). XGBoost on the same inputs: 0.0563. Worst surface: D50 at 0.059.
- **REF-H:** RMSE 0.0591 (MAPE 1.9%), with 61.6% interval coverage.
- **Interval coverage on unseen surfaces:** 90.1% overall, but 76% for water and 98% for 91 wt% glycerol.
- **No significant gain from:** Matérn 5/2, a Laan backbone, SEM CNN descriptors, the interaction kernel or nested selection.

Full tables are in `notes/research_summary.md`.

## How to run

```
cd Droplet_Intelligence_v2
python -m pip install -r requirements.txt
python -m droplet.serve --port 8000             # http://127.0.0.1:8000
python -m pip install -r requirements-sem.txt   # torch + Pillow, for the SEM tests
python -m unittest discover -s tests -v         # 18 tests
node tests/check_parity.mjs                     # browser worker vs Python
```
As a check, POST to `/api/predict` with `{"D_mm":2.5,"V":1.5,"rho":997.2375,"mu":0.000943923,"sigma":0.07246,"surface":"D200"}`. It should return β_max 2.859, interval [2.807, 2.913].

The `web/` pages use ES modules and `fetch`, so serve them over HTTP. Run `python -m http.server` in the page's folder.

## Not in this repository yet

These existed in the 1 Oct handoff package (six `droplet-intelligence-*.zip` files) but not in the surviving workspace. Add them from those zips if Parth still has them:
- **Final A0 portrait poster** (the submitted version): its PDF and sources, including `build6.py`, the patched `figs.py` and `render.py`, fonts and images.
- **Paper outputs and pipeline:** `Droplet_Spreading_Paper_v2.docx` / `.pdf`, `numbers.json` (the single source for paper and poster numbers), `paper_numbers.py`, `ablation.py` with its outputs, `figs.py` and the `fig1`–`fig4` PNGs.
- **The v1 workspace:**
  - `src/`: the 13-model screen in `models_extra.py` and `ft_transformer.py`, phase 2–4 experiments, CNN and OOD code;
  - `results/`, including `zoo_table.csv`;
  - the Streamlit + FastAPI backup dashboard `droplet_app/`.
- **The Python behind the 1 Oct site's newer features:** `droplet/extensions.py`, `predict_image.py`, `video.py` and the `image_only` model training. Only their browser ports and exported models are here.
- **Raw data:** the original SEM TIFFs and the dataset zip. Download them from Mendeley, doi:10.17632/wsh8rxwd38.1.

The poster and paper scripts here still contain cloud workspace paths. Map them before running:
- `/home/claude/di2/Droplet_Intelligence_v2` → `Droplet_Intelligence_v2`
- `/home/claude/paper` → `paper`

## Open items

1. **Pitch scripts** describe the landscape poster. The submitted poster is the portrait version:
   - panel 1 is "Background and objective";
   - a "Conclusions" band runs along the bottom;
   - panels are retitled ("Prediction intervals", "Variants tested", and others).
2. **Print quality:** the TIET logo and the cover image are low resolution for A0.
3. **The planning doc's architecture diagram** shows the early design (a Laan prior and a spacing descriptor). The final model is the plain GP on the five inputs above.
4. **Research next steps:**
   - measured advancing and receding contact angles for every fluid–surface pair, as a wettability input;
   - a noise model that depends on the Ohnesorge number;
   - new surfaces, with a test set fixed before any tuning.
