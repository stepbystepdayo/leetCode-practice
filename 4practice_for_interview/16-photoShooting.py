'''
'''


def solution(redShirtHeights,blueShirtHeights):
    redShirtHeights.sort(reverse = True)
    blueShirtHeights.sort(reverse = True)

    colorFirstRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'Blue'

    for index in range(len(redShirtHeights)):
        if colorFirstRow == 'RED':
            if redShirtHeights >= blueShirtHeights:
                return False
        else:
            if redShirtHeights <= blueShirtHeights:
                return False
    return True




print(solution([5,8,1,3,4],[6,9,2,4,5]))


