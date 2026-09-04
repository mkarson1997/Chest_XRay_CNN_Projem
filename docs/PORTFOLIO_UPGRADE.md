# Chest X-Ray CNN Portfolio Upgrade Plan

This project demonstrates an end-to-end image-classification workflow. The next upgrades should emphasize reproducibility, evaluation quality, and responsible framing.

## Priority 1

- Add a reproducible training configuration and environment lockfile.
- Add precision, recall, F1 and ROC-AUC alongside accuracy.
- Add per-class error analysis and representative false-positive/false-negative examples.
- Explain the unusually small validation split and compare against a more robust split strategy.

## Priority 2

- Compare the baseline CNN with transfer-learning models such as MobileNetV2 or DenseNet.
- Add deterministic seed handling where practical.
- Add a lightweight inference script or notebook section for a single image.
- Add automated checks for notebook or Python code quality.

## Responsible-use standard

This repository is educational and experimental. Model outputs must not be presented as clinical diagnosis or medical advice.