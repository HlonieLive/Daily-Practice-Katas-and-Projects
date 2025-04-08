import java.util.Scanner;

public class ShoppingCart {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        String item;
        double price;
        int quality;
        char currency = 'R';
        double total;

        System.out.print("Which item would you like to buy? ");
        item = scanner.nextLine();

        System.out.print("What is the price? ");
        price = scanner.nextDouble();

        System.out.print("How many would you like to buy?");
        quality = scanner.nextInt();

        total = price * quality;

        System.out.print("Your Total is: " + currency + total + "\nCheckout...");

        scanner.close();
    }
}