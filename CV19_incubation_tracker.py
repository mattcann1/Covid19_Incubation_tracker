# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:16:20 2020

@author: matth
"""
#=======================================================================IMPORTS
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import matplotlib.pyplot as plt
from datetime import datetime
# Data Source==================================================================
# @article{10.7326/M20-0504,
#     author = {Lauer, Stephen A. and Grantz, Kyra H. and Bi, Qifang and Jones, Forrest K. and Zheng, Qulu and Meredith, Hannah R. and Azman, Andrew S. and Reich, Nicholas G. and Lessler, Justin},
#     title = "{The Incubation Period of Coronavirus Disease 2019 (COVID-19) From Publicly Reported Confirmed Cases: Estimation and Application}",
#     journal = {Annals of Internal Medicine},
#     year = {2020},
#     month = {03},
#     abstract = "{A novel human coronavirus, severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2), was identified in China in December 2019. There is limited support for many of its key epidemiologic features, including the incubation period for clinical disease (coronavirus disease 2019 [COVID-19]), which has important implications for surveillance and control activities.To estimate the length of the incubation period of COVID-19 and describe its public health implications.Pooled analysis of confirmed COVID-19 cases reported between 4 January 2020 and 24 February 2020.News reports and press releases from 50 provinces, regions, and countries outside Wuhan, Hubei province, China.Persons with confirmed SARS-CoV-2 infection outside Hubei province, China.Patient demographic characteristics and dates and times of possible exposure, symptom onset, fever onset, and hospitalization.There were 181 confirmed cases with identifiable exposure and symptom onset windows to estimate the incubation period of COVID-19. The median incubation period was estimated to be 5.1 days (95\\% CI, 4.5 to 5.8 days), and 97.5\\% of those who develop symptoms will do so within 11.5 days (CI, 8.2 to 15.6 days) of infection. These estimates imply that, under conservative assumptions, 101 out of every 10 000 cases (99th percentile, 482) will develop symptoms after 14 days of active monitoring or quarantine.Publicly reported cases may overrepresent severe cases, the incubation period for which may differ from that of mild cases.This work provides additional evidence for a median incubation period for COVID-19 of approximately 5 days, similar to SARS. Our results support current proposals for the length of quarantine or active monitoring of persons potentially exposed to SARS-CoV-2, although longer monitoring periods might be justified in extreme cases.U.S. Centers for Disease Control and Prevention, National Institute of Allergy and Infectious Diseases, National Institute of General Medical Sciences, and Alexander von Humboldt Foundation.}",
#     issn = {0003-4819},
#     doi = {10.7326/M20-0504},
#     url = {https://doi.org/10.7326/M20-0504},
#     eprint = {https://annals.org/acp/content\_public/journal/aim/0/aime202005050-m200504.pdf},
# }
# =============================================================================

#==========================================================================MAIN

#Parameters for Gamma Distribution
parameter_1 = 5.807  #(3.585–13.865) 
parameter_2 = 0.948 #(0.368–1.696)

#Number of days between 0 and 20
x = np.linspace(0, 20, 100)

#Gamma pdf distribution
y1 = stats.gamma.pdf(x, a=parameter_1, scale=parameter_2)

#Enter date self-isolation begun
a = datetime(2020,4,22,14,0,0)
now = datetime.now()
delta = now-a #Difference in datetimes
x_current = float(delta.days)+delta.seconds/3600/24 #Current number of days as a float.

#Plots
plt.plot(x, y1, 'k')
plt.xlabel('Days since entered self-isolation')
plt.ylabel('Probabilty of showing symptoms')
plt.ylim((0,0.2))

plt.axvline(x=x_current,color='red', linestyle='--')
plt.fill_between(x, y1, where= x < x_current, alpha = 0.5)
                 
plt.show()  

#Probability from gamma distriution
y2 = stats.gamma.cdf(x_current, a=parameter_1, scale=parameter_2)
y3 = stats.gamma.sf(x_current, a=parameter_1, scale=parameter_2)

print('There is a probability of{:6.2f}% that you would have shown symptoms if infected.'.format(y2*100))
print('There is a probability of{:6.2f}% that you will show symptoms in the next{:6.2f} days.'.format(y3*100,(20-x_current)))

#%%