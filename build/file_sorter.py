import os as os 
username = os.getlogin()
def create_dir(dir_name, path):
    try:
        test = os.mkdir(rf'{path}\{dir_name}')
    except:
        print("Directory already made. Returning...")
        return
def get_all_extensions(src_path):
    filetype_list = []
    for file in os.listdir(src_path):
        filetype_list.append(os.path.splitext(file)[1])
    return set(filetype_list)
def sort_files(dest_dir_path, src_path, extensions, all):
    if all == 1:
        extensions = get_all_extensions(src_path)
    files = [f for f in os.listdir(src_path) if os.path.isfile(f)]
    for file in files:
        file_name, file_extension = os.path.splitext(file)
        if file_extension in extensions:
            create_dir(file_extension[1:].upper() + 's', dest_dir_path)
            os.rename(rf"{src_path}\{file}", rf"{os.path.join(dest_dir_path, file_extension[1:].upper() + 's')}\{file}")
def choose_input_params():
    directory_input = input("Input Working Directory (use File Explorer to get exact directory, copy paste here): ")
    if(directory_input == "Downloads"):
        directory_input = rf'C:\Users\{username}\Downloads'
    chosen_file_sort = input("Input filetype to be sorted (.pdf ,.txt, etc., type ALL if you want to sort everything): ")
    dir_name = input("Input directory name for sorted files: ")
    return (directory_input, chosen_file_sort, dir_name)

def filesystem(chosen_dir, dest_dir, filetype, all):
    os.chdir(chosen_dir)
    cwd = os.getcwd()
    filetype.split(", ")
    print(filetype)
    sort_files(dest_dir, os.getcwd(), filetype, all)


if __name__ == "__main__":
    params = choose_input_params()
    all = 0
    if params[1] == "ALL": all = 1
    filesystem(params[0], params[2], params[1], all)

