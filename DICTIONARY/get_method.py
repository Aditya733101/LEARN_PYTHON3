# get() method return the key accoridng to value
student ={
    "name":"Aditya",
    "class":9,
    "subject":{
        "chem":49,
        "math":76,
        "phy":21,
    }
}
print(student)
print(student.get("class"))
