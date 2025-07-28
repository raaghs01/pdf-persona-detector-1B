# PDF Intelligent Analyzer - Persona-Aware Document Processing

A sophisticated PDF analysis system that intelligently extracts and ranks relevant sections from PDF documents based on specific personas and tasks. This system uses semantic similarity and machine learning to provide personalized document insights.

## 🎯 Project Overview

The PDF Intelligent Analyzer is designed to process collections of PDF documents and extract the most relevant sections based on:
- **Persona**: The role/perspective of the user (e.g., Travel Planner, Student, Professional)
- **Job-to-be-done**: The specific task or goal the user wants to accomplish
- **Document Context**: The semantic content and structure of the PDFs

The system automatically processes multiple PDF collections and generates structured outputs with ranked sections and detailed analysis.

## 🏗️ Architecture

### Core Components

1. **Pipeline (`pipeline.py`)**: Main orchestration module that coordinates the entire analysis process
2. **Parser (`parser.py`)**: Extracts sections and headings from PDF documents using PyPDF2
3. **Retriever (`retriever.py`)**: Uses sentence transformers to find semantically relevant sections
4. **Scorer (`scorer.py`)**: Extracts detailed text content from identified sections
5. **ML Classifier (`ml_classifier.py`)**: Advanced heading classification using machine learning
6. **Utils (`utils.py`)**: Helper functions for text processing and utilities

### Data Flow

```
Input JSON → PDF Processing → Section Extraction → Semantic Ranking → Content Analysis → Output JSON
```

## 📁 Project Structure

```
pdf-intelligent-analyzer-persona-aware/
├── Collection_1/                    # Travel planning use case
│   ├── challenge1b_input.json      # Input configuration
│   ├── challenge1b_output.json     # Generated results
│   └── PDFs/                       # PDF documents
├── Collection_2/                    # Adobe Acrobat learning
│   ├── challenge1b_input.json
│   ├── challenge1b_output.json
│   └── PDFs/
├── Collection_3/                    # Recipe collection
│   ├── challenge1b_input.json
│   ├── challenge1b_output.json
│   └── PDFs/
├── data/
│   └── heading_training_data_final_corrected.csv  # Training data for ML classifier
├── pipeline.py                      # Main orchestration script
├── parser.py                        # PDF parsing and section extraction
├── retriever.py                     # Semantic similarity and ranking
├── scorer.py                        # Content extraction and analysis
├── ml_classifier.py                 # ML-based heading classification
├── utils.py                         # Utility functions
├── requirements.txt                 # Python dependencies
├── pyproject.toml                  # Project configuration
└── README.md                       # This file
```

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- pip or uv package manager

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd pdf-intelligent-analyzer-persona-aware
   ```

2. **Install dependencies:**
   ```bash
   # Using pip
   pip install -r requirements.txt
   
   # Or using uv (recommended)
   uv sync
   ```

3. **Fix TensorFlow compatibility issue (if needed):**
   ```bash
   # Add this to the top of pipeline.py and retriever.py
   import os
   os.environ["USE_TF"] = "0"
   
   # Or uninstall TensorFlow if not needed
   pip uninstall tensorflow tensorflow-cpu tensorflow-gpu -y
   ```

### Usage

1. **Run the pipeline on all collections:**
   ```bash
   python pipeline.py
   ```

2. **Process a specific collection:**
   ```python
   from pipeline import run_pipeline
   run_pipeline("Collection_1")
   ```

## 📊 Input Format

Each collection requires a `challenge1b_input.json` file with the following structure:

```json
{
    "challenge_info": {
        "challenge_id": "round_1b_002",
        "test_case_name": "travel_planner",
        "description": "France Travel"
    },
    "documents": [
        {
            "filename": "document1.pdf",
            "title": "Document Title"
        }
    ],
    "persona": {
        "role": "Travel Planner"
    },
    "job_to_be_done": {
        "task": "Plan a trip of 4 days for a group of 10 college friends."
    }
}
```

## 📈 Output Format

The system generates a `challenge1b_output.json` file with:

```json
{
    "metadata": {
        "input_documents": ["document1.pdf", "document2.pdf"],
        "persona": "Travel Planner",
        "job_to_be_done": "Plan a trip of 4 days...",
        "processing_timestamp": "2025-07-28T14:33:38.397549"
    },
    "extracted_sections": [
        {
            "document": "document1.pdf",
            "section_title": "Travel Tips",
            "importance_rank": 1,
            "page_number": 2
        }
    ],
    "subsection_analysis": [
        {
            "document": "document1.pdf",
            "refined_text": "Detailed content from the section...",
            "page_number": 2
        }
    ]
}
```

## 🔧 Technical Details

### Dependencies

- **PyMuPDF (fitz)**: Advanced PDF processing and text extraction
- **sentence-transformers**: Semantic similarity and embeddings
- **PyPDF2**: Basic PDF text extraction
- **pandas**: Data manipulation for ML classifier
- **joblib**: Model serialization
- **torch**: PyTorch for deep learning models

### Key Features

1. **Semantic Similarity**: Uses the `all-MiniLM-L6-v2` model for finding relevant sections
2. **Multi-level Processing**: Combines basic parsing with ML-based classification
3. **Persona-aware Ranking**: Ranks sections based on persona-task combinations
4. **Batch Processing**: Automatically processes multiple collections
5. **Structured Output**: Generates JSON with metadata and analysis

### ML Classifier

The `MLHeadingClassifier` provides advanced heading detection:
- Extracts font information, positioning, and text features
- Uses trained model to classify heading levels (H1, H2, H3, etc.)
- Merges adjacent lines and handles complex document structures
- Generates document outlines with hierarchical structure

## 📋 Use Cases

### 1. Travel Planning (Collection_1)
- **Persona**: Travel Planner
- **Task**: Plan a 4-day trip for 10 college friends
- **Documents**: 7 PDFs covering cities, cuisine, history, hotels, activities, tips, and culture

### 2. Software Learning (Collection_2)
- **Persona**: Software Learner
- **Task**: Learn Adobe Acrobat features
- **Documents**: 15 PDFs covering various Acrobat functionalities

### 3. Recipe Collection (Collection_3)
- **Persona**: Home Chef
- **Task**: Find meal ideas
- **Documents**: 9 PDFs with breakfast, lunch, and dinner recipes

## 🛠️ Development

### Adding New Collections

1. Create a new folder (e.g., `Collection_4/`)
2. Add PDF documents to `Collection_4/PDFs/`
3. Create `challenge1b_input.json` with appropriate persona and task
4. Run the pipeline to generate output

### Customizing the Pipeline

- **Modify ranking**: Adjust the `top_k` parameter in `retriever.py`
- **Change model**: Replace `all-MiniLM-L6-v2` with other sentence transformer models
- **Add preprocessing**: Extend `parser.py` with custom text cleaning
- **Enhance scoring**: Modify `scorer.py` for different content extraction strategies



## 🐛 Troubleshooting

### Common Issues

1. **TensorFlow DLL Error**:
   ```python
   # Add to the top of affected files
   import os
   os.environ["USE_TF"] = "0"
   ```

2. **Memory Issues**: Reduce `top_k` parameter or process smaller batches

3. **PDF Parsing Errors**: Ensure PDFs are not password-protected or corrupted

4. **Model Download Issues**: Check internet connection for sentence transformer model downloads

### Performance Optimization

- Use GPU acceleration for sentence transformers when available
- Process large PDF collections in batches
- Consider caching embeddings for repeated queries


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request


