"""A0 landscape poster in the sidebar template layout. Numbers from paper/numbers.json (v2.1 result files)."""
import os, json
N = json.load(open('/home/claude/paper/numbers.json'))

def font_faces():
    out = []
    for f in sorted(os.listdir('fonts')):
        if not f.endswith('.woff2') or '-sans-' not in f: continue
        parts = f.replace('.woff2', '').split('-'); w, st = parts[-2], parts[-1]
        rng = 'U+0370-03FF' if 'greek' in f else ('U+0100-024F,U+1E00-1EFF,U+2113,U+2C60-2C7F' if 'latin-ext' in f else 'U+0000-00FF,U+0131,U+0152-0153,U+02C6,U+02DC,U+2000-206F,U+2074,U+20AC,U+2122,U+2190-2193,U+2212,U+2215,U+2248,U+2264,U+2265,U+FEFF')
        out.append(f'@font-face{{font-family:"Plex";src:url("fonts/{f}") format("woff2");font-weight:{w};font-style:{st};unicode-range:{rng};}}')
    return '\n'.join(out)

ICON = {
 'drop': '<path d="M24 7C24 7 13 20 13 28a11 11 0 0 0 22 0C35 20 24 7 24 7Z" fill="none" stroke="#fff" stroke-width="2.6" stroke-linejoin="round"/>',
 'grid': '<g fill="none" stroke="#fff" stroke-width="2.4"><rect x="11" y="11" width="11" height="11" rx="1.5"/><rect x="26" y="11" width="11" height="11" rx="1.5"/><rect x="11" y="26" width="11" height="11" rx="1.5"/><rect x="26" y="26" width="11" height="11" rx="1.5"/></g>',
 'band': '<g fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"><path d="M9 33 C17 33 19 14 24 14 S31 33 39 33"/><line x1="24" y1="9" x2="24" y2="39" stroke-width="1.8" stroke-dasharray="2.5 3"/></g>',
 'check': '<path d="M13 25l7 7 15-16" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>',
 'layers': '<g fill="none" stroke="#fff" stroke-width="2.4" stroke-linejoin="round"><path d="M24 10l14 7-14 7-14-7z"/><path d="M10 24l14 7 14-7"/><path d="M10 31l14 7 14-7"/></g>',
}
def icon(k, cls=''): return f'<span class="ic {cls}"><svg viewBox="0 0 48 48">{ICON[k]}</svg></span>'

fl = N['by_fluid']
visc = {0: '0.94', 20: '1.6', 60: '9.1', 78: '36.7', 91: '151'}
rows = ''.join(f"<tr><td>{f['gly']}%</td><td>{visc[f['gly']]}</td><td>{f['loso_rmse']:.3f}</td><td>{f['loso_cov']:.0%}</td><td>{f['refh_rmse']:.3f}</td><td>{f['refh_cov']:.0%}</td></tr>" for f in fl)

