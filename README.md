# Chest X-Ray CNN Classification

An educational deep-learning project for binary chest X-ray image classification: `NORMAL` vs `PNEUMONIA`.

The repository demonstrates an end-to-end applied ML workflow including dataset preparation, CNN training, evaluation, metric visualization and confusion-matrix analysis.

> **Important:** This is a portfolio and educational project, not a medical diagnostic system. See [MODEL_CARD.md](MODEL_CARD.md) for limitations and intended use.

## Project summary

| Item | Value |
|---|---|
| Task | Binary image classification |
| Input size | `224 × 224` |
| Framework | TensorFlow / Keras |
| Optimizer | Adam |
| Learning rate | `0.001` |
| Loss | Binary Crossentropy |
| Recorded test accuracy | approximately `83.65%` |

## Dataset split

| Split | Images |
|---|---:|
| Train | 5,216 |
| Validation | 16 |
| Test | 624 |

The validation split is extremely small, so validation metrics should be interpreted cautiously. A larger stratified validation design would be required for stronger conclusions.

## Tech stack

- Python
- TensorFlow / Keras
- NumPy
- Matplotlib
- scikit-learn
- Google Colab

## Repository structure

```text
Chest_XRay_CNN_Projem/
├── notebook/
│   └── Chest_XRay_CNN_Projem.ipynb
├── docs/
│   ├── index.html
│   └── images/
│       ├── normal.png
│       ├── pneumonia.png
│       ├── accuracy.png
│       ├── loss.png
│       └── confusion_matrix.png
├── report.pdf
├── MODEL_CARD.md
└── README.md
```

## Workflow

```text
Chest X-ray dataset
        │
        ▼
Preprocessing / resize
        │
        ▼
CNN training
        │
        ▼
Validation monitoring
        │
        ▼
Test evaluation
        │
        ├── accuracy / loss curves
        └── confusion matrix
```

## Reproduce the experiment

Open the notebook in Google Colab:

https://colab.research.google.com/drive/1QvDpyKWrpE22qfl4iTTptSRBUgG38PCZ

The notebook contains the dataset-loading, model-definition, training and evaluation flow.

Dataset source:

https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia

## Evaluation notes

The recorded test accuracy is approximately `0.8365`.

Accuracy alone is not enough for a healthcare-related classification problem. A stronger evaluation should also report:

- precision,
- recall / sensitivity,
- specificity,
- F1 score,
- ROC-AUC,
- confidence intervals,
- calibration behavior.

The repository includes visual evaluation artifacts such as training curves and a confusion matrix.

## What this project demonstrates

- building and training a CNN with TensorFlow/Keras,
- preparing an image-classification workflow,
- tracking training and validation behavior,
- evaluating predictions with scikit-learn,
- communicating results through plots and a technical report,
- documenting model limitations responsibly.

## Limitations

- The validation set contains only 16 images.
- Results come from one public dataset and do not establish generalization to other hospitals or populations.
- The binary task simplifies real radiology interpretation substantially.
- The model has no clinical validation.

For the full statement, see [MODEL_CARD.md](MODEL_CARD.md).

## Roadmap

- Create a larger stratified validation split
- Add precision, recall, F1 and ROC-AUC reporting
- Add fixed random seeds and reproducibility metadata
- Compare transfer-learning baselines such as MobileNetV2, DenseNet and ResNet
- Add confidence intervals and calibration analysis
- Add an experiment configuration file
- Add lightweight automated notebook/data validation

## Links

- [GitHub Pages project page](https://mkarson1997.github.io/Chest_XRay_CNN_Projem/)
- [Colab notebook](https://colab.research.google.com/drive/1QvDpyKWrpE22qfl4iTTptSRBUgG38PCZ)
- [Dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)

---

Built by [Mahmoud Karzoun](https://github.com/mkarson1997).