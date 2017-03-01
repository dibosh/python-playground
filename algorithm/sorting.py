class MergeSort(object):
    def partition(self, items_array):
        return [[item] for item in items_array]

    def merge(self, arr1, arr2):
        left_cursor = 0
        right_cursor = 0
        merged_array = []

        first_array_length = len(arr1)
        second_array_length = len(arr2)

        expected_merged_array_length = first_array_length + second_array_length

        while len(merged_array) != expected_merged_array_length:
            if arr1[left_cursor] < arr2[right_cursor]:
                merged_array.append(arr1[left_cursor])
                if left_cursor < first_array_length - 1:
                    left_cursor += 1
            else:
                merged_array.append(arr2[right_cursor])
                if right_cursor < second_array_length - 1:
                    right_cursor += 1
        return merged_array