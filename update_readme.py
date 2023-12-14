import os
import configuration

# Constant
example_file = os.path.join(configuration.EXAMPLE_DIRECTORY, "example.py")

# Read the content of example.py
with open(example_file, 'r') as file:
    example_content = file.read()

# Read the content of README.md
with open('README.md', 'r') as file:
    readme_content = file.read()

# Find the '# Usage' section in README.md
usage_section_index = readme_content.find('# Example')

# If the '# Usage' section is found, update its content
if usage_section_index != -1:
    # Find the end of the '# Usage' section
    # For simplicity, we assume it ends at the end of the file
    updated_readme = readme_content[:usage_section_index] + '# Example\n\n```python\n' + example_content + '\n```\n' + readme_content[usage_section_index:]

    # Overwrite README.md with the updated content
    with open('README.md', 'w') as file:
        file.write(updated_readme)