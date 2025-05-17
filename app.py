def main():
    student_count = int(input("How many students are in your school? "))
    students_going = int(input("How many students are going on your field trip? "))
    if (students_going>student_count):
        print("Number of students going is more than the number of students in the school. Enter information again.")
    else:
        # The amount charged by the school to each student for the trip
        trip_price = 20

        # The amount the school is spending for each student for the trip
        trip_cost = 10

        # Total Revenue - how much did the school get paid by the students going
        total_revenue = calculate_total_revenue(num_students=students_going, price=trip_price)

        # How many students are staying back and NOT going to the field trip
        students_staying = student_count-students_going

        # How much is the school spending in total for the trip
        total_paid = trip_cost*students_going

        print(f"Total Revenue: {total_revenue}")
        print(f"Total paid to organization: {total_paid}")
        print(f"Amount of students going: {students_going}")
        print(f"Students staying back at school: {students_staying}")    

def calculate_total_revenue(num_students: int, price: int):
    """
    Calculate total revenue for the trip
    """
    total_revenue = num_students * price
    return total_revenue


if __name__ == "__main__":
    main()