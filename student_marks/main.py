from utils import open_file, get_index
import matplotlib.pyplot as plt


def gender_chart(col, data,ax):
    gender = get_index(col, "gender")

    gender_count = {}

    for i in data:
        gender_count[i[gender]] = gender_count.get(i[gender], 0) + 1
    ax.pie(gender_count.values(), labels=gender_count.keys())
    ax.set_title("Gender")


def marks_chart(col, data,ax):
    eng = get_index(col, "english")
    mat = get_index(col, "maths")

    marks_count = {"pass": 0, "fail": 0}

    for i in data:
        if int(i[eng]) + int(i[mat]) > 40:
            marks_count["pass"] += 1
        else:
            marks_count["fail"] += 1
    
    ax.pie(marks_count.values(),labels=marks_count.keys(),colors=['g','r'])
    ax.set_title("Pass v/s Fail")


if "__main__" == __name__:
    col, data = open_file("marks.csv")
    fig,ax = plt.subplots(1,2)
    gender_chart(col, data,ax[0])
    marks_chart(col,data,ax[1])
    plt.show()
