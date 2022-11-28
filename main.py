import inline
import matplotlib as matplotlib

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl


# belowed function intializes the plot give the name to the axes and clears the current figures and also
# don't plot any data in it we can also initialize the limit on x and y axes by just modifying the belowed
# function plt.xlim(-1,9) plt.ylim(24,18)




#we are writing a function who gonna save a values in text file this function kinda of saving the results
#we obtained from the condions we use here

def WriteCatalog(adressoffile, actualParameter, NameofParameter ):
    Catlog = open(adressoffile,'w')

    #we are writing the 1st Row of the Catlog which actually the header
    Catlog.write('#' + NameofParameter + '\n')
    #Now we are adding the values of the Parameters into the catalog so

    for i in range(len(actualParameter[0])): #Here we are iterating across no of rows = length of Single Column
        for j in range(len(actualParameter)): # across no of Columns i.e RA, DEC, XI...
            Catlog.write(str(actualParameter[j][i]))
            Catlog.write(' ')
        Catlog.write('\n') #Stating new line i.e new row i.e adding new row
    Catlog.close()
    return

#Okay, now that we have all our packages imported, we are ready to get to the science! The first
# thing we need to do is read in the file that contains all our data. This file contains the
# coordinates (ra, dec, xi, eta), the magnitudes (in two different bandpasses), and the velocities of
# all our stars (we will talk more about velocities next!).

#As we discussed, the color of the star is a very useful and important quantity; we define the array
# for "color" below.


ra, dec, xi, eta, f475w, f814w, v, verr = np.loadtxt('keck_hst_data.txt', unpack=True)
color = f475w-f814w


plt.scatter(color, f814w, c='grey', s=3, edgecolors='none' )

#========From here on is the part that you're going to copy and
#adapt for the RGB and AGB stars===============================

#Where condition to isolate main sequence stars
ms = (color < 1.75) & (f814w < 23)

#Plot MS stars in blue on the plot and label that region

plt.scatter(color, f814w, c = 'gray', s = 3, edgecolors = 'none')
plt.scatter(color[ms], f814w[ms], c = 'blue', edgecolors = 'none', s = 5)
plt.text(-0.5, 23.5, 'MS', color = 'blue', size = 16)

#Write a text file containing information for MS stars by calling the
#WriteCatalog function on the stars that satisfy the MS condition.
#You shouldn't modify the WriteCatalog function itself;
#only copy and modify the line below for the AGB and RGB groups.
WriteCatalog('MScatalog.txt',[ra[ms], dec[ms], xi[ms], eta[ms], f475w[ms], f814w[ms], v[ms], verr[ms]],'RA DEC XI ETA F475W F814W V VERR')

#==============================================================
#Replace a, h, and k with numbers, and see what happens
#rgb= (color > 1.75 ) & (f814w > a*(color-h)**2.+k)
##Add the RGB stars to the plot!
a=0.08
h=2
k=20.5
rgb= (color > 1.75 ) & (f814w > a*(color-h)**2.+k)
#Plot RGB stars in blue on the plot and label that region

plt.scatter(color[rgb], f814w[rgb], c = 'red', edgecolors = 'none', s = 5)
plt.text(6, 23.5, 'RGB', color = 'red', size = 16)

#Write a text file containing information for MS stars by calling the
#WriteCatalog function on the stars that satisfy the MS condition.
#You shouldn't modify the WriteCatalog function itself;
#only copy and modify the line below for the AGB and RGB groups.
WriteCatalog('RGBcatalog.txt',[ra[rgb], dec[rgb], xi[rgb], eta[rgb], f475w[rgb], f814w[rgb], v[rgb], verr[rgb]], 'RA DEC XI ETA F475W F814W V VERR')

#Write the catalog here when you're happy with your selection!
#Then, add the AGB stars to the plot and write an AGB catalog as well!
#==============================================================
##Add the RGB stars to the plot!
a=0.08
h=2
k=20.5
agb= (color > 1.75 ) & (f814w < a*(color-h)**2.+k)
#Plot AGB stars in green on the plot and label that region

plt.scatter(color[agb], f814w[agb], c = 'green', edgecolors = 'none', s = 5)
plt.text(6, 18.5, 'AGB', color = 'green', size = 16)

#Write a text file containing information for MS stars by calling the
#WriteCatalog function on the stars that satisfy the MS condition.
#You shouldn't modify the WriteCatalog function itself;
#only copy and modify the line below for the AGB and RGB groups.
WriteCatalog('AGBcatalog.txt',[ra[agb], dec[agb], xi[agb], eta[agb], f475w[agb], f814w[agb], v[agb], verr[agb]],'RA DEC XI ETA F475W F814W V VERR')
plt.xlabel('F475w-F814w (mag)')
plt.ylabel('F814w (mag)')
plt.xlim(-1, 9)
plt.ylim(24, 18)
plt.figure(figsize=(7,7))


# Determine what fraction of the entire catalog are selected by the MS, RGB, and AGB criteria
nstars = len(color)
print('Fraction of stars on the MS: {0:.3f}'.format(np.sum(ms)/nstars))
print('Fraction of stars on the RGB: {0:.3f}'.format(np.sum(rgb)/nstars))
print('Fraction of stars on the AGB: {0:.3f}'.format(np.sum(agb)/nstars))
selected = ms | rgb | agb
print('Fraction of stars not selected: {0:.3f}'.format(np.sum(~selected)/nstars))
plt.show()