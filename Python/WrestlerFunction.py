"""
Within the world of wrestling, there are winners and there are losers.
The winners are labeled as "Superstars" while the losers are given the 
lowly title of "Jobber". Using a function, create the code necessary to 
search through a list of wrestlers, determine their win, loss, and draw percentages.
"""

# module declaration 
import os 
import csv 

# path to the data file 
cwd = os.getcwd()
file_path = os.path.join(cwd,"Python/data/WWE-Data-2016.csv")

# data collecter 
new_wrestler_data = []

# using with, open the file
with open(file_path,'r') as f:

    file = csv.reader(f,delimiter =',') # file reading handler
    next(file) # skipping the title row

    for row in file:
        total_games = float(row[1]) + float(row[2]) + float(row[3]) 
        total_win_percentage = round(float(row[1])/total_games,2) *100
        total_loss_percentage = round(float(row[2])/total_games,2) *100
        total_draw_percentage = round(float(row[3])/total_games,2) *100
        status = 'none'

        if total_win_percentage > 50.0: 
            status = "Superstar"
        else:
            status = "Loser"
        
        new_wrestler_data.append([
                              row[0], # wrestler name
                              total_games, # wins + loss + draw
                              row[1], # wins
                              total_win_percentage, 
                              row[2], # losses
                              total_loss_percentage,
                              row[3], # draw
                              total_draw_percentage,
                              status])

def get_wrestler_info(wrestler):
    
    for i in new_wrestler_data:
        if wrestler == i[0]:
            print("Stats for " + i[0])
            print("WIN PERCENT: " + str(i[3]))
            print("LOSS PERCENT: " + str(i[5]))
            print("DRAW PERCENT: " + str(i[7]))
            print(i[0] + " is a " + i[8])

get_wrestler_info("AJ Styles")
