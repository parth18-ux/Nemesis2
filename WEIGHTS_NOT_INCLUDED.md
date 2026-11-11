# Model weight files left out of this zip

This zip holds all the code, data, results, notes, paper text and model settings (updated 11 Nov 2026). To fit in one small file, it leaves out the large trained-weight files (about 130 MB):

- `Droplet_Intelligence_v2/models/*.L.bin`: the five GP factors the demo app loads.
- `web/droplet-intelligence-site/models/*.L.txt` and `web/droplet-spread-predictor/L.txt`: the same factors as text, for the browser apps.
- `web/v1-beta-max-dashboard/gp_L.b64.txt`: the factor for the v1 dashboard.
- `web/droplet-intelligence-site/samples/*.png` and `*.webm`: sample inputs for the site's image and video demos.

Copies of all of them are in the full project folder from 25 Oct (`iisc/droplet-intelligence` on Parth's laptop). Copy them into the same paths before running the demo app or the web pages.
