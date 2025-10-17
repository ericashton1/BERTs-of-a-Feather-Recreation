# HANS Predictions

This directory contains the prediction files for all 20 BERT models evaluated on the HANS dataset.

## File Format

Each `bertXX_hans_predictions.tsv` file contains:
- `textid`: Unique identifier for each example
- `target`: Ground truth label (entailment or non-entailment)
- `model`: Model path used for prediction
- `tokenizer`: Tokenizer used
- `predicted`: Model's predicted label
- `prob`: Probability of the predicted label

## Models

Models `bert_00` through `bert_19` are BERT-base models fine-tuned on MNLI, differing only in:
1. Random initialization of the classification head
2. Order of training examples

All models used identical pre-trained BERT weights and training hyperparameters.
