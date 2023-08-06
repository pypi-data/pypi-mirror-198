import pandas as pd

from ..._pattern import pattern
from ..util import ( identify_skeleton_from_empty_graph,
                     identify_skeleton_by_ind,
                     identify_v_structure_with_adjacency_orient_faithfulness,
                     identify_meeks_rule_2,
                     identify_meeks_rule_3,
                     identify_meeks_rule_4 )

from ..test import get_test

class basic:
    def __init__(self):
        self.ptn = pattern()
    
    def identify(self, data:pd.DataFrame = None, test:str = None, ind:dict = None, vertex = None, **test_kwarg) -> pattern: 
        self.test = get_test(test)

        # STEP 0 ~ 1 : Find skeleton
        if ind is not None:
            self.identify_skeleton_by_ind(ind, vertex)
        else:
            self.identify_skeleton_from_empty_graph(data, test_kwarg = test_kwarg)


        # # STEP 2 : Find v-structure
        self.identify_v_structure_with_adjacency_orient_faithfulness()

        # STEP 3~5 : use Meek's rules
        cnt = True
        while cnt:
          cnt2 = self.identify_meeks_rule_2()
          cnt3 = self.identify_meeks_rule_3()
          cnt4 = self.identify_meeks_rule_4()

          cnt = cnt2 or cnt3 or cnt4 # Check there are vertexs which could be changed

        return self.ptn

    def draw(self):
        self.ptn.draw()

    def draw_by_pos(self, pos):
        self.ptn.draw_by_pos(pos)
        
basic.identify_skeleton_from_empty_graph = identify_skeleton_from_empty_graph
basic.identify_v_structure_with_adjacency_orient_faithfulness = identify_v_structure_with_adjacency_orient_faithfulness
basic.identify_meeks_rule_2 = identify_meeks_rule_2
basic.identify_meeks_rule_3 = identify_meeks_rule_3
basic.identify_meeks_rule_4 = identify_meeks_rule_4
basic.identify_skeleton_by_ind = identify_skeleton_by_ind