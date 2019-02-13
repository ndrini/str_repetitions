# -*- coding: utf-8 -*-

import copy




class StrPattern():
    """ pass from a sting of coupled numebers to a logic cluster and viceversa
    """

    def fromStr2Tpl(self, myList):
        # pass a list of number to a couple of tuples
        result = []
        """         try:         except:           """
        if len(myList) % 2 != 0:
            return None
            # TO DO refactor   [x for x in myList if x % 2 == 0]
        for i in range(len(myList)):
            if i % 2 == 0:  # even number
                result.append((myList[i], myList[i + 1]))
        return result

    def logic(self, rows):
        # return the logic of a list on numbers
        result = []
        # rows = self.fromStr2Tpl(myList)
        if not rows:
            return []
        # print("\n\nrows:", rows)
        initial_rows = []    # the rows, typically from the left side,
                             # we want to compare to the others
                             # on the right side
        repeated_rows = []     # the max length repetition
        for i in range(len(rows) // 2):   # till half rows
            initial_rows.append(rows[i])
            # print("initial_rows:", initial_rows)
            if i == 0:
                times = 2
                # while initial_rows == [rows[times-1]] and times < (len(rows)-1):
                if len(rows) == 1:
                    return [None, ]
                if len(rows) == times:
                    if rows[0]==rows[1]:
                        return [{"times": 2, "rows": [rows[0]]}]
                else:
                    while initial_rows == [rows[times-1]] and times < (len(rows)):
                        repeated_rows = copy.deepcopy(initial_rows)
                        times += 1
                    if repeated_rows:
                        result.append({"times": times, "rows": repeated_rows})
            else:
                # while initial_rows == rows[i + 1:2 * i]   time +1
                times = 2
                if initial_rows == rows[i+1:2*i+2]:
                    repeated_rows = copy.deepcopy( initial_rows)
                    result.append({"times": times, "rows": repeated_rows})

        if result:
            return self.best_result(result)

        else:
            return [{"times": 1, "rows": rows},]
            # return [{"times": 1, "rows": rows[0]}, {"times": 0, "rows": rows[1:]},]


    def best_result(self, result):
        if len(result)<2:
            return [result[0]]
        else:
            #   return [max(value) for k,v in result][0]
            seq = [x['times'] for x in result]
            return [next(item for item in result if item["times"] == max(seq))]

    def fromList2Logic(self, mylist):

        rows = self.fromStr2Tpl(myList)

        # while ...

        result = logic(self, rows)


        return result

if __name__ == '__main__':
    # example
    print("Define a list of rows")
