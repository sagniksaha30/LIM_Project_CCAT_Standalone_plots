#Define necessary functions.
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def save_array_to_file(array, file_name, delimiter='\n'):
    with open(file_name, 'a') as file:
        if file.tell() != 0:  # Check if the file is not empty
            file.write(delimiter)
        file.write(','.join(map(str, array)))

def read_arrays_from_file(file_name, delimiter='\n'):
    values = []
    with open(file_name, "r") as file:
        # Read each line from the file
        for line in file:
            # Convert the line to an integer and append it to the array
            value = float(line.strip())
            values.append(value)
    return values

def read_arrays_from_file_commas(file_name):

    values = []
    with open(file_name, "r") as file:
        # Read the file content as a single string and split it by commas
        data = file.read()
        value_strings = data.split(',')
        # Convert the value strings to floats and append them to the array
        for value_str in value_strings:
            value = float(value_str.strip())
            values.append(value)

    return values

#Read necessary files.
#Get the fit line.
best_fit_x = read_arrays_from_file_commas('bestfit_x.txt')
best_fit_y1 = read_arrays_from_file_commas('bestfit_y1.txt')
best_fit_y2 = read_arrays_from_file_commas('bestfit_y2.txt')
best_fit_y3 = read_arrays_from_file_commas('bestfit_y3.txt')
best_fit_y4 = read_arrays_from_file_commas('bestfit_y4.txt')

#Now plot the CCAT data points.
xaxis = read_arrays_from_file('xaxis.txt')
p1_y = read_arrays_from_file('plot1_yaxis.txt')
p1_err = read_arrays_from_file('plot1_errors.txt')

p2_y = read_arrays_from_file('plot2_yaxis.txt')
p2_err = read_arrays_from_file('plot2_errors.txt')

p3_y = read_arrays_from_file('plot3_yaxis.txt')
p3_err = read_arrays_from_file('plot3_errors.txt')

p4_y = read_arrays_from_file('plot4_yaxis.txt')
p4_err = read_arrays_from_file('plot4_errors.txt')

#Plot the other surveys.
#eboss
x_eboss = read_arrays_from_file('z_eboss.txt')

eboss_y1 = read_arrays_from_file('eboss_y1.txt')
eboss_y2 = read_arrays_from_file('eboss_y2.txt')
eboss_y3 = read_arrays_from_file('eboss_y3.txt')
eboss_y4 = read_arrays_from_file('eboss_y4.txt')

eboss_err1 = read_arrays_from_file('eboss_err1.txt')
eboss_err2 = read_arrays_from_file('eboss_err2.txt')
eboss_err3 = read_arrays_from_file('eboss_err3.txt')
eboss_err4 = read_arrays_from_file('eboss_err4.txt')

#desi
x_desi = read_arrays_from_file_commas('z_desi.txt')

desi_y1 = read_arrays_from_file_commas('desi_y1.txt')
desi_y2 = read_arrays_from_file_commas('desi_y2.txt')
desi_y3 = read_arrays_from_file_commas('desi_y3.txt')
desi_y4 = read_arrays_from_file_commas('desi_y4.txt')

desi_err1 = read_arrays_from_file_commas('desi_err1.txt')
desi_err2 = read_arrays_from_file_commas('desi_err2.txt')
desi_err3 = read_arrays_from_file_commas('desi_err3.txt')
desi_err4 = read_arrays_from_file_commas('desi_err4.txt')

#desi_bgs
x_desi_bgs = read_arrays_from_file_commas('z_desi_bgs.txt')

desi_bgs_y1 = read_arrays_from_file_commas('desi_bgs_y1.txt')
desi_bgs_y2 = read_arrays_from_file_commas('desi_bgs_y2.txt')
desi_bgs_y3 = read_arrays_from_file_commas('desi_bgs_y3.txt')
desi_bgs_y4 = read_arrays_from_file_commas('desi_bgs_y4.txt')

desi_bgs_err1 = read_arrays_from_file_commas('desi_bgs_err1.txt')
desi_bgs_err2 = read_arrays_from_file_commas('desi_bgs_err2.txt')
desi_bgs_err3 = read_arrays_from_file_commas('desi_bgs_err3.txt')
desi_bgs_err4 = read_arrays_from_file_commas('desi_bgs_err4.txt')

