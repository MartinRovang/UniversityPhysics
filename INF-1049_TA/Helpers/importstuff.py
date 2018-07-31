import numpy as np
import matplotlib.pyplot as plt
import sys



# file = open("data.dat")

# data = file.read()

# print (data)

# file.close()


# with open('data.dat', 'r') as data:
#     print(data.read())

try:
    data = np.loadtxt('%s'%sys.argv[1], skiprows= 1).transpose() 

    #Fire arrays
    dato_array = data[0]
    Vadso_array = data[1]
    Tromso_array = data[2]
    Bodo_array = data[3]


    y = np.array([data[1], data[2], data[3]])



    # Maksimum og minimum https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.argmax.html
    def find_max_min(date_array, array_data):
        j = 0
        k = 0
        temp_array_biggest = []
        temp_date = []
        temp_array_smallest = []

        for i in array_data[0]:
            biggest_value = round(max(array_data[0][j], array_data[1][j], array_data[2][j]),2)
            smallest_value = round(min(array_data[0][j], array_data[1][j], array_data[2][j]),2)
            temp_array_biggest.append(biggest_value)
            temp_array_smallest.append(smallest_value)
            temp_date.append(round(date_array[j],2))
            j += 1

        return temp_array_biggest, temp_array_smallest, temp_date





    labels = ["Vadsø","Tromsø","Bodø"]
    Max, Min, dates = find_max_min(dato_array, y)


    for y_array, label in zip(y, labels):
        plt.plot(dato_array, y_array, label = label)
    plt.scatter(dates[y_array.argmax()], max(Max), color = 'red')
    plt.scatter(dates[y_array.argmin()], min(Min), color = 'blue')



    plt.xticks(dato_array)
    plt.xlabel("Dato")
    plt.ylabel("Temperatur")
    plt.legend(loc = "best")

    plt.show()



    # Max, Min, dates = find_max_min(dato_array, y)

    # for y_array, label in zip(y, labels):
    #     plt.plot(dato_array, y_array, label = label)
    #     print(max(y_array))
    #     plt.scatter(max(y_array), dato_array[y_array.argmax()])


    # plt.xticks(dato_array)
    # plt.xlabel("Dato")
    # plt.ylabel("Temperatur")
    # plt.legend(loc = "best")
except IndexError: #https://docs.python.org/2/tutorial/errors.html
    print('Det oppsto en feil')


