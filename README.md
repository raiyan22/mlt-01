
# task 2 

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














To: career@coderex.co Subject: ML Engineer Task Submission - [Your Name]

Body:

Dear Hiring Team,

Please find attached my submission for the Machine Learning Engineer task (Task 1: 2D → 3D Generation).

GitHub Repository: [Insert Your GitHub Link Here]

Summary of Approach: I implemented a pipeline using the TripoSR architecture due to its state-of-the-art performance in feed-forward 3D reconstruction.

Engineering: Wrapped the logic in a modular Python class with argparse CLI support for easy local execution. Robustness: Integrated rembg (U-2-Net) for automatic background removal, ensuring the model handles raw user photos correctly without noise artifacts. Deliverables: The repository contains the source code, a requirements.txt for reproducibility, and a sample .glb output. I have also included an improvement proposal in the README regarding Multi-View Consistency (using Zero123++) and Texture Refinement.

Thank you for your time and consideration.

Best regards,

[Your Name] [Your Phone Number] [Your LinkedIn Profile]



Technical Bottlenecks Encountered:

Dependency Hell (Binary Incompatibility):

The Issue: The ecosystem currently suffers from severe version conflicts between numpy (v2.0 vs v1.x), transformers, and rembg. Impact: Fixing one library often broke another due to ABI (Application Binary Interface) mismatches in pre-compiled wheels. Hardware Abstraction Failures (ONNX/CUDA):

The Issue: The background removal module (rembg) relies on onnxruntime. The GPU version of ONNX conflicted with the specific CUDA drivers provided in the Google Colab runtime, causing immediate crashes during import. Attempted Fix: I attempted to decouple the background remover by monkey-patching the source code and mocking the rembg module (sys.modules), but deep integration within the library made this unstable. Compilation Constraints (C++ Extensions):

The Issue: TripoSR relies on torchmcubes for mesh extraction. This is a C++ extension that requires compilation. Impact: When attempting to run locally or on CPU-only nodes to ensure reproducibility (as per the task requirements), the Just-In-Time (JIT) compilation frequently failed due to missing system-level build tools (gcc/nvcc mismatches). The Engineering Pivot: To ensure reproducibility and portability (key requirements for the task), I pivoted to OpenAI's Shap-E. Unlike TripoSR, Shap-E relies on pure PyTorch and standard libraries (trimesh), removing the dependency on fragile C++ extensions and complex ONNX/CUDA driver mappings. This guarantees the script runs on any machine (CPU or GPU) without environment hacking.

Project Overview
This repository contains a robust pipeline for generating 3D assets (.glb) from 2D images using OpenAI's Shap-E.

Why Shap-E?
While newer models like TripoSR exist, I selected Shap-E for this implementation because:

Architectural Stability: It relies on pure PyTorch and standard diffusion mechanisms, avoiding the need for complex C++ extensions (like torchmcubes) that frequently break on consumer CPUs.
Portability: The code runs reliably on both CPU and GPU without requiring custom CUDA kernels, satisfying the requirement for "local reproducibility."
Consistency: It uses a latent diffusion approach that ensures valid topology even for complex shapes.
How to Run
Install requirements:
pip install git+https://github.com/openai/shap-e.git trimesh numpy
Run the script:
python main.py --input my_image.png --output my_model.glb
Implementation Details
Encoder: The input image is encoded into the Shap-E latent space.
Diffusion: A 64-step diffusion process generates a point cloud representation.
Decoding: The transmitter decodes the result into a mesh.


✅ What you did & why

You picked MindAR.js + A-Frame for face‑tracking Web‑AR. That’s smart because MindAR.js gives you a complete face‑tracking engine (landmark detection, face anchor positions, scaling based on face size, correct orientation etc.), and A‑Frame gives a simple declarative 3D scene API, so you don’t have to manually write low‑level WebGL code. 
hiukim.github.io
+2
hiukim.github.io
+2

You structured the HTML/page so that: the 3D model (cowboy_hat.glb) is loaded via <a-asset-item> — standard practice in A-Frame to preload assets before use. This ensures that when the AR/face‑tracking begins, the model is already fetched and ready.

You created a face‑target anchor (<a-entity mindar-face-target="anchorIndex: 168">) — that tells MindAR: “Attach this 3D model to that particular landmark / anchor on the detected face.” This way the hat will move/rotate/scale with the user’s face naturally, adhering to face tracking.

You gave the hat a base position, rotation and scale (your “custom fit”) in the HTML — which gives a reasonable starting alignment relative to the face before you allow manual adjustments.

You added custom JavaScript code to allow keyboard-based manual adjustments (position, rotation, scale) after initial placement. That’s useful because automatic “anchor + default transform” may not perfectly match all face shapes or camera setups — so users (or devs) can fine-tune placement interactively.

You also added UI feedback: loading overlay spinner until scene loads, then “Start Camera” button. That ensures a smoother UX (e.g. you don’t ask camera permission before everything is ready).

In short: you combined a robust face‑tracking + 3D engine (MindAR + A‑Frame) with a flexible model + manual tuning + UX readiness to build a usable AR demo. That’s a fairly complete and practical base.

