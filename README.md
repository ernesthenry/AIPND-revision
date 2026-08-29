# AIPND-revision: Image Classification for a City Dog Show

**Author / Programmer:** Kato Ernest Henry  
**Date Created:** August 29, 2026  
**Revised Date:** August 29, 2026  
**Program:** AI Programming with Python Nanodegree

---

## Project Overview

This project uses pretrained Deep Learning Convolutional Neural Networks (CNNs) to identify dog breeds and differentiate between dogs and non-dog animals/objects for a citywide dog show contestant registration system.

The project evaluates and compares three CNN architectures:
1. **ResNet-18**
2. **AlexNet**
3. **VGG-16**

---

## Principal Objectives

1. **Dog Identification:** Correctly identify which pet images are of dogs (even if the breed is misclassified) and which are not dogs.
2. **Breed Classification:** Correctly classify the breed of dog for the images that are dogs.
3. **Architecture Comparison:** Determine which CNN model architecture (ResNet, AlexNet, or VGG) best achieves objectives 1 and 2.
4. **Computational Efficiency:** Measure the execution runtime and compare the accuracy-to-time trade-offs across all three architectures.

---

## Key Tasks & Implementations

- **Task 0: Timing Code (`check_images.py`)**  
  Measures total program execution runtime using Python's `time` module and formats elapsed time in `hh:mm:ss`.

- **Task 1: Command Line Arguments (`get_input_args.py`)**  
  Implements `argparse` to accept `--dir` (image folder), `--arch` (CNN model architecture: `vgg`, `resnet`, `alexnet`), and `--dogfile` (text file of dog names).

- **Task 2: Pet Image Labels (`get_pet_labels.py`)**  
  Extracts ground-truth pet labels from image filenames, cleans and formats them into lowercase whitespace-stripped strings, and stores them in `results_dic`.

- **Task 3: Classifier Labels (`classify_images.py`)**  
  Uses pretrained PyTorch CNN models (`classifier.py`) to classify images and compares classifier labels against true pet labels.

- **Task 4: Classifying as Dogs (`adjust_results4_isadog.py`)**  
  Matches labels against `dognames.txt` to determine if images are dogs or non-dogs.

- **Task 5: Calculating Results (`calculates_results_stats.py`)**  
  Computes summary counts (`n_images`, `n_dogs_img`, `n_notdogs_img`, `n_correct_dogs`, `n_correct_notdogs`, `n_correct_breed`) and percentage metrics (`pct_match`, `pct_correct_dogs`, `pct_correct_breed`, `pct_correct_notdogs`).

- **Task 6: Printing Results (`print_results.py`)**  
  Formats and prints summary statistics, model performance percentages, and optionally prints misclassified dogs and misclassified breeds.

---

## How to Run

### Single Model Run:
```bash
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
```

### Batch Processing for All 3 Models:
```bash
sh run_models_batch.sh
```

---

## Summary of Results

- **VGG-16** achieved the best overall performance with **100% accuracy** on distinguishing dogs from non-dogs and **~93.3% accuracy** on dog breed classification.
- **AlexNet** achieved 100% accuracy on dog detection and lower runtime, but lower breed accuracy (~80%).
- **ResNet** provided fast inference and high breed accuracy (~90%), with ~90% accuracy on dog detection.
