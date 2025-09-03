import json
import sys

def extract_messages_from_json(json_file_path, output_file_path):
    print(f"Reading JSON file: {json_file_path}")
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    messages = data['messages'] if isinstance(data, dict) and 'messages' in data else data
    print(f"Found {len(messages)} total messages.")

    message_count = 0
    with open(output_file_path, 'w', encoding='utf-8') as out_file:
        for message in messages:
            if 'text' not in message:
                continue

            text_field = message['text']
            text_content = ""

            if isinstance(text_field, str):
                text_content = text_field.strip()
            elif isinstance(text_field, list):
                for item in text_field:
                    if isinstance(item, dict) and 'text' in item:
                        text_content += str(item['text'])
                    elif isinstance(item, str):
                        text_content += item
                    else:
                        text_content += str(item)
                text_content = text_content.strip()
            else:
                text_content = str(text_field).strip()

            if text_content:
                out_file.write(text_content + '\n')
                message_count += 1

    print(f"Successfully extracted {message_count} text messages to '{output_file_path}'.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_telegram_json.py <input_json_file> <output_text_file>")
        print("Example: python extract_telegram_json.py result.json all_messages.txt")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    extract_messages_from_json(input_file, output_file)
