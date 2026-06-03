from src.mlops_blueprint.main import model_card_status


def test_model_requires_approval():
    assert model_card_status(0.9, 0.05, False)["ready_for_promotion"] is False


def test_model_ready_when_metrics_and_approval_pass():
    assert model_card_status(0.86, 0.08, True)["ready_for_promotion"] is True