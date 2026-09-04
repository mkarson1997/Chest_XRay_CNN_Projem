# Experiment Protocol

This document defines the reproducibility standard for future Chest X-Ray CNN experiments. It does not replace the existing notebook results; it specifies what new runs should record before results are compared.

## 1. Data provenance

Record:

- dataset name and source URL,
- dataset version/date when available,
- number of images per class,
- whether splitting is image-level or patient-level,
- any excluded/corrupt images and the reason.

Patient-level splitting should be preferred when metadata makes it possible because images from the same patient appearing across splits can inflate evaluation estimates.

## 2. Deterministic split

A new experiment should define a reproducible train/validation/test split with:

- fixed random seed,
- stratification by class where appropriate,
- a validation set large enough to support model-selection decisions,
- no tuning against the final test set.

The currently documented 16-image validation set is retained as historical experiment context, not as the target protocol for future comparisons.

## 3. Preprocessing

Record exactly:

- input size,
- color-channel handling,
- normalization/scaling,
- augmentation operations and probabilities,
- any class weighting or resampling.

## 4. Training configuration

Record:

- model architecture,
- initialization/pretrained weights,
- optimizer,
- learning rate and scheduler,
- loss function,
- batch size,
- number of epochs,
- early stopping criteria,
- checkpoint-selection rule,
- random seeds,
- TensorFlow/Keras and Python versions.

## 5. Required evaluation

At minimum report:

- confusion matrix,
- accuracy,
- precision,
- recall/sensitivity,
- F1 score,
- ROC-AUC when probabilities are available,
- selected decision threshold.

Where practical, also report:

- specificity,
- PR-AUC,
- confidence intervals,
- calibration metrics/plots.

## 6. Baselines

Compare the custom CNN against at least:

1. a simple baseline,
2. a transfer-learning model such as MobileNetV2, DenseNet or ResNet.

The purpose is not to maximize one headline number but to show whether architectural complexity produces a reproducible improvement.

## 7. Result table template

| Run | Model | Seed | Val design | Accuracy | Precision | Recall | F1 | ROC-AUC | Notes |
|---|---|---:|---|---:|---:|---:|---:|---:|---|
| baseline-001 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | |
| cnn-001 | custom CNN | TBD | TBD | TBD | TBD | TBD | TBD | TBD | |
| transfer-001 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | |

## 8. Responsible interpretation

Results apply only to the documented experimental setup and dataset. They must not be described as clinical diagnostic performance or evidence of deployment readiness.

See [MODEL_CARD.md](MODEL_CARD.md) for intended use and limitations.
