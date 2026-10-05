# Computer Networks Quiz One

An interactive practice site for CS330 Computer Networks, Quiz 1 (Chapter 1 *Introduction* and Chapter 2 *Application Layer*).

It contains 89 questions taken from past Quiz 1 papers. The site shows one question at a time, and each one comes with:

- the answer
- an explanation
- where the answer comes from (the Chapter 1 or 2 slide number, or the matching Tutorial 1 problem)

A few questions from later chapters (TCP congestion control, IP addressing, NAT) are included and labelled as outside the Chapter 1–2 slides.

## Use it

Open `index.html` in any browser. It is a single self-contained file, so no server or internet connection is needed (fonts load from Google Fonts when online).

To host it, enable GitHub Pages for this repository (Settings → Pages → deploy from the `main` branch, root folder).

## Edit it

- Questions, answers, explanations and sources: `src/data.js`
- Layout, styles and behaviour: `src/template.html`
- Figures cropped from the exam scans: `src/fig/`

After editing, rebuild `index.html`:

```bash
python build.py
```

## Credits

The explanations cite the lecture slides from *Computer Networking: A Top-Down Approach*, 8th edition, by J.F. Kurose and K.W. Ross (Pearson, 2020).
