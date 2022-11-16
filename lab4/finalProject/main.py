def email_gen(list_of_names, nameDomen='@company.io'):
    emails = []
    for i in list_of_names:
        letter = 1
        while i[1] + '.' + i[0][0:letter] + nameDomen in emails:
            letter += 1
        emails.append(i[1] + '.' + i[0][0:letter] + nameDomen)
    return emails


def validation_employees_data(list_of_data):
    check_name = str(list_of_data[1]).isalpha() and (len(list_of_data[1]) != 0)
    check_surname = str(list_of_data[2]).isalpha() and (len(list_of_data[2]) != 0)
    check_tel = str(list_of_data[3]).isdigit() and (len(list_of_data[3]) == 7)
    check_city = str(list_of_data[4].replace('\n', '')).isalpha() and (len(list_of_data[4]) != 0)

    return check_name and check_surname and check_tel and check_city


if __name__ == '__main__':
    dataReader = open("../sharedData/task_file.txt", 'r')
    dataWriterValidData = open("tmp", 'w')
    dataWriterBadData = open("badData", 'w')
    try:
        title = dataReader.readline()  # title file
        data = dataReader.readlines()  # read all lines from file
        for line in data:
            if validation_employees_data(line.split(', ')):
                dataWriterValidData.write(line)
            else:
                dataWriterBadData.write(line[2::])  # write not valid line in file
    finally:
        dataReader.close()
        dataWriterValidData.close()

    dataReader = open("tmp", 'r')
    try:
        data = dataReader.readlines()
        listName = []

        for line in data:
            tmpVal = line.split(', ')
            tmpList = [tmpVal[1], tmpVal[2]]
            listName.append(tmpList)
        email_name = email_gen(listName)
    finally:
        dataReader.close()

    dataReader = open("tmp", 'r')
    dataWriterValidData = open("dataBase", 'w')
    try:
        data = dataReader.readlines()
        i = 0
        dataWriterValidData.write(title)
        for line in data:
            if validation_employees_data(line.split(', ')):
                dataWriterValidData.write(str(email_name[i]) + ' ' * 4 + line[2::])
                i += 1
    finally:
        dataReader.close()
        dataWriterValidData.close()
