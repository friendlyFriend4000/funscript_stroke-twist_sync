import glob
import os
import json

input_folder = 'input_scripts/'
output_folder = 'output/'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)


def get_axis_data_from_funscript(extension):
    # go through ALL files in the input folder
    input_dir = 'input_scripts/'
    files = os.listdir(input_dir)

    matched_file = [file for file in files if file.endswith(extension)]

    complete_file_path = os.path.join(input_dir, matched_file[0])

    with open(complete_file_path, 'r') as input:
        file_actions = json.load(input)

    matched_file_actions = file_actions.get("actions", [])

    return matched_file_actions


# Iterate over files in the input folder
for filename in os.listdir(input_folder):

    if filename.endswith('.funscript')\
            and not filename.endswith('sway.funscript')\
            and not filename.endswith('surge.funscript')\
            and not filename.endswith('twist.funscript')\
            and not filename.endswith('roll.funscript')\
            and not filename.endswith('pitch.funscript'):
        input_file_path = os.path.join(input_folder, filename)

        # Add 'twist_added' to the output file name
        output_filename = f'merged_{filename}'
        output_file_path = os.path.join(output_folder, output_filename)

        with open(input_file_path, 'r') as input_file:
            file_contents_data = json.load(input_file)


        # check if axis.funscript exists then append
        file_contents_data['axes'] = []
        if any(glob.glob(os.path.join('input_scripts/', f'*{"sway.funscript"}'))):
            sway_axis_L2 = {"id": "L2", "actions": get_axis_data_from_funscript('sway.funscript')}
            file_contents_data['axes'].append(sway_axis_L2)

        if any(glob.glob(os.path.join('input_scripts/', f'*{"surge.funscript"}'))):
            surge_axis_L1 = {"id": "L1", "actions": get_axis_data_from_funscript('surge.funscript')}
            file_contents_data['axes'].append(surge_axis_L1)

        if any(glob.glob(os.path.join('input_scripts/', f'*{"twist.funscript"}'))):
            twist_axis_R0 = {"id": "R0", "actions": get_axis_data_from_funscript('twist.funscript')}
            file_contents_data['axes'].append(twist_axis_R0)

        if any(glob.glob(os.path.join('input_scripts/', f'*{"roll.funscript"}'))):
            roll_axis_R1 = {"id": "R1", "actions": get_axis_data_from_funscript('roll.funscript')}
            file_contents_data['axes'].append(roll_axis_R1)

        if any(glob.glob(os.path.join('input_scripts/', f'*{"pitch.funscript"}'))):
            pitch_axis_R2 = {"id": "R2", "actions": get_axis_data_from_funscript('pitch.funscript')}
            file_contents_data['axes'].append(pitch_axis_R2)

        print(file_contents_data)

        with open(output_file_path, 'w') as output_file:
            json.dump(file_contents_data, output_file, indent=2)

# Save the modified data to the output file
# with open(output_file_path, 'w') as output_file:
#    json.dump(file_contents_data, output_file, indent=2)


print("Processing complete.")
