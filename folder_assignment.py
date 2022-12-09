import pathlib
import shutil

directory_in_home = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject")
new_directory_in_home = directory_in_home / "my_folder"
new_directory_in_home.mkdir(exist_ok=True)

new_file_one = new_directory_in_home / "file1.txt"
new_file_one.touch()

new_file_two = new_directory_in_home / "file2.txt"
new_file_two.touch()

new_file_three = new_directory_in_home / "image1.png"
new_file_three.touch()


images_directory = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\my_folder")
new_images_directory = images_directory / "images"
new_images_directory.mkdir(exist_ok=True)


source = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\my_folder\image1.png")
destination = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\my_folder") / "images" / "image1.png"
source.replace(destination)


file = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\my_folder")
file1 = file / "file1.txt"
file1.unlink()


my_folder = directory_in_home / "my_folder"
shutil.rmtree(my_folder)
