# creating a program to compute statistics from a list of exam grades
# (instead of using packages)

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

# function to print out the list of grades, one element at a time
def print_grades(grades_input):
  for grade in grades_input:
    return grade

# function to print the sum of scores
# looping through list to compute rolling sum
def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total

# function to print out the average
# sum divided by total #
def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input)
  average = sum_of_grades / float(len(grades_input))
  return average

# function to print out the variance
# variance: how the grades varied against the average
# a large variance means that the students' grades were all over the place
# a small variance means that the majority of the students had similar grades
def grades_variance(scores):
  average = grades_average(scores)
  variance = 0
  for score in scores:
    diff = (average - score) ** 2
    variance += diff
  total = variance / float(len(scores))
  return total

# function to print out the standard deviation
# square root of the variance
def grades_std_deviation(variance):
  return variance ** 0.5

## printing all statistics
# all grades
print print_grades(grades)
# sum
print grades_sum(grades)
# average
print grades_average(grades)
# variance
print grades_variance(grades)
# standard deviation
variance = grades_variance(grades)
print grades_std_deviation(variance)