CSS = r"""
@page { size: 1189mm 841mm; margin: 0; }
:root { --side:#7b6b5d; --side2:#6b5c4f; --ink:#2f2620; --ink2:#51463e; --brown:#7a4f32; --rule:#d8cec4; --tint:#f3eee8; --tint2:#e9e1d8; --foot:#4a3a2e; --cream:#efe6da; }
* { box-sizing:border-box; margin:0; padding:0; }
html,body { background:#fff; }
body { width:1189mm; height:841mm; font-family:"Plex",sans-serif; color:var(--ink); font-size:21pt; line-height:1.36;
       -webkit-print-color-adjust:exact; print-color-adjust:exact; overflow:hidden; display:grid; grid-template-columns:292mm 1fr; grid-template-rows:1fr 15mm; }
b { font-weight:600; }
sub,sup { font-size:.7em; line-height:0; }
/* sidebar */
aside { background:var(--side); color:#fff; padding:24mm 20mm 16mm; display:flex; flex-direction:column; gap:10mm; }
aside h1 { font-size:66pt; line-height:1.07; font-weight:700; letter-spacing:-.005em; }
aside .sub { font-size:31pt; line-height:1.2; font-weight:600; color:var(--cream); }
aside .who { font-size:24pt; line-height:1.35; }
aside .who b { font-size:28pt; font-weight:700; display:block; }
aside .intro { font-size:23pt; line-height:1.4; padding-top:8mm; border-top:1.2mm solid rgba(255,255,255,.35); }
aside h2 { font-size:23pt; letter-spacing:.08em; font-weight:700; color:var(--cream); text-transform:uppercase; margin-bottom:5mm; }
.kt { display:flex; flex-direction:column; gap:6.5mm; }
.kt div { display:grid; grid-template-columns:24mm 1fr; gap:6mm; align-items:center; font-size:21pt; line-height:1.3; }
.ic { width:24mm; height:24mm; border-radius:50%; background:var(--brown); display:grid; place-items:center; }
aside .ic { background:rgba(255,255,255,.18); }
.ic svg { width:15mm; height:15mm; }
.logos { margin-top:auto; background:#fff; border-radius:3mm; padding:6mm 7mm; display:flex; align-items:center; justify-content:space-around; gap:6mm; }
.logos img { height:34mm; width:auto; }
.logos img.ws { height:27mm; }
/* main */
main { padding:18mm 22mm 12mm 20mm; display:flex; flex-direction:column; min-height:0; }
.top { display:flex; justify-content:flex-end; align-items:baseline; gap:8mm; margin-bottom:9mm; }
.top .t1 { font-size:27pt; font-weight:700; color:var(--ink); letter-spacing:.02em; text-transform:uppercase; }
.top .t2 { font-size:21pt; color:var(--brown); font-weight:600; letter-spacing:.06em; text-transform:uppercase; }
.cols { flex:1; display:grid; grid-template-columns:1fr 1.18fr .92fr; gap:17mm; min-height:0; }
.col { display:flex; flex-direction:column; gap:8mm; min-height:0; }
h2 { font-size:30pt; font-weight:700; color:var(--brown); text-transform:uppercase; letter-spacing:.04em; padding-bottom:2.5mm; border-bottom:.7mm solid var(--rule); margin-bottom:4.5mm; }
h3 { font-size:22.5pt; font-weight:700; color:var(--ink); margin:4.5mm 0 1.5mm; }
section > h3:first-of-type { margin-top:0; }
p + p { margin-top:3mm; }
.lead { color:var(--ink2); }
ul.b { list-style:none; display:flex; flex-direction:column; gap:1.6mm; }
ul.b li { padding-left:6mm; position:relative; }
ul.b li::before { content:""; position:absolute; left:0; top:.55em; width:2.2mm; height:2.2mm; border-radius:50%; background:var(--brown); }
.eq { background:var(--tint); border-radius:2mm; padding:3mm 5mm; margin:2.5mm 0; font-size:21pt; text-align:center; }
.eq i { font-style:italic; }
.photos { display:grid; grid-template-columns:1fr 1fr; gap:4mm; margin-top:auto; }
.photos figure { display:flex; flex-direction:column; }
.photos img { width:100%; aspect-ratio:1.3; object-fit:cover; display:block; }
.photos figure.w { grid-column:1/-1; }
.photos figure.w img { aspect-ratio:2.7; object-position:center 45%; }
figcaption { background:var(--tint2); font-size:16.5pt; padding:1.6mm 3mm; color:var(--ink2); }
.fig { display:grid; grid-template-columns:1fr 64mm; gap:5mm; align-items:center; }
.fig img, img.full { width:100%; display:block; }
.call { background:var(--tint); border-left:1.4mm solid var(--brown); padding:4mm 4.5mm; font-size:18.5pt; line-height:1.35; }
.call .v { font-size:36pt; font-weight:700; color:var(--brown); line-height:1.05; display:block; margin-bottom:1.5mm; }
.note { font-size:16.5pt; color:var(--ink2); margin-top:1.5mm; }
table { width:100%; border-collapse:collapse; font-size:18pt; font-variant-numeric:tabular-nums; }
th { background:var(--tint2); color:var(--ink); font-weight:600; text-align:right; padding:2mm 2.6mm; line-height:1.2; vertical-align:bottom; }
td { text-align:right; padding:1.7mm 2.6mm; border-bottom:.4mm solid var(--rule); }
th:first-child, td:first-child { text-align:left; }
th.g { text-align:center; font-size:15.5pt; background:none; color:var(--brown); border-bottom:.5mm solid var(--brown); padding-bottom:1mm; }
.concl { display:flex; flex-direction:column; gap:5.5mm; }
.concl div { display:grid; grid-template-columns:22mm 1fr; gap:5mm; align-items:center; font-size:20pt; line-height:1.3; }
.concl .ic { width:22mm; height:22mm; } .concl .ic svg { width:13mm; height:13mm; }
.refs { font-size:15.5pt; line-height:1.35; display:flex; flex-direction:column; gap:1.4mm; color:var(--ink2); }
code { font-family:"Plex",monospace; background:var(--tint); padding:0 1.5mm; border-radius:1mm; font-size:.92em; }
.hyp { font-size:12pt; font-weight:700; letter-spacing:.08em; color:var(--brown); border:.4mm solid var(--brown); padding:0 1.2mm; border-radius:1mm; vertical-align:.15em; }
footer { grid-column:1/-1; background:var(--foot); color:#e6dcd1; display:flex; justify-content:space-between; align-items:center; padding:0 20mm; font-size:15pt; letter-spacing:.03em; }
"""

