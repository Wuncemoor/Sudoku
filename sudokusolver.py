class SudokuSolver():
    
    def __init__(self):
        pass
    
    def remove_colrowcube(self, nodes):
        
        for i in nodes:
            for j in nodes:
                if i.endval is None and j.endval is not None:
                    if i.column == j.column or i.row == j.row or i.cube == j.cube:
                        try:
                            i.possibilities.remove(j.endval)
                        except:
                            pass


                if len(i.possibilities) == 2:
                    i.endval = i.possibilities[1]