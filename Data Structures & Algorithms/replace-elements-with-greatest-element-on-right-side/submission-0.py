class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            max_element = arr[i + 1]

            for k in range(i + 1, len(arr)):
                if arr[k] > max_element:
                    max_element = arr[k]

            arr[i] = max_element

        arr[-1] = -1
        return arr