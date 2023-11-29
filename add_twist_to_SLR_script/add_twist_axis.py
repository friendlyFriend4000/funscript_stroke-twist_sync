import os
import json

input_folder = 'input_scripts/'
output_folder = 'output/'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

# Iterate over files in the input folder
for filename in os.listdir(input_folder):
    if filename.endswith('.funscript'):
        input_file_path = os.path.join(input_folder, filename)

        # Add 'twist_added' to the output file name
        output_filename = f'twist_added_{filename}'
        output_file_path = os.path.join(output_folder, output_filename)

        # Read JSON file
        with open(input_file_path, 'r') as input_file:
            file_contents_data = json.load(input_file)

        # Extract the "actions" field from the original JSON data
        script_file_actions = file_contents_data.get("actions", [])

        # Create a new "twist" axis
        twist_axis_R0 = {"id": "R0", "actions": script_file_actions}

        # Add the new "twist" axis to the JSON data
        file_contents_data['axes'] = [twist_axis_R0]

        # Save the modified data to the output file
        with open(output_file_path, 'w') as output_file:
            json.dump(file_contents_data, output_file, indent=2)

print("Processing complete.")
