# Group-9-cyber-security-project
Training and evaluation data will include both synthetic and real-world message samples, with attention to colloquial expressions and common scam patterns.

---
# LocalPhishingDetector: A Proposal for Offline Phishing Detection in Ethiopian Languages

## 1. Overview

This document outlines a technical proposal for a local, offline-capable system designed to detect phishing messages in digital communications, with a focus on Ethiopian languages. The system is intended to operate without reliance on cloud services, preserving user privacy and enabling deployment in low-connectivity environments.

The primary communication platform under consideration is Telegram, with an initial focus on detecting phishing in direct messages and group chats. The system will support multiple Ethiopian languages, including Amharic, Tigrinya, Oromo, and Somali, in both native scripts (e.g., Ge'ez) and Latinized (romanized) forms.

---

## 2. Background and Motivation

### 2.1 Rising Use of Digital Messaging in Ethiopia

With increasing internet penetration, platforms such as Telegram have become widely used for personal, educational, and institutional communication in Ethiopia. This growth has been accompanied by a rise in social engineering attacks, particularly phishing attempts delivered through direct messages.

Common attack patterns include:
- Impersonation of family members or officials
- Fake bank or government alerts
- Requests for urgent financial transfers
- False account verification notices

These messages are increasingly composed in local languages and use informal, conversational styles that evade traditional filtering mechanisms.

### 2.2 Limitations of Existing Solutions

Current phishing detection tools exhibit several shortcomings in the Ethiopian context:

- Language support: Most models are trained on English text and perform poorly on Amharic, Oromo, and other local languages.
- Script handling: Few systems support Ge'ez script or recognize Latinized variants (e.g., "kemey?" for ከመይ?).
- Connectivity dependence: Cloud-based AI models require stable internet, limiting usability in rural or low-infrastructure areas.

There is currently no publicly available tool that provides offline, privacy-preserving phishing detection for Ethiopian language messages.

---

## 3. Objectives

The project aims to develop a system with the following capabilities:

1. Detect phishing content in text messages written in Amharic, Tigrinya, Oromo, and Somali.
2. Support both Ge'ez script and Latinized orthographies.
3. Operate entirely offline, with no external data transmission.
4. Integrate with Telegram through a bot interface.
5. Provide real-time feedback to users without storing message content.

---

## 4. System Design

### 4.1 Architecture

The system consists of three main components:

1. Inference Engine: Runs a lightweight large language model (LLM) locally.
2. Message Interface: A Telegram bot that receives forwarded messages for analysis.
3. Classification Logic: A prompt-based or fine-tuned model that classifies messages as phishing or non-phishing.

All processing occurs on the user’s device or a trusted local server. No message data is stored or transmitted beyond the device.

### 4.2 Technical Components

| Component | Technology |
|---------|------------|
| AI Model | Phi-3-mini-4k-instruct (quantized GGUF format) |
| Inference Backend | llama.cpp |
| Runtime Environment | Python 3.10+ |
| Telegram Integration | python-telegram-bot library |
| Operating System | Linux (Ubuntu/Debian recommended) |
| Hardware Requirements | x86-64 CPU, 8GB RAM, 256GB storage |

The model will be run in 4-bit quantized mode (e.g., Q4_K_M) to reduce memory usage and enable operation on consumer-grade hardware.

---

## 5. Language and Script Support

The system will be tested and evaluated on the following language-script combinations:

| Language | Script | Notes |
|--------|--------|-------|
| Amharic | Ge'ez | Primary focus |
| Amharic | Latinized | Common in informal messaging |
| Tigrinya | Ge'ez | Secondary focus |
| Tigrinya | Latinized | Informal usage |
| Oromo | Latin | Official orthography |
| Somali | Latin | Official orthography |
## 6. User Interaction Model

Due to Telegram API limitations, the system will not automatically monitor incoming direct messages. Instead, it will rely on user-initiated forwarding to a dedicated bot.

### Workflow:
1. A user receives a suspicious message in a chat or group.
2. The user forwards the message to the bot.
3. The bot processes the message using the locally hosted model.
4. The bot replies with a classification: "Potential phishing" or "No signs of phishing detected."
5. The message is discarded after processing.

This method ensures user control, maintains privacy, and complies with platform policies.

---

## 7. Development Plan

### Phase 1: Environment Setup (Week 1-2)
- Install and configure llama.cpp and dependencies
- Load and test Phi-3-mini model with sample inputs
- Verify multilingual inference capability

### Phase 2: Data Collection (week 3-4)
- Compile a dataset of phishing and non-phishing messages
- Include examples in Amharic, Oromo, Somali, and Tigrinya
- Annotate messages with labels and metadata

### Phase 3: Bot Development (week 5)
- Implement Telegram bot using python-telegram-bot
- Connect bot to local inference pipeline
- Test end-to-end message processing

### Phase 4: Evaluation and Refinement (week 6 and beyond)
- Conduct internal testing with 10–20 users
- Collect feedback on accuracy and usability
- Adjust prompts or fine-tune model if needed

### Phase 5: Future Work (Beyond v1)
- Explore Android deployment using ONNX or ML Kit
- Investigate speech-to-text integration for voice messages
- Extend to SMS or email platforms
- Develop a multi-user dashboard for organizational use

---


## 8. Ethical Considerations

The following principles guide the design and deployment of the system:

- No passive monitoring: The system only analyzes messages explicitly forwarded by the user(DM feature)
- No data retention: Messages are processed in memory and discarded immediately.
- User agency: Users must actively choose to use the tool.
- No profiling: The system does not collect user identities or behavioral data.

The goal is to support user autonomy, not to enable surveillance or automated filtering.

---

## 9. Expected Outcomes

- A functional prototype capable of classifying phishing messages in Ethiopian languages
- A publicly available dataset of labeled local-language phishing samples
- Documentation for installation, usage, and contribution
- A foundation for future research into localized AI safety tools

The system is not expected to achieve 100% accuracy, especially in early versions, but aims to provide meaningful assistance in high-risk scenarios.

---

## 10. Deliverables

- Local inference pipeline using Phi-3-mini and llama.cpp
- Telegram bot interface with classification capability
- Labeled dataset in JSONL format
- Setup and user guide (in English and Amharic)
- Public GitHub repository with MIT license

---

## 11. Conclusion

This project addresses a gap in digital security tools for Ethiopian language users by proposing a local, offline, and privacy-preserving approach to phishing detection. By leveraging recent advances in small language models and focusing on real-world usage patterns, the system aims to provide practical support in environments where connectivity, literacy, and trust are key constraints.

The use of message forwarding to a local bot provides a feasible and ethical method for user interaction, avoiding automated surveillance while still enabling timely feedback.

Future work will depend on community input, data availability, and hardware accessibility, with the long-term goal of contributing to broader efforts in inclusive and responsible AI development.

---
