from pathlib import Path
from src.mlops_blueprint.main import load_model_cards, promotion_candidates

if __name__ == "__main__":
    for model in promotion_candidates(load_model_cards(Path("data/model_registry.csv"))):
        print(f"{model['model_id']} | ready={model['ready_for_promotion']} | accuracy={model['accuracy']} | drift={model['drift_index']} | approved={model['approved']}")