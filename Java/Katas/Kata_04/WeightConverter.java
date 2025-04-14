import java.util.Scanner;

public class WeightConverter {
    public static void main(String[] args) {
        // Weight Coversion Program
        Scanner scanner = new Scanner(System.in);

        double weight, newWeight;
        int choice;

        System.out.println("Weight Conversion Program: ");
        System.out.println("1. Convert lbs to kgs.");
        System.out.println("2. Convert kgs to lbs.");

        System.out.println("Choose your option: ");
        choice = scanner.nextInt();

        if (choice == 1) {
            System.out.println("Enter the weight in lbs: ");
            weight = scanner.nextDouble();
            newWeight = weight * 0.453592;
            System.out.println("The new weight in kgs is: "+ newWeight);
        }


        // Prompt for user choice

        // Option 1: convert lbs to kgs

        // Option 2: convert kgs to lbs

        // Invalid choice
    }
}