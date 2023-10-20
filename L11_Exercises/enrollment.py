def gather_credits(max_credits, *courses):
    enrolled_courses = set()
    total_credits = 0

    for course in courses:
        if course[0] not in enrolled_courses and total_credits < max_credits:
            enrolled_courses.add(course[0])
            total_credits += course[1]

    credits_shortage = max_credits - total_credits # calculate the credits shortage

    if credits_shortage > 0:
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."
    else:
        sorted_courses = sorted(list(enrolled_courses))
        return f"Enrollment finished! Maximum credits: {total_credits}.\nCourses: {', '.join(sorted_courses)}"

print(gather_credits(
    80,
    ("Basics", 27),
))
print()
print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))

# Write a function called gather_credits that receives information about credits needed, courses, and
# their credits, and returns the result. The function will receive a different number of arguments.
# The arguments will be passed as follows:
#     • The first argument will be the number of credits you need - an integer in the range [0, 200];
#     • The following arguments will be the tuples with two elements - the first one is the course name (string),
# and the second one is the course credits (integer);
# After receiving the information and calling the function, the program should start tracking the enrollment process:
#     • Take the course’s name from each tuple successively and if you need more credits,
# enroll in it, and proceed to the next one.
#     • If a course has already been enrolled in, ignore it, and proceed to the next one.
#     • If you have reached the needed number of credits, STOP enrolling!
#  In the end:
#     • If you’ve managed to gather the needed credits, return the message,
#     including the enrolled courses on a new line:
# "Enrollment finished! Maximum credits: {gathered_credits}.
# Courses: {course1, course2, …, courseN}"
#         ◦ return the courses’ names sorted alphabetically, in ascending order.
#     • Otherwise, return the message:
# "You need to enroll in more courses! You have to gather {credits_shortage} credits more."
# Note: Submit only the function in the judge system
# Input
#     • There will be no input from the console, just parameters passed to your function.
# Output
#     • Return one of the strings shown above depending on the result.
# Constraints
#     • The first argument will always be an integer.
#     • Each tuple given will always contain the course name with its credits.
#
# Input:
# print(gather_credits(
#     80,
#     ("Basics", 27),
# ))
# Output:
# You need to enroll in more courses! You have to
# gather 53 credits more.
#
# Input:
# print(gather_credits(
#     80,
#     ("Advanced", 30),
#     ("Basics", 27),
#     ("Fundamentals", 27),
# ))
# Output:
# Enrollment finished! Maximum credits: 84.
# Courses: Advanced, Basics, Fundamentals
