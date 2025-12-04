# 2D to 3D Model Generator

A simple script I threw together to convert 2D images into 3D `.glb` models using OpenAI's Shap-E. 

It runs locally. It's set up to force CPU usage on Macs to avoid the common "MPS float64" crashes that happen with PyTorch on Apple Silicon.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Project Structure

two-d-to-three-d/
├── gen_3d.py          
├── requirements.txt   
├── README.md          
└── input/             # source images here

# after cloning repo create and activate virtual environment
python3 -m venv venv
source venv/bin/activate
# on Windows use: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
#
python3 gen_3d.py --input "input/hat.jpeg" --output "output/hat.glb"

Flag	            Default	        Description
--input / -i	Required	        Path to the image you want to convert.
--output / -o	output/model.glb	Where to save the file.
--steps / -s	64	                Number of diffusion steps. Lower is faster. Higher is slower but better detail.

# example
python3 gen_3d.py -i input/image.png -s 8 


First Run: The first time it will be downloading about 2GB of models from OpenAI. It might take around 25 to 30 mins (to download the models) for the first time to run as it runs on CPU by default on Mac. This is normal and may take around 4 minutes per image for subsequent runs.

Mac Users: I've disabled GPU acceleration (MPS) in the script because Shap-E uses 64-bit floats that Apple's Metal shaders don't support yet. It runs on CPU

After generating a .glb file, it can viewed at [meshy.ai](https://www.meshy.ai/3d-tools/online-viewer/glb) or in macOS via spacebar in finder



# pip list 
Package             Version
------------------- -----------
asttokens           3.0.1
blobfile            3.1.0
certifi             2025.11.12
charset-normalizer  3.4.4
clip                1.0
comm                0.2.3
contourpy           1.3.0
cycler              0.12.1
decorator           5.2.1
exceptiongroup      1.3.1
executing           2.2.1
filelock            3.19.1
fire                0.7.1
fonttools           4.60.1
fsspec              2025.10.0
ftfy                6.3.1
humanize            4.13.0
idna                3.11
ImageIO             2.37.2
importlib_resources 6.5.2
ipython             8.18.1
ipywidgets          8.1.8
jedi                0.19.2
Jinja2              3.1.6
jupyterlab_widgets  3.0.16
kiwisolver          1.4.7
lazy_loader         0.4
lxml                6.0.2
MarkupSafe          3.0.3
matplotlib          3.9.4
matplotlib-inline   0.2.1
mpmath              1.3.0
networkx            3.2.1
numpy               1.26.4
packaging           25.0
parso               0.8.5
pexpect             4.9.0
pillow              11.3.0
pip                 21.2.4
prompt_toolkit      3.0.52
ptyprocess          0.7.0
pure_eval           0.2.3
pycryptodomex       3.23.0
Pygments            2.19.2
pyparsing           3.2.5
python-dateutil     2.9.0.post0
PyYAML              6.0.3
regex               2025.11.3
requests            2.32.5
scikit-image        0.24.0
scipy               1.13.1
setuptools          58.0.4
shap-e              0.0.0
six                 1.17.0
stack-data          0.6.3
sympy               1.14.0
termcolor           3.1.0
tifffile            2024.8.30
torch               2.8.0
torchvision         0.23.0
tqdm                4.67.1
traitlets           5.14.3
trimesh             4.10.0
typing_extensions   4.15.0
urllib3             2.5.0
wcwidth             0.2.14
widgetsnbextension  4.0.15
zipp                3.23.0