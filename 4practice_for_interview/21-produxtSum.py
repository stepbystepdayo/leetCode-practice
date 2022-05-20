'''

  Write a function that takes in a "special" array and returns its product sum.

  A "special" array is a non-empty array that contains either integers or other
  "special" arrays. The product sum of a "special" array is the sum of its
  elements, where "special" arrays inside it are summed themselves and then
  multiplied by their level of depth.
  
  The depth of a "special" array is how far nested it is. For instance, the
  depth of [] is 1; the depth of the inner array in [[]] is 2; the depth of innermost arrayin [[[]]] is 3.

  therefore, the product sum of [x,y] is x + y; the products sum of[x,[y,z]] is x+2*(y+z); the product sum of [x,[y,[z]]] is x + 2*(y+3z)
'''


def solution(array, multiplier = 1):
  sum = 0
  for element in array:
    print(element)
    # if the element type is list, add solution(element, multiplier +1)<= this is recursive. to sum
    if type(element) is list:
      sum += solution(element, multiplier + 1)
    # otherwise, add element number to sum
    else:
      sum += element
    #
  return sum * multiplier

print(solution([5,2,[7,-1],3,[6,[-13,8],4]]))
# 5 + 2 +2 * (7-1)+ 3 +2 *(6 + 3 * (-13 + 8) +4) 