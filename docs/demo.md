# Demo

This demo simulates an enterprise model registry review for promotion readiness.

Run:

```bash
python demo/run_demo.py
```

Expected behavior:

- Evaluates candidate models by accuracy, drift, and approval status
- Promotes only the model that satisfies metric and governance checks
- Demonstrates why MLOps is a lifecycle discipline, not just deployment automation