from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK = ROOT / "notebook" / "Chest_XRay_CNN_Projem.ipynb"

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "MODEL_CARD.md",
    ROOT / "EXPERIMENT_PROTOCOL.md",
    ROOT / "SECURITY.md",
    ROOT / "CONTRIBUTING.md",
    ROOT / "LICENSE",
    ROOT / "THIRD_PARTY_NOTICES.md",
    NOTEBOOK,
]


def fail(message: str) -> int:
    print(f"ERROR: {message}")
    return 1


def main() -> int:
    missing = [path.relative_to(ROOT) for path in REQUIRED_FILES if not path.exists()]
    if missing:
        return fail("missing required portfolio artifact(s): " + ", ".join(map(str, missing)))

    try:
        notebook = json.loads(NOTEBOOK.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return fail(f"notebook is not valid readable JSON: {exc}")

    nbformat = notebook.get("nbformat")
    cells = notebook.get("cells")
    if not isinstance(nbformat, int) or nbformat < 4:
        return fail(f"unexpected notebook format: {nbformat!r}")
    if not isinstance(cells, list) or not cells:
        return fail("notebook has no cells")

    code_cells = [cell for cell in cells if cell.get("cell_type") == "code"]
    markdown_cells = [cell for cell in cells if cell.get("cell_type") == "markdown"]
    if not code_cells:
        return fail("notebook has no code cells")
    if not markdown_cells:
        return fail("notebook has no markdown/documentation cells")

    print(
        "ML portfolio validation passed: "
        f"nbformat={nbformat}, cells={len(cells)}, "
        f"code={len(code_cells)}, markdown={len(markdown_cells)}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
