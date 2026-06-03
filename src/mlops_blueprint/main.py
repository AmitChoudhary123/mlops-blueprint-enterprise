def model_card_status(accuracy: float, drift_index: float, approved: bool) -> dict:
    """Evaluate whether a model is ready for controlled promotion."""
    ready = accuracy >= 0.82 and drift_index <= 0.15 and approved
    return {"ready_for_promotion": ready, "accuracy": accuracy, "drift_index": drift_index}