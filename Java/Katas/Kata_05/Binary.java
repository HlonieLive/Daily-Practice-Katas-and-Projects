public class Binary {
    public static void main(String[] args) {

        int nums[] = {2,3,4,6,8,9,10,11,12,16,17,21,25,26,27,30,31};
        int target = 11;

        int results = BinarySearch(nums, target);

        if( results!= -1) {
            System.out.println("Element fount at Index: " + results);
        } else System.out.println("Element not found");
    }

    public static int BinarySearch (int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;

        while (left <= right) {
            int mid = (left + right) / 2;
            if(nums[mid] == targe) {
                return mid;
            }else if(nums[mid] < target) {
                left = mid + 1;
            }else {
                right = mid - 1;
            }
        }

        return -1;
    }
}