// package com.example;

import org.junit.jupiter.api.Test;

import com.example.Utils;

import static org.junit.jupiter.api.Assertions.*;



public class UtilsTest {

    @Test
    void testIsEven() {
        assertTrue(Utils.isEven(2));
        assertFalse(Utils.isEven(3));
    }

    @Test
    void testReverse() {
        assertEquals("cba", Utils.reverse("abc"));
        assertEquals("", Utils.reverse(""));
    }

    @Test
    void testSumArray() {
        assertEquals(6, Utils.sumArray(new int[]{1, 2, 3}));
        assertEquals(0, Utils.sumArray(new int[]{}));
    }

    @Test
    void testIsPalindrome() {
        assertTrue(Utils.isPalindrome("madam"));
        assertFalse(Utils.isPalindrome("hello"));
    }

    @Test
    void testGenerateMultiplicationTable() {
        int[][] table = Utils.generateMultiplicationTable(2, 3);
        assertEquals(2, table.length);
        assertEquals(3, table[0].length);
        assertEquals(1, table[0][0]);
        assertEquals(2, table[0][1]);
        assertEquals(3, table[0][2]);
        assertEquals(2, table[1][0]);
        assertEquals(4, table[1][1]);
        assertEquals(6, table[1][2]);
    }
}
