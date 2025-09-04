import json
import sys

def extract_messages_from_json(json_file_path, output_file_path):
    """
    Parses a Telegram JSON export and writes the 'text' field of every message to a file.
    Each message is guaranteed to be on a single line (newlines replaced with spaces).
    """
    # Read the JSON file
    print(f"Reading JSON file: {json_file_path}")
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Extract all messages. The structure is usually {"messages": [list of messages]}
    if isinstance(data, dict) and 'messages' in data:
        messages = data['messages']
    else:
        messages = data

    print(f"Found {len(messages)} total messages.")

    # Open the output file
    with open(output_file_path, 'w', encoding='utf-8') as out_file:
        message_count = 0
        for message in messages:
            text_content = ""
            
            # Check if the message has the 'text' field
            if 'text' not in message:
                continue
                
            text_field = message['text']
            
            # Case 1: 'text' is a simple string
            if isinstance(text_field, str):
                text_content = text_field.strip()
                
            # Case 2: 'text' is a list (of dictionaries or strings)
            elif isinstance(text_field, list):
                for item in text_field:
                    # If the item is a dictionary with a 'text' key
                    if isinstance(item, dict) and 'text' in item:
                        text_content += str(item['text'])
                    # If the item is a simple string
                    elif isinstance(item, str):
                        text_content += item
                    # Handle other unexpected types by converting to string
                    else:
                        text_content += str(item)
                text_content = text_content.strip()
            
            # Case 3: 'text' is some other type (number, boolean, etc.)
            else:
                text_content = str(text_field).strip()
            
            # CRITICAL: Replace any newlines with spaces to ensure single line
            text_content = text_content.replace('\n', ' ').replace('\r', ' ')
            
            # Remove extra spaces and ensure it's a clean single line
            text_content = ' '.join(text_content.split())
            
            # Only write non-empty messages
            if text_content:
                out_file.write(text_content + '\n')
                message_count += 1

    print(f"Successfully extracted {message_count} text messages to '{output_file_path}'.")
    print("All messages are guaranteed to be on single lines (newlines replaced with spaces).")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_telegram_json.py <input_json_file> <output_text_file>")
        print("Example: python extract_telegram_json.py result.json all_messages.txt")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    extract_messages_from_json(input_file, output_file)
