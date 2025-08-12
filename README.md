# Group-9-cyber-security-project
Training and evaluation data will include both synthetic and real-world message samples, with attention to colloquial expressions and common scam patterns.

---

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