#desi_Lya
x_desi_Lya = read_arrays_from_file_commas('z_desi_Lya.txt')

desi_Lya_y1 = read_arrays_from_file_commas('desi_Lya_y1.txt')
desi_Lya_y2 = read_arrays_from_file_commas('desi_Lya_y2.txt')
desi_Lya_y3 = read_arrays_from_file_commas('desi_Lya_y3.txt')
desi_Lya_y4 = read_arrays_from_file_commas('desi_Lya_y4.txt')

desi_Lya_err1 = read_arrays_from_file_commas('desi_Lya_err1.txt')
desi_Lya_err2 = read_arrays_from_file_commas('desi_Lya_err2.txt')
desi_Lya_err3 = read_arrays_from_file_commas('desi_Lya_err3.txt')
desi_Lya_err4 = read_arrays_from_file_commas('desi_Lya_err4.txt')

#bossdr12
x_bossdr12 = read_arrays_from_file_commas('z_bossdr12.txt')

bossdr12_y1 = read_arrays_from_file_commas('bossdr12_y1.txt')
bossdr12_y2 = read_arrays_from_file_commas('bossdr12_y2.txt')
bossdr12_y3 = read_arrays_from_file_commas('bossdr12_y3.txt')
bossdr12_y4 = read_arrays_from_file_commas('bossdr12_y4.txt')

bossdr12_err1 = read_arrays_from_file_commas('bossdr12_err1.txt')
bossdr12_err2 = read_arrays_from_file_commas('bossdr12_err2.txt')
bossdr12_err3 = read_arrays_from_file_commas('bossdr12_err3.txt')
bossdr12_err4 = read_arrays_from_file_commas('bossdr12_err4.txt')

#bossdr14
x_bossdr14 = read_arrays_from_file_commas('z_bossdr14_Lya.txt')

bossdr14_y1 = read_arrays_from_file_commas('bossdr14_Lya_y1.txt')
bossdr14_y2 = read_arrays_from_file_commas('bossdr14_Lya_y2.txt')
bossdr14_y3 = read_arrays_from_file_commas('bossdr14_Lya_y3.txt')
bossdr14_y4 = read_arrays_from_file_commas('bossdr14_Lya_y4.txt')

bossdr14_err1 = read_arrays_from_file_commas('bossdr14_Lya_err1.txt')
bossdr14_err2 = read_arrays_from_file_commas('bossdr14_Lya_err2.txt')
bossdr14_err3 = read_arrays_from_file_commas('bossdr14_Lya_err3.txt')
bossdr14_err4 = read_arrays_from_file_commas('bossdr14_Lya_err4.txt')

#zsx_halpha
x_zsx_halpha = read_arrays_from_file_commas('zsx_halpha.txt')
zsx_halpha_y1 = read_arrays_from_file_commas('zsx_halpha_y1.txt')
zsx_halpha_y2 = read_arrays_from_file_commas('zsx_halpha_y2.txt')
zsx_halpha_y3 = read_arrays_from_file_commas('zsx_halpha_y3.txt')
zsx_halpha_y4 = read_arrays_from_file_commas('zsx_halpha_y4.txt')

zsx_halpha_err1 = read_arrays_from_file_commas('zsx_halpha_err1.txt')
zsx_halpha_err2 = read_arrays_from_file_commas('zsx_halpha_err2.txt')
zsx_halpha_err3 = read_arrays_from_file_commas('zsx_halpha_err3.txt')
zsx_halpha_err4 = read_arrays_from_file_commas('zsx_halpha_err4.txt')

#zsx_lyalpha
x_zsx_lyalpha = read_arrays_from_file_commas('zsx_lyalpha.txt')

zsx_lyalpha_y1 = read_arrays_from_file_commas('zsx_lyalpha_y1.txt')
zsx_lyalpha_y2 = read_arrays_from_file_commas('zsx_lyalpha_y2.txt')
zsx_lyalpha_y3 = read_arrays_from_file_commas('zsx_lyalpha_y3.txt')
zsx_lyalpha_y4 = read_arrays_from_file_commas('zsx_lyalpha_y4.txt')

