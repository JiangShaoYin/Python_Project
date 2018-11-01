#!   /usr/bin/python
#    coding:utf-8
 
 
import tensorflow as tf
import numpy as np
import random as rd

capitals ={'Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix',
        'Arkansas':'Little Rock','California':'Sacramento', 'Colorado':'Denver',
        'Conectticut':'Hartford','Delaware':'Dover','Florida':'Tallahassee',
        'Georgia':'Atlanta', 'Hawaii':'Honolulu', 'Idaho':'Boise','Illinois':'Springfield',
        'Indiana':'Indianapolis', 'Iowa':'Des Moines','Kansas':'Topeka',
        'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge', 'Maine':'Augusta',
        'Maryland':'Annapolis','Massachusetts':'Boston', 'Michigan':'Lansing',
        'Minnesota':'Saint Paul','Mississipppi':'Jackson', 'Missouri':'Jerferson City',
        'Montana':'Helena','Nebraska':'Lincoln', 'Nevada':'Carson City','New Hampshire':'Concord',
        'Newjersey':'Trenton', 'New Mexico':'Santa Fe','New York':'Albany', 'North Carolina':'Raleigh'
        'North Dakota':'Bismarcck', 'Ohio':'Columbus', 'Oklahoma':'Oklahoma City'
        'Oregon':'Salem', 'Pennsylvania':'Harrisburg', 'Rhode Island':'Providence',
        'South Carolina':'Columbia', 'South Dakota':'Pierre', 'Tennessee':'Nashville'
        'Texas':'Austin', 'Utah':'Salt Lake City','Vermont':'Montpelier', 'Virginia':'Richmond',
        'Washington':'Olypia', 'WestVirginia':'Charlesston', 'Wisconsin':'Madison','Wyoming','cheyenne'}

#generate 35 quiz file
for quiz_num in range(35):
    quiz_file = open('capitals_quiz%s.txt' % quiz_num, 'w')       #filename: capitals_quiz1.txt
    answer_file = open('answer%s.txt'%quiz_num,'w')               #%s,%d?difference?

    #write out the header of the quiz
    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((''*20)+'State Capitals Quiz(Form %s)' % quiz_num +'\n\n')

    #shuffle the order of the states
    states = list(capital)




