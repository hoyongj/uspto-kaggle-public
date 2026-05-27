# USPTO Patent Data Pipeline & Search Optimization

A data engineering and NLP pipeline built to process, index, and analyze over 13 million patent records from the USPTO dataset. The goal of the project was to efficiently extract textual features and integrate them with search indexing tools to retrieve relevant patent neighbors.

## Core Pipeline & Engineering

This repository highlights the data wrangling, feature extraction, and pipeline assembly required to handle massive text datasets on local compute without out-of-memory (OOM) failures.

### 1. Large-Scale Data Handling
- Processed a massive dataset of patent metadata (over 13 million rows, 130GB+ scale).
- Leveraged `Polars` and `Dask` distributed dataframes for high-performance, parallelized data aggregation and filtering, ensuring the pipeline ran efficiently under memory constraints.

### 2. Feature Extraction (TF-IDF)
- Built an NLP pipeline using `scikit-learn` to process unstructured text data (Patent Titles, Abstracts, and CPC classifications).
- Converted millions of text corpus rows into highly dimensional **TF-IDF sparse matrices**, filtering down the terminology space to surface the most relevant key features.

### 3. Search Engine Integration
- Integrated the processed data with **Whoosh**, a localized Python search engine library.
- Built automated scripts to inject our extracted features into the inverted index, allowing for rapid retrieval and neighbor testing.

## Technical Stack
- **Data Engineering:** Python, Polars, Pandas, Numpy
- **NLP & Machine Learning:** Scikit-learn (TF-IDF, Sparse Matrices)
- **Search Infrastructure:** Whoosh
