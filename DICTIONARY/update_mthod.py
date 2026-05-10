#  The update() method inserts the specified items to the dictionary.

student ={
    "name":"Aditya",
    "class":9,
    "subject":{
        "chem":49,
        "math":76,
        "phy":21,
    }
}
student.update({"colour" : "black"})
print(student)