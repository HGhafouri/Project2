from tkinter import *
import tkinter as tk
from tkinter import ttk
import pandas as pd
import pickle
import numpy as np

import os
import pandas as pd
import seaborn as sns
from datetime import datetime
import matplotlib.pylab as plt
import numpy as np


root = Tk()
root.geometry("250x520")
root.title("UptoData")


file_to_read = open("test_H.pickle", "rb")
stest2 = pickle.load(file_to_read)
file_to_read.close()


file_to_read = open("model_H.pickle", "rb")
model = pickle.load(file_to_read)
file_to_read.close()

# print(model.predict(np.array(stest2).reshape(1,-1)))
# print(stest2)


def Take_input():

    
    Bedrooms = inputtxt.get("1.0", "end-1c")
    
    Beds = inputtxt2.get("1.0", "end-1c")


    Accommodates = inputtxt3.get("1.0", "end-1c")

    minimumNights = inputtxt4.get("1.0", "end-1c")

    availability_90 = inputtxt5.get("1.0", "end-1c")

    host_listings_count = inputtxt6.get("1.0", "end-1c")

    review_scores_location = inputtxt7.get("1.0", "end-1c")




    for _ in regions:
        stest2[_] = 0
    for _ in rooms:
        stest2[_] = 0

    stest2[str(regionchoosen.get())] = 1
    stest2[str(roomchoosen.get())] = 1

    stest2['bedrooms'] = int(Bedrooms)
    stest2['beds'] = int(Beds)
    stest2['accommodates'] = int(Accommodates)

    stest2['minimum_nights'] = int(minimumNights)
    stest2['availability_90'] = int(availability_90)
    stest2['host_listings_count'] = float(host_listings_count)
    stest2['review_scores_location'] = float(review_scores_location)


    print(stest2)
    print(stest2['bedrooms'])
    print(stest2['beds'])
    print(stest2['accommodates'])
    print(stest2['minimum_nights'])
    print(stest2['availability_90'])
    print(stest2['host_listings_count'])
    print(stest2['review_scores_location'])




    price = model.predict((stest2))
    print('price',price)

    Output.delete('1.0', END)
    Output.insert(END,'price: ' + str(price[0]))




    # Output.delete('1.0', END)
    # try:
    #     if regionchoosen.get() == 'Equation1':
            
    #         Output.insert(END,float(INPUT) + float(INPUT2)**2)
    #         print(float(INPUT) + float(INPUT2)**2)

    #     elif regionchoosen.get() == 'Equation2':
            
    #         Output.insert(END,float(INPUT) + float(INPUT2))
    #         print(float(INPUT) + float(INPUT2))

    # except:
    #     Output.insert(END,'Sth wrong!!!')
    #     print('Sth wrong!!!')