html = f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Cross-Surface Droplet Poster</title>
<style>{font_faces()}{CSS}</style></head><body>
<aside>
 <h1>Physics-Informed Machine Learning for Cross-Surface Droplet Impact Prediction</h1>
 <div class="sub">Predicting how far a droplet spreads on a surface the model has never seen</div>
 <div class="who"><b>Parth Sharma</b>Thapar Institute of Engineering and Technology, Patiala, Punjab, India</div>
 <p class="intro">Droplet-impact models are usually scored on random splits, where every test surface was also in training. Surface design needs the opposite: a prediction <b>before</b> the surface is made. We trained on 12 laser-textured surfaces, always holding one out, and stress-tested on a smooth plate never used in training.</p>
 <div>
  <h2>Key takeaways</h2>
  <div class="kt">
   <div>{icon('drop')}<span>A Gaussian process predicts β<sub>max</sub> on an <b>unseen surface</b> to within <b>0.040</b> RMSE, 29% better than XGBoost.</span></div>
   <div>{icon('grid')}<span>The <b>smooth-plateau fraction φ</b> read from SEM puts textured and smooth surfaces on one scale.</span></div>
   <div>{icon('band')}<span><b>90%</b> of unseen-surface impacts fall inside the 90% interval; only <b>62%</b> on the smooth plate, where wettability differs.</span></div>
  </div>
 </div>
 <div class="logos"><img class="ws" src="logo_ws.png" alt="Workshop logo"><img src="logo_iisc.png" alt="IISc logo"><img src="logo_tiet.png" alt="Thapar Institute logo"></div>
</aside>

