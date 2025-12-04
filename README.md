
# mlt-01

## Overview
This project is a lightweight browser-based face-tracking AR demo built with **MindAR** and **A-Frame**. It overlays a 3D model (cowboy hat) on the user’s face and allows real-time adjustments via keyboard controls.

---

## Features
- Real-time face tracking with MindAR.
- Load and display a GLB 3D model.
- Keyboard controls for adjusting:
  - Position (`Arrow Keys`, `W/S` for depth)
  - Rotation (`Q/E` tilt, `A/D` yaw)
  - Scale (`+/-`)
  - Presets (`R` reset, `T` custom fit)
- Export adjusted entity markup with `Enter`.

---

## Folder Structure
project-root/
├─ index.html 
├─ cowboy_hat.glb  # input .glb
└─ README.md 

We ensure `cowboy_hat.glb` is in the same directory as `index.html`

### Prerequisites
- VS Code with **Live Server** extension installed.
- Modern browser (Chrome, Edge) with camera support.
- Camera access allowed in the browser.

### Running the Demo
1. Open the project folder in VS Code.
2. Right-click `index.html` → **“Open with Live Server”**.
3. The demo will launch in the default browser (Live Server serves via `http://127.0.0.1:5500` or similar).
4. Click **Start Camera** to initialize face tracking.

### Keyboard Controls
| Key(s)            | Action                           |
|------------------|----------------------------------|
| `Arrow Keys`      | Move X/Y                        |
| `W` / `S`         | Move Z (depth)                  |
| `Q` / `E`         | Tilt (X rotation)               |
| `A` / `D`         | Yaw (Y rotation)                |
| `+` / `-`         | Scale up / down                 |
| `R`               | Reset to default preset         |
| `T`               | Apply custom preset             |


### References
- [A-Frame Documentation](https://aframe.io/docs/)
- [MindAR.js Documentation](https://hiukim.github.io/mind-ar-js-doc/)


Performance Optimization
FPS monitor can be Implemented to dynamically adjust model detail if performance drops.
