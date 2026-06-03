from pathlib import Path
from src.mlops_blueprint.main import load_model_cards, model_card_status, promotion_candidates


def test_promotion_demo_selects_ready_model():
    ranked = promotion_candidates(load_model_cards(Path("data/model_registry.csv")))
    assert ranked[0]["ready_for_promotion"] is True
    assert ranked[0]["model_id"] == "churn-v2"


def test_model_requires_approval():
    assert model_card_status(0.9, 0.05, False)["ready_for_promotion"] is False