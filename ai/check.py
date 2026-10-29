"""Basic consistency check for the library UC lab. Run from any working directory."""
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
spec = (root / "spec.md").read_text(encoding="utf-8")
plant = (root / "diagram.puml").read_text(encoding="utf-8")
ai = (root / "ai/prompt.md").read_text(encoding="utf-8")
for name in ["Book", "Author", "Copy", "Member", "Loan"]:
    assert name in spec, f"Missing entity {name}"
for i in range(1, 17):
    assert len(re.findall(rf'\| FR-{i:02d} \|', spec)) == 2, f"FR-{i:02d} should occur in requirement+matrix tables"
for i in range(1,9):
    assert len(re.findall(rf'\*\*S-{i:02d}\.',spec)) == 1, f"Missing scenario S-{i:02d}"
for i in range(1,9):
    assert len(re.findall(rf'^\| S-{i:02d} \|',spec, re.M)) == 1, f"Missing reverse trace S-{i:02d}"
for i in range(1,11):
    assert f'UC-{i:02d}' in spec
assert '<<include>>' in plant and '<<extend>>' in plant and '--|>' in plant
assert "# Приклад правильної взаємодії студента з AI під час ЛР2" in ai
assert not re.search(r'Warehouse|Supplier|Movement|Stock|складськ', spec + '\n' + ai, flags=re.I)
for filename in ["DEFENSE.md","README.md","diagram.puml","diagram.svg","ai/audit.md"]:
    assert (root/filename).exists(), filename
print("OK: library entities, 16 FR, 8 Gherkin, 8 reverse-trace rows, 10 UC and no warehouse entities")