<main>
 <div class="top"><span class="t1">Workshop on Interfacial Phenomena in Droplets</span><span class="t2">IISc Bengaluru · 5–7 Oct 2026</span></div>
 <div class="cols">
  <div class="col">
   <section><h2>Background</h2>
    <p>The maximum spreading ratio β<sub>max</sub> = <i>D</i><sub>max</sub>/<i>D</i><sub>0</sub> sets how much of a surface a droplet wets, which matters for cooling, coating and anti-icing. Laser texturing changes it, but scaling laws were derived on smooth wettable surfaces.</p>
    <p>Machine-learning studies on textured surfaces, including a random-split GP on this data [2], test on surfaces already seen in training. <b>We ask whether a model generalizes to a new surface.</b></p>
   </section>
   <section><h2>Methods</h2>
    <h3>Data</h3>
    <ul class="b">
     <li>Public dataset of Može et al. [1]: 1,498 impacts on 12 laser-textured aluminium surfaces, plus 125 on a smooth plate (REF-H).</li>
     <li>Channel pitch 50–800 µm, depth 6 or 25 µm; water to 91 wt% glycerol (0.94–151 mPa·s); <i>We</i> 8–119, <i>Re</i> 9–4,435.</li>
    </ul>
    <h3>Surface descriptors from SEM</h3>
    <p>Track widths <i>w</i> read from SEM (≈45 µm deep, 30 µm shallow) give every surface the same two quantities:</p>
    <div class="eq"><i>φ</i> = (1 − <i>w</i>/<i>s</i>)<sup>2</sup> &nbsp;&nbsp; <i>V</i><sub>tex</sub> = (1 − <i>φ</i>)<i>h</i></div>
    <p>Textured φ runs from 0.01 (D50) to 0.93 (S800); the smooth plate is simply φ = 1.</p>
    <h3>Model and evaluation</h3>
    <ul class="b">
     <li>Inputs ln <i>Re</i>, ln <i>We</i>, ln <i>D</i><sub>0</sub>, φ, <i>V</i><sub>tex</sub>; target ln β<sub>max</sub>. Gaussian process, Matérn 3/2 kernel.</li>
     <li><b>Leave-one-surface-out</b> (12 folds) picks the model, since repeated impacts make random splits leak.</li>
     <li>Changes accepted only if the 95% CI from resampling whole surfaces (4,000 draws) excludes zero.</li>
     <li>REF-H never used to train or choose a model.</li>
    </ul>
   </section>
   <div class="photos">
    <figure><img src="D200_43.jpg" alt="SEM of D200 at 43x"><figcaption>D200 textured surface, 43×</figcaption></figure>
    <figure><img src="REF-H_43.jpg" alt="SEM of REF-H at 43x"><figcaption>Smooth plate REF-H, 43×</figcaption></figure>
    <figure class="w"><img src="D200_350.jpg" alt="SEM of D200 at 350x"><figcaption>D200, 350×: rough laser track beside a smooth plateau</figcaption></figure>
   </div>
  </div>

  <div class="col">
   <section><h2>Results</h2>
    <h3>1. Accuracy on unseen surfaces</h3>
    <p class="lead">Thirteen learners, same five inputs, each surface held out in turn.</p>
    <div class="fig"><img src="f_models.svg" alt="Unseen-surface RMSE of 13 models">
     <div class="call"><span class="v">0.040</span>Gaussian process RMSE on the held-out surface (1.1% mean error), vs 0.056 for XGBoost. Difference 95% CI: 0.006–0.028.</div></div>
    <h3>2. Knowing when not to trust it</h3>
    <p class="lead">Share of impacts inside the calibrated 90% interval.</p>
    <div class="fig"><img src="f_fluid.svg" alt="Interval coverage by glycerol content">
     <div class="call"><span class="v">90.1%</span>coverage on unseen textured surfaces overall, but 76% for water and 98% for 91 wt% glycerol. Thin fluids feel the surface more.</div></div>
    <h3>3. Error and coverage by fluid</h3>
    <table>
     <thead><tr><th rowspan="2" style="text-align:left">Glycerol</th><th rowspan="2">µ (mPa·s)</th><th class="g" colspan="2">Unseen textured</th><th class="g" colspan="2">Smooth plate REF-H</th></tr>
     <tr><th>RMSE</th><th>In 90%</th><th>RMSE</th><th>In 90%</th></tr></thead>
     <tbody>{rows}
      <tr><td><b>All</b></td><td></td><td><b>0.040</b></td><td><b>90%</b></td><td><b>0.059</b></td><td><b>62%</b></td></tr></tbody>
    </table>
    <p class="note">RMSE of β<sub>max</sub>. Coverage per held-out surface: 84–96%.</p>
    <h3>4. Smooth-plate stress test</h3>
    <div class="fig"><img src="f_parity.svg" alt="REF-H predicted versus measured">
     <div class="call"><span class="v">1.9%</span>mean error on REF-H (RMSE 0.059), but only 62% inside the interval. The model over-predicts at high <i>We</i> by 0.041: REF-H is hydrophobic, the textures superhydrophobic.</div></div>
   </section>
  </div>

  <div class="col">
   <section><h2>What did not help</h2>
    <img class="full" src="f_forest.svg" alt="Change in unseen-surface error for model variants">
    <p class="note">Paired surface-bootstrap 95% CIs. Only XGBoost differs significantly, and it is worse. A CNN reading φ straight from SEM images gave 0.038, not significant.</p>
   </section>
   <section><h2>Conclusions</h2>
    <div class="concl">
     <div>{icon('check')}<span>Judge droplet models on <b>unseen surfaces</b>; random splits hide the gap.</span></div>
     <div>{icon('layers')}<span>Describe surfaces with quantities <b>every surface has</b>, like φ.</span></div>
     <div>{icon('drop')}<span>A plain <b>GP</b> beats 12 alternatives; physics backbones add no significant gain.</span></div>
     <div>{icon('band')}<span>Intervals hold on average, not per fluid, and fail on a new wettability. <b>Say so on the tool.</b></span></div>
    </div>
   </section>
   <section><h2>Future work</h2>
    <ul class="b">
     <li>Measured contact angles for every fluid–surface pair as an input.</li>
     <li>Noise that depends on viscosity.</li>
     <li>New surfaces with a test set held back before any tuning.</li>
    </ul>
   </section>
   <section><h2>Software</h2>
    <p style="font-size:18.5pt">Python package and browser app with 5 trained GPs; every prediction carries its interval and flags extrapolation. Browser and Python agree to 5×10<sup>−12</sup>. <code>python -m droplet.serve</code></p>
   </section>
   <section><h2>References</h2>
    <div class="refs">
     <div>[1] M. Može et al., Data in Brief 61 (2025) 111697; doi:10.17632/wsh8rxwd38.1</div>
     <div>[2] S. Jereb et al., Biomimetics 10 (2025) 357</div>
     <div>[3] N. Laan et al., Phys. Rev. Applied 2 (2014) 044018</div>
    </div>
   </section>
  </div>
 </div>
</main>
<footer><span>Data: Može et al. (2025), University of Ljubljana · Analysis, models and software: Parth Sharma</span><span>Workshop on Interfacial Phenomena in Droplets · IISc Bengaluru · 2026</span></footer>
</body></html>'''
open('poster.html', 'w').write(html)
print('ok')
