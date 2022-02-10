from numpy import *
import opusFC as opusFC
from pandas import *
import matplotlib.pyplot as plt


f = 'c:\\Users\\aruna\\OneDrive\\Desktop\\OpusFC test\\test_PVA.1'
dbs = opusFC.listContents(f)
print(dbs[1])
data = opusFC.getOpusData(f, dbs[1])

# data_test = opusFC.getOpusData(f, ('SSC', '2D', 'NONE’))
# What SSC  means here?

print(data)

# data.x                    # X coordinates
# data.parameters['SNM']    # Sample name
# data.description          # Description of data object
# opusFC.paramDict['SNM']     # String description of SNM
# print(filenames)
# print(sys.path)

plt.plot(data.x , data.y)
plt.show()

# sample = opusFC.getOpusData(f, ('SSC', '2D', 'NONE’))
# background = opusFC.getOpusData(backgrondFile, ('SSC', '2D', 'NONE’))
# A = -log10(sample/background)
# print(data.x)

### Access and save visible images
# images = opusFC.getVisImages(f)

# for img in images:
#     data = img['image']
#     title = img['Title']
#     imgext = img['imgext']
#     f = "{0}_{1}.{2}".format(f, title, imgext)
#     with open(f, 'wb') as fd:
#         fd.write(data)