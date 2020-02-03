from os.path import dirname
import os
import datetime


def plot_preparations(title, par_list):
    """
    Prepares directory, file name and caption for a plot. 
    :param title: a title of a plot to be incorporated into a file name. 
    :param par_list: a dictionary of parameters that go to caption. 
    :return: file_name, caption, to be used later for plotting. 
    """
    # create directory for output if it doesn't exist
    parent_dir = dirname(dirname(__file__))
    output_folder = os.path.join(parent_dir, "output")

    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # create file name for plot
    now = datetime.datetime.now()
    file_name = os.path.join(output_folder, 'plot for ') + title + str(
        par_list).replace(': ', '=') + '_' + now.strftime("%H;%M;%S;%f") + \
                '.png'

    # get values out of par_list and make it string
    caption = ""
    for i, key in enumerate(par_list, start=1):
        caption += str(key) + " = " + str(par_list[key])
        if i % 3 == 0:
            caption += "\n"
        elif i != len(par_list):
            caption += ", "

    return file_name, caption
