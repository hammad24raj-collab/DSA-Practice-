def countInversions(arr):
    return count_invrs(arr, 0, len(arr) - 1)

def count_invrs(arr, left, right):
    if left >= right:
        return 0

    mid = (left + right) // 2
    left_count = count_invrs(arr, left, mid)
    right_count = count_invrs(arr, mid + 1, right)

    temp = []
    i, j = left, mid + 1
    count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1
            count += mid - i + 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    arr[left:right + 1] = temp
    return left_count + right_count + count


if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().split()))
        print(countInversions(arr))