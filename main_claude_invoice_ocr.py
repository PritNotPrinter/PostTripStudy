import os
from anthropic import Anthropic
from datetime import datetime
import json
from agents.ocr.claude_invoice_ocr import extracttext

def main():
    data_folder = "data/input_images"
    
    image_files = [f for f in os.listdir(data_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
    
    if not image_files:
        print("No image files found in the data folder.")
        return
    
    output_folder = "data/extracted_text"
    os.makedirs(output_folder, exist_ok=True)

    for image_file in image_files:
        image_path = os.path.join(data_folder, image_file)
        print(f"Processing image: {image_file}")
        
        try:
            print("Extracted text:")
            print(extracttext(image_path))

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"{timestamp}_{os.path.splitext(image_file)[0]}.json"
            output_path = os.path.join(output_folder, output_filename)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(result, f, indent=2)
            
            print(f"Saved extracted data to: {output_path}")
            print(result)
            print("-" * 50)
        except Exception as e:
            print(f"Error processing {image_file}: {str(e)}")
            print("-" * 50)

if __name__ == "__main__":
    main()
