# Sentiment Analysis Web Application

A web application built with **Python, Flask, and TextBlob** that analyzes user-entered text and classifies its sentiment as Positive, Negative, or Neutral. It displays polarity and subjectivity scores through a clean, responsive web interface.

## Features

- **Sentiment Classification:** Identifies text as Positive, Negative, or Neutral.
- **Polarity Score:** Measures sentiment from -1.0 (negative) to +1.0 (positive).
- **Subjectivity Score:** Measures subjectivity from 0.0 (objective) to 1.0 (subjective).
- **Interactive Web Interface:** Submit text and view analysis results.
- **Visual Score Indicators:** Displays polarity and subjectivity with visual progress indicators.
- **REST API:** Accepts JSON requests and returns sentiment results.
- **Input Validation:** Rejects empty, invalid, and excessively long text.
- **Automated Testing:** Includes unit tests for sentiment logic and Flask routes.
- **Responsive Design:** Built with HTML and CSS for desktop and mobile screens.

## Technologies Used

- Python
- Flask
- TextBlob
- HTML5
- CSS3
- unittest

## Project Structure

```text
sentiment-analysis-web/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   └── sentiment.py
├── templates/
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
└── tests/
    ├── test_app.py
    └── test_sentiment.py
```

The virtual environment (`venv/`) is created locally and excluded from version control.

## Getting Started

### Prerequisites

- Python 3.12 or newer, subject to dependency compatibility
- pip

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd sentiment-analysis-web
```

Replace the placeholder with your repository's actual URL.

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open the following address in your browser:

http://127.0.0.1:5000/

Enter a sentence or review, click **Analyze Sentiment**, and view the result.

## Example Results

| Input Text | Sentiment | Polarity | Subjectivity |
|---|---|---:|---:|
| I absolutely love this product! | Positive | 0.625 | 0.600 |
| This product is terrible and disappointing. | Negative | -0.800 | 0.850 |
| The meeting starts at 10 AM. | Neutral | 0.000 | 0.000 |

*Scores are examples produced by TextBlob for these specific sentences.*

## REST API

The application provides a JSON API endpoint for programmatic sentiment analysis.

### Endpoint

```http
POST /analyze
Content-Type: application/json
```

### Request

```json
{
  "text": "I absolutely love this product!"
}
```

### Example response

```json
{
  "sentiment": "Positive",
  "polarity": 0.625,
  "subjectivity": 0.6
}
```

### Test the API using PowerShell

```powershell
Invoke-RestMethod `
  -Uri "http://127.0.0.1:5000/analyze" `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"text":"I absolutely love this product!"}'
```

### Validation

The API returns an error response for invalid JSON structures, missing or empty text, unsupported content types, and text exceeding 5,000 characters.

## Running Tests

Run the complete test suite from the project root:

```bash
python -m unittest discover -s tests -v
```

The tests cover:

- Positive, negative, and neutral sentiment.
- Empty and invalid input.
- Result structure and score types.
- Flask homepage and API routes.
- HTML form submission.
- Unsupported content types.
- The 5,000-character input limit.

## How It Works

1. The user submits text through the web interface or API.
2. Flask validates the input.
3. TextBlob analyzes the text and calculates polarity and subjectivity.
4. The application classifies the polarity:
   - Polarity greater than zero: Positive
   - Polarity less than zero: Negative
   - Polarity equal to zero: Neutral
5. Flask returns JSON data or renders an HTML results page.

## Limitations

TextBlob provides lexicon-based sentiment analysis rather than a context-aware, fine-tuned transformer model. Results may be inaccurate for sarcasm, slang, ambiguous language, negation, and mixed sentiment.

The application classifies sentiment using the polarity score and does not measure prediction accuracy against a labeled dataset.

The Flask development server is intended for local development, not production deployment.

## Future Improvements

- Add sentiment history and downloadable reports.
- Add interactive score visualizations.
- Support batch sentiment analysis.
- Add multilingual sentiment analysis.
- Compare TextBlob with a machine-learning classifier or transformer model.
- Deploy the application using a production-ready web server.

## Learning Outcomes

This project demonstrates practical skills in Python, natural language processing, Flask web development, REST API design, input validation, automated testing, and frontend integration.

## License

This project is available under the MIT License if you choose to add an MIT `LICENSE` file to the repository.