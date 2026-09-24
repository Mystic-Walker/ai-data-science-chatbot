# AI Data Science Staff Assistant

An AI-powered Data Science chatbot built with **Google Gemini API, Python, and Streamlit**.

The application acts as a Data Science Staff Assistant capable of answering technical questions, generating Python and SQL code, explaining concepts, providing step-by-step solutions, and maintaining conversation context.

## Features

* Google Gemini API integration
* Data Science Staff Engineer persona
* Natural-language conversation
* Conversation context and multi-turn interaction
* Python and SQL code generation
* Step-by-step technical explanations
* Data Science and Machine Learning guidance
* Configurable temperature
* API error handling
* Simple Streamlit chat interface
* Clear conversation functionality

## Technology Stack

* **Python**
* **Google Gemini API**
* **Google Gen AI Python SDK**
* **Streamlit**
* **python-dotenv**

## Supported Topics

The assistant is designed to help with:

* Python
* SQL
* Statistics
* Data Analysis
* Machine Learning
* Deep Learning
* Generative AI
* Large Language Models (LLMs)
* Data Visualization
* Model Evaluation
* Debugging
* Code Explanation

## Project Structure

```text
ai-data-science-chatbot/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env                # Gemini API key (not committed)
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd ai-data-science-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

The API key is loaded using `python-dotenv` and is not stored directly in the source code.

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in the browser.

## Configuration

The application uses the Gemini model:

```text
gemini-3.5-flash-lite
```

The temperature can be configured using the sidebar slider.

### Temperature

Lower temperature values generally produce more focused and consistent responses.

Higher temperature values allow greater variation in generated responses.

This allows the effect of the generation parameter to be demonstrated directly through the application.

## System Persona

The chatbot uses a system instruction that defines it as an experienced **Data Science Staff Engineer**.

The system instruction guides the assistant to:

* Provide technically accurate answers
* Explain concepts clearly
* Generate Python and SQL code
* Explain generated code
* Provide step-by-step solutions
* Suggest appropriate Data Science approaches
* Help debug Python, SQL, and Machine Learning problems
* Ask for clarification when requirements are unclear
* Maintain conversation context
* Respond professionally

## Conversation Context

Conversation messages are maintained using Streamlit session state.

Previous user and assistant messages are included when generating a new response, allowing the assistant to maintain context across multiple turns.

For example:

```text
User: What is overfitting?

Assistant: [Explanation of overfitting]

User: How can I prevent it?

Assistant: [Explanation of overfitting prevention]
```

The second question can be interpreted using the context of the previous conversation.

## API Error Handling

The application handles common API failures, including:

* Missing API key
* Authentication errors
* Rate-limit errors
* Temporary Gemini service unavailability
* Empty responses
* Other unexpected API errors

User-friendly error messages are displayed in the Streamlit interface instead of allowing the application to fail silently.

## Assignment Requirement Mapping

| Requirement                         | Implementation                                             |
| ----------------------------------- | ---------------------------------------------------------- |
| Gemini API integration              | Google Gen AI Python SDK                                   |
| API key configuration               | `.env` + `python-dotenv`                                   |
| Send prompts to Gemini              | `client.models.generate_content()`                         |
| Display Gemini response             | Streamlit chat interface                                   |
| API error handling                  | Exception handling with user-friendly messages             |
| Gemini LLM                          | `gemini-3.5-flash-lite`                                    |
| Configurable temperature            | Streamlit temperature slider                               |
| Temperature demonstration           | Same prompts can be tested at different temperature values |
| Data Science Staff persona          | System instruction in `app.py`                             |
| Python expertise                    | Included in system instruction                             |
| SQL expertise                       | Included in system instruction                             |
| Statistics                          | Included in system instruction                             |
| Data Analysis                       | Included in system instruction                             |
| Machine Learning                    | Included in system instruction                             |
| Deep Learning                       | Included in system instruction                             |
| Generative AI                       | Included in system instruction                             |
| LLM concepts                        | Included in system instruction                             |
| Visualization                       | Included in system instruction                             |
| Model evaluation                    | Included in system instruction                             |
| Debugging                           | Included in system instruction                             |
| Code explanation                    | Included in system instruction                             |
| Natural-language understanding      | Gemini LLM                                                 |
| Python/SQL generation               | System instruction + Gemini                                |
| Step-by-step solutions              | System instruction                                         |
| Approach suggestions                | System instruction                                         |
| Clarification for unclear questions | System instruction                                         |
| Conversation context                | Streamlit session state                                    |

## Example Questions

The chatbot can be tested with questions such as:

```text
What is overfitting in machine learning?

What is the difference between precision and recall?

Write Python code to calculate F1 score using sklearn.

How should I handle missing values in a dataset?

Explain the difference between bagging and boosting.

Write a SQL query to find the second highest salary.

How would you evaluate a classification model?

Why might my Random Forest model be overfitting?

Explain ROC-AUC with an example.
```

## Security

The Gemini API key is stored in `.env` and excluded from version control through `.gitignore`.

The `.env` file should never be committed to GitHub.

## Future Improvements

Potential future improvements include:

* Streaming responses
* Conversation export
* File/data upload for Data Science analysis
* Data visualization generation
* Model selection
* Persistent conversation history
* Authentication
* Deployment to a cloud platform
