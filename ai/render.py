"""Render an overview SVG from the semantic Graphviz diagram.

Requires Graphviz `dot`. Authoritative editable UML source: diagram.puml.
Usage: python ai/render.py
"""
from pathlib import Path
import shutil
import subprocess

root = Path(__file__).resolve().parents[1]
if not shutil.which("dot"):
    raise SystemExit("Graphviz 'dot' not found. Use diagram.puml with PlantUML.")
subprocess.run(["dot", "-Tsvg", "-o", str(root / "diagram.svg"), str(root / "diagram.dot")], check=True)
print("diagram.svg generated from diagram.dot (PlantUML source remains diagram.puml)")
