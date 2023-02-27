import os


def rename_txt(path, prefix):
    # check if it is a valid path
    assert os.path.exists(path), 'The path doesnt exist'
    txt_files = [file for file in os.listdir(path) if file.endswith('.txt')]
    for txt_file in txt_files:
        old_path = os.path.join(path, txt_file)
        new_path = os.path.join(path, ''.join((prefix, txt_file)))
        os.rename(old_path, new_path)
        print(f'{old_path} changed to {new_path}')
        