from __future__ import annotations

import csv
from pathlib import Path


def model_card_status(accuracy: float, drift_index: float, approved: bool) -> dict:
    ready = accuracy >= 0.82 and drift_index <= 0.15 and approved
    return {"ready_for_promotion": ready, "accuracy": accuracy, "drift_index": drift_index}


def load_model_cards(path: str | Path) -> list[dict]:
    with Path(path).open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    for row in rows:
        row["accuracy"] = float(row["accuracy"])
        row["drift_index"] = float(row["drift_index"])
        row["approved"] = row["approved"].lower() == "true"
    return rows


def promotion_candidates(rows: list[dict]) -> list[dict]:
    evaluated = [{**row, **model_card_status(row["accuracy"], row["drift_index"], row["approved"])} for row in rows]
    return sorted(evaluated, key=lambda row: (row["ready_for_promotion"], row["accuracy"]), reverse=True)