from read_data import read_file


class Calories:
    def __init__(self, start, end, path) -> None:
        self.data = read_file(path)
        self.start = self.calculate_date(start)
        self.end = self.calculate_date(end)

    def avg(self):
        res = 0
        data = self.get_data()
        for cal in data:
            res += int(cal)
        return res / len(data)

    def get_data(self):
        data = []
        for date, cal in self.data:
            cal_date = self.calculate_date(date)
            if self.start <= cal_date <= self.end:
                data.append(cal)
            elif cal_date > self.end:
                break
        return data

    def std(self):
        avg_val = self.avg()
        res = 0.0
        data = self.get_data()
        for cal in data:
            res += abs((float(cal) - avg_val)) ** 0.5

        return res / len(data)

    def highest_cal(self):
        res = 0
        curr_date = self.start
        prev_date = self.start
        max_ = []
        for date, cal in self.data:

            cal_date = self.calculate_date(date)
            if self.start <= cal_date <= self.end:
                curr_date = cal_date
                if curr_date == prev_date:
                    res += int(cal)
                else:
                    prev_date = curr_date
                    max_.append(res)
                    res = int(cal)
            elif cal_date > self.end:
                break
        max_.append(res)
        return max(max_)

    def highest_meal_cal(self):
        data = self.get_data()
        return max(data)

    @staticmethod
    def calculate_date(date):
        a = [int(i) for i in date.split("/")]
        a[1] *= 10
        return sum(a)
