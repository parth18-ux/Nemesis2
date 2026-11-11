# Droplet Intelligence

Predicting how far a droplet spreads (maximum spreading ratio β_max) on a laser-textured surface the model has never seen.

- **Author:** Parth Sharma, Thapar Institute of Engineering and Technology, Patiala.
- **Presented:** poster at the International Conference on Interfacial Phenomena in Droplets, IISc Bengaluru, 5–7 Oct 2026.
- **Final model:** a Gaussian process on ln Re, ln We, ln D₀ and two texture descriptors (φ, V_tex).
  - Error on unseen textured surfaces: RMSE 0.040.
  - Smooth plate REF-H: 1.9% mean error.

## What is here

| Folder | Contents |
|---|---|
| `Droplet_Intelligence_v2/` | Main code package (v2.1): data, five trained GP models, all fold-level results, the local web app and API, 18 tests. |
| `web/droplet-intelligence-site/` | Hosted site (1 Oct 2026). Browser inference for six GP models, an SEM image reader and a drop-impact video measurement. |
| `web/droplet-spread-predictor/` | Live browser predictor (24 Sept 2026). |
| `web/v1-beta-max-dashboard/` | Earlier v1 dashboard (23 Sept 2026). |
| `paper/` | Full text of the working paper (`research_paper_v2.md`) and an earlier revision of its Word builder. |
| `poster/` | Build scripts for the landscape and first portrait A0 posters, plus source assets: logos, the organisers' conference logo file, the cover image. |
| `notes/` | Research summary, pitch scripts, the Phase 1 audit and plan, the Phases 2–4 report and the hackathon brief. |
| `archive/early_pages/` | Build log and the first presentation and poster drafts. |

## Run the demo

```
cd Droplet_Intelligence_v2
python -m pip install -r requirements.txt
python -m droplet.serve --port 8000
```

Open http://127.0.0.1:8000. On Windows you can also run `run_demo.bat`.

The pages in `web/` need a local server. Run `python -m http.server` inside a folder, then open the address it prints.

## Data

Može et al., *Data in Brief* 61 (2025) 111697; Mendeley Data doi:10.17632/wsh8rxwd38.1, University of Ljubljana. The experiments are theirs. This project contributes:
- the surface-held-out evaluation;
- the surface descriptors;
- the models;
- the uncertainty analysis.

`CLAUDE.md` has the full guide, including what is still to be added.
