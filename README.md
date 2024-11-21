

---

# Enhanced Q&A Chatbot With Groq Models

This repository hosts a **Streamlit-based chatbot** application powered by **Groq models** via LangChain. The app allows users to engage with advanced Groq language models for efficient question answering and text generation.

---

## Features

- **Dynamic Model Selection**:  
  Seamlessly switch between multiple Groq models:  
  - `gemma2-9b-it`  
  - `mixtral-8x7b-32768`  
  - `llama-3.2-90b-text-preview`

- **Customizable Parameters**:  
  - Fine-tune **temperature** to control the creativity of responses.

- **User-Friendly Interface**:  
  - Simple and interactive text input and parameter adjustment using Streamlit.

- **Robust Error Handling**:  
  - Ensures uninterrupted usage even in case of API issues.

---

## Installation

Follow these steps to set up the application locally:

1. **Clone the Repository**:  
   ```bash
   git clone https://github.com/0Xuser100/End-To-End-Q-A-Chatbots-Gen-Ai-App-with-Groq-cloud.git
   cd End-To-End-Q-A-Chatbots-Gen-Ai-App-with-Groq-cloud
   ```

2. **Set Up a Virtual Environment**:  
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```

4. **Add Environment Variables**:  
   Create a `.env` file in the root directory and add your **Groq API Key**:  
   ```bash
   GROQ_API_KEY=your-groq-api-key
   ```

---

## Usage

1. **Run the Application**:  
   ```bash
   streamlit run app.py
   ```

2. **Interact with the Chatbot**:  
   - Open the app in your browser (usually at `http://localhost:8501`).  
   - Enter your query in the input box.  
   - Select a Groq model and fine-tune the temperature parameter in the sidebar.  

---

## Parameters Explained

### **Temperature**:  
Controls the randomness and creativity of responses:  
- `0.0`: Deterministic responses with minimal variation.  
- `1.0`: Highly diverse and creative responses.  

### **Model Selection**:  
Choose from the available Groq models based on your specific task requirements.

---

## Future Enhancements

### **Chat History**:  
- Add features to maintain conversational context across multiple interactions.

### **Token Control**:  
- Introduce a `max_tokens` parameter for better control over output length.

### **Integration**:  
- Extend the app for multi-language support and domain-specific use cases.

---

## Acknowledgments

Special thanks to the following technologies that made this project possible:  
- **LangChain** for seamless model integration.  
- **Streamlit** for providing a user-friendly interface.  
- **Groq Models** for powering cutting-edge language capabilities.

--- 

