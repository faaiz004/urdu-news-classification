# Urdu News Classification

A machine learning project at LUMS that classifies Urdu news articles into five categories using Multinomial Naive Bayes, a neural network, and K-Nearest Neighbors. The project covers data collection, Urdu text preprocessing, feature extraction, model training, and evaluation.

## Dataset

The dataset contains **1,119 Urdu news articles** across five categories:

- Business
- Entertainment
- Science and Technology
- Sports
- World

Articles were collected from Geo, Jang, Express, Samaa, Dunya, and Dawn. Website categories were mapped to a common label set, with article titles, content, source links, and labels stored in CSV files.

Preprocessing includes Urdu stopword removal and punctuation cleaning. Bag-of-Words vocabularies are built from the training data.

## Models

### Multinomial Naive Bayes

- Custom NumPy implementation.
- Bag-of-Words features extracted from article content.
- Laplace smoothing and log-probability calculations.

### Neural Network

- PyTorch feedforward classifier.
- Separate Bag-of-Words representations for titles and content, concatenated into a single input.
- Two hidden layers with **1,024** and **512** units.
- LeakyReLU activations, cross-entropy loss, and Adam optimization.
- Mini-batch training with CUDA support when available.

### K-Nearest Neighbors

- Custom implementation with Euclidean and Manhattan distance functions.
- Evaluated using Euclidean distance with **k = 4**.
- Bag-of-Words features extracted from article content.
- Includes a cross-validation implementation.

## Results

Results reported in the project report using an **80/20 train/test split**:

| Model | Accuracy |
|-------|---------:|
| Multinomial Naive Bayes | 96.43% |
| Neural Network | **97.32%** |
| K-Nearest Neighbors | 78.57% |

The notebooks also include precision, recall, F1 scores, confusion matrices, and a neural network training-loss plot.

## Repository Structure

| Directory / File | Description |
|------------------|-------------|
| `Model1_Multinomial Naive Bayes Classifier/` | Naive Bayes notebook, dataset, and Urdu stopwords |
| `Model2_Neural Network/` | Neural network notebook and dataset |
| `Model3_KNN/` | KNN notebook, dataset, and Urdu stopwords |
| `Web-Scraping and Data Pre-Processing/` | Scraping notebook and preprocessing scripts |
| `Group 10 Report.pdf` | Project methodology, results, and analysis |

## Getting Started

### Install Dependencies

```bash
python -m venv .venv
source .venv/bin/activate
pip install numpy pandas matplotlib seaborn scikit-learn torch jupyter requests beautifulsoup4
```

On Windows, activate the environment using:

```powershell
.venv\Scripts\activate
```

### Run the Notebooks

```bash
jupyter notebook
```

Open the desired notebook inside its model directory and run the cells in order. Keep the dataset and stopword files alongside their corresponding notebooks so relative paths resolve correctly.

The included CSV files allow the models to run without repeating the scraping process.

## Contributions

| Contributor | Contribution |
|-------------|--------------|
| Hamza Malik | Data scraping and initial preprocessing |
| Maaz Kashif | Data preprocessing and Multinomial Naive Bayes implementation |
| **Faaiz Umer** | **Data preprocessing and neural network implementation** |
| Hamza Bin Mubeen | Data preprocessing and KNN implementation |
| Ahsan Usman | Final analysis and documentation |

## Technologies

Python · NumPy · pandas · PyTorch · scikit-learn · Matplotlib · Seaborn · Beautiful Soup · Jupyter