import os

input_dir = "./templates"
output_dir = "./generated"

if os.path.exists(output_dir):
    os.system(f"rm -rf {output_dir}")

os.makedirs(output_dir)

for file in os.listdir(input_dir):
    with open(f"./{input_dir}/{file}", "r") as f:
        content = f.read()

    new_content = content.replace("{", "{{").replace("}", "}}").replace("{{0}}", "{0}").replace("{{1}}", "{1}").replace("{{2}}", "{2}").replace("{{3}}", "{3}").splitlines()

    for (index, item) in enumerate(new_content):
        new_content[index] = item.strip()

    with open(f"./{output_dir}/{file.replace('.html', '.temp')}", "w") as f:
        f.write("".join(new_content))
