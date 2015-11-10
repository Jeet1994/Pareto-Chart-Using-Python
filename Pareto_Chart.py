from paretochart import pareto #Importing the required dependancies.

data = [123, 22, 33, 24, 2425, 5625, 112, 11233, 1200, 2356]
#Feeding the Dummy Data. It is the number of counts of Deaths due to various reasons.

labels = ['Epidemic', 'Diabetes', 'Suicide', 'Food Poisoning', 'Domestic Violence', 'Natural Disaster', 'Industrial Accidents', 'Unknown', 'Terrorism']
#Thses are the reasons why people died.

import matplotlib.pyplot as jeet
#importing matplotlib as my name.

fig, axes = jeet.subplots(2, 2)
#Alloting space for grids of subplots

pareto(data, axes=axes[0, 0]) 
jeet.title('Basic chart without labels', fontsize=9)
#This is the first plot and it will have only the data visualisation.

pareto(data, labels, axes=axes[0, 1], limit=0.75, line_args=('r',))
jeet.title('Data with labels, red cum. line, limit= 75%', fontsize=9)
#In the second plot, we have added labels and have put a cumulative limit  75% and turn the cumulative line blue


pareto(data, labels, cumplot=False, axes=axes[1, 0], data_kw={'width': 0.1,'color': 'b'})
jeet.title('Data without cum. line, blue bar width=0.1', fontsize=9)
#In the third plot,we have removed the cumulative line and the limit line, making the bars blue. Just a tweak for visualistion.

pareto(data, labels, limit=0.95, axes=axes[1, 1], limit_kw={'color': 'g'})
jeet.title('Data trimmed at 95%, green limit line', fontsize=10)
#In the fourth plot,we have put the cumullative limit at 95% and made the line green.


fig.canvas.set_window_title('Pareto Plot')
jeet.show()
#This is the final image. This is a matplotlib function to display the function.
