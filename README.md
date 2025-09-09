# Support Ticket Auto-Tagging (Gemini + LangChain)

## 🎯 Objective
The goal of this project is to automatically classify customer support tickets into the most relevant categories (tags) using Google Gemini LLM and LangChain. This helps reduce manual work for support teams and ensures faster response times.

---

## ⚙️ Methodology / Approach
1. **Data Input**: User pastes a support ticket into a Streamlit interface.
2. **Prompt Engineering**: A structured prompt is used to guide Gemini-1.5-Flash in classifying tickets.
3. **Prediction**: The model returns the **Top 3 most probable tags** with confidence scores (0 to 1).
4. **Output**: Cleaned JSON is parsed and displayed in a user-friendly format.

Tags include:  
`billing, login, payment, refund, bug, feature_request, account, password, performance, other`

---

## 📊 Key Results / Observations
- The model provides **consistent JSON output** that can be easily parsed.  
- Predictions are interpretable with **confidence scores** for each tag.  
- Integration with **Streamlit** makes the tool easy to use interactively.  
- Future extensions:  
  - Support for multi-language tickets.  
  - Integration with CRM systems.  
  - Fine-tuning with real customer data.  

---

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/support-ticket-auto-tagging.git
   cd support-ticket-auto-tagging
