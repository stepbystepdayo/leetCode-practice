'''

  It's photo day at the local school, and you're the photographer assigned to
  take class photos. The class that you'll be photographing has an even number
  of students, and all these students are wearing red or blue shirts. In fact,
  exactly half of the class is wearing red shirts, and the other half is wearing
  blue shirts. You're responsible for arranging the students in two rows before
  taking the photo. Each row should contain the same number of the students and
  should adhere to the following guidelines:
'''


def solution(redShirtHeights,blueShirtHeights):
    redShirtHeights.sort(reverse = True)
    blueShirtHeights.sort(reverse = True)

    colorFirstRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'Blue'

    for index in enumerate(redShirtHeights):
        if colorFirstRow == 'RED':
            if redShirtHeights >= blueShirtHeights:
                return False
        else:
            if redShirtHeights <= blueShirtHeights:
                return False
    return True




print(solution([5,8,1,3,4],[6,9,2,4,5]))


