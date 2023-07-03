import json
import os


import base64

def convert_email_to_filename(email):
    # Encode the email address using Base64
    encoded_email = base64.urlsafe_b64encode(email.encode()).decode()

    # Replace any padding characters in the Base64 encoding
    encoded_email = encoded_email.replace("=", "")

    return encoded_email

def convert_filename_to_email(filename):
    # Remove the file extension and decode the Base64 encoding
    encoded_email = filename  # Remove the file extension (e.g., .txt)
    encoded_email += "=" * (-len(encoded_email) % 4)  # Add back any removed padding characters
    decoded_email = base64.urlsafe_b64decode(encoded_email).decode()

    return decoded_email


def save_location(name, email, notes, location):
    print(location)
    data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
    data_to_save = dict(
        name=name,
        email=email,
        notes=notes,
        location=location,
    )
    with open(os.path.join(data_path, convert_email_to_filename(email)), 'w') as f:
        json.dump(data_to_save, f)


def load_locations():
    data_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "data")
    json_data_list = []
    for root, dirs, files in os.walk(data_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                try:
                    json_data = json.load(f)
                    json_data_list.append(json_data)
                except json.JSONDecodeError:
                    print(f"Error loading JSON file: {file_path}")

    return json_data_list



