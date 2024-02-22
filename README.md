# End-to-End NLP Text Summarizer

This project is an End-to-End Text Summarization system utilizing the state-of-the-art model Pegasus, trained on custom data. Text summarization is a crucial task in natural language processing (NLP), aiming to condense lengthy documents or articles into concise summaries while preserving key information. Leveraging the power of Pegasus, this system automates the summarization process, making it efficient and effective.

## Dataset Overview
The project utilizes the SAMSum dataset, comprising approximately 16,000 messenger-like conversations accompanied by summaries. Linguists proficient in English crafted these conversations, simulating real-life interactions and covering a diverse range of topics. The conversations exhibit varied styles and registers, including informal, semi-formal, or formal tones, and may incorporate elements such as slang, emoticons, and typographical errors. Annotators then meticulously summarized these conversations, aiming to provide a succinct overview of the dialogue's content in the third person. The SAMSum dataset, developed by Samsung R&D Institute Poland, is made available for research purposes under a non-commercial license (CC BY-NC-ND 4.0), facilitating advancements in text summarization research.

## Workflow

1. **Update config.yaml**: Begin by updating the configuration file (`config.yaml`). This file holds various settings and parameters crucial for the functioning of the system. Ensure that the configurations align with your requirements and dataset specifications.

2. **Update params.yaml**: Next, update the parameters file (`params.yaml`). This file typically contains hyperparameters and other settings specific to the model and training process. Adjust these parameters as necessary based on your task and dataset characteristics.

3. **Update entity**: Update any relevant entity information. This step involves ensuring that the entities within your dataset or application are correctly represented and integrated into the system.

4. **Update the configuration manager in src config**: Update the configuration manager within the src directory. This manager handles the loading and management of configuration settings during runtime related to the data and model pipelines.

5. **Update the components**: Proceed to update various components of the system. These components include data ingestion, transformation, validation, model training, and evaluation classes. Ensure they are up-to-date and aligned with the project requirements.

6. **Update the pipeline**: This pipeline orchestrates the flow of data from training to prediction within the system, so it's crucial to keep it synchronized with the latest changes.

7. **Update main.py**: Update the main script (`main.py`) responsible for orchestrating the execution of the system. This script typically initializes the pipeline components, loads necessary resources, and logs the status as well. Update it according to any modifications or additions made to the project.

8. **Update app.py**: If applicable, update the Flask or FastAPI application script (`app.py`). This script initializes the web service or interface for interacting with the text summarization system. Ensure it reflects the latest changes and integrates seamlessly with the backend functionality.

# Installation and Run

## Steps:

1. **Clone the Repository**: Begin by cloning the project repository from GitHub using the provided URL:
    ```bash
    git clone https://github.com/sg13041995/NLP_TextSummarizer.git
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
