# set_srt_colour.py

This Python script is for applying custom subtitle text colour by adding your desired colour attribute into subtitle file in SRT format.  

# BACKGROUND
The reason why I drafted this script is due to the imperfection of the feature of dynamic LED brightness for my BenQ X12000H Projector.  The pure white or any preset color of font style for subtitle will trigger the dynamic brightness in dark scene, which makes the whole dark scene too bright or we will say grey-out seriously as a result.  It affects the mood of the scnene and the movie at the end.  In order to fix this, I had the POC to see if subtitle in dark grey colour can be a tricks not to trigger projector built-in dynamic brightness feature in dark scene.  BINGO!!! It works flawlessly!!!  But I am not going to edit subtitle file one by one manually for the purpose. Therefore, this python script is born.

# PREREQUISITION
It's simple a Python script so Python is a must, please ensure your system having python installed

Python download link here just in case
https://www.python.org/downloads/

# HOW TO USE
Run it in "command prompt" for Windows system, "Terminal" for Macintosh system, or even in NAS with Python environment installed.
  
The script is looking for 2 arguments, the last one is optional.</br>
    1st argument is the filename of the original srt file,</br>
    2nd argument is the optional output filename to be desired (You can skip it for sure. *** If no output filename is defined, original file with suffix defined in the script ".greyfont." as suffix will be used)
)

Below is the format of the command</br>
    sh% python set_srt_colour.py input_subtitle_file.srt [***Optional_output_subtitle_file.srt]

REMARKS:
    You can redefine your desired colour as well as the default suffix of the output file in the script as following
  
    font_color_code = "#333333" #Here you can define your desired colour code
    file_suffix = "greyfont" #Here you can define your desired default suffix of output filename
