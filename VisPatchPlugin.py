import PyPluMA
import PyIO
import pickle
import os
from dataset import PISToN_dataset

class VisPatchPlugin:
    def input(self, inputfile):
        self.parameters = PyIO.readParameters(inputfile)
    def run(self):
        pass
    def output(self, outputfile):
        GRID_DIR=PyPluMA.prefix()+"/"+self.parameters["grid"]
        ppi_list = os.listdir(GRID_DIR)
        ppi_list = [x.split('.npy')[0] for x in ppi_list if 'resnames' not in x and '.ref' not in x]
        masifObj = PISToN_dataset(GRID_DIR, ppi_list)

        #myMasif = open(PyPluMA.prefix()+"/"+self.parameters["masif"], "rb")
        myID = self.parameters["id"]
        masifObj.vis_patch(myID, outputfile)
