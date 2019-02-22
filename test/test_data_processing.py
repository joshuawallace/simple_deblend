'''test_data_processing.py - Joshua Wallace - Feb 2019

This tests classes and methods in the data_processing.py file.
'''

import unittest
import sys, os
sys.path.insert(1,os.path.abspath('../src'))
print(os.path.abspath('../src'))
import data_processing as dproc
import numpy as np


class test_data_processing_init(unittest.TestCase):

    def setUp(self):
        pass

    def test_lc_collection_setup(self):
        # Test initialization of the lc_collection_for_processing class
        self.assertIsInstance(dproc.lc_collection_for_processing(1.),
                                dproc.lc_collection_for_processing)

    def test_periodsearch_results_setup(self):
        #Test initialization of the periodsearch_results class
        self.assertIsInstance(dproc.periodsearch_results('1'),
                                  dproc.periodsearch_results)

class test_data_processing_run(unittest.TestCase):

    def setUp(self):
        self.col_a = dproc.lc_collection_for_processing(1.,nworkers=4)
        sample_len_1 = 1000
        t1 = np.linspace(0,42,sample_len_1)
        self.col_a.add_object(t1,10.+np.sin(t1),[.1]*sample_len_1,0.,0.,'object1')
        self.col_a.add_object(t1,[10.]*(sample_len_1-1) + [10.0001],[.1]*sample_len_1,0.5,0,'object2')

    def test_lc_collection_setup(self):
        # Test initialization of the lc_collection_for_processing class
        self.assertIsInstance(dproc.lc_collection_for_processing(1.),
                                dproc.lc_collection_for_processing)

    def test_periodsearch_results_setup(self):
        #Test initialization of the periodsearch_results class
        self.assertIsInstance(dproc.periodsearch_results('1'),
                                  dproc.periodsearch_results)

    def test_basic_run(self):
        # Test a basic run of the iterative deblending
        self.col_a.run_ls(startp=0.5,endp=4.)
        print("\n\n\n\n\n.....")
        print(self.col_a.results.keys())

        with self.assertRaises(KeyError):
            self.col_a.results['object1']['BLS']

        self.assertEqual(self.col_a.results['object1']['LS'].good_periods_info[0]['lsp_dict']['bestperiod'],2.*np.pi)
        self.assertEqual(len(self.col_a.results['object1']),1)
        for a in self.col_a.results['object1']['LS'].good_periods_info:
            print(a['lsp_dict']['bestperiod'])
        self.assertEqual(len(self.col_a.results['object1']['LS'].good_periods_info),1)
        self.assertEqual(len(self.col_a.results['object2']),0)
        




if __name__ == '__main__':
    unittest.main()
