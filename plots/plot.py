
import sys

import numpy as np

import myplots as plts
import seaborn as sns

path = sys.argv[1]
data = {}

with open(path) as f:
  for line in f:
    vals = [val.strip() for val in line.strip().split(',')]
    if vals[0] not in data.keys():
      data[vals[0]] = {}
    ftype=''
    name = vals[1]
    if '.' in name:
      tmp = name.split('.')
      ftype = tmp[0]+'.'
      name = tmp[1]
    if name=='gfm':
      name = 'Current'
    if name=='fm2list':
      name = 'SalSSA-MOp'
    if name=='fm':
      name = 'FMSA'
    if name=='llfm':
      name = 'Identical'
    if name=='llvm':
      name = 'Identical'
    if name=='soa':
      name = 'Edler'
    data[vals[0]][ftype+name] = float(vals[2])

#print data

BlueRedPallete = ['black',sns.color_palette("Blues_r", n_colors=3)[0],sns.color_palette("Reds_r", n_colors=6)[4],sns.color_palette("Reds_r", n_colors=6)[2],sns.color_palette("Reds_r", n_colors=6)[0],sns.color_palette("Greens_r", n_colors=3)[0]]
#BlueRedPallete = ['black',sns.color_palette("Blues_r", n_colors=3)[0],sns.color_palette("Reds_r", n_colors=6)[4],sns.color_palette("Reds_r", n_colors=6)[2],sns.color_palette("Reds_r", n_colors=6)[0],sns.color_palette("Greens_r", n_colors=6)[4],sns.color_palette("Greens_r", n_colors=6)[2],sns.color_palette("Greens_r", n_colors=6)[0]]
#BlueRedPallete = ['black',sns.color_palette("Blues_r", n_colors=3)[0],sns.color_palette("Reds_r", n_colors=3)[0],sns.color_palette("Greens_r", n_colors=3)[0]]
#BlueRedPallete = ['black',sns.color_palette("Reds_r", n_colors=3)[0],sns.color_palette("Greens_r", n_colors=3)[0]]

#gorder = ['Identical','SOA','FMSA [t=1]','FMSA [t=5]','FMSA [t=10]','FMSA [oracle]']
#oracle = ['FMSA [t=1]','FMSA [t=5]','FMSA [t=10]','FMSA [oracle]']
#gorder = ['Identical','SOA','FMSA [t=1]','FMSA [t=5]','FMSA [t=10]','GFM [t=1]','GFM [t=5]','GFM [t=10]']
#gorder = ['Identical','SOA','FMSA','Current']
gorder = ['Identical','Edler','SalSSA-MOp']
#gorder = ['FMSA','Current']
#oracle = ['FMSA [t=1]','FMSA [t=5]','FMSA [t=10]','GFM [t=1]','GFM [t=5]','GFM [t=10]']

pdata = {}
for k in data.keys():
  pdata[k] = {}
  for name in gorder:
    val = data[k]['o.'+name]
    #if name=='FMSA [oracle]':
    #  val = min([data[k]['o.'+n] for n in oracle]) 
    #  pdata[k]['FMSA [oracle]'] = (data[k]['o.bl']/val-1)*100
    #else:
    pdata[k][name] = (data[k]['o.bl']/val-1)*100
    print(k, name, pdata[k][name])

plts.bars(pdata,'Reduction (%)',groups=gorder,palette = BlueRedPallete,edgecolor='black',labelAverage=True,decimals=1,legendPosition='upper left')#,filename='code-size-reduction.pdf')


pdata = {}
for k in data.keys():
  pdata[k] = {}
  for name in gorder:
    val = data[k][name]
    #if name=='FMSA [oracle]':
    #  val = min([data[k]['o.'+n] for n in oracle]) 
    #  pdata[k]['FMSA [oracle]'] = (data[k]['o.bl']/val-1)*100
    #else:
    pdata[k][name] = (data[k]['bl']/val-1)*100
    print(k, name, pdata[k][name])

#plts.bars(pdata,'Reduction (%)',groups=gorder,palette = BlueRedPallete,edgecolor='black',labelAverage=True,decimals=1,legendPosition='upper left',filename='exec-size-reduction.pdf')
plts.bars(pdata,'Reduction (%)',groups=gorder,palette = BlueRedPallete,edgecolor='black',labelAverage=True,decimals=1,legendPosition='upper left',filename=None)
