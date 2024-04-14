#Code for generating graphs for PSNR and MSSSIM 
import matplotlib.pyplot as plt
epoch = [0,50,100,150,200,250,300,350,400,
         450,500,550,600,650,700,750,800,
         850,900,950,1000,1050,1100,1150,1200]

#----------data for 1200e_NeRV_S_cholec80 / taken from logs-----------------
PSNR = [0.0,
       23.47,
       25.83,
       26.72,
       27.89,
       28.94,
       30.08,
       31.02,
       31.87,
       32.51,
       33.12,
       33.71,
       34.19,
       34.52,
       34.95,
       35.33,
       35.65,
       36.03,
       36.25,
       36.46,
       36.59,
       36.69,
       36.74,
       36.77,
       36.78

       ]

MSSSIM = [0.0,
          0.8522,
          0.8885,
          0.9054,
          0.9235,
          0.9365,
          0.948,
          0.956,
          0.9624,
          0.9666,
          0.9696,
          0.9721,
          0.9741,
          0.9754,
          0.9768,
          0.9779,
          0.9788,
          0.9796,
          0.9802,
          0.9807,
          0.981,
          0.9812,
          0.9814,
          0.9815,
          0.9815

          ]

#--------------------------------------------------
#----------data for 1200e_NeRV_S_cholec80 every second frame / taken from logs-----------------
PSNR_2 = [0.0,
          22.47,
          24.63,
          25.72,
          26.56,
          27.38,
          28.44,
          29.55,
          30.48,
          31.21,
          31.8,
          32.32,
          32.83,
          33.31,
          33.68,
          34.02,
          34.33,
          34.63,
          34.86,
          35.07,
          35.2,
          35.28,
          35.33,
          35.35,
          35.36]

MSSSIM_2 = [0.0,
            0.8342,
            0.872,
            0.8953,
            0.9112,
            0.9246,
            0.9371,
            0.9480,
            0.9557,
            0.9609,
            0.9647,
            0.9673,
            0.9695,
            0.9716,
            0.973,
            0.9741,
            0.9752,
            0.9761,
            0.9767,
            0.9772,
            0.9776,
            0.9779,
            0.978,
            0.9781,
            0.9782]



#------plotting PSNR----------
# Plot
plt.figure(figsize=(10, 6))
plt.plot(epoch, PSNR, marker='o', linestyle='-',label='PSNR for subsequent frames in training')
plt.plot(epoch, PSNR_2, marker='o', linestyle='-',label='PSNR for every second frame in training')
plt.title('PSNR vs. Epoch for NeRV S 1200 epochs')
plt.xlabel('Epoch')
plt.ylabel('PSNR')
plt.grid(True)
plt.legend()

# Save the graph as a PNG file in the same folder
# PSNR_vs_Epoch_1200_cholec80 or PSNR_vs_Epoch_1200_cholec80_every_2
plt.savefig('PSNR_vs_Epoch_1200_cholec80_comparison.png')

plt.show()

#------plotting MSSSIM----------
# Plot
plt.figure(figsize=(10, 6))
plt.plot(epoch, MSSSIM, marker='o', linestyle='-',label='MSSSIM for subsequent frames in training')
plt.plot(epoch, MSSSIM_2, marker='o', linestyle='-',label='MSSSIM for every second frame in training')
plt.title('MSSSIM vs. Epoch for NeRV S 1200 epochs')
plt.xlabel('Epoch')
plt.ylabel('MSSSIM')
plt.grid(True)
plt.legend()

# Save the graph as a PNG file in the same folder
# MSSSIM_vs_Epoch_1200_cholec80 or MSSSIM_vs_Epoch_1200_cholec80_every_2

plt.savefig('MSSSIM_vs_Epoch_1200_cholec80_comparison.png')

plt.show()