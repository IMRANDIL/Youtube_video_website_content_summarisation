

# 🐦 LangChain Summarization App

This Streamlit app leverages the power of **LangChain** and **Groq API** to summarize text content from YouTube videos or websites. It generates concise summaries based on the provided URL, creating a structured and easy-to-read summary with key points.


![Screenshot 2024-10-19 065341](https://github.com/user-attachments/assets/0004042b-870e-430a-98b1-0e4af76d2851)

## Features
- Summarize content from YouTube videos and websites.
- Outputs a 300-word summary with a well-structured title and numbered key points.
- Uses LangChain's **ChatGroq** model for summarization.
- Supports user-provided Groq API key for text processing.
- Streamlit-based web app interface with a clean and simple layout.

## Prerequisites

To run this project, you'll need to have the following installed:

- Python 3.8 or later
- Groq API key (You can obtain this by signing up for Groq)
- The following Python packages:
  - `langchain`
  - `langchain_groq`
  - `streamlit`
  - `validators`
  - `langchain_community`

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/IMRANDIL/Youtube_video_website_content_summarisation.git
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter your **Groq API Key** in the sidebar.
2. Provide a valid **YouTube video URL** or a **website URL** in the input box.
3. Click on **"Summarize the Content from YT or Website"** to get a summary of the content.

   - If the URL is a valid YouTube video or a website, the app will extract the text and summarize it.
   - The summary will be displayed in 300 words with key points listed in numbers.

## Example Workflow

1. Input the Groq API key and URL of the website or YouTube video you want summarized.
2. After clicking the button, the app will display the summary:
   - Title of the summary
   - Key points in a numbered format

## Error Handling

- If you enter an invalid URL, the app will display an error message requesting a valid URL.
- The app also handles general exceptions and will notify users if something goes wrong during processing.

## Contributing

Feel free to fork the repository, create a new branch, and submit pull requests. Any feedback or contribution is appreciated.


