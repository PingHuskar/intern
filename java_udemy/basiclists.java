import java.util.ArrayList;
public class basiclists {
    public static void main(String[] args){
        ArrayList<String> fruits = new ArrayList<>();
        fruits.add("apple");
        fruits.add("orange");
        fruits.add("peach");
        fruits.add("kiwi");
        int fruitsize = fruits.size();
        String place = fruits.get(2);
        System.out.println(fruits);
        fruits.set(1,"green apple");
        System.out.println(fruits);
        fruits.remove(1);
        System.out.println(place);
        System.out.println(fruits);
        System.out.println(fruits.size());
        fruits.clear();
        System.out.println(fruits.size());
    }
}
