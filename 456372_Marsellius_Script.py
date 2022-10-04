# Mengimpor library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Membaca dataset
data_path  = 'car data.csv'
car_data = pd.read_csv(data_path)


# Menghitung regresi linear
X = list(car_data['Year'])
Y = list(car_data['Selling_Price'])

n = len(X)
sigma_x = sum(X)
sigma_y = sum(Y)
sigma_xy = 0
for i in range(n):
    sigma_xy = sigma_xy + X[i] * Y[i]
sigma_xx = 0
for i in range(n):
    sigma_xx = sigma_xx + X[i] * X[i]
sigma_yy = 0
for i in range(n):
    sigma_yy = sigma_yy + Y[i] * Y[i]
      
b = (n*sigma_xy-sigma_x*sigma_y)/(n*sigma_xx-sigma_x*sigma_x)
a = (sigma_y-b*sigma_x)/(n)


# Menggambar garis regresi linear
x = np.linspace (np.min(X) - 0, np.max(X) + 0, 100)
y = a + b * x
plt.plot(x, y, color='#58b970')
plt.scatter(X, Y)
plt.xlabel('Year')
plt.ylabel('Price (*100000$)')
plt.show()


# Menentukan corelation coefficient (r) dan coefficient of determination (r^2)
r = (n*sigma_xy - sigma_x*sigma_y)/(((n*sigma_xx-sigma_x*sigma_x)*(n*sigma_yy-sigma_y*sigma_y))**0.5)
print("Corelation coefficient = %0.3f"%r)
print("Coefficient of determination = %0.3f"%r**2)
