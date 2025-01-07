# # ====== Import thư viện ====== #
# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# from skimpy import skim
# from sklearn.datasets import fetch_california_housing
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import Lasso, LassoCV, Ridge, RidgeCV
# from sklearn.metrics import mean_squared_error

# # ====== Tải dữ liệu ====== #
# data = fetch_california_housing(as_frame=True)

# # ====== Hiểu về dữ liệu ====== #
# # Thông tin về các thuộc tính trong tập dữ liệu
# print(data.DESCR)

# # Chuyển dữ liệu thành DataFrame
# df = data.frame
# print(df.head())

# ====== Import thư viện ====== #
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from skimpy import skim
from sklearn.datasets import fetch_california_housing

# ====== Tải dữ liệu ====== #
data = fetch_california_housing(as_frame=True)
df = data.frame

# ====== Hiển thị Thống kê mô tả ====== #
print('=' * 40)
print('\033[1m    Table 1: Descriptive Statistics: \033[0m')
print('=' * 40)
skim(df)
print('-' * 135)

# ====== Biểu đồ phân phối của từng biến ====== #
df.hist(bins=60, edgecolor='white', figsize=(12, 10), color='lightpink')
plt.suptitle('Figure 1: Distribution of Each Feature', fontsize=14, fontweight='bold')
plt.subplots_adjust(hspace=0.7, wspace=0.4)
plt.show()
print('-' * 135)

# ====== Ma trận tương quan ====== #
# Tính ma trận tương quan
corr_matrix = df.corr()

# Tạo mặt nạ cho tam giác trên để giảm lặp thông tin
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# Thiết lập figure của matplotlib
plt.figure(figsize=(10, 8))

# Định nghĩa colormap tùy chỉnh
cmap = sns.diverging_palette(220, 20, as_cmap=True)

# Vẽ heatmap cho ma trận tương quan
sns.heatmap(corr_matrix, mask=mask, annot=True, cmap=cmap, vmin=-1, vmax=1, linewidths=0.5, cbar=True)

# Tùy chỉnh biểu đồ
plt.title('Figure 2: Correlation Matrix of the Raw Data', fontsize=14, fontweight='bold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

