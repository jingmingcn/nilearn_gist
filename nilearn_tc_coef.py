import numpy
from tkinter.filedialog import askopenfilename

time_series = numpy.loadtxt(askopenfilename(),skiprows=1,usecols=(x for x in range(2,118)))

# Download atlas from internet
# Retrieve the atlas and the data
from nilearn import datasets
atlas = datasets.fetch_atlas_aal()
# Loading atlas image stored in 'maps'
atlas_filename = atlas['maps']
# Loading atlas data stored in 'labels'
labels = atlas['labels']



############################################################################
# Build and display a correlation matrix
from nilearn.connectome import ConnectivityMeasure
correlation_measure = ConnectivityMeasure(kind='correlation')
correlation_matrix = correlation_measure.fit_transform([time_series])[0]

from matplotlib import pyplot as plt
plt.figure(figsize=(10, 10))
# Mask out the major diagonal
numpy.fill_diagonal(correlation_matrix, 0)
plt.imshow(correlation_matrix, interpolation="nearest", cmap="RdBu_r",
           vmax=0.8, vmin=-0.8)
plt.colorbar()
# And display the labels
x_ticks = plt.xticks(range(len(labels)), labels, rotation=90)
y_ticks = plt.yticks(range(len(labels)), labels)

############################################################################
# Build and display a correlation matrix
from nilearn.connectome import ConnectivityMeasure
correlation_measure = ConnectivityMeasure(kind='correlation')
correlation_matrix = correlation_measure.fit_transform([time_series])[0]

from nilearn import plotting
#coords = atlas.region_coords
coords = [(-38.65,-5.68,50.94),
(41.37,-8.21,52.09),
(-18.45,34.81,42.2),
(21.9,31.12,43.82),
(-16.56,47.32,-13.31),
(18.49,48.1,-14.02),
(-33.43,32.73,35.46),
(37.59,33.06,34.04),
(-30.65,50.43,-9.62),
(33.18,52.59,-10.73),
(-48.43,12.73,19.02),
(50.2,14.98,21.41),
(-45.58,29.91,13.99),
(50.33,30.16,14.17),
(-35.98,30.71,-12.11),
(41.22,32.23,-11.91),
(-47.16,-8.48,13.95),
(52.65,-6.25,14.63),
(-5.32,4.85,61.38),
(8.62,0.17,61.85),
(-8.06,15.05,-11.46),
(10.43,15.91,-11.26),
(-4.8,49.17,30.89),
(9.1,50.84,30.22),
(-5.17,54.06,-7.4),
(8.16,51.67,-7.13),
(-5.08,37.07,-18.14),
(8.35,35.64,-18.04),
(-35.13,6.65,3.44),
(39.02,6.25,2.08),
(-4.04,35.4,13.95),
(8.46,37.01,15.84),
(-5.48,-14.92,41.57),
(8.02,-8.83,39.79),
(-4.85,-42.92,24.67),
(7.44,-41.81,21.87),
(-25.03,-20.74,-10.13),
(29.23,-19.78,-10.33),
(-21.17,-15.95,-20.7),
(25.38,-15.15,-20.47),
(-23.27,-0.67,-17.14),
(27.32,0.64,-17.5),
(-7.14,-78.67,6.44),
(15.99,-73.15,9.4),
(-5.93,-80.13,27.22),
(13.51,-79.36,28.23),
(-14.62,-67.56,-4.63),
(16.29,-66.93,-3.87),
(-16.54,-84.26,28.17),
(24.29,-80.85,30.59),
(-32.39,-80.73,16.11),
(37.39,-79.7,19.42),
(-36.36,-78.29,-7.84),
(38.16,-81.99,-7.61),
(-31.16,-40.3,-20.23),
(33.97,-39.1,-20.18),
(-42.46,-22.63,48.92),
(41.43,-25.49,52.55),
(-23.45,-59.56,58.96),
(26.11,-59.18,62.06),
(-42.8,-45.82,46.74),
(46.46,-46.29,49.54),
(-55.79,-33.64,30.45),
(57.61,-31.5,34.48),
(-44.14,-60.82,35.59),
(45.51,-59.98,38.63),
(-7.24,-56.07,48.01),
(9.98,-56.05,43.77),
(-7.63,-25.36,70.07),
(7.48,-31.59,68.09),
(-11.46,11,9.24),
(14.84,12.07,9.42),
(-23.91,3.86,2.4),
(27.78,4.91,2.46),
(-17.75,-0.03,0.21),
(21.2,0.18,0.23),
(-10.85,-17.56,7.98),
(13,-17.55,8.09),
(-41.99,-18.88,9.98),
(45.86,-17.15,10.41),
(-53.16,-20.68,7.13),
(58.15,-21.78,6.8),
(-39.88,15.14,-20.18),
(48.25,14.75,-16.86),
(-55.52,-33.8,-2.2),
(57.47,-37.23,-1.47),
(-36.32,14.59,-34.08),
(44.22,14.55,-32.23),
(-49.77,-28.05,-23.17),
(53.69,-31.07,-22.32),
(-36.067,-66.72,-28.934),
(37.456,-67.137,-29.547),
(-28.636,-73.26,-38.204),
(32.057,-69.016,-39.949),
(-8.8004,-37.223,-18.581),
(12.319,-34.466,-19.391),
(-15.004,-43.486,-16.933),
(17.199,-42.861,-18.151),
(-23.238,-59.101,-22.131),
(24.691,-58.316,-23.645),
(-32.358,-59.82,-45.449),
(33.139,-63.178,-48.457),
(-25.751,-54.519,-47.685),
(25.064,-56.34,-49.468),
(-10.947,-48.95,-45.903),
(9.4602,-49.5,-46.327),
(-22.614,-33.8,-41.765),
(25.995,-33.838,-41.347),
(0.75743,-38.792,-20.05),
(1.3804,-39.931,-11.398),
(1.2207,-52.362,-6.1138),
(1.1414,-67.059,-15.123),
(1.1458,-71.93,-25.141),
(1.1521,-64.429,-34.08),
(0.86467,-54.875,-34.896),
(0.35584,-45.8,-31.683)]

# We threshold to keep only the 20% of edges with the highest value
# because the graph is very dense
plotting.plot_connectome(correlation_matrix, coords,
                         edge_threshold="80%", colorbar=True)

plotting.show()

view = plotting.view_connectome(correlation_matrix, coords,
                         edge_threshold="80%")
view.open_in_browser()
