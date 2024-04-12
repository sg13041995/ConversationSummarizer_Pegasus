# TextSummarizer_Pegasus_Pipeline

This is a Text Summarization system that extracts insights from text data with an embedded end-to-end pipeline that eases the work of model fine-tuning. Powered by the cutting-edge Pegasus model pre-trained on the CNN / DailyMail Dataset, and meticulously fine-tuned on the SAMSum dataset, this system demonstrates efficiency and effectiveness in natural language processing (NLP).

In today's information-rich landscape, the ability to distil key points from lengthy conversations is paramount. This Text Summarization system tackles this challenge head-on, offering a seamless solution to condense sprawling dialogues into succinct summaries without compromising on essential details.

The system features an embedded pipeline that simplifies the fine-tuning process of the underlying model. This will make it convenient for the developers to fine-tune the system and make it adapt to their specific data and requirements.

## Dataset Overview

- **CNN / DailyMail:** The CNN / DailyMail Dataset is an English-language dataset containing just over 300k unique news articles as written by journalists at CNN and the Daily Mail. The current version supports both extractive and abstractive summarization, though the original version was created for machine reading and comprehension and abstractive question answering.

- **SAMSum:** The project utilizes the SAMSum dataset, comprising approximately 16,000 messenger-like conversations accompanied by summaries. Linguists proficient in English crafted these conversations, simulating real-life interactions and covering a diverse range of topics. The conversations exhibit varied styles and registers, including informal, semi-formal, or formal tones, and may incorporate elements such as slang, emoticons, and typographical errors. Annotators then meticulously summarized these conversations, aiming to provide a succinct overview of the dialogue's content in the third person. The SAMSum dataset, developed by Samsung R&D Institute Poland, is made available for research purposes under a non-commercial license (CC BY-NC-ND 4.0), facilitating advancements in text summarization research.

## Workflow

1. **Update config.yaml**

2. **Update params.yaml**

3. **Update entity**

4. **Update the configuration manager in src config**

5. **Update the components**

6. **Update the pipeline**

7. **Update main.py**

8. **Update app.py**

# Installation and Run

## Steps:

1. **Clone the Repository**: Begin by cloning the project repository from GitHub using the provided URL:
    ```bash
    https://github.com/sg13041995/ConversationSummarizer_Pegasus.git
    ```

2. **Create a Virtual Environment**: After navigating into the cloned repository directory, create a new virtual environment:
    ```bash
    python -m virtual_env_name env
    ```

3. **Activate the Environment**: Activate the newly created virtual environment:
    ```bash
    source virtual_env_name/Scripts/activate
    ```

4. **Install Requirements**: Install the required Python packages specified in the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

5. **Run the Application**: Finally, execute the main application script:
    ```bash
    python app.py
    ```

6. **Access the Application**: Once the application is running, access it through your local host and port.

# About the Author

**Name**: Subhankar Ghosh  
**Role**: Data Scientist | Trainer | Content Developer  
**Email**: subhankar.130495@gmail.com  

# Acknowledgments

- https://github.com/krishnaik06
- https://github.com/entbappy
- https://www.youtube.com/@krishnaik06
- https://www.youtube.com/@dswithbappy
- https://huggingface.co/datasets/samsum
- https://www.freecodecamp.org/
