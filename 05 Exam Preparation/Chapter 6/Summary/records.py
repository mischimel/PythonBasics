class StudentRecord:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

def write_record(file_name, student_record):
    with open(file_name, 'a') as file:
        file.write(f"{student_record.name},{student_record.grade}\n")

def read_records(file_name):
    records = []
    with open(file_name, 'r') as file:
        for line in file:
            name, grade = line.strip().split(',')
            records.append(StudentRecord(name, int(grade)))
    return records

def display_records(records):
    for record in records:
        print(f"Name: {record.name}, Grade: {record.grade}")

# Example usage
# Writing records
student1 = StudentRecord("Alice", 90)
student2 = StudentRecord("Bob", 85)

write_record("student_records.txt", student1)
write_record("student_records.txt", student2)

# Reading and displaying records
all_records = read_records("student_records.txt")
display_records(all_records)
