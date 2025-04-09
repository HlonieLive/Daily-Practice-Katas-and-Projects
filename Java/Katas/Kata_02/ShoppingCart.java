import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.Scanner;

class Item {
    String name;
    double price;
    int quantity;

    public Item(String name, double price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
    }
    public double getTotal() {
        return price * quantity;
    }
}

public class ShoppingCart {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        ArrayList<Item> cart = new ArrayList<>();
        char currency = 'R';

        while (true){
            System.out.print("Enter item name (or type 'done' to checkout): ");
            String itemName = scanner.nextLine();

            if (itemName.equals("done")) break;

            System.out.print("Enter price: ");
            double itemPrice = scanner.nextDouble();

            System.out.print("Enter quantity: ");
            int itemQuantity = scanner.nextInt();
            scanner.nextLine();

            cart.add(new Item(itemName, itemPrice, itemQuantity));
        }

        double grandTotal = 0;
        System.out.println("Receipt:");
        for (Item item: cart) {
            System.out.printf("%s x%d @ %c%.2f each = %c%.2f%n", item.name, item.quantity, currency, item.price, currency, item.getTotal());
            grandTotal += item.getTotal();
        }
        System.out.printf("Total: %c%.2f%n", currency, grandTotal);
        System.out.println("\nCheckout complete. Thank you!");

        scanner.close();
    }
}