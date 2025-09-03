# Group-9-cyber-security-project

AI-Powered social-engineering Detection for Ethiopian Languages

## 📋 Project Overview
We are building a practical, local AI system to detect social engineering messages in Amharic and other Ethiopian languages. Unlike our initial plan to use large models like Phi-3, we've adapted to a more efficient approach using a specialized text classification model that runs reliably on standard hardware.

## 🎯 What We're Actually Building
A focused text classifier that distinguishes between:

- ✅ **Legitimate messages** (normal conversations, news, information)  
- 🚨 **Phishing messages** (scams, fraud attempts, social engineering)

### Key Changes from Initial Plan:
- Using **DistilBERT multilingual** instead of Phi-3 (much more efficient)
- No local LLM inference — building a **specialized classifier**
- Works on **everyday computers** (8GB RAM, no special GPU needed)
- Faster and more reliable for this specific task

## 🛠️ Our Current Technical Stack

| Component             | Technology                          | Why We Chose It                                  |
|-----------------------|-------------------------------------|--------------------------------------------------|
| AI Model              | `distilbert-base-multilingual-cased`| Lightweight, understands 100+ languages including Amharic |
| Training              | Google Colab (free GPU)             | No expensive hardware needed                     |
| Labeling              | Doccano                             | Best open-source labeling tool                   |
| Local Inference       | Python + Transformers               | Runs on any computer                             |
| Languages             | Amharic, Oromo, Somali              | Focus on Ethiopian languages                     |

## 📊 How It Works - Simple Pipeline
1. **Data Collection** → Gather real Amharic messages from Telegram  
2. **Data Cleaning** → Extract clean text from JSON/HTML exports  
3. **Labeling** → Use Doccano to tag messages as "phishing" or "legitimate"  
4. **Training** → Fine-tune DistilBERT on Google Colab  
5. **Deployment** → Run the trained model locally for inference  

## 🚀 Current Progress
✅ **Already Working:**
- Telegram JSON data extraction script
- Doccano installation and setup
- Data cleaning pipeline
- DistilBERT fine-tuning code ready for Colab

🔄 **In Progress:**
- Mass labeling of Ethiopian phishing messages
- Building the labeled dataset
- Testing model performance

## 💻 Hardware Requirements - Much Simpler!
**Minimum:**
- Intel i5 or equivalent CPU
- 8GB RAM
- 2GB free storage
- Any OS (Windows, Mac, Linux)

❌ **No Need For:**
- Powerful GPU
- 16GB+ RAM
- Specialized hardware

## 🌍 Language Support
Currently working with:
- **Amharic** (Ge-ez ፊደል and Latin script)


Future expansion:
- **Tigrinya** (ፊደል) — planned for Phase 5
- **Oromo** (Latin script)
- **Somali** (Latin script)
## 🗺️ Project Roadmap

### **Phase 1: Data Foundation** 
- Collect 5,000+ Amharic message samples
- Label 1,000+ messages using Doccano (500 phishing, 500 legitimate)
- Create clean, balanced dataset for training
- Establish data quality validation process

### **Phase 2: Model Development** 
- Complete initial DistilBERT fine-tuning on Google Colab
- Achieve 85%+ accuracy on validation set
- Test model on Oromo and Somali samples
- Develop confidence scoring system

### **Phase 3: Local Deployment** 
- Build simple Python inference script
- Create installation guide for Windows/Linux/Mac
- Test on minimum hardware requirements
- Develop batch processing capability for multiple messages

### **Phase 4: User Interface** 
- Develop simple web interface (Flask/FastAPI)
- Add file upload functionality for message batches
- Implement real-time single message checking
- Create result visualization dashboard

## 📊 Project Status
- **Phase:** Active data labeling and model preparation  
- **Current Focus:** Building high-quality Ethiopian language dataset  

