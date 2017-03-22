/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 


//·¨1

int* twoSum(int* nums, int numsSize, int target) {
    int *ret;
    ret = (int *)malloc(sizeof(int) * 2);
    for (int i = 0; i < numsSize; i++)
        for (int j = i + 1; j < numsSize; j++) 
            if (nums[j] == target - nums[i]) {
                ret[0] = i;
                ret[1] = j;
            }
    return ret;
}

//·¨2
struct node{
    int val;
    int index;
};

int* twoSum(int* nums, int numsSize, int target) {
    int *ret;
    struct node *arr;
    ret = (int *)malloc(sizeof(int) * 2);
    arr = (struct node *)malloc(sizeof(struct node) * numsSize);
    for(int i = 0; i < numsSize; i++){
        arr[i].val = nums[i];
        arr[i].index = i;
    }
    for (int i = 0; i < numsSize; i++)
        for (int j = i + 1; j < numsSize; j++) 
            if (arr[j].val == target - arr[i].val) {
                ret[0] = arr[i].index;
                ret[1] = arr[j].index;
            }
    free(arr);
    return ret;
}
