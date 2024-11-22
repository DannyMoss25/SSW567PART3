import unittest
import main
import time
import csv

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

        data = [["Num.Lines", "W/O Test", "W Test"]]
        first = main.timing(1)

        before = time.perf_counter()
        self.assertNotEqual(main.timing(1), "testing")
        after = time.perf_counter()

        data.append([1, first, after - before])



        before = time.perf_counter()
        self.assertNotEqual(main.timing(10), "testing")
        after = time.perf_counter()
        second = main.timing(10)
        data.append([10, second, after - before])




        before = time.perf_counter()
        self.assertNotEqual(main.timing(100), "testing")
        after = time.perf_counter()
        third = main.timing(100)
        data.append([100, third, after - before])



        # Test for values between 1000 and 10000, step 1000
        for num_lines in range(1000, 11000, 1000):
            before = time.perf_counter()
            result = main.timing(num_lines)
            after = time.perf_counter()

            # Add assertions and record data
            self.assertNotEqual(result, "testing")
            data.append([num_lines, result, after - before])
        with open('RecordReportFull.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
            csvfile.close()




if __name__ == '__main__':

    unittest.main()