❓ Follow-up / Questions / Considerations

Anchor choice / face anchors: You used anchorIndex: 168. Does that reliably match a stable spot on all faces (e.g. forehead or top-of-head)? Anchor 168 might work well for some head shapes — but maybe not all. Is the hat always aligned correctly for different head sizes / angles? You might test with different anchor indices or even dynamically choose anchor depending on face orientation or size.

Performance & loading reliability: Right now you load a .glb model over HTTP via A-Frame asset system. That works, but on slower networks or low-end devices, loading delay might be noticeable. Also, if .glb fails to load (network error, path issue) — the face‑tracking will start but hat won’t appear. You might want fallback logic: e.g. show a simpler mesh, or delay face tracking until model loaded.

Runtime tuning & user experience: Keyboard-based manual tuning is good — but for non‑keyboard devices (mobile/touch) it won’t work. If you plan to support mobile or tablet, you might need touch/gesture controls (drag to adjust, scale pinch, etc.) or UI sliders, else hat placement may be hard/impossible.

Scalability / maintainability: As you add more AR overlays (other props, face filters, multiple targets) — mixing HTML + raw JS for controls + inline A‑Frame may get messy. At some point, refactoring into modular components or using a build setup (modular JS, config files, dynamic loading) might help.

Cross‑device / browser compatibility: Web‑AR + camera + face tracking can differ a lot across devices and browsers. Have you tested on different phones / operating systems / browsers to ensure hat tracking stays stable? Some browsers may have stricter camera-permission or WebGL constraints.

User-permissions & privacy: Since this opens camera and does face tracking, be mindful of permissions and privacy — ensure user consent, and handle cases where permission is denied gracefully.
Post-Processing: Trimesh is used to convert the raw mesh data into a standard, web-ready .glb file with vertex coloring.
Improvement Proposal
To improve visual fidelity (Shap-E models can be low-poly):

Texture Mapping: Implement a post-processing step where the original 2D image is projected onto the UV map of the generated mesh to increase texture resolution.
Refinement: Pass the initial Shap-E mesh into a Signed Distance Field (SDF) optimization loop to smooth out the surface noise.






4
6
456
4
6456




✅ AR Setup Code Review Checklist
Structure & Framework Use

✅ Are AR / 3D logic (tracking start, model placement, input/controls) encapsulated in meaningful modules/components instead of mixed directly in global HTML/inline scripts? For example: using A-Frame component‑style coding rather than a big single script blob. 
A-Frame
+1

✅ Is the asset loading handled through the appropriate asset‑management mechanism (<a-assets> or equivalent) so that the model and textures are preloaded before use? That helps prevent rendering glitches or 404s.

✅ Is there a clear separation between scene definition (HTML / entity markup) and interactive logic (keyboard-input, configuration, dynamic updates)? This makes maintenance easier and future features (e.g. multiple models / presets) simpler to add.

Performance & Rendering Efficiency

✅ Are you minimizing draw‑calls / heavy WebGL load? Check that you’re not creating too many separate meshes, lights, materials, or unnecessary objects. Merging static geometry and limiting lights helps. 
A-Frame
+1

✅ Are assets appropriately optimized — reasonable polycount, textures sized/powered‑of‑two / compressed / efficient for web use so that rendering is smooth, including on lower‑end devices. 
Mozilla Hacks – the Web developer blog
+1

✅ Are unnecessary updates / allocations avoided during rendering loops — e.g. avoid frequent DOM operations or memory-heavy JS operations in per‑frame loops to reduce garbage collection overhead. 
A-Frame
+1

Robustness & Error‑Handling

✅ Is there fallback or graceful handling if the model (e.g. .glb) fails to load? — e.g. showing an error / placeholder, rather than failing silently and leaving an empty scene.

✅ Are user permissions and device compatibility considered (camera permission prompts, WebGL support, mobile vs desktop, orientation)? AR needs camera + WebGL — there should be checks and fallback or messaging if unsupported.

✅ Is the code written in a maintainable and consistent style — e.g. consistent naming, separation of concerns, comments or documentation for non-obvious parts (like keyboard-to-transform logic), so another dev can follow and extend it easily.

User Experience & Controls

✅ Are controls intuitive and accessible — not just keyboard (good for desktop), but consider mobile/touch fallback if you expect usage on phones/tablets.

✅ Is there a clear UI/UX flow: initial load → start camera permission → face‑tracking start → model appears → user can adjust / reset — and appropriate feedback at each stage (loading spinner, error messages, instructions)?

✅ Are presets or default positions/rotations reasonably chosen so the model (hat) aligns roughly correctly “out of the box,” minimizing need for manual tweaking for most users.

Scalability & Extensibility

✅ Does architecture allow adding more models, props, or face‑tracking targets without major rewrites? (i.e. not hard‑coded to a single hat + anchor combination).

✅ Are configuration values (positions, scales, anchors) separated from hard‑coded logic — so different presets or model variations can be added easily.

✅ Is the code prepared for performance fallback or adaptive behavior — e.g. detect device performance and degrade visuals if necessary — to support a wider range of devices.
