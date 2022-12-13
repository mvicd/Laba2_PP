import tqdm

def directory(c_directory: str):
    """Сreates a folder at the specified path, return NONE.
    Args:
        c_directory (str): full path to create a folder.
    """
    if not os.path.isdir(c_directory):
        os.makedirs(c_directory)

def copy_dataset(directory_obj: str, c_directory_obj: str, name: str):
    """Copies all files from one folder to another, return NONE.
    Args:
        directory_obj (str): the path of the source folder.
        c_directory_obj (str): folder path to copy.
        name (str): object class.
    """
    data = os.listdir(directory_obj)
    for i in tqdm.tqdm(data):
        shutil.copy(directory_obj + "\\" + i, c_directory_obj + "\\"+ name + "_" + i)

def write_csv_copy(directory_obj: str, start: str, name: str):
    """Writes the absolute and relative path of the image to csv, return NONE.
    Args:
        directory_obj (str): full path to the folder.
        start (str): intermediate folder path.
        name (str): object class.
    """
    file = "copy_patch.csv"
    f = open(file, "a", encoding = "utf-8", newline = "")
    f_writer = csv.DictWriter(f, fieldnames = ["Absolut_path", "Relative_patch", "Class"], delimiter = "|")
def write_csv_copy(directory_obj: str, start: str, name: str):
        f_writer.writerow({"Absolut_path": directory_obj + "\\" + i, "Relative_patch":  r_directory_obj + "\\" + i, "Class": name})

def main():
    """Separates code blocks."""
    c_directory = "D:\Lab Python\Lab_2\dataset2"
    directory_rose = "D:\VS Code project\Images.py\dataset\ rose"
    directory_tulip = "D:\VS Code project\Images.py\dataset\ tulip"
    start = "D:\Lab Python\Lab_2\\"
    directory(c_directory)
    copy_dataset(directory_rose, c_directory, "rose")
    write_csv_copy(c_directory, start, "rose")

    copy_dataset(directory_tulip, c_directory, "tulip")
    write_csv_copy(c_directory, start, "tulip")


if __name__ == "__main__":
    main()