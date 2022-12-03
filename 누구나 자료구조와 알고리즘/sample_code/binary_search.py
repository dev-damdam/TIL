def binary_search(array, search_value):
    # 최초의 상한선은 배여르이 첫 번째 값, 하한선은 마지막 값
    lower_bound = 0
    upper_bound = len(array) - 1
    while lower_bound <= upper_bound:
        # 중간 지점 찾기 // 연산자를 이용해서 결과값이 정수로 딱 떨어지게 함
        mid_idx = (lower_bound + upper_bound) // 2

        # 찾는 값 비교, 값이 더 큰지 혹은 작은지에 따라 상한선 혹은 하한선을 바꾼다.
        if array[mid_idx] == search_value:
            return mid_idx
        elif array[mid_idx] > search_value:
            upper_bound = mid_idx - 1
        else:
            lower_bound = mid_idx + 1
    
    # 찾는 값이 없으면 None 리턴
    return None

array = [3, 17, 75, 80, 202]
search_value = 75
print(binary_search(array, search_value))