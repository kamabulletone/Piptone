from unittest import TestCase

from LectureTasks.lecture1.fast_mul import fast_mul


class Test(TestCase):
    def test_fast_mul(self):
        for i in range(100):
            for j in range(100):
                #print(i,j, fast_mul(i,j))
                assert fast_mul(i,j) == i*j
