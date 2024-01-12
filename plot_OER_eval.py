# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:44:52 2022

@author: Yi
"""

import numpy as np
from matplotlib import pyplot as plt
import csv

fig, axs = plt.subplots(2, 3)
x = np.arange(1, 11)


plot_rmse_p1 = []
plot_rel_p1 = []
plot_lo10_p1 = []
plot_delta1_p1 = []
plot_delta2_p1 = []
plot_delta3_p1 = []

plot_rmse_p2 = []
plot_rel_p2 = []
plot_lo10_p2 = []
plot_delta1_p2 = []
plot_delta2_p2 = []
plot_delta3_p2 = []

plot_rmse_p3 = []
plot_rel_p3 = []
plot_lo10_p3 = []
plot_delta1_p3 = []
plot_delta2_p3 = []
plot_delta3_p3 = []



with open('./metrics_each_epoch_P1.txt') as f:  # 'with' will auto close after loop
    count = 0
    for row in f:
        count += 1
        if count % 2 == 0:
            plot_rmse_p1.append(float(row.split(",")[0]))
            plot_rel_p1.append(float(row.split(",")[2]))
            plot_lo10_p1.append(float(row.split(",")[3]))
            plot_delta1_p1.append(float(row.split(",")[4]))
            plot_delta2_p1.append(float(row.split(",")[5]))
            plot_delta3_p1.append(float(row.split(",")[6]))

with open('./metrics_each_epoch_P2.txt') as f:  # 'with' will auto close after loop
    count = 0
    for row in f:
        count += 1
        if count % 2 == 0:
            plot_rmse_p2.append(float(row.split(",")[0]))
            plot_rel_p2.append(float(row.split(",")[2]))
            plot_lo10_p2.append(float(row.split(",")[3]))
            plot_delta1_p2.append(float(row.split(",")[4]))
            plot_delta2_p2.append(float(row.split(",")[5]))
            plot_delta3_p2.append(float(row.split(",")[6]))

with open('./metrics_each_epoch_P3.txt') as f:  # 'with' will auto close after loop
    count = 0
    for row in f:
        count += 1
        if count % 2 == 0:
            plot_rmse_p3.append(float(row.split(",")[0]))
            plot_rel_p3.append(float(row.split(",")[2]))
            plot_lo10_p3.append(float(row.split(",")[3]))
            plot_delta1_p3.append(float(row.split(",")[4]))
            plot_delta2_p3.append(float(row.split(",")[5]))
            plot_delta3_p3.append(float(row.split(",")[6]))




    axs[0, 0].plot(x, plot_rmse_p1, 'rd-.', label='P1')
    axs[0, 0].plot(x, plot_rmse_p2, 'bd-.', label='P2')
    axs[0, 0].plot(x, plot_rmse_p3, 'gd-.', label='P3')
    axs[0, 0].legend(prop={'size':7})
    axs[0, 0].set_xticks(x)
    axs[0, 0].set_ylabel("RMSE")
    axs[0, 0].grid()


    axs[0, 1].plot(x, plot_rel_p1, 'rd-.', label='P1')
    axs[0, 1].plot(x, plot_rel_p2, 'bd-.', label='P2')
    axs[0, 1].plot(x, plot_rel_p3, 'gd-.', label='P3')
    axs[0, 1].legend(prop={'size':7})
    axs[0, 1].set_xticks(x)
    axs[0, 1].set_ylabel("Rel")
    axs[0, 1].grid()



    axs[0, 2].plot(x, plot_lo10_p1, 'rs-', label='P1')
    axs[0, 2].plot(x, plot_lo10_p2, 'bs-', label='P2')
    axs[0, 2].plot(x, plot_lo10_p3, 'gs-', label='P3')
    axs[0, 2].legend(prop={'size':7})
    axs[0, 2].set_xticks(x)
    axs[0, 2].set_ylabel("log10")
    axs[0, 2].grid()


    axs[1, 0].plot(x, plot_delta1_p1, 'rd-.', label='P1')
    axs[1, 0].plot(x, plot_delta1_p2, 'bd-.', label='P2')
    axs[1, 0].plot(x, plot_delta1_p3, 'gd-.', label='P3')
    axs[1, 0].legend(prop={'size':7})
    axs[1, 0].set_xticks(x)
    axs[1, 0].set_ylabel(r"$\delta_1$")
    axs[1, 0].grid()




    axs[1, 1].plot(x, plot_delta2_p1, 'rs-', label='P1')
    axs[1, 1].plot(x, plot_delta2_p2, 'bs-', label='P2')
    axs[1, 1].plot(x, plot_delta2_p3, 'gs-', label='P3')
    axs[1, 1].legend(prop={'size':7})
    axs[1, 1].set_xticks(x)
    # axs[1, 1].set_ylabel("δ2")
    axs[1, 1].set_ylabel(r"$\delta_2$")
    axs[1, 1].grid()


    axs[1, 2].plot(x, plot_delta3_p1, 'rd-.', label='P1')
    axs[1, 2].plot(x, plot_delta3_p2, 'bd-.', label='P2')
    axs[1, 2].plot(x, plot_delta3_p3, 'gd-.', label='P3')
    axs[1, 2].legend(prop={'size':7})
    # axs[1, 2].legend(loc="upper right", prop={'size': 7})
    axs[1, 2].set_xticks(x)
    axs[1, 2].set_ylabel(r"$\delta_3$")
    axs[1, 2].grid()

# plt.subplots_adjust(left=1,
#                     bottom=0.1,
#                     right=1.001,
#                     top=0.9,
#                     wspace=0.4,
#                     hspace=0.4)
# # plt.tight_layout(rect=[0, 0, 1, 0.95])
#
plt.subplots_adjust(top=0.957,
                    bottom=0.081,
                    left=0.131,
                    right=0.957,
                    hspace=0.235,
                    wspace=0.548)
plt.show()
# plt.savefig('fixed_seed_GPU_vs_CPU_tf_2_4_1_tf_2_5_1.eps', dpi=2000, bbox_inches="tight")




