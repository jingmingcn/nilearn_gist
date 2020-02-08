from nilearn import masking
mask = masking.compute_background_mask(r'E:\home\bct_test\NC_01_0001\rs6_f8dGR_w3_rabrat_4D.nii')
print(mask.get_data().shape)
from nilearn.masking import apply_mask
masked_data = apply_mask(r'E:\home\bct_test\NC_01_0001\rs6_f8dGR_w3_rabrat_4D.nii', mask)
print(masked_data.shape)
# masked_data shape is (timepoints, voxels). We can plot the first 150
# timepoints from two voxels

# And now plot a few of these
import matplotlib.pyplot as plt
plt.figure(figsize=(7, 5))
plt.plot(masked_data[:230, 98:100])
plt.xlabel('Time [TRs]', fontsize=16)
plt.ylabel('Intensity', fontsize=16)
plt.xlim(0, 150)
plt.subplots_adjust(bottom=.12, top=.95, right=.95, left=.12)

plt.show()