zsx_lyalpha_err1 = read_arrays_from_file_commas('zsx_lyalpha_err1.txt')
zsx_lyalpha_err2 = read_arrays_from_file_commas('zsx_lyalpha_err2.txt')
zsx_lyalpha_err3 = read_arrays_from_file_commas('zsx_lyalpha_err3.txt')
zsx_lyalpha_err4 = read_arrays_from_file_commas('zsx_lyalpha_err4.txt')

#comap1
x_comap1 = read_arrays_from_file('z_comap1.txt')

comap1_y1 = read_arrays_from_file('z_comap1_y1.txt')
comap1_y2 = read_arrays_from_file('z_comap1_y2.txt')
comap1_y3 = read_arrays_from_file('z_comap1_y3.txt')
comap1_y4 = read_arrays_from_file('z_comap1_y4.txt')

comap1_err1 = read_arrays_from_file('z_comap1_err1.txt')
comap1_err2 = read_arrays_from_file('z_comap1_err2.txt')
comap1_err3 = read_arrays_from_file('z_comap1_err3.txt')
comap1_err4 = read_arrays_from_file('z_comap1_err4.txt')

#comap
x_comap = read_arrays_from_file('z_comap.txt')

comap_y1 = read_arrays_from_file('z_comap_y1.txt')
comap_y2 = read_arrays_from_file('z_comap_y2.txt')
comap_y3 = read_arrays_from_file('z_comap_y3.txt')
comap_y4 = read_arrays_from_file('z_comap_y4.txt')

comap_err1 = read_arrays_from_file('z_comap_err1.txt')
comap_err2 = read_arrays_from_file('z_comap_err2.txt')
comap_err3 = read_arrays_from_file('z_comap_err3.txt')
comap_err4 = read_arrays_from_file('z_comap_err4.txt')

#ims3
x_ims3 = read_arrays_from_file_commas('z_ims3.txt')

ims3_y1 = read_arrays_from_file_commas('z_ims3_y1.txt')
ims3_y2 = read_arrays_from_file_commas('z_ims3_y2.txt')
ims3_y3 = read_arrays_from_file_commas('z_ims3_y3.txt')
ims3_y4 = read_arrays_from_file_commas('z_ims3_y4.txt')

ims3_err1 = read_arrays_from_file_commas('z_ims3_err1.txt')
ims3_err2 = read_arrays_from_file_commas('z_ims3_err2.txt')
ims3_err3 = read_arrays_from_file_commas('z_ims3_err3.txt')
ims3_err4 = read_arrays_from_file_commas('z_ims3_err4.txt')

print('success')


#####PLOTTING STARTS HERE #########
#Make H(z) plots.

#Plot 1
color = plt.rcParams['axes.prop_cycle'].by_key()['color']
f, ax = plt.subplots(2,1, gridspec_kw = {'hspace':0,'height_ratios':[5,3],'top':.98,'right':.98}, sharex='col',figsize=(10,7))

ax[0].plot(best_fit_x,best_fit_y1,lw=1.5,c='k',zorder=0,ls='--')

ax[0].errorbar(x_eboss,eboss_y1,yerr=eboss_err1,capsize=2,capthick=1,color=color[4],zorder=2,ls='',alpha=0.8)
ax[0].scatter(x_eboss,eboss_y1,color=color[4],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,label='BOSS/eBOSS',alpha=0.8)

