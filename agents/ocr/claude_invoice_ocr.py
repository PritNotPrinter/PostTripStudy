import base64
import json
import os
import configparser
from anthropic import Anthropic
from typing import Dict, Any
from configparser import ConfigParser

def extracttext(image_path: str) -> Dict[str, Any]:
    """
    Extract text from an image using Claude Haiku API.

    Args:
        image_path (str): Path to the image file.

    Returns:
        Dict[str, Any]: JSON response containing extracted text and metadata.
    """
    # Read API key from config file
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), '..', '..', 'config', '.anthropic_config')
    config.read(config_path)
    api_key = "sk-ant-api03-Q72ihqTLegJwQJRr0mPL5LUNiX_DkxbxUR4N8A_AH3LbVIjbvcqt0sNsjT9SEHFYk4nM2O7xWr7XcFXR35_IZQ-TBIpkQA"


    anthropic = Anthropic(api_key=api_key)

    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode('utf-8')

    response = anthropic.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=500,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": encoded_image
                        }
                    },
                    {
                        "type": "text",
                        "text": "This image is an invoice. Extract key invoice details in JSON format. Do not include any other text."
                    }
                ]
            }
        ]
    )

    # Parse and return the JSON response
    extracted_text = json.loads(response.content[0].text)
    result = extracttext("path/to/your/image.jpg")
    print(result)
    print(extracted_text)
    return extracted_text

# Example usage:
# result = extract_text_from_image("path/to/your/image.jpg")
# print(result)
