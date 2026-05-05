
# Project Title: Clothing Review Sentiment Analysis

## Description

This project provides a comprehensive solution for sentiment analysis of clothing reviews, enabling businesses to understand customer feedback and identify key areas for improvement. It covers the entire machine learning pipeline from data preparation to model deployment and visualization.

### Key Components:

*   **Data Loading and Preprocessing**: Efficiently handles raw text data from customer reviews, including cleaning, tokenization, and vectorization, to prepare it for machine learning models.
*   **Custom Sentiment Model (Logistic Regression)**: Develops and trains a bespoke Logistic Regression model for multi-class sentiment classification (positive, neutral, negative), optimized for this specific dataset.
*   **Topic Extraction**: Utilizes techniques like Count Vectorization to identify and visualize common themes and issues discussed within negative customer reviews, offering actionable insights.
*   **Hugging Face Model Comparison**: Integrates and evaluates a pre-trained, state-of-the-art Hugging Face sentiment analysis model to compare its performance, strengths, and weaknesses against the custom-trained model.
*   **Visualizations**: Generates insightful plots and charts, including sentiment distribution bar charts, confusion matrices for model evaluation, and word clouds to highlight prevalent terms in reviews.
*   **Deployment (Streamlit Application)**: Includes a basic interactive Streamlit web application that allows users to input text and receive real-time sentiment predictions using a Hugging Face model, demonstrating practical deployment.

## Setup and Installation

To set up and run this project, you need to install the required Python packages. It is recommended to use a virtual environment.

```bash
pip install pandas scikit-learn matplotlib seaborn transformers wordcloud streamlit requests
```

## Usage

### Running the Notebook

Open the `sentiment_analysis.ipynb` file in Google Colab or Jupyter Notebook. Execute the cells sequentially to follow the entire analysis workflow, from data loading to model evaluation and visualization. Ensure all dependencies are installed prior to execution.

### Using the Streamlit App

The Streamlit application interacts with the Hugging Face Inference API for real-time sentiment analysis. To use it:

1.  **Obtain a Hugging Face API Token**: Generate your personal API token from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
2.  **Configure Token**: Replace `"YOUR_HF_TOKEN"` in the `app.py` (or the relevant cell in the notebook) with your actual Hugging Face API token. For secure deployment, consider using environment variables or Streamlit secrets.
3.  **Run the App**: Execute the Streamlit code. In Colab, you would typically need a tunneling service like `ngrok` to expose the local Streamlit server to the web. Run `streamlit run app.py` in your terminal.

## Data Source

The dataset used in this project is `Womens_Clothing_E-Commerce_Reviews.csv`. This CSV file contains various attributes related to customer reviews of women's clothing items, including `Review Text`, `Rating`, `Recommended IND`, `Division Name`, `Department Name`, and `Class Name`.

## Key Findings and Insights

*   **Sentiment Distribution**: The dataset exhibits a class imbalance, with a significantly higher number of positive reviews compared to neutral and negative ones. This was addressed during model training using `class_weight="balanced"`.
*   **Department-wise Sentiment**: Visualizations show how sentiment varies across different clothing departments, allowing for targeted improvements in specific product categories (e.g., identifying departments with higher negative feedback).
*   **Common Negative Themes**: Word cloud analysis and topic extraction from negative reviews revealed frequently mentioned terms like 'fabric', 'fit', 'size', and 'dress', indicating common pain points for customers.
*   **Model Comparison**: While the custom Logistic Regression model achieved a reasonable accuracy of ~77%, the Hugging Face model demonstrated superior performance and nuanced sentiment detection for certain edge cases, especially for neutral or mixed sentiment texts.

## Model Performance Details

### Custom Logistic Regression Model

*   **Accuracy**: Approximately 77% on the test set.
*   **Key Challenge**: The model struggled more with accurately classifying 'neutral' and 'negative' sentiments due to the inherent data imbalance and the subtle differences in language.
*   **Confusion Matrix**: Provides a detailed breakdown of correct and incorrect classifications, highlighting misclassifications between sentiment classes.

### Hugging Face Sentiment Analysis Model

*   **Performance**: Generally offers higher confidence scores and more precise sentiment detection, especially for complex or subtly nuanced reviews.
*   **Advantages**: Leverages advanced transformer architectures, making it robust across various text patterns.
*   **Disadvantages**: Requires external API calls or more computational resources if self-hosted, and may not always align perfectly with the specific sentiment definition (e.g., 3-star rating as neutral) used in the custom model.

## Explanations of Visualizations

*   **Sentiment Distribution Bar Chart**: This bar chart visually represents the number of reviews falling into 'negative', 'neutral', and 'positive' categories. It clearly illustrates the imbalanced nature of the dataset, with a large majority of reviews being positive.
*   **Sentiment Distribution by Department Name (Stacked Bar Chart)**: This chart breaks down the sentiment distribution within each `Department Name`. It allows us to quickly identify which departments receive more positive, neutral, or negative feedback, providing actionable insights for department-specific strategies.
*   **Word Cloud of Negative Reviews**: This visualization highlights the most frequently occurring words in the 'negative' review texts. Larger words in the cloud indicate higher frequency, helping to quickly grasp common complaints or issues expressed by dissatisfied customers (e.g., 'size', 'fabric', 'fit').
*   **Confusion Matrix**: The confusion matrix visually summarizes the performance of the classification model. It shows the number of true positive, true negative, false positive, and false negative predictions for each sentiment class, making it easy to identify where the model excels and where it makes errors.

## Project Structure

```
project-name/
│
├── app/
│   ├── app.py         # The Streamlit application's main entry point for sentiment analysis.
│   └── utils.py       # Helper functions used by the Streamlit app (e.g., text cleaning).
│
├── notebooks/
│   └── sentiment_analysis.ipynb # This Jupyter/Colab notebook containing the full analysis pipeline.
│
├── data/
│   └── Womens_Clothing_E-Commerce_Reviews.csv # The raw dataset used for the project.
│
├── requirements.txt   # Lists all Python package dependencies required to run the project.
└── README.md          # This file, providing an overview, setup, usage, and project details.
```

## License

This project is released under the [MIT License](https://opensource.org/licenses/MIT). You are free to use, modify, and distribute this software for both commercial and non-commercial purposes, provided you include the original copyright and license notice.

## Contact

For any questions, feedback, or collaborations, please feel free to reach out via GitHub issues or by contacting the maintainer at [your.email@example.com](mailto:your.email@example.com) or [Your GitHub Profile URL](https://github.com/your-username).
```
