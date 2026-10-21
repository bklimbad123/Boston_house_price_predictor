<!-- ABOUT THE PROJECT -->
## Project

Boston housing price prediction using regression algorithms.

### CSV Dataset Fields

The `boston_housing_prices.csv` file contains 13 input features and one target column, `prices`. Each row represents one Boston-area census tract in the dataset. The CSV headers use the original dataset abbreviations; the descriptions below explain what each column stores.

| CSV column | Detailed meaning | Units / interpretation |
| --- | --- | --- |
| `CRIM` | Per-capita crime rate by town. | Crime-rate measure; not a count of crimes for an individual property. |
| `ZN` | Proportion of residential land zoned for lots over 25,000 square feet. | Percentage-like proportion, conventionally recorded from 0 to 100. |
| `INDUS` | Proportion of non-retail business acres per town. | Percentage-like proportion, conventionally recorded from 0 to 100. |
| `CHAS` | Charles River boundary indicator. | Binary value: `1` if the tract borders the river, otherwise `0`. |
| `NOX` | Nitric oxides concentration. | Concentration in parts per 10 million. |
| `RM` | Average number of rooms per dwelling. | Rooms per dwelling; may be fractional. |
| `AGE` | Proportion of owner-occupied homes built before 1940. | Percentage from 0 to 100. |
| `DIS` | Weighted distance to five Boston employment centers. | Weighted distance index; larger values indicate greater distance. |
| `RAD` | Index of accessibility to radial highways. | Integer index from 1 to 24 in the original dataset. |
| `TAX` | Full-value property-tax rate per $10,000. | Tax rate per $10,000 of property value. |
| `PTRATIO` | Pupil-teacher ratio by town. | Number of pupils per teacher. |
| `B` | Transformed feature based on the proportion of Black residents, `Bk`: `1000 × (Bk - 0.63)²`. | Transformed numeric value, not a direct percentage. |
| `LSTAT` | Percentage of the population classified as lower status. | Percentage from 0 to 100. |
| `prices` | Median value of owner-occupied homes. | Thousands of dollars; for example, `24` represents $24,000. This is the prediction target, not an input feature. |

### Prediction Fields

Enter one numeric value for each field. The limits below are the input limits currently set in the web form; they describe accepted values, not typical values for every neighborhood.

| Form field | What it represents | Form input limits | Number format |
| --- | --- | --- | --- |
| Crime Rate (CRIM) | Per-capita crime rate by town. | 0 to 100 | Decimal or whole number |
| Zone (ZN) | Proportion of residential land zoned for lots over 25,000 square feet. | 0 to 100 | Decimal or whole number |
| Industries (INDUS) | Proportion of non-retail business acres per town. | 0 to 100 | Decimal or whole number |
| Charles River (CHAS) | Whether the tract borders the Charles River: 1 means yes; 0 means no. | 0 or 1 | Whole number only |
| Nitric Oxide Concentration (NOX) | Nitric oxides concentration, measured in parts per 10 million. | 0 to 1 | Decimal or whole number |
| Rooms (RM) | Average number of rooms per dwelling. | 0 to 20 | Decimal or whole number |
| Age (AGE) | Proportion of owner-occupied homes built before 1940, represented on a 0-to-100 scale in this form. | 0 to 100 | Decimal or whole number |
| Distance (DIS) | Weighted distance to five Boston employment centers. | 0 to 20 | Decimal or whole number |
| Highways (RAD) | Index of accessibility to radial highways. | 1 to 25 | Whole number only |
| Tax (TAX) | Full-value property-tax rate per $10,000. | 0 to 1,000 | Decimal or whole number |
| Teacher Ratio (PTRATIO) | Pupil-teacher ratio by town. | 0 to 40 | Decimal or whole number |
| African-American (B) | Transformed Black population feature, calculated as `1000 × (Bk - 0.63)²`, where `Bk` is the proportion of Black residents by town. This is a transformed feature, not a percentage to enter directly. | 0 to 500 | Decimal or whole number |
| Lower Status (LSTAT) | Percentage of the population classified as lower status. | 0 to 100 | Decimal or whole number |

The form requires all 13 fields. Use `0` or `1` for Charles River and a whole number from `1` to `25` for Highways; the other fields allow decimal values within their listed limits.

### Built With

* [Python](python)
* [Flask](flask)

<!-- GETTING STARTED -->
## Getting Started

Follow these steps to run the project locally.

### Prerequisites

- Python 3.10+
- pip
- Virtual environment (recommended)

### Installation

1. Open a terminal in the project folder.

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Start the Flask app:

```bash
python app.py
```

5. Open the app in your browser:

```text
http://127.0.0.1:5000/
```

### Run the app in production mode

```bash
gunicorn app:app
```
