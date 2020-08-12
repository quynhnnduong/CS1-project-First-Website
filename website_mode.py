"""
Website Mode:
I choose to create a paragraph dataclass to make it easier to store the paragraphs. Then, I processed the paragraph
information from the paragraph objects. I took the user's input and the paragraph info from the file to create a html
file.
Final Project
Author: Nhu Quynh Duong
"""
import wizard_mode
from dataclasses import dataclass


@dataclass
class Paragraph:
    title: str
    content: str
    image_url: str


def readfile(filename):
    """
    This function takes in a file and reads it.
    Creates paragraph objects from the file.
    Stores the objects in a data structure (list).
    :param filename: a file
    :return: a list of the website title and the paragraph objects
    """
    paragraph_flag = False
    first_line_flag = True
    lst = []
    paragraph_lst = []
    content = []
    title = ""
    image = ""
    with open(filename) as f:
        for line in f:
            lines = line.split()
            if first_line_flag:
                paragraph_lst.append(lines)
                first_line_flag = False
                continue
            if lines != [] and lines[0] == "!new_paragraph":
                paragraph_flag = True
            if not lines:
                paragraph_flag = False
                paragraph = Paragraph(title, content, image)
                paragraph_lst.append(paragraph)

            if paragraph_flag:
                if lines[0] == "!title":
                    title = lines[1]
                elif lines[0] == "!image":
                    image = lines[1]
                elif lines[0] == "!new_paragraph":
                    pass
                else:
                    content += lines
            else:
                pass
        return paragraph_lst


def create_web_title(paragraph_lst):
    """
    This function returns the website title.
    I am aware that the title looks a little funny with the "['title']" format. However, I do not know how to change it.
    :param paragraph_lst: a list of paragraph objects
    :return: the website title
    """
    return str(paragraph_lst[0])


def create_title_list(paragraph_lst):
    """
    This function returns the paragraph titles.
    :param paragraph_lst: a list of paragraph objects
    :return: the list of paragraph titles
    """
    paragraph_title_lst = []
    new_paragraph_lst = paragraph_lst[1:]
    for paragraph in new_paragraph_lst:
        paragraph_title = str(paragraph.title)
        paragraph_title_lst.append(paragraph_title)
    return paragraph_title_lst


def create_content_lst(paragraph_lst):
    """
    This function returns the list of paragraph content
    :param paragraph_lst: a list of paragraph objects
    :return: the list paragraph content
    """
    content_lst = []
    new_paragraph_lst = paragraph_lst[1:]
    for paragraph in new_paragraph_lst:
        content = " ".join(paragraph.content)
        content_lst.append(content)
    return content_lst


def create_image_lst(paragraph_lst):
    """
    This function returns the list of image url.
    :param paragraph_lst: a list of paragraph objects
    :return: the list of image url
    """
    image_lst = []
    new_paragraph_lst = paragraph_lst[1:]
    for paragraph in new_paragraph_lst:
        image_url = str(paragraph.image_url)
        image_lst.append(image_url)
    return image_lst


def get_paragraph_info(paragraph_titles, content, url):
    """
    This function creates the html syntax for the paragraphs from the titles, content, and url.
    :param paragraph_titles: list of paragraph titles
    :param content: list of paragraph contents
    :param url: list of url
    :return: html syntax for the paragraphs
    """
    paragraph = ""
    for i in range(0, len(content)):
        paragraph += "<h2>" + paragraph_titles[i] + "\n</h2>\n"
        paragraph += "<p>" + content[i] + "\n</p>\n"
        paragraph += "<img src=" + url[i] + ' class="center">\n'
    return paragraph


def create_file(title, color, headcolor, font, color_text, paragraph_info):
    """
    This function creates the html file from all the infomation in file and user input
    :param title: website title
    :param color: color of background
    :param headcolor: head color
    :param font: the fontstyle
    :param color_text: the text color
    :param paragraph_info: the paragraph html syntax
    :return: None
    """
    file = open("style_template.txt")
    f = open("index2.html", "a")
    html_head = "<!DOCTYPE html>\n" \
                "<html>\n" \
                "<head>\n" \
                "<title>" + title + "\n</title>"

    html_body = "\n</head>\n" \
                "<body>\n" \
                "<h1>" + title + "\n</h1>\n" \
                                 "\n<hr/>\n" + paragraph_info + "\n</html><style>"

    acc = ""
    for line in file:
        if '@BACKCOLOR' in line:
            acc += line.replace('@BACKCOLOR', color)
        elif '@HEADCOLOR' in line:
            acc += line.replace('@HEADCOLOR', headcolor)
        elif '@FONTSTYLE' in line:
            acc += line.replace('@FONTSTYLE', font)
        elif '@FONTCOLOR' in line:
            acc += line.replace('@FONTCOLOR', color_text)
        else:
            acc += line
    f.write(html_head + acc + html_body)


def get_user_input():
    """
    This function take in all user input
    Calls the list of titles, image url, and content
    create html files from the given information

    I know that I am supposed to pass in more than one txt files as parameters and connect the links. However,
    I couldn't get figure out that implementation.
    :return: None
    """
    color = str(input("Choose the name of a color, or in format '#XXXXXX': "))
    back_color = wizard_mode.get_color(color)
    print("You will now choose a font.")
    font = str(input("Do you want to see what the fonts look like? [yes] "))
    if font == "yes":
        wizard_mode.font_window()
        print("Choose a font by its number.")
        print(" 0: Arial, size 14 \n 1: Comic Sans MS, size 14 \n 2: Lucida Grande, size 14 \n 3: "
              "Tahoma, size 14 "
              "\n 4: Verdana, size 14 \n 5: Helvetica, size 14 \n 6: Times New Roman, size 14 \n")

    else:
        print("Choose a font by its number.")
        print(" 0: Arial, size 14 \n 1: Comic Sans MS, size 14 \n 2: Lucida Grande, size 14 \n 3: "
              "Tahoma, size 14 "
              "\n 4: Verdana, size 14 \n 5: Helvetica, size 14 \n 6: Times New Roman, size 14 \n")

    choose_font = int(input("Choose a number: "))
    the_font = wizard_mode.get_font(choose_font)
    print("Paragraph Text Color")
    color_text = str(input("Choose the name of a color, or in format '#XXXXXX': "))
    text_color = wizard_mode.get_color(color_text)
    print("Heading Color")
    color_head = str(input("Choose the name of a color, or in format '#XXXXXX': "))
    head_color = wizard_mode.get_color(color_head)
    file = str(input("Enter a file: "))  # I could not figure out how to pass in the files as parameter
    paragraph_lst = readfile(file)
    title = create_web_title(paragraph_lst)
    url = create_image_lst(paragraph_lst)
    paragraph_info = get_paragraph_info(create_title_list(paragraph_lst), create_content_lst(paragraph_lst), url)
    create_file(title, back_color, head_color, the_font, text_color, paragraph_info)


def main():
    """
    This function runs the program.
    :return: None
    """
    get_user_input()


if __name__ == '__main__':
    main()
