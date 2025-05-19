package com.example;

import java.util.*;

public class Utils {

    // Task 1: Return true if number is even
    public static boolean isEven(int number) {
        return number % 2 == 0;
    }

    // Task 2: Reverse a string
    public static String reverse(String input) {
        String reversed = "";

        for (int i = 0; i < input.length(); i++) {
            int j = input.length() - 1 - i;
            reversed += input.charAt(j);
        }
        return reversed;
    }

    // Task 3: Sum elements in an array
    public static int sumArray(int[] numbers) {
        int sum = 0;

        for (int number: numbers) {
            sum += number;
        }
        return sum;
    }

    // Task 4: Check if a string is a palindrome
    public static boolean isPalindrome(String word) {
        // TODO: Implement this
        return false;
    }

    // Task 5: Generate multiplication table (2D array)
    public static int[][] generateMultiplicationTable(int rows, int cols) {
        // TODO: Implement this
        return new int[rows][cols];
    }
}