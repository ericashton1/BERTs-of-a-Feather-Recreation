





# BERTs-of-a-Feather-Recreation

## Overview

This is a recreation of [McCoy et al.'s BERTs of a Feather Do Not Generalize Together](https://github.com/tommccoy1/hans/tree/master/berts_of_a_feather). The study shows how BERTs that only differ in fine-tuning weights and order of data seen vary greatly in accuracies when evaluated on out-of-distribution data.

## Steps and Files to Create

Gather data sets. Files to create:
.tsv file in format NLP can read for MNLI data sets
.tsv file in format NLP can read for HANS data sets

Fine-tune Pre-trained models. Files to create:
Fine-tuned models

Test 20 MNLI pre-trained models 100 times on MNLI Test data. Files to create:
Analyze files from running NLPScholar on MNLI data


Test 20 MNLI models 100 times on HANS heuristic data. Files to create:
Analyze files from running NLPScholar on HANS data


Compile, analyse, and reflect on results. Files to create:
Results data table
Writeup on results and process


## Models

The models folder contains 1 exmaple of the 20 models we used in our recreation of the McCoy et al. study. Each of the other models is identical to this BERT model that was fine-tuned on MNLI data except for their weights and the order in which they were exposed to MNLI premise/hypothesis pairs.

## Data Set Creation

dataset_creation_scripts.py is the python file used to create the .tsv files that can be found in the data folder.

## Data

This contains the .tsv files that were analyzed and evaluated by each of the models. One tsv file contains MNLI data and another HANS data. Each datset has a textid, premise, hypothesis, and target (entailment or non-entailment).

## Configs

The configs folder contains the config files used to analyze and evaluate the data using NLPScholar.

## MNLI Predictions

The MNLI_predictions folder contains the results from running evaluate on the MNLI data. Each predictions file corresponds with one of the 20 models.

## MNLI Results

The MNLI_results folder contains the results from running analyze on the MNLI data. Each results file corresponds with one of the 20 models.

## HANS Predictions

The HANS_predictions folder contains the results from running evaluate on the HANS data. Each predictions file corresponds with one of the 20 models.

## HANS Results

The HANS_results folder contains the results from running analyze on the HANS data. Each results file corresponds with one of the 20 models.