ax[0].errorbar(x_desi,desi_y1,yerr=desi_err1,capsize=2,capthick=1,color=color[1],zorder=1,ls='',alpha=0.8)
ax[0].errorbar(x_desi_bgs,desi_bgs_y1,yerr=desi_bgs_err1,capsize=2,capthick=1,color=color[1],zorder=1,ls='',alpha=0.8)
ax[0].errorbar(x_desi_Lya,desi_Lya_y1,yerr=desi_Lya_err1,capsize=2,capthick=1,color=color[1],lw=1,zorder=1,ls='',alpha=0.8)
ax[0].scatter(x_desi,desi_y1,color=color[1],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[0].scatter(x_desi_bgs,desi_bgs_y1,color=color[1],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[0].scatter(x_desi_Lya,desi_Lya_y1,color=color[1],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,label='DESI',alpha=0.8)
ax[0].errorbar(x_bossdr12,bossdr12_y1,yerr=bossdr12_err1,capsize=2,capthick=1,color=color[4],zorder=1,ls='',alpha=0.8)
ax[0].scatter(x_bossdr12,bossdr12_y1,color=color[4],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[0].errorbar(x_bossdr14,bossdr14_y1,yerr=bossdr14_err1,capsize=2,capthick=1,color=color[4],zorder=1,ls='',alpha=0.8)
ax[0].scatter(x_bossdr14,bossdr14_y1,color=color[4],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[0].errorbar(x_zsx_halpha,zsx_halpha_y1,elinewidth=2,capsize=6,capthick=2,yerr=zsx_halpha_err1,color=color[2],zorder=1,ls='')
ax[0].scatter(x_zsx_halpha,zsx_halpha_y1,color=color[2],marker='o',s=50,edgecolors='k',lw=1,zorder=2,label=r'SPHEREx (H$\alpha$)')
ax[0].errorbar(x_zsx_lyalpha,zsx_lyalpha_y1,elinewidth=2,capsize=6,capthick=2,yerr=zsx_lyalpha_err1,color='r',zorder=1,ls='')
ax[0].scatter(x_zsx_lyalpha,zsx_lyalpha_y1,color='r',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label=r'SPHEREx (Ly$\alpha$)')
ax[0].errorbar(x_comap1,comap1_y1,elinewidth=2,capsize=6,capthick=2,yerr=comap1_err1,color='fuchsia',zorder=1,ls='')
ax[0].scatter(x_comap1,comap1_y1,color='fuchsia',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='COMAP1')
ax[0].errorbar(x_comap,comap_y1,elinewidth=2,capsize=6,capthick=2,yerr=comap_err1,color='blue',zorder=1,ls='')
ax[0].scatter(x_comap,comap_y1,color='blue',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='COMAP2')
ax[0].errorbar(x_ims3,ims3_y1,elinewidth=2,capsize=6,capthick=2,yerr=ims3_err1,color='c',zorder=1,ls='')
ax[0].scatter(x_ims3,ims3_y1,color='c',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='IMS3 (CO)')


#CCAT1
ax[0].errorbar(xaxis[0],p1_y[0],elinewidth=2,capsize=6,capthick=2,yerr=p1_err[0],color='y',zorder=1,ls='')
ax[0].scatter(xaxis[0],p1_y[0],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='CCAT')

#CCAT2
ax[0].errorbar(xaxis[1],p1_y[1],elinewidth=2,capsize=6,capthick=2,yerr=p1_err[1],color='y',zorder=1,ls='')
ax[0].scatter(xaxis[1],p1_y[1],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2)

#CCAT3
ax[0].errorbar(xaxis[2],p1_y[2],elinewidth=2,capsize=6,capthick=2,yerr=p1_err[2],color='y',zorder=1,ls='')
ax[0].scatter(xaxis[2],p1_y[2],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2)

#CCAT4
ax[0].errorbar(xaxis[3],p1_y[3],elinewidth=2,capsize=6,capthick=2,yerr=p1_err[3],color='y',zorder=1,ls='')
ax[0].scatter(xaxis[3],p1_y[3],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2)


ax[0].set_ylim(-250,500)

ax[0].set_xlim(0.0,9)
ax[0].set_xlabel(r'$z$',fontsize=22)
ax[0].set_ylabel(r'$\frac{H(z)r_{\rm s}/r_{\rm s}^{\rm fid}}{\left(1+z\right)^{3/2}}$ [km/s/Mpc]',fontsize=26)
ax[0].tick_params(axis='both',width=1,length=8,labelsize=14)
legend = ax[0].legend(loc=1,fontsize=14,ncol=3,markerscale=1.8)



#Plot 2

ax[1].plot(best_fit_x,best_fit_y2,lw=.5,c='k',zorder=0,ls='-')

ax[1].errorbar(x_desi,desi_y2,yerr=desi_err2,capsize=2,capthick=1,color=color[1],zorder=1,ls='',alpha=0.8)
ax[1].errorbar(x_desi_bgs,desi_bgs_y2,yerr=desi_bgs_err2,capsize=2,capthick=1,color=color[1],zorder=1,ls='',alpha=0.8)
ax[1].errorbar(x_desi_Lya,desi_Lya_y2,yerr=desi_Lya_err2,capsize=2,capthick=1,color=color[1],lw=1,zorder=1,ls='',alpha=0.8)
ax[1].scatter(x_desi,desi_y2,color=color[1],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[1].scatter(x_desi_bgs,desi_bgs_y2,color=color[1],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[1].scatter(x_desi_Lya,desi_Lya_y2,color=color[1],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,label='DESI',alpha=0.8)
ax[1].errorbar(x_bossdr12,bossdr12_y2,yerr=bossdr12_err2,capsize=2,capthick=1,color=color[4],zorder=1,ls='',alpha=0.8)
ax[1].scatter(x_bossdr12,bossdr12_y2,color=color[4],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,label='BOSS',alpha=0.8)
ax[1].errorbar(x_bossdr14,bossdr14_y2,yerr=bossdr14_err2,capsize=2,capthick=1,color=color[4],zorder=1,ls='',alpha=0.8)
ax[1].scatter(x_bossdr14,bossdr14_y2,color=color[4],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[1].errorbar(x_eboss,eboss_y2,yerr=eboss_err2,capsize=2,capthick=1,color=color[4],zorder=2,ls='',alpha=0.8)
ax[1].scatter(x_eboss,eboss_y2,color=color[4],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,label='eBOSS',alpha=0.8)
ax[1].errorbar(x_comap1,comap1_y2,elinewidth=2,capsize=6,capthick=2,yerr=comap1_err2,color='fuchsia',zorder=1,ls='')
ax[1].scatter(x_comap1,comap1_y2,color='fuchsia',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='COMAP2')
ax[1].errorbar(x_comap,comap_y2,elinewidth=2,capsize=6,capthick=2,yerr=comap_err2,color='blue',zorder=1,ls='')
ax[1].scatter(x_comap,comap_y2,color='blue',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='COMAP2')
ax[1].errorbar(x_ims3,ims3_y2,elinewidth=2,capsize=6,capthick=2,yerr=ims3_err2,color='c',zorder=1,ls='')
ax[1].scatter(x_ims3,ims3_y2,color='c',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='IMS3 (CO)')
ax[1].errorbar(x_zsx_halpha,zsx_halpha_y2,elinewidth=2,capsize=6,capthick=2,yerr=zsx_halpha_err2,color=color[2],zorder=1,ls='')
ax[1].scatter(x_zsx_halpha,zsx_halpha_y2,color=color[2],marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='IMS3 (CO)')
ax[1].errorbar(x_zsx_lyalpha,zsx_lyalpha_y2,elinewidth=2,capsize=6,capthick=2,yerr=zsx_lyalpha_err2,color='r',zorder=1,ls='')
ax[1].scatter(x_zsx_lyalpha,zsx_lyalpha_y2,color='r',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='IMS3 (CO)')



#CCAT1
ax[1].errorbar(xaxis[0],p2_y[0],elinewidth=2,capsize=6,capthick=2,yerr=p2_err[0],color='y',zorder=1,ls='')
ax[1].scatter(xaxis[0],p2_y[0],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='IMS3 (CO)')

#CCAT2
ax[1].errorbar(xaxis[1],p2_y[1],elinewidth=2,capsize=6,capthick=2,yerr=p2_err[1],color='y',zorder=1,ls='')
ax[1].scatter(xaxis[1],p2_y[1],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='IMS3 (CO)')

#CCAT3
ax[1].errorbar(xaxis[2],p2_y[2],elinewidth=2,capsize=6,capthick=2,yerr=p2_err[2],color='y',zorder=1,ls='')
ax[1].scatter(xaxis[2],p2_y[2],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='IMS3 (CO)')

#CCAT4
ax[1].errorbar(xaxis[3],p2_y[3],elinewidth=2,capsize=6,capthick=2,yerr=p2_err[3],color='y',zorder=1,ls='')
ax[1].scatter(xaxis[3],p2_y[3],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='IMS3 (CO)')

ax[1].set_xlim(0.0,9)
ax[1].set_xlabel(r'$z$',fontsize=26)
ax[1].set_ylabel(r'$\frac{H(z)r_{\rm s}}{\left(H(z)r_{\rm s}\right)^{\rm fid}}$',fontsize=28)
ax[1].tick_params(axis='both',width=1,length=8,labelsize=14)
ax[1].set_ylim(-8,8)
#ax[1].set_yticks([0.85,0.9,0.95,1.,1.05,1.1,1.15])


#D(z) plots.
#Plot 3
color = plt.rcParams['axes.prop_cycle'].by_key()['color']
f, ax = plt.subplots(2,1, gridspec_kw = {'hspace':0,'height_ratios':[5,3],'top':.98,'right':.98}, sharex='col',figsize=(10,7))

ax[0].plot(best_fit_x,best_fit_y3,lw=1.5,c='k',zorder=0,ls='--')


ax[0].errorbar(x_eboss,eboss_y3,yerr=eboss_err3,capsize=2,capthick=1,color=color[4],zorder=1,ls='',alpha=0.8)
ax[0].scatter(x_eboss,eboss_y3,color=color[4],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,label='BOSS/eBOSS',alpha=0.8)
ax[0].errorbar(x_desi,desi_y3,yerr=desi_err3,capsize=2,capthick=1,color=color[1],zorder=1,ls='',alpha=0.8)
ax[0].errorbar(x_desi_Lya,desi_Lya_y3,yerr=desi_Lya_err3,capsize=2,capthick=1,color=color[1],lw=1,zorder=1,ls='',alpha=0.8)
ax[0].errorbar(x_desi_bgs,desi_bgs_y3,yerr=desi_bgs_err3,capsize=2,capthick=1,color=color[1],lw=1,zorder=1,ls='',alpha=0.8)
ax[0].scatter(x_desi,desi_y3,color=color[1],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[0].scatter(x_desi_bgs,desi_bgs_y3,color=color[1],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[0].scatter(x_desi_Lya,desi_Lya_y3,color=color[1],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,label='DESI',alpha=0.8)
ax[0].errorbar(x_bossdr12,bossdr12_y3,yerr=bossdr12_err3,capsize=2,capthick=1,color=color[4],zorder=1,ls='',alpha=0.8)
ax[0].scatter(x_bossdr12,bossdr12_y3,color=color[4],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[0].errorbar(x_bossdr14,bossdr14_y3,yerr=bossdr14_err3,capsize=2,capthick=1,color=color[4],zorder=1,ls='',alpha=0.8)
ax[0].scatter(x_bossdr14,bossdr14_y3,color=color[4],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[0].errorbar(x_zsx_halpha,zsx_halpha_y3,elinewidth=2,capsize=6,capthick=2,yerr=zsx_halpha_err3,color=color[2],zorder=1,ls='')
ax[0].scatter(x_zsx_halpha,zsx_halpha_y3,color=color[2],marker='o',s=50,edgecolors='k',lw=1,zorder=2,label=r'SPHEREx (H$\alpha$)')
ax[0].errorbar(x_zsx_lyalpha,zsx_lyalpha_y3,elinewidth=2,capsize=6,capthick=2,yerr=zsx_lyalpha_err3,color='r',zorder=1,ls='')
ax[0].scatter(x_zsx_lyalpha,zsx_lyalpha_y3,color='r',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label=r'SPHEREx (Ly$\alpha$)')
ax[0].errorbar(x_comap1,comap1_y3,elinewidth=2,capsize=6,capthick=2,yerr=comap1_err3,color='fuchsia',zorder=1,ls='')
ax[0].scatter(x_comap1,comap1_y3,color='fuchsia',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='COMAP1')
ax[0].errorbar(x_comap,comap_y3,elinewidth=2,capsize=6,capthick=2,yerr=comap_err3,color='b',zorder=1,ls='')
ax[0].scatter(x_comap,comap_y3,color='b',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='COMAP2')
ax[0].errorbar(x_ims3,ims3_y3,elinewidth=2,capsize=6,capthick=2,yerr=ims3_err3,color='c',zorder=1,ls='')
ax[0].scatter(x_ims3,ims3_y3,color='c',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='IMS3 (CO)')



#CCAT1
ax[0].errorbar(xaxis[0],p3_y[0],elinewidth=2,capsize=6,capthick=2,yerr=p3_err[0],color='y',zorder=1,ls='')
ax[0].scatter(xaxis[0],p3_y[0],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='CCAT1')

#CCAT2
ax[0].errorbar(xaxis[1],p3_y[1],elinewidth=2,capsize=6,capthick=2,yerr=p3_err[1],color='y',zorder=1,ls='')
ax[0].scatter(xaxis[1],p3_y[1],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='CCAT2')

#CCAT3
ax[0].errorbar(xaxis[2],p3_y[2],elinewidth=2,capsize=6,capthick=2,yerr = p3_err[2],color='y',zorder=1,ls='')
ax[0].scatter(xaxis[2],p3_y[2],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='CCAT3')

#CCAT4
ax[0].errorbar(xaxis[3],p3_y[3],elinewidth=2,capsize=6,capthick=2,yerr=p3_err[3],color='y',zorder=1,ls='')
ax[0].scatter(xaxis[3],p3_y[3],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='CCAT4')

ax[0].set_xlim(0.0,9)
ax[0].set_ylim(-3000,5000)
ax[0].set_xlabel(r'$z$',fontsize=22)
ax[0].set_ylabel(r'$D_A(z)\left(\frac{r_{\rm s}^{\rm fid}}{r_{\rm s}}\right)$ [Mpc]',fontsize=22)
ax[0].tick_params(axis='both',width=1,length=8,labelsize=14)
#legend = ax[0].legend(loc=4,fontsize=14,ncol=3,markerscale=1.8)


#Plot 4
ax[1].plot(best_fit_x,best_fit_y4,lw=.5,c='k',zorder=0,ls='-')


ax[1].errorbar(x_desi,desi_y4,yerr=desi_err4,capsize=2,capthick=1,color=color[1],zorder=1,ls='',alpha=0.8)
ax[1].errorbar(x_desi_Lya,desi_Lya_y4,yerr=desi_Lya_err4,capsize=2,capthick=1,color=color[1],lw=1,zorder=1,ls='',alpha=0.8)
ax[1].errorbar(x_desi_bgs,desi_bgs_y4,yerr=desi_bgs_err4,capsize=2,capthick=1,color=color[1],lw=1,zorder=1,ls='',alpha=0.8)
ax[1].scatter(x_desi,desi_y4,color=color[1],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[1].scatter(x_desi_bgs,desi_bgs_y4,color=color[1],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[1].scatter(x_desi_Lya,desi_Lya_y4,color=color[1],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,label='DESI',alpha=0.8)
ax[1].errorbar(x_bossdr12,bossdr12_y4,yerr=bossdr12_err4,capsize=2,capthick=1,color=color[4],zorder=1,ls='',alpha=0.8)
ax[1].scatter(x_bossdr12,bossdr12_y4,color=color[4],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,label='BOSS',alpha=0.8)
ax[1].errorbar(x_bossdr14,bossdr14_y4,yerr=bossdr14_err4,capsize=2,capthick=1,color=color[4],zorder=1,ls='',alpha=0.8)
ax[1].scatter(x_bossdr14,bossdr14_y4,color=color[4],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,alpha=0.8)
ax[1].errorbar(x_eboss,eboss_y4,yerr=eboss_err4,capsize=2,capthick=1,color=color[4],zorder=1,ls='',alpha=0.8)
ax[1].scatter(x_eboss,eboss_y4,color=color[4],marker='o',s=50,edgecolors='k',linewidth=1.5,zorder=2,label='eBOSS',alpha=0.8)
ax[1].errorbar(x_comap1,comap1_y4,elinewidth=2,capsize=6,capthick=2,yerr=comap1_err4,color='fuchsia',zorder=1,ls='')
ax[1].scatter(x_comap1,comap1_y4,color='fuchsia',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='COMAP1')
ax[1].errorbar(x_comap,comap_y4,elinewidth=2,capsize=6,capthick=2,yerr=comap_err4,color='b',zorder=1,ls='')
ax[1].scatter(x_comap,comap_y4,color='b',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='COMAP2')
ax[1].errorbar(x_ims3,ims3_y4,elinewidth=2,capsize=6,capthick=2,yerr=ims3_err4,color='c',zorder=1,ls='')
ax[1].scatter(x_ims3,ims3_y4,color='c',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='CO IMS3')
ax[1].errorbar(x_zsx_halpha,zsx_halpha_y4,elinewidth=2,capsize=6,capthick=2,yerr=zsx_halpha_err4,color=color[2],zorder=1,ls='')
ax[1].scatter(x_zsx_halpha,zsx_halpha_y4,color=color[2],marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='CO IMS3')
ax[1].errorbar(x_zsx_lyalpha,zsx_lyalpha_y4,elinewidth=2,capsize=6,capthick=2,yerr=zsx_lyalpha_err4,color='r',zorder=1,ls='')
ax[1].scatter(x_zsx_lyalpha,zsx_lyalpha_y4,color='r',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='CO IMS3')


#CCAT 1
ax[1].errorbar(xaxis[0],p4_y[0],elinewidth=2,capsize=6,capthick=2,yerr=p4_err[0],color='y',zorder=1,ls='')
ax[1].scatter(xaxis[0],p4_y[0],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='CO IMS3')

#CCAT 2
ax[1].errorbar(xaxis[1],p4_y[1],elinewidth=2,capsize=6,capthick=2,yerr=p4_err[1],color='y',zorder=1,ls='')
ax[1].scatter(xaxis[1],p4_y[1],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='CO IMS3')

#CCAT 3
ax[1].errorbar(xaxis[2],p4_y[2],elinewidth=2,capsize=6,capthick=2,yerr=p4_err[2],color='y',zorder=1,ls='')
ax[1].scatter(xaxis[2],p4_y[2],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='CO IMS3')

#CCAT 4
ax[1].errorbar(xaxis[3],p4_y[3],elinewidth=2,capsize=6,capthick=2,yerr=p4_err[3],color='y',zorder=1,ls='')
ax[1].scatter(xaxis[3],p4_y[3],color='y',marker='o',s=50,edgecolors='k',lw=1,zorder=2,label='CO IMS3')


ax[1].set_xlim(0.0,9)
ax[1].set_xlabel(r'$z$',fontsize=26)
ax[1].set_ylabel(r'$\frac{D_A(z)/r_{\rm s}}{\left( D_A(z)/r_{\rm s} \right)^{\rm fid}}$',fontsize=28)
ax[1].tick_params(axis='both',width=1,length=8,labelsize=14)
ax[1].set_ylim(-3,6)
#ax[1].set_ylim(0.8,1.2)

legend = [Line2D([-1], [-1], marker='o', color='w', label='BOSS/eBOSS',
                        markerfacecolor=color[4], markersize=12),
          Line2D([-1], [-1], marker='o', color='w', label='DESI',
                        markerfacecolor=color[1], markersize=12),
          Line2D([-1], [-1], marker='o', color='w', label='',
                        markerfacecolor='w', markersize=12),
          Line2D([-1], [-1], marker='o', color='w', label='COMAP1',
                        markerfacecolor='fuchsia', markersize=12),
         Line2D([-1], [-1], marker='o', color='w', label='COMAP2',
                        markerfacecolor='b', markersize=12),
         Line2D([-1], [-1], marker='o', color='w', label='IMS3 (CO)',
                        markerfacecolor='c', markersize=12),
         Line2D([-1], [-1], marker='o', color='w', label=r'SPHEREx H$\alpha$',
                        markerfacecolor=color[2], markersize=12),
         Line2D([-1], [-1], marker='o', color='w', label=r'SPHEREx Ly$\alpha$',
                        markerfacecolor='r', markersize=12),

#Legend for CCAT:

           Line2D([-1], [-1], marker='o', color='w', label='CCAT',
                         markerfacecolor='y', markersize=12),
         ]
ax[0].legend(handles=legend,loc=8,frameon=True, fontsize=15,ncol=3)

plt.show()
print('success')