regions =  ("N_South Parkdale","N_Oakridge","N_Wexford/Maryvale","N_Rosedale-Moore Park","N_Bay Street Corridor","N_South Riverdale","N_Church-Yonge Corridor","N_Niagara","N_Dufferin Grove","N_Waterfront Communities-The Island","N_Danforth East York","N_High Park-Swansea","N_Woburn","N_Humewood-Cedarvale","N_Junction Area","N_Little Portugal","N_Cabbagetown-South St.James Town","N_Annex","N_Caledonia-Fairbank","N_Roncesvalles","N_Casa Loma","N_North St.James Town","N_Leaside-Bennington","N_Blake-Jones","N_High Park North","N_Willowdale East","N_The Beaches","N_Danforth","N_Moss Park","N_University","N_Flemingdon Park","N_East End-Danforth","N_Woodbine Corridor","N_Brookhaven-Amesbury","N_Oakwood Village","N_Dovercourt-Wallace Emerson-Junction","N_Palmerston-Little Italy","N_Weston-Pellam Park","N_Morningside","N_Kensington-Chinatown","N_Mount Pleasant West","N_Don Valley Village","N_Thistletown-Beaumond Heights","N_Forest Hill South","N_Pleasant View","N_Newtonbrook West","N_Broadview North","N_Playter Estates-Danforth","N_Greenwood-Coxwell","N_North Riverdale","N_Mimico (includes Humber Bay Shores)","N_Trinity-Bellwoods","N_Scarborough Village","N_Yorkdale-Glen Park","N_Islington-City Centre West","N_Regent Park","N_Parkwoods-Donalda","N_Taylor-Massey","N_Old East York","N_Stonegate-Queensway","N_Corso Italia-Davenport","N_St.Andrew-Windfields","N_Birchcliffe-Cliffside","N_Yonge-Eglinton","N_Bayview Village","N_Lawrence Park North","N_Bendale","N_Englemount-Lawrence","N_Mount Dennis","N_Kennedy Park","N_Clanton Park","N_Willowdale West","N_Bayview Woods-Steeles","N_Mount Pleasant East","N_Cliffcrest","N_Yonge-St.Clair","N_New Toronto","N_Agincourt North","N_Newtonbrook East","N_O'Connor-Parkview","N_Etobicoke West Mall","N_Bedford Park-Nortown","N_Rockcliffe-Smythe","N_Guildwood","N_L'Amoreaux","N_Lambton Baby Point","N_Woodbine-Lumsden","N_Bridle Path-Sunnybrook-York Mills","N_Wychwood","N_Runnymede-Bloor West Village","N_Tam O'Shanter-Sullivan","N_Lansing-Westgate","N_Long Branch","N_York University Heights","N_Lawrence Park South","N_Westminster-Branson","N_Hillcrest Village","N_Keelesdale-Eglinton West","N_Bathurst Manor","N_Agincourt South-Malvern West","N_Ionview","N_Pelmo Park-Humberlea","N_Clairlea-Birchmount","N_Kingsway South","N_Eglinton East","N_Eringate-Centennial-West Deane","N_West Humber-Clairville","N_Highland Creek","N_Princess-Rosethorn","N_Black Creek","N_Beechborough-Greenbrook","N_Edenbridge-Humber Valley","N_Alderwood","N_Rouge","N_Rexdale-Kipling","N_Downsview-Roding-CFB","N_Willowridge-Martingrove-Richview","N_Victoria Village","N_Banbury-Don Mills","N_Henry Farm","N_Markland Wood","N_Dorset Park","N_Thorncliffe Park","N_West Hill","N_Malvern","N_Weston","N_Mount Olive-Silverstone-Jamestown","N_Kingsview Village-The Westway","N_Humber Heights-Westmount","N_Glenfield-Jane Heights","N_Steeles","N_Elms-Old Rexdale","N_Forest Hill North","N_Milliken","N_Maple Leaf","N_Humbermede","N_Centennial Scarborough","N_Humber Summit","N_Rustic")
rooms = ("R_Entire home/apt","R_Shared room","R_Hotel room")


l1 = Label(text = "choose a neighboorhood")

n = tk.StringVar()

m = tk.StringVar()

regionchoosen = ttk.Combobox(root, width = 23, textvariable = n)
regionchoosen['values'] = regions

l2 = Label(text = "choose room type ")

roomchoosen = ttk.Combobox(root, width = 23, textvariable = m)
roomchoosen['values'] = rooms

l3 = Label(text = "Enter Number of bedrooms ")
inputtxt = Text(root, height = 3,
                width = 23,
                bg = "light yellow")

l4 = Label(text = "Enter Number of beds ")
inputtxt2 = Text(root, height = 3,
                width = 23,
                bg = "light yellow")

l5 = Label(text = "Number of accommodates ")
inputtxt3 = Text(root, height = 3,
                width = 23,
                bg = "light yellow")

l6 = Label(text = "Minimum nights")
inputtxt4 = Text(root, height = 3,
                width = 23,
                bg = "light yellow")

l7 = Label(text = "Listing Availability (Past 3 months)")#availability_90
inputtxt5 = Text(root, height = 3,
                width = 23,
                bg = "light yellow")

l8 = Label(text = "Number of Host Listings ")#host_listings_count
inputtxt6 = Text(root, height = 3,
                width = 23,
                bg = "light yellow")

l9 = Label(text = "Review scores location")#review_scores_location
inputtxt7 = Text(root, height = 3,
                width = 23,
                bg = "light yellow")

############################################################################
Output = Text(root, height = 3,
              width = 23,
              bg = "light cyan")
 
Display = Button(root, height = 1,
                 width = 20,
                 text ="Show the Price",
                 command = lambda:Take_input())


l1.pack()
regionchoosen.pack()
regionchoosen.current()

l2.pack()
roomchoosen.pack()
roomchoosen.current()

l3.pack()
inputtxt.pack()

l4.pack()
inputtxt2.pack()

l5.pack()
inputtxt3.pack()

l6.pack()
inputtxt4.pack()

l7.pack()
inputtxt5.pack()

l8.pack()
inputtxt6.pack()

l9.pack()
inputtxt7.pack()

Display.pack()
Output.pack()


mainloop()