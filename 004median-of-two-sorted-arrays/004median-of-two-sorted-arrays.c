double max(double x,double y){
    return(x>y?x:y);
}
  
double min(double x,double y){
    return(x>y?y:x);
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {

    if (nums1Size < nums2Size) return findMedianSortedArrays(nums2, nums2Size,nums1,nums1Size);	// Make sure A2 is the shorter one.
    
    if (nums2Size == 0) return ((double)nums1[(nums1Size-1)/2] + (double)nums1[nums1Size/2])/2;  // If A2 is empty
    
    int lo = 0, hi = nums2Size * 2;
    while (lo <= hi) {
        int mid2 = (lo + hi) / 2;   // Try Cut 2 
        int mid1 = nums1Size + nums2Size - mid2;  // Calculate Cut 1 accordingly
        
        double L1 = (mid1 == 0) ? INT_MIN : nums1[(mid1-1)/2];	// Get L1, R1, L2, R2 respectively
        double L2 = (mid2 == 0) ? INT_MIN : nums2[(mid2-1)/2];
        double R1 = (mid1 == nums1Size * 2) ? INT_MAX : nums1[(mid1)/2];
        double R2 = (mid2 == nums2Size * 2) ? INT_MAX : nums2[(mid2)/2];
        
        if (L1 > R2) lo = mid2 + 1;		// A1's lower half is too big; need to move C1 left (C2 right)
        else if (L2 > R1) hi = mid2 - 1;	// A2's lower half too big; need to move C2 left.
        else return (max(L1,L2) + min(R1, R2)) / 2;	// Otherwise, that's the right cut.
    }
    return -1;

}
