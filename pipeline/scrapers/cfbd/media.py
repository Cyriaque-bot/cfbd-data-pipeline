import sys
from pathlib import Path



project_root = Path(__file__).resolve().parents[3]
sys.path.append(str(project_root))

from pipeline.loaders.cfbd.load_media import load_media


def fetch_media(): 
    return load_media()
