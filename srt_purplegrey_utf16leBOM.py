#!/usr/bin/python

import sys, getopt
import os.path
from os import path

#font_color_code = "#333333" #Here you can define your desired colour code
font_color_code = "#666699" #Here you can define your desired colour code
file_suffix = "Purplefont" #Here you can define your desired default suffix of output filename

if len(sys.argv) > 1: #Run script only if filename is passed as argument
    #if !path.isfile(sys.argv[1]):
    #input file

    #fin = open(sys.argv[1], "rt") #filename is passed as argument-1

    #output file to write the result to
    if len(sys.argv)>2: #Output filename is passed as argument-2
        fout = open(sys.argv[2], "wt")
    else: #If no output file is defined, original file with "greyfont_" as suffix will be used
        fout = open(sys.argv[1].rpartition(".")[0]+"."+file_suffix+"."+sys.argv[1].rpartition(".")[2], "wt")
    #for each line in the input file
    lcount = 1
    rownum = 1

    with open(sys.argv[1], 'rt', encoding='utf-16le') as fin:
        while True:
            # Get next line from file

            line = fin.readline()

            # For debug purpose, show what it read from line
            # print(line.strip())
            linecontent = line.strip()

            if not line:
                break

            # Replace the string and write to output file
            if linecontent == "": # Empty line means end of section
                rownum = 1 # reset to rownum 1 if empty line is found
                # write file statement should be placed directly
                # for debug purpose
                #print("EMPTY LINE FOUND -->"+" Lcount is "+str(lcount)+" Line Content "+linecontent+ "\r\n")
                fout.write(linecontent + "\r\n")
            elif rownum == 1: # Row number 1 here
                rownum = 2 # increase rownum to 2 for next check
                # for debug purpose
                #print("Line No 1 - BINGO"+" Lcount is "+str(lcount)+" Line Content "+linecontent+ "\r\n")
                # write file statement should be placed directly
                fout.write(linecontent + "\r\n")
            elif rownum == 2:
            #and linecontent[2:3] == ":": # Row number 2 here, also double check if ":" is found for line 2 cue time formatted content
                rownum = 3 # increase rownum to 3 for next check
                # for debug purpose
                #print("Line No 2 is here"+" Lcount is "+str(lcount)+" Line Content "+linecontent+ "\r\n")
                # write file statement should be placed directly
                fout.write(linecontent + "\r\n")
            elif rownum > 2:
                rownum = rownum + 1
                # for debug purpose
                #print("Line No > 2 , Row no is "+str(rownum)+" Lcount is "+str(lcount)+" Line Content "+linecontent)
                # Add new color effect to the content here
                #print('<font color="'+font_color_code+'">'+linecontent+'</font>'+ "\r\n")
                fout.write('<font color="'+font_color_code+'">'+linecontent+'</font>' + "\r\n")
            #lcount = lcount+1 # line counter increment
            lcount += 1 # line counter increment
        fin.close()
        fout.close()
else:
    print("Please specify the filename of the SRT file to be modified, \n\rCOMMAND: srt_grey.py input_subtitle_file.srt [***Optional_output_subtitle_file.srt]\n\r")
    print("*** If no output filename is defined, original file with "+"."+file_suffix+"."+" as suffix will be used")
