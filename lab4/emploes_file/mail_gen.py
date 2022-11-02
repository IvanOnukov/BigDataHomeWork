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
    dataReader = open("task_file.txt", 'r')
    dataWriter = open("tmp", 'w')
    try:
        title = dataReader.readline()
        data = dataReader.readlines()
        for line in data:
            if validation_employees_data(line.split(', ')):
                dataWriter.write(line)
    finally:
        dataReader.close()
        dataWriter.close()

    dataReader = open("tmp", 'r')
    try:
        data = dataReader.readlines()
        listName = []

        for line in data:
            tmpVal = line.split(', ')
            tmpList = []
            tmpList.append(tmpVal[1])
            tmpList.append(tmpVal[2])
            listName.append(tmpList)
        email_name = email_gen(listName)
    finally:
        dataReader.close()

    dataReader = open("tmp", 'r')
    dataWriter = open("dataBase", 'w')
    try:
        data = dataReader.readlines()
        i = 0
        dataWriter.write(title)
        for line in data:
            if validation_employees_data(line.split(', ')):
                dataWriter.write(str(email_name[i]) + ' '*4 + line[2::])
                i += 1
    finally:
        dataReader.close()
        dataWriter.close()
