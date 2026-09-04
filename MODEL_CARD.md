# Model Card: Chest X-Ray CNN

## Model summary

This project trains a convolutional neural network to classify chest X-ray images into two labels:

- `NORMAL`
- `PNEUMONIA`

The model was created as an educational machine-learning project and is not a medical device.

## Intended use

Appropriate uses:

- learning image-classification workflows,
- experimenting with CNN architectures,
- studying model evaluation and confusion matrices,
- demonstrating an end-to-end ML portfolio project.

Not appropriate for:

- clinical diagnosis,
- treatment decisions,
- triage,
- replacing a qualified medical professional,
- deployment in a healthcare production environment without substantial validation and regulatory review.

## Dataset

The project uses the public Chest X-Ray Images (Pneumonia) dataset distributed through Kaggle.

Repository documentation records the following split sizes:

| Split | Images |
|---|---:|
| Train | 5,216 |
| Validation | 16 |
| Test | 624 |

Input images are resized to `224 × 224`.

## Training configuration

- Framework: TensorFlow / Keras
- Task: binary image classification
- Loss: Binary Crossentropy
- Optimizer: Adam
- Recorded learning rate: `0.001`

## Recorded evaluation

The project README records a test accuracy of approximately `0.8365`.

That single metric should not be treated as sufficient evidence of medical performance. Accuracy can hide class imbalance and different error costs, especially in healthcare-related datasets.

## Important limitations

### Very small validation split

The validation split contains only 16 images. That is too small for stable model-selection conclusions and can cause large swings in validation metrics.

### Dataset shift

Performance on one public dataset does not establish performance on images from different hospitals, scanners, patient populations or acquisition protocols.

### Binary framing

The task reduces chest X-rays to two labels and does not represent the complexity of real radiology interpretation.

### No clinical validation

The model has not been prospectively validated, independently audited or reviewed for clinical deployment.

## Recommended next steps

- Build a larger and stratified validation split
- Report precision, recall, F1 and ROC-AUC in addition to accuracy
- Add confidence intervals
- Compare against transfer-learning baselines such as MobileNet, DenseNet or ResNet
- Add calibration analysis
- Evaluate class imbalance explicitly
- Use patient-level splitting where metadata permits
- Add explainability experiments only as supplementary analysis, not as proof of clinical validity
- Add reproducible experiment tracking and fixed random seeds

## Ethical note

Machine-learning results involving medical images should be communicated conservatively. This repository is intended to demonstrate ML engineering skills, not medical capability.
