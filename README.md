# Welcome to the JP Morgan Digital Transformation Assistance System

This application leverages large language models and Retrieval-Augmented Generation (RAG) to provide guidance on digital transformation.

## Setup Instructions

1. **Clone the Project**

   Clone the repository to your local machine:

   ```bash
   git clone https://github.com/RyanZzz233/JPM_Assist.git
   cd JPM_Assist
   ```

2. **Install Dependencies**

   Use the following command to install the necessary packages:

   ```bash
   pip install langchain-community langchain-openai python-dotenv
   ```

3. **Set Up the `.env` File**

   Create a `.env` file in the project root directory and add your OpenAI API key:

   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the Application**

   Execute the main script:

   ```bash
   python chatbot.py
   ```

You're all set to go!