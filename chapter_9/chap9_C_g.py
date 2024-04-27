name = ['Aditi' , 'Mrunal' , 'Aditya' , 'Girish' , 'Ankit' , 'Meenal']
rollno = ['12' , '43' , '45' , '50' , '66' , '21']
marks = ['90' , '45' , '82' , '75' , '95' , '65']
name = tuple(name)
rollno = tuple(rollno)
marks = tuple(marks)

new_list = [name, rollno, marks]

#second method

new_list_zip = list(zip(name, rollno, marks))
print(new_list_zip)