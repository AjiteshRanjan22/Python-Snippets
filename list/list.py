courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses)
print(len(courses))
print(courses[:3])
print(courses[::2])
print(*courses)
courses.append('art')
courses.insert(1,'chemistry')
course = ['electronics', 'mechanical']
courses.extend(course)

print(courses)
courses.remove('History')
print(courses)

print(courses.pop())
courses.sort()
print(courses)
courses.sort(reverse=True)
print(courses)
q = sorted(courses)
print(courses)
print(min(courses))
print(courses.index('Physics'))
print('Math' in courses)
