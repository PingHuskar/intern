import java.util.Scanner;
public class car {
    public static void main(String[] args){
        System.out.println("Do you want a car?");
        Scanner scan = new Scanner(System.in);
        String ans1 = scan.next();
        if (ans1.equals("y")) {
            System.out.println("What's your fav color?");
            Scanner scan2 = new Scanner(System.in);
            String ans2 = scan2.next();
            if (ans2.equals("red")){
                System.out.println("Would you like to see it?");
                Scanner scan3 = new Scanner(System.in);
                String ans3 = scan3.next();
                if (ans3.equals("y")) {
                    System.out.println("Let's check the car");
                }
                else {
                    System.out.println("check st else");
                }
            }
            else if (ans2.equals("blue")){
                System.out.println("We can order it");
            }
            else {
                System.out.println("We don't have it");
            }
        }
        else {
            System.out.println("Have a good day!");
        }
        System.out.println();
    }
}
