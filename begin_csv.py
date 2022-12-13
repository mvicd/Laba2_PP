
import os

def write_csv(directory_obj : str, start : str, name: str):
    """Writes the absolute and relative path of the image to csv, return NONE.
      Args:
            directory_obj (str): full path to the folder.
            start (str): intermediate folder path.
            name (str): object class.
        """
    file = "patch.csv"
    f = open(file, "a", encoding="utf-8", newline="")





def write_csv(directory_obj: str, start: str, name: str):
    f_writer.writerow(
        {"Absolut_path": directory_obj + "\\" + i, "Relative_patch": r_directory_obj + "\\" + i, "Class": name})

    def main():
        directory_rose = "D:\VS Code project\Images.py\dataset\ rose"
        directory_tulip = "D:\VS Code project\Images.py\dataset\ tulip"
        start_rose = "D:\VS Code project\Images.py\\"
        start_tulip = "D:\VS Code project\Images.py\\"

        write_csv(directory_rose, start_rose, "rose")
        write_csv(directory_tulip, start_tulip, "tulip")

    if __name__ == "__main__":
        main()