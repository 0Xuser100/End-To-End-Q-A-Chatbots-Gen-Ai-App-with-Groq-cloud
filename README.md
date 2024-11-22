# 🚀 Enhanced Q&A Chatbot with Groq Models  

This repository hosts a **Streamlit-based chatbot application** that leverages the power of **Groq models** via LangChain for dynamic question answering and text generation. Engage with cutting-edge language models in an intuitive, user-friendly interface designed for efficiency and flexibility.  

---

## 🌟 Features  

### 🔄 **Dynamic Model Selection**  
Switch effortlessly between powerful Groq models:  
- `gemma2-9b-it`  
- `mixtral-8x7b-32768`  
- `llama-3.2-90b-text-preview`  

### 🎛️ **Customizable Parameters**  
- Adjust **temperature** to control response creativity and coherence.  

### 🖥️ **Interactive User Interface**  
- Simple text input and sidebar controls for a seamless experience.  

### 🛡️ **Robust Error Handling**  
- Ensures smooth operation even during API errors or connectivity issues.  

---

## 📥 Installation  

### Step 1: Clone the Repository  
```bash  
git clone https://github.com/0Xuser100/End-To-End-Q-A-Chatbots-Gen-Ai-App-with-Groq-cloud.git  
cd End-To-End-Q-A-Chatbots-Gen-Ai-App-with-Groq-cloud  
```  

### Step 2: Set Up a Virtual Environment  
```bash  
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  
```  

### Step 3: Install Dependencies  
```bash  
pip install -r requirements.txt  
```  

### Step 4: Configure Environment Variables  
Create a `.env` file in the root directory and include your Groq API key:  
```bash  
GROQ_API_KEY=your-groq-api-key  
```  

---

## 🚀 Usage  

### Step 1: Run the Application  
```bash  
streamlit run app.py  
```  

### Step 2: Interact with the Chatbot  
- Open the app in your browser (usually at `http://localhost:8501`).  
- Enter your query in the text input box.  
- Use the sidebar to:  
  - **Select a Groq model** for response generation.  
  - **Adjust the temperature** for response customization.  

---

## ⚙️ Parameters  

### **Temperature**  
Controls the balance between creativity and determinism:  
- `0.0`: Predictable and precise responses.  
- `1.0`: Creative and diverse outputs.  

### **Model Selection**  
Choose a model tailored to your specific needs. Each model is designed for unique tasks and scenarios.  

---

## 🔮 Future Enhancements  

### 🕒 **Chat History**  
- Enable context-aware conversations with memory for multi-turn interactions.  

### ✂️ **Token Control**  
- Add `max_tokens` functionality for managing output length.  

### 🌍 **Multi-language Support**  
- Extend capabilities for domain-specific use cases and language flexibility.  

---

## 🙏 Acknowledgments  

This project was made possible by:  
- **LangChain**: For seamless integration of language models.  
- **Streamlit**: Providing a rich and interactive user interface.  
- **Groq Models**: Delivering exceptional language generation performance.  

---

## 📞 Contact  

For questions, feedback, or collaboration opportunities:  
- **Name**: Mahmoud Abdelhamid  
- **Email**: [mahmoudabdulhamid22@gmail.com](mailto:mahmoudabdulhamid22@gmail.com)  
- **GitHub**: [https://github.com/0Xuser100](https://github.com/0Xuser100)  
- **LinkedIn**: [https://www.linkedin.com/in/mahmoud-abdulhamid-052244230/](https://www.linkedin.com/in/mahmoud-abdulhamid-052244230/)  

---  

Unleash the power of Groq models with this enhanced chatbot application! 🚀
