import pathlib
import shutil

directory_in_home = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject")
new_directory_in_home = directory_in_home / "Chapter_12_Practice"
new_directory_in_home.mkdir(exist_ok=True)

document = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\Chapter_12_Practice")
document_folder = document / "documents"
document_folder.mkdir(exist_ok=True)

new_file_one = document / "image1.png"
new_file_one.touch()

new_file_two = document / "image2.gif"
new_file_two.touch()

new_file_three = document / "image3.png"
new_file_three.touch()

new_file_four = document / "image4.jpg"
new_file_four.touch()

directory = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\Chapter_12_Practice")
images_folder = directory / "images"
images_folder.mkdir(exist_ok=True)

source = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\Chapter_12_Practice\image1.png")
destination = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\Chapter_12_Practice\images") / "image1.png "
source.replace(destination)

source = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\Chapter_12_Practice\image2.gif")
destination = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\Chapter_12_Practice\images") / "image2.gif "
source.replace(destination)

source = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\Chapter_12_Practice\image3.png")
destination = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\Chapter_12_Practice\images") / "image3.png "
source.replace(destination)

source = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\Chapter_12_Practice\image4.jpg")
destination = pathlib.Path(r"C:\Users\ADMIN\PycharmProjects\pythonProject\Chapter_12_Practice\images") / "image4.jpg "
source.replace(destination)
