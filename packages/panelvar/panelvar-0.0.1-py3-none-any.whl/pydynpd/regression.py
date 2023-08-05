import numpy as np



# import pydynpd.ar_test as ar_test
import pydynpd.gmm_module as gmm_module

import time
import warnings

from pandas import DataFrame

from pydynpd.dynamic_panel_model import dynamic_panel_model

#from pydynpd.model_organizer import model_oranizer
from pydynpd.model_summary import model_summary
from pydynpd.panel_data import panel_data
from sys import exit

import sys

warnings.filterwarnings("ignore", category=RuntimeWarning)


class abond:

    def __init__(self, command_str, df: DataFrame, identifiers: list):

        if len(identifiers) != 2:
            print('two variables needed')
            exit()


        pdata = panel_data(df, identifiers)
        
        try:
            (temp_part1_list, temp_iv_list, DGMM_list, LGMM_list, List_parts, options) =   gmm_module.process_command(pdata.T, command_str, df.columns)
        except Exception as e:
            print(e)
            sys.exit(1)

        pdata.export_data(df, temp_part1_list, temp_iv_list, DGMM_list, LGMM_list, options.timedumm)

        
        (reg_table,  hansen, AR_test, basic_info)=gmm_module.prepare_data(pdata.data,temp_part1_list, temp_iv_list, DGMM_list, options, List_parts, [pdata.N, pdata.T], pdata.cols, pdata.col_timedumm)

        self.model=dynamic_panel_model(identifiers, reg_table, basic_info, hansen, AR_test, options, List_parts)

        self.form_results(self.model)

 

    

 

    def form_results(self, model):
  
        if model.name != '':
            print(' ' + model.name)

 
        ms = model_summary()
        ms.print_summary(model)

        #self.models.append(model)  # results = {}

    def check_model(self, model):
        tbr = False
        num_ARs = len(model.AR_list)
        last_AR = model.AR_list[num_ARs - 1]

        if last_AR.P_value > 0.05:
            if model.hansen.p_value > 0.05 and model.hansen.p_value < 0.99999:
                return True
        else:
            return False
