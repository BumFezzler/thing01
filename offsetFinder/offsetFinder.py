import json
import os

class SDKData:
    """
    * The main SDKData class
    * Responsible for loading and parsing SDK data from JSON files,
    * fetching memory offsets and sizes, and writing required offsets to an output file.
    """
    
    def __init__(self):
        self.data = {}

    def load_json_file(self, file_name):
        """
        * Load a JSON file into the data dictionary.
        * @param file_name: The name of the file to load.
        """
        if file_name not in self.data:
            with open(os.path.join('SDK', f'{file_name}.json')) as file:
                self.data[file_name] = json.load(file)

    def get_memory_offset(self, class_name, key, file_name):
        """
        * Get the memory offset for a given class and key from a specified JSON file.
        * @param class_name: The name of the class.
        * @param key: The key.
        * @param file_name: The name of the JSON file.
        * @return: The memory offset, or None if not found.
        """
        self.load_json_file(file_name)
        if file_name in self.data:
            data = self.data[file_name]
            if class_name in data:
                components = data[class_name]
                attributes = components.get('Attributes', None)
                if attributes:
                    for attribute in attributes:
                        if attribute['Name'] == key:
                            return int(attribute.get('Offset'), 16)
        return None

    def get_size(self, class_name, file_name):
        """
        * Get the size for a given class from a specified JSON file.
        * @param class_name: The name of the class.
        * @param file_name: The name of the JSON file.
        * @return: The size, or None if not found.
        """
        self.load_json_file(file_name)
        if file_name in self.data:
            data = self.data[file_name]
            if class_name in data:
                components = data[class_name]
                attributes = components.get('Attributes', None)
                if attributes:
                    for attribute in attributes:
                        size = attribute.get('Size', None)
                        if size is not None:
                            return int(size, 16)
        return None

    def read_needed_offsets(self, input_file="neededOffsets.json"):
        """
        * Read the needed offsets from an input file.
        * @param input_file: The name of the input file.
        * @return: The needed offsets.
        """
        with open(input_file, 'r') as f:
            return json.load(f)

    def write_offsets_to_file(self, input_data, output_file="offsets.json"):
        """
        * Write the required offsets to an output file.
        * @param input_data: The input data.
        * @param output_file: The name of the output file.
        """
        results = {}
        for item in input_data:
            file_name = item['file']
            class_name = item["class"]
            key = item.get("key", None)
            operation = item["operation"]
            if operation == "offset":
                value = self.get_memory_offset(class_name, key, file_name)
                result_key = f"{class_name}.{key}"
            elif operation == "size":
                value = self.get_size(class_name, file_name)
                result_key = f"{class_name}.Size"

            if value is not None:
                results[result_key] = value
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=4)

    def clear_data(self):
        """
        * Clears the data dictionary, removing all loaded JSON data from memory.
        """
        self.data.clear()

# Creating an instance of SDKData
sdk_data = SDKData()
# Read the needed offsets from the input file
input_data = sdk_data.read_needed_offsets()
# Write the required offsets to the output file
sdk_data.write_offsets_to_file(input_data)
# Clear the data dictionary to free up memory
sdk_data.clear_data()
