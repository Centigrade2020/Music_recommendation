output_filename = "data"
output_format = 'csv'

fn = f"{output_filename}.{output_format}"

with open("rawdata.csv", 'r') as f:
    content = f.read()
    data_list = []
    lines = content.split('\n')
    del lines[0]
    for i in lines:
        data_list.append(i.split(','))

    for i in data_list:
        if i[4].strip() != '':
            i[3] += " | "+i[4]
        del i[4]

        try: 
            int(i[1])
        except ValueError:
            data_list.remove(i)


with open(fn, 'w') as f:
    f.write("name,age,gender,genre\n")
    li = []
    for i in data_list:
        string = ""
        for j in i:
            string += j+","
        li.append(string[:len(string)-1])

    li = set(li)
    for i in li:
        f.write(i+'\n')

print("Task completed successfully")
        