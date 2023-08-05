# prompts.py
import os
import yaml

class Prompt:
    def __init__(self, name, prompt_string, parameters):
        self.name = name
        self.prompt_string = prompt_string
        self.parameters = parameters

    def render(self, **kwargs):
        missing = set(self.parameters.keys()) - set(kwargs.keys())
        if missing:
            raise ValueError(f"Missing parameters: {', '.join(missing)}")

        extra = set(kwargs.keys()) - set(self.parameters.keys())
        if extra:
            raise ValueError(f"Extra parameters: {', '.join(extra)}")

        result = self.prompt_string
        for key, value in kwargs.items():
            result = result.replace(self.parameters[key], value)
        return result

class PromptBook:
    def __init__(self, prompts):
        self.prompts = {prompt.name: prompt for prompt in prompts}

    def get_prompt(self, name):
        return self.prompts[name]

def load_prompt_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if not file_path.endswith('.prompt'):
        raise ValueError(f"Invalid file extension, expected '.prompt': {file_path}")

    with open(file_path, 'r') as file:
        prompt_data = yaml.safe_load(file)

    prompts = []
    for name, prompt_entry in prompt_data.items():
        prompt_string = prompt_entry['prompt']
        parameters = prompt_entry['parameters']
        prompts.append(Prompt(name, prompt_string, parameters))

    return PromptBook(prompts)